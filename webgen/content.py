# -*- coding: utf-8 -*-
# Page bodies for drzuluanorion.org — Dr. Zuluan Orion in his own warm, first-person voice.
# url(), ext(), hero(), FC, SB are injected by build.py.
BODY = {'en': {}, 'es': {}}
import blog
I = '/assets/img/'
BK = '/assets/img/books/'

def Lx(lang):
    return (lambda e, s: e if lang == 'en' else s)

# ------------------------------------------------------------------ shared pieces
def bk(img, title, sub=''):
    top = (f'<img src="{BK}{img}.webp?v=3e" alt="{title}" loading="lazy">' if img else
           f'<div class="ph cover"><span class="ct">{title}</span>{f"<span class=cs>{sub}</span>" if sub else ""}<span class="ca">Dr. Zuluan Orion</span></div>')
    return f'<div class="book">{top}<div class="t"><h4>{title}</h4>{f"<p>{sub}</p>" if sub else ""}</div></div>'

def shelf(lang):
    L = Lx(lang)
    g = lambda *b: '<div class="books shelf">' + ''.join(b) + '</div>'
    return f'''<section><div class="narrow center">
<p class="lead">{L('Books that explore, simply and in depth, the paths that heal the soul and lead to the realization of the Self.', 'Libros que exploran, de forma sencilla y profunda, los caminos que sanan el alma y conducen a la realización del Ser.')}</p>
</div></section>
<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">{L('ILLUMINATION, HEALING AND MEDITATION', 'ILUMINACIÓN, SANACIÓN Y MEDITACIÓN')}</p><h2>{L('The path of the Self', 'El camino del Ser')}</h2>
{g(bk('iluminacion', 'Iluminación'), bk('transformacion_cuantica', 'Transformación Cuántica'), bk('transformacion_cuantica_nivel1', 'Transformación Cuántica · Nivel 1'), bk('puntos_transformacion_cuantica', 'Puntos de Transformación Cuántica'), bk('meditacion_cuantica', 'Meditación Cuántica'), bk('el_refugio_del_corazon', 'El refugio del Corazón'), bk('deshojando_corazon_eternidad', 'Deshojando el Corazón de la Eternidad'))}
<p class="eyebrow" style="margin-top:60px">{L('THE LIGHT CODES', 'LOS CÓDIGOS DE LUZ')}</p><h2>{L('Codes for the mind, the heart, dreams and energy', 'Códigos para la mente, el corazón, los sueños y la energía')}</h2>
{g(bk('cl_mente', 'Códigos de Luz para tu Mente'), bk('cl_corazon', 'Códigos de Luz para tu Corazón'), bk('cl_suenos', 'Códigos de Luz para tus Sueños'), bk('cl_energia', 'Códigos de Luz para tu Energía'), bk('meditacion_codigos_luz', 'Meditación de Códigos de Luz'))}
<p class="eyebrow" style="margin-top:60px">{L('THE FLAME CODEX AND THE DESCENT', 'EL CÓDICE DE LA LLAMA Y EL DESCENSO')}</p><h2>{L('The sacred language and the living account', 'El lenguaje sagrado y el relato vivo')}</h2>
{g(bk('codice1', 'El Códice de la Llama · Vol. I'), bk('codice2', 'El Códice de la Llama · Vol. II'), bk('arte_angelico_1', 'El Arte Angélico · Vol. I'), bk('arte_angelico_2', 'El Arte Angélico · Vol. II'), bk('yoga_descenso_puerta', 'Yoga del Descenso · Libro Puerta'), bk('yoga_descenso_morada', 'Yoga del Descenso · Libro de la Morada'), bk('llama_encarnada', 'La Llama Encarnada'))}
<p style="margin-top:18px"><a class="btn" href="{ext(FC, lang)}">{L('Discover the Flame Codex ↗', 'Conoce el Códice de la Llama ↗')}</a></p>
<p class="eyebrow" style="margin-top:60px">{L('NOVELS AND STORIES', 'NOVELAS E HISTORIAS')}</p><h2>{L('Spiritual fiction', 'Ficción espiritual')}</h2>
{g(bk('selarin', 'Selarín'), bk('dipti_la_invasora_esperada', 'DIPTI · La invasora esperada'), bk('zendrick_virtudes_khudday', 'Zendrick y las virtudes del Khudday'), bk('zendrick_ii_cinco_virtudes', 'Zendrick II y las cinco virtudes'), bk('zendrick_iii_batalla_xino', 'Zendrick III · La batalla de Xino'), bk('la_busqueda_del_rey', 'La búsqueda del rey'))}
</div></section>
'''

CREDS = {'en': ['Board-certified in biofeedback', 'Certified by the board of natural medicine of North America', 'Reverend'],
         'es': ['Certificado por el board de biofeedback', 'Certificado por el board de medicina natural de Norteamérica', 'Reverendo']}

def honors(lang):
    L = Lx(lang)
    figs = [('award_aapna_ceremony.jpg', L('Dhanwantari Award', 'Premio Dhanwantari'), L('AAPNA · Association of Ayurvedic Professionals of North America · 2025', 'AAPNA · Asociación de Profesionales Ayurvédicos de Norteamérica · 2025')),
            ('award_aapna_temple.jpg', 'AAPNA 2025', L('Ayurveda and the Mind, Pennsylvania', 'Ayurveda and the Mind, Pensilvania')),
            ('award_siisdet.jpg', L('Leader in Health Sciences', 'Líder en Ciencias de la Salud'), L('Health Sciences Awards · Santander, Spain · 2022', 'Health Sciences Awards · Santander, España · 2022')),
            ('award_lifestyle.jpg', 'Lifestyle Plus Awards', 'Lifestyle Plus Magazine')]
    stats = [('60,000+' if lang == 'en' else '60.000+', L('hours of meditation', 'horas de meditación')), ('12½', L('years in India', 'años en la India')), ('8', L('years in Thailand', 'años en Tailandia')), ('12,000+' if lang == 'en' else '12.000+', L('people initiated into meditation', 'personas iniciadas en la meditación'))]
    f = ''.join(f'<figure><img src="{I}{im}" alt="{a}" loading="lazy"><figcaption><b>{a}</b><span>{b}</span></figcaption></figure>' for im, a, b in figs)
    s = ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in stats)
    return f'''<section class="honors"><div class="wrap">
<p class="eyebrow">{L('RECOGNITION', 'RECONOCIMIENTOS')}</p><h2>{L('Honored for his work', 'Reconocido por su trabajo')}</h2>
<p class="sub">{L('International recognition for integrating Ayurveda, quantum medicine and consciousness in the service of healing.', 'Reconocimiento internacional por integrar la Ayurveda, la medicina cuántica y la consciencia al servicio de la sanación.')}</p>
<div class="row">{f}</div>
<div class="stats">{s}</div>
<div class="creds">{''.join(f'<span>{c}</span>' for c in CREDS[lang])}</div>
<p class="center" style="margin-top:26px"><a class="btn" href="{url(lang, 'recognition')}">{L('Recognition and studies', 'Reconocimientos y formación')}</a></p>
</div></section>
'''

TESTI = [
 ("Conocer a Zulu es una gran bendición en mi vida y en la de mi familia.", "Knowing Zulu is a great blessing in my life and in my family's.", "Astrid Ramírez", "Ecuador"),
 ("Zuluan ha sido, es y seguirá siendo un mentor.", "Zuluan has been, is and will always be a mentor.", "Gina Moreno", "Colombia"),
 ("Conocí a Zuluan en un momento difícil de mi vida.", "I met Zuluan at a difficult moment in my life.", "Jennifer Peterson Hunter", "USA"),
 ("En mis años de formación con Zuluan, he transformado mi vida y mi visión de ella, me siento plena y con propósito.", "In my years of training with Zuluan I have transformed my life and the way I see it. I feel whole and full of purpose.", "Diana Collazos", "Colombia"),
 ("Conocer a el Dr Zuluan ha sido de un beneficio tremendo para mí en todo nivel.", "Meeting Dr. Zuluan has been a tremendous benefit to me on every level.", "Sangudy Lowe", "Miami"),
 ("Zuluan is awakened amazing Being.", "", "Kuro", "Hawaii"),
]

def testimonials(lang):
    L = Lx(lang)
    cards = ''
    for es, en, name, place in TESTI:
        tr = f'<p class="note" style="margin-top:6px">{en}</p>' if (lang == 'en' and en) else ''
        cards += f'<div class="card"><blockquote style="margin:0 0 10px;font-size:21px">“{es}”</blockquote>{tr}<p class="eyebrow" style="margin:12px 0 0">{name} · {place}</p></div>'
    return f'<section class="alt"><div class="wrap"><p class="eyebrow center">{L("IN THEIR WORDS", "EN SUS PALABRAS")}</p><h2 class="center">{L("What people say", "Lo que dicen")}</h2><div class="grid3" style="margin-top:30px">{cards}</div></div></section>\n'

def sbcta(lang, cls='left'):
    L = Lx(lang)
    return f'''<div class="sbcta {cls}"><p class="q">{L('Looking for therapy or personal work?', '¿Buscas terapia o trabajo personal?')}</p>
<a class="btn gold" href="{ext(SB, lang)}">{L('Visit Spiritual Balance &middot; Therapy &amp; personal sessions &#8599;', 'Visita Spiritual Balance &middot; Terapias y trabajo personal &#8599;')}</a>
<p class="a">{L('If you are seeking the spiritual teaching, stay here.', 'Si buscas la enseñanza espiritual, quédate aquí.')}</p></div>'''

# ------------------------------------------------------------------ HOME
def home(lang):
    L = Lx(lang)
    v = '?v=1'
    anchor = L('welcome', 'bienvenida')
    # 1) the doctor himself, filling the first screen; 2) his words; 3) the honors
    return f'''<section class="dzopen" aria-label="Dr. Zuluan Orion">
<picture>
<source media="(max-aspect-ratio: 4/5)" srcset="{I}hero_home-t720.jpg{v} 720w, {I}hero_home-t1080.jpg{v} 1080w" sizes="100vw">
<img src="{I}hero_home-w1800.jpg{v}" srcset="{I}hero_home-w1200.jpg{v} 1200w, {I}hero_home-w1800.jpg{v} 1800w, {I}hero_home-w2400.jpg{v} 2400w, {I}hero_home-w2990.jpg{v} 2990w" sizes="100vw" width="2990" height="1717" alt="Dr. Zuluan Orion" fetchpriority="high">
</picture>
<a class="cue" href="#{anchor}" aria-label="{L('Continue', 'Continuar')}"><svg viewBox="0 0 24 24" width="28" height="28" aria-hidden="true"><path d="M5 9l7 7 7-7" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
</section>
<section class="hero dzintro" id="{anchor}"><div class="wrap">
<p class="kicker">{L('SPIRITUAL GUIDE · PHYSICIAN · AUTHOR', 'GUÍA ESPIRITUAL · MÉDICO · AUTOR')}</p>
<h1>Dr. Zuluan Orion</h1>
<p class="sub">{L('Ayurveda · Natural and quantum medicine · Meditation · Illumination', 'Ayurveda · Medicina natural y cuántica · Meditación · Iluminación')}</p>
<p class="lede">{L('I was born in Bogotá in 1971. My life has been a path toward illumination: meditation, the masters of India and Thailand, a medicine that cares for body and soul, and a question that never let me go: <em>who am I?</em> I invite you to walk it with me.',
                   'Nací en Bogotá en 1971. Mi vida ha sido un camino hacia la iluminación: la meditación, los maestros de la India y Tailandia, una medicina que cuida el cuerpo y el alma, y una pregunta que nunca me soltó: <em>¿quién soy?</em> Te invito a recorrerlo conmigo.')}</p>
<div class="btns"><a class="btn solid" href="{url(lang, 'story')}">{L('My story', 'Mi historia')}</a><a class="btn" href="{url(lang, 'illumination')}">{L('Illumination', 'Iluminación')}</a><a class="btn" href="{ext(FC, lang)}">{L('The Flame Codex ↗', 'El Códice de la Llama ↗')}</a></div>
{sbcta(lang, '')}
</div></section>
{honors(lang)}
<section><div class="wrap">
<p class="eyebrow center">{L('THREE DOORS', 'TRES PUERTAS')}</p>
<h2 class="center">{L('Where would you like to begin?', '¿Por dónde quieres comenzar?')}</h2>
<div class="doors">
<a class="door" href="{url(lang, 'illumination')}"><img src="{I}portrait_side.jpg" alt="" loading="lazy"><div><p class="eyebrow">{L('THE TEACHING', 'LA ENSEÑANZA')}</p><h3>{L('Illumination', 'Iluminación')}</h3><p>{L('The nondual teaching: recognizing what you are, in the middle of your own life. Satsang and darshan.', 'La enseñanza no dual: reconocer lo que eres, en medio de tu propia vida. Satsang y darshan.')}</p><span class="more">{L('ENTER →', 'ENTRAR →')}</span></div></a>
<a class="door" href="{ext(FC, lang)}"><img src="{I}llaves/ahr.webp" alt="AHR" loading="lazy" class="plate"><div><p class="eyebrow">{L('THE SACRED LANGUAGE', 'EL LENGUAJE SAGRADO')}</p><h3>{L('The Flame Codex', 'El Códice de la Llama')}</h3><p>{L('A language of 177 keys born of the Descent of the Flame, with its Light Code meditation.', 'Un lenguaje de 177 llaves nacido del Descenso de la Llama, con su meditación de Códigos de Luz.')}</p><span class="more">{L('VISIT ↗', 'VISITAR ↗')}</span></div></a>
<a class="door" href="{ext(SB, lang)}"><img src="{I}logo_spiritual_balance.webp" alt="Spiritual Balance" loading="lazy" class="sig"><div><p class="eyebrow">{L('THE CLINIC · WESTON, FLORIDA', 'LA CLÍNICA · WESTON, FLORIDA')}</p><h3>Spiritual Balance</h3><p>{L('Therapy and personal work: Quantum Transformation, Ayurveda, Panchakarma and energy therapies.', 'Terapias y trabajo personal: Transformación Cuántica, Ayurveda, Panchakarma y terapias energéticas.')}</p><span class="more">{L('VISIT ↗', 'VISITAR ↗')}</span></div></a>
</div>
</div></section>

<section class="alt"><div class="wrap grid2">
<figure><img class="portrait" src="{I}zuluan_outdoor_purple.jpg" alt="Dr. Zuluan Orion" loading="lazy"></figure>
<div>
<p class="eyebrow">{L('MY STORY', 'MI HISTORIA')}</p>
<h2>{L('A life of practice', 'Una vida de práctica')}</h2>
<p>{L('More than sixty thousand hours of meditation. Almost two decades in Asia: twelve and a half years in India and eight in Thailand. Masters of Kriya Yoga, shaktipat, Vedic meditation and Buddhism, the Kalachakra of His Holiness the Dalai Lama, and an awakening to the Self that has not reversed in nearly thirty years.',
      'Más de sesenta mil horas de meditación. Casi dos décadas en Asia: doce años y medio en la India y ocho en Tailandia. Maestros de Kriya Yoga, shaktipat, meditación védica y budismo, el Kalachakra de Su Santidad el Dalai Lama, y un despertar al Ser que no se ha revertido en casi treinta años.')}</p>
<p>{L('And then, much later, the Descent of the Flame. From there were born the Flame Codex and the work I share today.', 'Y después, mucho más tarde, el Descenso de la Llama. De ahí nacieron el Códice de la Llama y el trabajo que hoy comparto.')}</p>
<p><a class="btn" href="{url(lang, 'story')}">{L('Read my story', 'Leer mi historia')}</a></p>
</div>
</div></section>

<section class="dark"><div class="narrow center">
<blockquote style="border:0;padding:0;font-size:1.25em">{L('If my presence and my experience can help you recognize more clearly what you are, and live from there with more love and freedom, that is the meaning of my service.', 'Si mi presencia y mi experiencia pueden ayudarte a reconocer con mayor claridad lo que eres, y a vivir desde allí con más amor y libertad, ese es el sentido de mi servicio.')}</blockquote>
<p class="eyebrow" style="margin-top:18px">Dr. Zuluan Orion</p>
</div></section>

<section><div class="wrap">
<p class="eyebrow">{L('BOOKS', 'LIBROS')}</p>
<h2>{L('More than twenty books', 'Más de veinte libros')}</h2>
<div class="books shelf">{bk('iluminacion', 'Iluminación')}{bk('transformacion_cuantica', 'Transformación Cuántica')}{bk('meditacion_cuantica', 'Meditación Cuántica')}{bk('codice1', 'El Códice de la Llama · Vol. I')}{bk('llama_encarnada', 'La Llama Encarnada')}</div>
<p style="margin-top:18px"><a class="btn" href="{url(lang, 'books')}">{L('See all the books', 'Ver todos los libros')}</a></p>
</div></section>

<section class="ba" style="padding:0;text-align:left"><div style="position:relative">
<img src="{I}viajes/grupo_01.jpg" alt="Chiang Mai" style="width:100%;height:min(60vh,520px);object-fit:cover;object-position:center 35%;display:block;opacity:.45" loading="lazy">
<div class="wrap" style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;max-width:1120px">
<p class="eyebrow" style="color:var(--gold2)">{L('JOURNEYS AND RETREATS · JUNE 2027', 'VIAJES Y RETIROS · JUNIO 2027')}</p>
<h2 style="font-size:clamp(28px,4.5vw,48px);margin:0 0 12px">{L('Thailand and India, with me', 'Tailandia y la India, conmigo')}</h2>
<p style="font-size:clamp(17px,2vw,22px);max-width:640px;color:#F1E9FA">{L('A holistic retreat in Chiang Mai and a pilgrimage through Northern India. Small groups, sacred places, silence and integration.', 'Un retiro holístico en Chiang Mai y una peregrinación por el norte de la India. Grupos pequeños, lugares sagrados, silencio e integración.')}</p>
<p><a class="btn solid" href="{url(lang, 'journeys')}">{L('See the journeys', 'Ver los viajes')}</a></p>
</div></div></section>
{testimonials(lang)}
{blog.teaser(lang)}
<section><div class="narrow center">
<p class="eyebrow">{L('CONTACT', 'CONTACTO')}</p>
<h2>{L('Write to me', 'Escríbeme')}</h2>
<p>{L('For the teaching, the books, satsang, journeys or talks:', 'Para la enseñanza, los libros, el satsang, los viajes o las conferencias:')}</p>
<p><a class="btn solid" href="mailto:zuluanorion@gmail.com">zuluanorion@gmail.com</a> <a class="btn" href="tel:+19546680348">(954) 668-0348</a></p>
</div></section>
'''

# ------------------------------------------------------------------ MY STORY
def story(lang):
    L = Lx(lang)
    tl = [
        ('1971', L('Born in Bogotá, Colombia.', 'Nazco en Bogotá, Colombia.')),
        ('1991', L('I travel to England, where I study Celtic magic with RJ Stuart.', 'Viajo a Inglaterra, donde estudio magia celta con RJ Stuart.')),
        (L('Age 23', 'A los 23'), L('A meditation course that Bob Fickes was teaching in Thailand opens the door to Asia.', 'Un curso de meditación que Bob Fickes dictaba en Tailandia me abre la puerta de Asia.')),
        ('1996', L('Bali, Indonesia: I train as a teacher of bija mantra meditation.', 'Bali, Indonesia: me formo como maestro de meditación con bija mantra.')),
        ('1998', L('Mahayana Buddhism with the monk and master Kruba Wom. The Atharva Veda in New Delhi. In India I practise yoga and meditation and study Ayurvedic medicine.', 'Budismo Mahayana con el monje y maestro Kruba Wom. El Atharva Veda en Nueva Delhi. En la India practico yoga y meditación y estudio medicina ayurvédica.')),
        ('2000', L('I study beside Dr. Reddy Kumar, today a friend and a respected Ayurvedic physician in India.', 'Estudio al lado del Dr. Reddy Kumar, hoy amigo y respetado médico ayurvédico de la India.')),
        ('2001', L('Pilgrimage to the Kumbh Mela.', 'Peregrinación a la Kumbh Mela.')),
        ('2004–2010', L('Thailand: I live in San Kamphaeng, very close to Me Pat, a channel of the Medicine Buddha since she was eighteen, who teaches healing through the devas and the angelic presences. I learn and work beside her until 2010.', 'Tailandia: vivo en San Kamphaeng, muy cerca de Me Pat, canal del Buda de la Medicina desde sus dieciocho años, que enseña la sanación a través de los devas y las presencias angélicas. Aprendo y trabajo a su lado hasta 2010.')),
        ('2006', L('I receive the Kalachakra empowerment from His Holiness the Dalai Lama.', 'Recibo la iniciación del Kalachakra de Su Santidad el Dalai Lama.')),
        ('2013', L('Doctorate in Natural Medicine and Doctorate in Humanitarian Services, World Organization of Natural Medicine.', 'Doctorado en Medicina Natural y Doctorado en Servicios Humanitarios, World Organization of Natural Medicine.')),
        ('2014', L('PhD in Quantum Medicine, a doctorate the university prepared especially for me. Since then, my clinic in Weston, Florida: today Spiritual Balance.', 'PhD en Medicina Cuántica, un doctorado que la universidad preparó especialmente para mí. Desde entonces, mi clínica en Weston, Florida: hoy Spiritual Balance.')),
        ('2022', L('Health Sciences Awards, Santander, Spain: Leader in Research and Health Sciences for the Benefit of Mankind.', 'Health Sciences Awards, Santander, España: Líder en Investigación y Ciencias de la Salud en Beneficio de la Humanidad.')),
        ('2025', L('Dhanwantari Award, AAPNA. The first journey to Thailand with a group.', 'Premio Dhanwantari, AAPNA. El primer viaje a Tailandia con un grupo.')),
        ('2025–2026', L('From 29 March 2025 to 26 January 2026, the year of the Incarnate Flame. From the Descent, the Flame Codex is born.', 'Del 29 de marzo de 2025 al 26 de enero de 2026, el año de la Llama Encarnada. Del Descenso nace el Códice de la Llama.')),
    ]
    tlh = ''.join(f'<li><b>{y}</b><span>{t}</span></li>' for y, t in tl)
    return f'''<section><div class="wrap grid2 top">
<figure><img class="portrait" src="{I}portrait_front.jpg" alt="Dr. Zuluan Orion"></figure>
<div>
<p class="eyebrow">{L('IN SHORT', 'EN POCAS PALABRAS')}</p>
<p class="lead">{L('More than sixty thousand hours of meditation. Almost two decades living and studying in Asia: twelve and a half years in India and eight in Thailand. Initiation in Kriya Yoga, shaktipat, Vedic meditation and the Kalachakra. An awakening to the Self, <em>I Am That</em>, that has not reversed in nearly thirty years.',
                   'Más de sesenta mil horas de meditación. Casi dos décadas viviendo y estudiando en Asia: doce años y medio en la India y ocho en Tailandia. Iniciación en Kriya Yoga, shaktipat, meditación védica y Kalachakra. Un despertar al Ser, <em>Yo Soy Eso</em>, que no se ha revertido en casi treinta años.')}</p>
<p>{L('And then, much later, the descent: Consciousness entering the body as fire, then as cool fire, settling in the root. The Flame Codex was born inside that descent.', 'Y después, mucho más tarde, el descenso: la Consciencia entrando en el cuerpo como fuego, luego como fuego frío, asentándose en la raíz. El Códice de la Llama nació dentro de ese descenso.')}</p>
</div>
</div></section>

<section class="dark"><div class="wrap">
<div class="stats">
<div><b>{'60,000+' if lang == 'en' else '60.000+'}</b><span>{L('hours of meditation', 'horas de meditación')}</span></div>
<div><b>12½</b><span>{L('years in India', 'años en la India')}</span></div>
<div><b>8</b><span>{L('years in Thailand', 'años en Tailandia')}</span></div>
<div><b>{'12,000+' if lang == 'en' else '12.000+'}</b><span>{L('people initiated into meditation', 'personas iniciadas en meditación')}</span></div>
</div>
</div></section>

<section><div class="narrow">
<h2 style="margin-top:0">{L('A life of practice', 'Una vida de práctica')}</h2>
<p>{L('This work did not begin as a book. It began as a life. I grew up in Bogotá in a hard home, and the void it left in my heart became the beginning of a spiritual path: I needed to find something, though I did not know what. For most of my life the central question was not academic. It was a wound and a fire.',
      'Esta obra no comenzó como un libro. Comenzó como una vida. Crecí en Bogotá en un hogar difícil, y el vacío que dejó en mi corazón se convirtió en el comienzo de un camino espiritual: necesitaba encontrar algo, aunque no sabía qué. Durante la mayor parte de mi vida la pregunta central no fue académica. Fue una herida y un fuego.')}</p>
<p>{L('My way into Asia opened at twenty-three, through a meditation course that Bob Fickes was teaching in Thailand. There I spent a year learning ancient meditation techniques, meditating sixteen to twenty hours a day. In India I lived twelve and a half years and studied Ayurvedic medicine, graduating as a Bachelor of Ayurvedic Medicine and Science (B.A.M.S.) and receiving the title of Vachaspati, known in the West as MD in Ayurveda. In Thailand, all together, I lived eight years. Almost two decades in Asia.',
      'Mi camino hacia Asia se abrió a los veintitrés años, con un curso de meditación que Bob Fickes dictaba en Tailandia. Allí pasé un año aprendiendo técnicas milenarias de meditación, meditando de dieciséis a veinte horas al día. En la India viví doce años y medio y estudié medicina ayurvédica, graduándome como Licenciado en Medicina y Ciencia Ayurvédica (B.A.M.S.) y recibiendo el título de Vachaspati, conocido en Occidente como MD en Ayurveda. En Tailandia, en total, viví ocho años. Casi dos décadas en Asia.')}</p>
<p>{L('I have sat in meditation for more than sixty thousand hours. I have initiated more than twelve thousand people into different systems of meditation, and I have spent more than twenty years in healing rooms, seeing the same pattern again and again: what feels like reality itself turns out to be a cage, and beneath the cage something alive remains.',
      'He meditado más de sesenta mil horas. He iniciado a más de doce mil personas en distintos sistemas de meditación, y llevo más de veinte años en salas de sanación, viendo el mismo patrón una y otra vez: lo que se siente como la realidad misma resulta ser una jaula, y debajo de la jaula algo vivo permanece.')}</p>
</div></section>

<section class="alt"><div class="narrow">
<p class="eyebrow">{L('THE PATH, YEAR BY YEAR', 'EL CAMINO, AÑO POR AÑO')}</p>
<h2>{L('A timeline', 'Una línea de vida')}</h2>
<ol class="tl">{tlh}</ol>
</div></section>

<section><div class="narrow">
<h2 style="margin-top:0">{L('The masters and the streams', 'Los maestros y las corrientes')}</h2>
<ul class="lineage">
<li><b>Ramana Maharshi {L('and', 'y')} Papaji</b>: {L('the direct nondual path. Turn inward and discover what you truly are. Not as belief. As recognition.', 'el camino directo no dual. Vuelve hacia adentro y descubre lo que eres en verdad. No como creencia. Como reconocimiento.')}</li>
<li><b>Kriya Yoga</b>: {L('through Lahiri Mahasaya, Sri Yukteswar, Paramahansa Yogananda and Paramahamsa Hariharananda, who initiated me and with whom I meditated for more than a year in his house in Kendall, Florida. <em>«Meditate, meditate, meditate and become aware of God.»</em>', 'a través de Lahiri Mahasaya, Sri Yukteswar, Paramahansa Yogananda y Paramahamsa Hariharananda, quien me inició y con quien medité durante más de un año en su casa de Kendall, Florida. <em>«Medita, medita, medita y toma consciencia de Dios.»</em>')}</li>
<li><b>{L('Vedic meditation', 'Meditación védica')}</b>: {L('through Bob Fickes, a teacher who became a brother and a friend.', 'a través de Bob Fickes, un maestro que llegó a ser hermano y amigo.')}</li>
<li><b>Shaktipat</b>: {L('through the living stream of Shri Dhyanyogi Madhusudandas: awakening as transmission, current and inner fire.', 'a través de la corriente viva de Shri Dhyanyogi Madhusudandas: el despertar como transmisión, corriente y fuego interior.')}</li>
<li><b>{L('Buddhism', 'Budismo')}</b>: {L('with master Chen Yen Lu; Mahayana with the monk Kruba Wom; a long friendship with the monk Kruba Tuang; and the Kalachakra empowerment of His Holiness the Dalai Lama.', 'con el maestro Chen Yen Lu; el Mahayana con el monje Kruba Wom; una larga amistad con el monje Kruba Tuang; y la iniciación del Kalachakra de Su Santidad el Dalai Lama.')}</li>
<li><b>{L('Healing with the devas', 'Sanación con los devas')}</b>: {L('beside Me Pat, a channel of the Medicine Buddha, in Thailand.', 'junto a Me Pat, canal del Buda de la Medicina, en Tailandia.')}</li>
<li><b>{L('The Western streams', 'Las corrientes de Occidente')}</b>: {L('Celtic magic with RJ Stuart in England, and the teachings of Elizabeth Prophet and Luis de la Lama.', 'la magia celta con RJ Stuart en Inglaterra, y las enseñanzas de Elizabeth Prophet y Luis de la Lama.')}</li>
<li><b>{L('Embodied awakening', 'Despertar encarnado')}</b>: {L('Saniel Bonder, Phil Servedio and Nick Arjuna Ardagh, in whose presence I awakened.', 'Saniel Bonder, Phil Servedio y Nick Arjuna Ardagh, en cuya presencia desperté.')}</li>
<li><b>Sunburst</b>: {L('Norman Paulsen, through the Sun Meditation, who refined my Kriya practice.', 'Norman Paulsen, a través de la Meditación del Sol, quien refinó mi práctica de Kriya.')}</li>
</ul>
<p class="note">{L('I name these streams with gratitude, not as a claim of endorsement. They prepared the vessel. Life tested the vessel.', 'Nombro estas corrientes con gratitud, no como una afirmación de respaldo. Prepararon la vasija. La vida puso a prueba la vasija.')}</p>

<h2>{L('The awakening', 'El despertar')}</h2>
<p>{L('It opened in stages. On a night of meditation on the central stone of the Great Pyramid the kundalini rose along my spine, and a blue pearl in my chest kept asking <em>«Who am I?»</em>, and something within answered, every time, <em>«You are.»</em> Eight months later, in the most ordinary moment: <em>the mind has no being of its own.</em>',
      'Se abrió por etapas. Una noche de meditación sobre la piedra central de la Gran Pirámide, la kundalini subió por mi columna, y una perla azul en mi pecho preguntaba una y otra vez <em>«¿Quién soy yo?»</em>, y algo dentro respondía, cada vez, <em>«Tú eres.»</em> Ocho meses después, en el momento más ordinario: <em>la mente no tiene ser propio.</em>')}</p>
<p>{L('Then I saw that my tireless search had built a new identity, the seeker, and I gave it up. I put away the books, took down the altars, went to work as an engineer and let everything rest. On my birthday, in a simple exercise at Arjuna&rsquo;s seminar, my heart opened into <em>I Am That</em>, and I laughed: <em>«It can&rsquo;t be that easy.»</em> One with everything, without separation.',
      'Entonces vi que mi búsqueda incansable había construido una nueva identidad, el buscador, y la dejé. Guardé los libros, desmonté los altares, me fui a trabajar como ingeniero y dejé que todo descansara. El día de mi cumpleaños, en un ejercicio sencillo en el seminario de Arjuna, mi corazón se abrió al <em>Yo Soy Eso</em>, y me reí: <em>«No puede ser tan fácil.»</em> Uno con todo, sin separación.')}</p>
<p><a class="btn" href="{url(lang, 'illumination')}">{L('Illumination: the nondual teaching', 'Iluminación: la enseñanza no dual')}</a></p>

<h2>{L('The vessel must be transformed', 'La vasija debe transformarse')}</h2>
<p>{L('The vessel was transformed through life: years in Asia, years of practice and healing work, and years of real trial, seasons that were neither peaceful nor luminous. Those years taught me that discernment is not optional, that spiritual power without humility is dangerous, and that the deepest service is not to make people believe in you, but to return them to their own light.',
      'La vasija se transformó a través de la vida: años en Asia, años de práctica y de trabajo sanador, y años de prueba real, temporadas que no fueron pacíficas ni luminosas. Esos años me enseñaron que el discernimiento no es opcional, que el poder espiritual sin humildad es peligroso, y que el servicio más hondo no consiste en lograr que las personas crean en ti, sino en devolverlas a su propia luz.')}</p>

<h2>{L('The Descent of the Flame', 'El Descenso de la Llama')}</h2>
<p>{L('For twenty-eight years I lived from the recognition of nondual consciousness. Over the years I understood that this awakening still had a depth to reveal. I call that movement the Descent of the Flame. It came by Grace, after many years of practice, devotion and integration, without my being able to program it: a presence asking for room within my humanity, in the mind, in the heart, in vitality and, in an especially deep way, in the root.',
      'Durante veintiocho años viví desde el reconocimiento de la consciencia no dual. Con los años comprendí que ese despertar todavía tenía una profundidad por revelar. A ese movimiento lo llamo el Descenso de la Llama. Llegó por Gracia, después de muchos años de práctica, devoción e integración, sin que yo pudiera programarlo: una presencia que pedía lugar dentro de mi humanidad, en la mente, en el corazón, en la vitalidad y, de manera especialmente profunda, en la raíz.')}</p>
<p><a class="btn" href="{FC}{'/es/' if lang == 'es' else '/'}descent/">{L('Read the full account in the Flame Codex ↗', 'Lee el relato completo en el Códice de la Llama ↗')}</a></p>
</div></section>

<section class="alt"><div class="wrap grid2 top">
<div>
<p class="eyebrow">{L('MY WORK', 'MI TRABAJO')}</p>
<h2>{L('Healing, teaching and accompanying', 'Sanar, enseñar y acompañar')}</h2>
<p>{L('I am the originator of Quantum Transformation, the system I created to guide the soul to purify itself, unblock its energy and reconnect with the Spirit. I direct Spiritual Balance, my clinic in Weston, Florida, where I integrate Ayurvedic, natural and quantum medicine with biofeedback, bio-resonance and GDV technology, and where people arrive from many parts of the world.',
      'Soy el originador de la Transformación Cuántica, el sistema que creé para guiar al alma a depurarse, desbloquear su energía y reconectar con el Espíritu. Dirijo Spiritual Balance, mi clínica en Weston, Florida, donde integro la medicina ayurvédica, natural y cuántica con la tecnología de biofeedback, biorresonancia y GDV, y adonde llegan personas de muchas partes del mundo.')}</p>
<p>{L('I developed Archangelical Touch, an energy system that helps people channel the energy of the five elements and the different rays of the spectrum. My doctoral thesis was on the transformation of negative archetypes into positive archetypes, and it is used in therapy. For many years I have worked in the cleansing of cellular memory.',
      'Desarrollé el Toque Arcangélico (Archangelical Touch), un sistema energético que ayuda a canalizar la energía de los cinco elementos y los distintos rayos del espectro. Mi tesis doctoral trató sobre la transformación de arquetipos negativos en arquetipos positivos, y se usa en terapia. Desde hace muchos años trabajo en la limpieza de la memoria celular.')}</p>
<p>{L('I am board-certified in biofeedback and certified by the board of natural medicine of North America. I am also a reverend.', 'Estoy certificado por el board de biofeedback y por el board de medicina natural de Norteamérica. También soy reverendo.')}</p>
<p>{L('Some years ago, one of my patients shared their testimony of life on a well-known national program in the United States, telling how their health had been transformed. That story touched many people.',
      'Hace unos años, uno de mis pacientes compartió su testimonio de vida en un conocido programa nacional de los Estados Unidos, contando cómo se había transformado su salud. Su historia conmovió a muchas personas.')}</p>
<p>{L('During the long lockdown of the pandemic I offered emotional support through social media to the people who were affected, reminding them that connecting with themselves helps us pass through depression and anxiety.',
      'Durante el largo encierro de la pandemia di soporte emocional, a través de las redes sociales, a las personas que se vieron afectadas, recordándoles que conectar consigo mismas ayuda a atravesar la depresión y la ansiedad.')}</p>
<p><a class="btn solid" href="{ext(SB, lang)}">{L('Spiritual Balance ↗', 'Spiritual Balance ↗')}</a></p>
</div>
<figure><img class="portrait" src="{I}zuluan_tuning_forks.jpg" alt="Dr. Zuluan Orion" loading="lazy"><figcaption>{L('In my clinic in Weston, Florida.', 'En mi clínica de Weston, Florida.')}</figcaption></figure>
</div></section>

<section><div class="narrow">
<h2 style="margin-top:0">{L('What I do not claim', 'Lo que no afirmo')}</h2>
<p>{L('I am not special. I am not chosen. I am a finite form through which the Divine is coming to know itself. What I share is not for making anyone a master; it is for returning each person to the light they never lost.',
      'No soy especial. No soy elegido. Soy una forma finita a través de la cual lo Divino se está conociendo. Lo que comparto no existe para convertir a nadie en maestro; existe para devolver a cada persona a la luz que nunca perdió.')}</p>
<blockquote>{L('The root is the throne. The heart is the love. The crown is the knowing.', 'La raíz es el trono. El corazón es el amor. La corona es el saber.')}</blockquote>
<p class="center"><a class="btn" href="{url(lang, 'recognition')}">{L('Recognition and studies', 'Reconocimientos y formación')}</a></p>
</div></section>
'''

# ------------------------------------------------------------------ ILLUMINATION
def illumination(lang):
    L = Lx(lang)
    return f'''<section><div class="narrow center">
<p class="eyebrow">{L('ILLUMINATION · THE NONDUAL TEACHING', 'ILUMINACIÓN · LA ENSEÑANZA NO DUAL')}</p>
<p class="lead">{L('The teaching I share in <em>Illumination</em> is born of a very intimate question:', 'La enseñanza que comparto en <em>Iluminación</em> nace de una pregunta muy íntima:')}</p>
<blockquote style="font-size:1.35em">{L('Who am I, beyond everything<br>I have learned to think about myself?', '¿Quién soy, más allá de todo<br>lo que he aprendido a pensar sobre mí?')}</blockquote>
</div></section>

<section class="alt"><div class="wrap grid2">
<figure><img class="portrait" src="{I}portrait_prayer.jpg" alt="Dr. Zuluan Orion"></figure>
<div>
<p class="eyebrow">{L('SELF-KNOWLEDGE', 'AUTOCONOCIMIENTO')}</p>
<h2>{L('The presence that observes', 'La presencia que observa')}</h2>
<p>{L('Self-knowledge begins when we stop to look and recognize that our thoughts, emotions and stories change, while there is a conscious presence that can observe them.', 'El autoconocimiento comienza cuando nos detenemos a mirar y reconocemos que nuestros pensamientos, emociones e historias cambian, mientras hay una presencia consciente que puede observarlos.')}</p>
<p>{L('I invite you to become familiar with that presence, to discover it in your own experience. That recognition can begin right here, in the middle of your life, with your questions, your difficulties and your humanity.', 'Te invito a familiarizarte con esa presencia, a descubrirla en tu propia experiencia. Ese reconocimiento puede comenzar aquí mismo, en medio de tu vida, con tus preguntas, tus dificultades y tu humanidad.')}</p>
</div>
</div></section>

<section><div class="narrow">
<p class="eyebrow">{L('THE RECOGNITION', 'EL RECONOCIMIENTO')}</p>
<h2>{L('Who is the one who looks?', '¿Quién es el que mira?')}</h2>
<p>{L('For years I lived as if the mind were the centre of my life. The mind searched, argued, suffered, desired, feared, interpreted, defended and named. And then attention turned toward the one who was aware of the mind.', 'Durante años viví como si la mente fuera el centro de mi vida. La mente buscaba, discutía, sufría, deseaba, temía, interpretaba, defendía, nombraba. Y entonces la atención se volvió hacia aquel que era consciente de la mente.')}</p>
<p>{L('Something loosened. The mind was seen as movement. The witness was seen as stillness. The personal self was seen as a wave within a greater ocean. The wave had never been separate from the ocean; it had only been fascinated by its own form.', 'Algo se aflojó. La mente fue vista como movimiento. El testigo fue visto como quietud. El yo personal fue visto como una ola dentro de un océano mayor. La ola nunca había estado separada del océano; solo había estado fascinada con su propia forma.')}</p>
<blockquote>{L('What is this life? What is suffering?<br>Who is the one who suffers? Who is the one who looks?<br>And what remains when the one who looks is finally seen?', '¿Qué es esta vida? ¿Qué es el sufrimiento?<br>¿Quién es el que sufre? ¿Quién es el que mira?<br>¿Y qué permanece cuando aquel que mira es por fin visto?')}</blockquote>
<h3>{L('Not a belief', 'No es una creencia')}</h3>
<p>{L('This recognition is not a doctrine to accept or a philosophy to defend. It is direct. It is what the great nondual teachers, Ramana Maharshi and Papaji, point to with a single question: turn inward and discover who or what you truly are. Not as belief. Not as spiritual clothing. As recognition.', 'Este reconocimiento no es una doctrina que aceptar ni una filosofía que defender. Es directo. Es aquello a lo que apuntan los grandes maestros no duales, Ramana Maharshi y Papaji, con una sola pregunta: vuelve hacia adentro y descubre quién o qué eres en verdad. No como creencia. No como vestidura espiritual. Como reconocimiento.')}</p>
<p>{L('When it happened for me it was simple, almost comic. I laughed: <em>«It can&rsquo;t be that easy.»</em> In the days that followed the personality was seen for what it is: an event within Consciousness. That recognition has not reversed in nearly thirty years.', 'Cuando me ocurrió fue sencillo, casi cómico. Me reí: <em>«No puede ser tan fácil.»</em> En los días que siguieron la personalidad fue vista como lo que es: un acontecimiento dentro de la Consciencia. Ese reconocimiento no se ha revertido en casi treinta años.')}</p>
<p>{L('The source of liberation is not the facilitator and it is not the method. The source is Consciousness itself. A wound does not heal because someone hands the person something. It frees itself because the person&rsquo;s own Consciousness recognizes what was false and returns to what was always true.', 'La fuente de la liberación no es el facilitador ni el método. La fuente es la Consciencia misma. La herida no sana porque alguien le entregue algo a la persona. Se libera porque la propia Consciencia de la persona reconoce lo que era falso y regresa a lo que siempre fue verdadero.')}</p>
</div></section>

<section class="dark"><div class="narrow">
<p class="eyebrow">{L('NONDUALITY', 'NO DUALIDAD')}</p>
<h2>{L('One same reality', 'Una misma realidad')}</h2>
<p>{L('As that relationship deepens, nonduality begins to take on a living meaning: the consciousness you recognize in yourself and the life you meet in others share in one same reality.', 'Al profundizar en esa relación, la no dualidad comienza a cobrar un sentido vivo: la consciencia que reconoces en ti y la vida que encuentras en los demás participan de una misma realidad.')}</p>
<p>{L('For me, this discovery opened a deeply loving relationship with God, with the Self, with what sustains us from within. That intimacy also becomes devotion, gratitude and a more sensitive way of being in the world.', 'Para mí, este descubrimiento abrió una relación profundamente amorosa con Dios, con el Ser, con aquello que nos sostiene desde dentro. Esa intimidad también se vuelve devoción, gratitud y una manera más sensible de estar en el mundo.')}</p>
<blockquote>{L('Awakening goes on maturing in how we live,<br>in how we pass through pain, listen to another person,<br>and allow love to find expression in everyday life.', 'El despertar continúa madurando en cómo vivimos,<br>en cómo atravesamos el dolor, escuchamos a otra persona<br>y permitimos que el amor encuentre expresión en lo cotidiano.')}</blockquote>
</div></section>

<section><div class="wrap">
<div class="narrow center" style="padding:0">
<p class="eyebrow">{L('MEETING IN TRUTH AND SILENCE', 'ENCUENTRO EN VERDAD Y SILENCIO')}</p>
<h2>Satsang &amp; Darshan</h2>
</div>
<div class="grid2 cards4" style="max-width:760px;margin:0 auto 30px">
<div class="card"><p class="eyebrow">SATSANG</p><h3>{L('Exploring together', 'Explorar juntos')}</h3><p>{L('The meeting in which we explore together the truth of what we are.', 'El encuentro para explorar juntos la verdad de lo que somos.')}</p></div>
<div class="card"><p class="eyebrow">DARSHAN</p><h3>{L('Presence and silence', 'Presencia y silencio')}</h3><p>{L('A contemplative meeting where presence and silence have their place.', 'El encuentro contemplativo donde la presencia y el silencio tienen su lugar.')}</p></div>
</div>
<div class="narrow" style="padding:0">
<p>{L('That is why I value them so much. The company of someone who has recognized their own nature can help us discover, more simply, what we are still seeking. On my own path, sharing with beings who had awakened was a blessing: sometimes a question, a glance or a moment of silence allowed something to become evident.', 'Por eso valoro tanto el satsang y el darshan. La compañía de alguien que ha reconocido su propia naturaleza puede ayudarnos a descubrir con más sencillez aquello que todavía buscamos. En mi camino, compartir con seres que habían despertado fue una bendición: a veces una pregunta, una mirada o un momento de silencio permitió que algo se hiciera evidente.')}</p>
<p>{L('Such accompaniment has value when it returns us to our own experience and strengthens our inner freedom.', 'Ese acompañamiento tiene valor cuando nos devuelve a nuestra propia experiencia y fortalece nuestra libertad interior.')}</p>
<p class="center" style="font-style:italic;color:var(--violet);font-size:1.15em">{L('Recognition has its own time; Grace cannot be forced.', 'El reconocimiento tiene su tiempo; la Gracia no puede forzarse.')}</p>
</div>
</div></section>

<section class="alt"><div class="wrap grid2">
<div class="books shelf one">{bk('iluminacion', 'Iluminación', L('A path toward the realization of the Self', 'Un camino hacia la realización del Ser'))}</div>
<div>
<p class="eyebrow">{L('MY SERVICE', 'MI SERVICIO')}</p>
<h2>{L('A close and human meeting', 'Un encuentro cercano y humano')}</h2>
<p>{L('From what I have lived, I am here to serve in that function: to offer a space where we can meet with honesty, ask questions, share silence and look together.', 'Desde lo que he vivido, estoy aquí para servir en esa función: ofrecer un espacio donde podamos encontrarnos con honestidad, hacer preguntas, compartir silencio y mirar juntos.')}</p>
<p>{L('I too have known the search, the confusion and the pain; that is why it matters to me that this meeting be close and human. What I share goes on maturing in my own life.', 'Yo también he conocido la búsqueda, la confusión y el dolor; por eso me importa que este encuentro sea cercano y humano. Lo que comparto sigue madurando en mi propia vida.')}</p>
<p>{L('If my presence and my experience can help you recognize more clearly what you are, and live from there with more love and freedom, that is the meaning of my service.', 'Si mi presencia y mi experiencia pueden ayudarte a reconocer con mayor claridad lo que eres, y a vivir desde allí con más amor y libertad, ese es el sentido de mi servicio.')}</p>
<div class="btns" style="justify-content:flex-start"><a class="btn solid" href="{url(lang, 'contact')}">{L('Write to me about satsang', 'Escríbeme sobre el satsang')}</a><a class="btn" href="{FC}{'/es/' if lang == 'es' else '/'}descent/">{L('Continue: the Descent of the Flame ↗', 'Continúa: el Descenso de la Llama ↗')}</a></div>
</div>
</div></section>
'''

# ------------------------------------------------------------------ RECOGNITION
def recognition(lang):
    L = Lx(lang)
    return f'''<section><div class="wrap">
<div class="award2">
<div class="pics"><img class="portrait" src="{I}award_aapna_ceremony.jpg" alt="" loading="lazy"><img class="portrait" src="{I}award_aapna_temple.jpg" alt="" loading="lazy"></div>
<div>
<p class="eyebrow">AAPNA · 4 {L('MAY', 'DE MAYO DE')} 2025</p>
<h2>{L('Dhanwantari Award', 'Premio Dhanwantari')}</h2>
<p>{L('Awarded by the Association of Ayurvedic Professionals of North America (AAPNA). The Dhanwantari Award is one of the highest recognitions given in Ayurveda internationally; I received it, with gratitude, for my work integrating Ayurveda with contemporary science.',
      'Otorgado por la Asociación de Profesionales Ayurvédicos de Norteamérica (AAPNA). El Premio Dhanwantari es uno de los más altos reconocimientos otorgados en el ámbito de la Ayurveda a nivel internacional; lo recibí, con gratitud, por mi trabajo al integrar la Ayurveda con la ciencia contemporánea.')}</p>
<p class="note">{L('AAPNA 2025 · Ayurveda and the Mind, Pennsylvania.', 'AAPNA 2025 · Ayurveda and the Mind, Pensilvania.')}</p>
</div>
</div>

<div class="award2 rev">
<div class="pics one"><img class="portrait" src="{I}award_siisdet.jpg" alt="" loading="lazy"></div>
<div>
<p class="eyebrow">HEALTH SCIENCES AWARDS 2021–2022 · SANTANDER, {L('SPAIN', 'ESPAÑA')}</p>
<h2>{L('Prize to the Leader in Research and Health Sciences for the Benefit of Mankind', 'Premio al Líder en Investigación y Ciencias de la Salud en Beneficio de la Humanidad')}</h2>
<p>{L('Received at the 7th Health Sciences Awards ceremony, on 5 June 2022, in the main auditorium of the Universidad Europea del Atlántico in Santander, after the VII International Medical-Scientific and Business Development Congress, «Reencuentro de Dos Continentes: Unificando Conceptos», held on 3 and 4 June 2022 in Torrelavega, Cantabria.',
      'Recibido en la 7.ª entrega de los Health Sciences Awards, el 5 de junio de 2022, en el auditorio principal de la Universidad Europea del Atlántico de Santander, después del VII Congreso Internacional Médico Científico y Desarrollo Empresarial, «Reencuentro de Dos Continentes: Unificando Conceptos», celebrado el 3 y 4 de junio de 2022 en Torrelavega, Cantabria.')}</p>
<p>{L('There I presented my work in Ayurvedic and Quantum Medicine in a paper broadcast to more than fifty-six countries, and took part in the categories Award for the Best Investigation Work 2022 and Best Scientific Poster 2022.',
      'Allí expuse mi trabajo en Medicina Ayurveda y Cuántica con una ponencia retransmitida en más de cincuenta y seis países, y participé por los reconocimientos al Mejor Trabajo de Investigación 2022 y al Mejor Póster Científico 2022.')}</p>
</div>
</div>

<div class="award2">
<div class="pics one"><img class="portrait" src="{I}award_lifestyle.jpg" alt="" loading="lazy"></div>
<div>
<p class="eyebrow">LIFESTYLE PLUS MAGAZINE</p>
<h2>Lifestyle Plus Awards</h2>
<p>{L('An honour from Lifestyle Plus Magazine for my work.', 'Un reconocimiento de Lifestyle Plus Magazine a mi trabajo.')}</p>
</div>
</div>
</div></section>

<section class="alt"><div class="wrap grid2 top">
<div>
<p class="eyebrow">{L('MEDICINE', 'MEDICINA')}</p>
<h2>{L('Studies', 'Formación')}</h2>
<table class="cred">
<tr><td>{L('MD in Ayurveda (Vaidya Shiromani / Vachaspati)', 'MD en Ayurveda (Vaidya Shiromani / Vachaspati)')}</td><td>{L('India', 'India')}</td></tr>
<tr><td>{L('Bachelor of Ayurvedic Medicine and Science (B.A.M.S.)', 'Licenciatura en Medicina y Ciencia Ayurvédica (B.A.M.S.)')}</td><td>{L('India', 'India')}</td></tr>
<tr><td>{L('Doctorate in Natural Medicine · World Organization of Natural Medicine', 'Doctorado en Medicina Natural · World Organization of Natural Medicine')}</td><td>2013</td></tr>
<tr><td>{L('Doctorate in Humanitarian Services · World Organization of Natural Medicine', 'Doctorado en Servicios Humanitarios · World Organization of Natural Medicine')}</td><td>2013</td></tr>
<tr><td>{L('PhD in Quantum Medicine', 'PhD en Medicina Cuántica')}</td><td>2014</td></tr>
<tr><td>{L('Double doctorate in Natural and Quantum Medicine, certified by the Council of Natural Medicine and Specialists of North America', 'Doble doctorado en Medicina Natural y Cuántica, certificado por el Consejo de Medicina Natural y Especialistas de América del Norte')}</td><td></td></tr>
</table>
<p class="note" style="margin-top:14px;font-size:17px">{L('My PhD in Quantum Medicine was a doctorate the university prepared especially for me, for the knowledge I had contributed. Only five physicians in the United States hold a PhD in this field.', 'Mi PhD en Medicina Cuántica fue un doctorado que la universidad preparó especialmente para mí, por el conocimiento que he aportado. Solo cinco médicos en Estados Unidos tienen un PhD en esta rama.')}</p>
<p class="eyebrow" style="margin-top:30px">{L('CERTIFICATIONS', 'CERTIFICACIONES')}</p>
<table class="cred">
<tr><td>{L('Board-certified in biofeedback', 'Certificado por el board de biofeedback')}</td><td></td></tr>
<tr><td>{L('Certified by the board of natural medicine of North America · Council of Natural Medicine and Specialists of North America', 'Certificado por el board de medicina natural de Norteamérica · Consejo de Medicina Natural y Especialistas de América del Norte')}</td><td></td></tr>
<tr><td>{L('Reverend', 'Reverendo')}</td><td></td></tr>
</table>
<p class="eyebrow" style="margin-top:30px">{L('MEMBERSHIPS', 'MEMBRESÍAS')}</p>
<table class="cred">
<tr><td>{L('Academic Council member · AAPNA, Association of Ayurvedic Professionals of North America', 'Miembro del Consejo Académico · AAPNA, Association of Ayurvedic Professionals of North America')}</td><td></td></tr>
<tr><td>{L('Member · NAMA, National Ayurvedic Medical Association', 'Miembro · NAMA, National Ayurvedic Medical Association')}</td><td></td></tr>
</table>
<p class="eyebrow" style="margin-top:30px">{L('THESIS AND SYSTEMS', 'TESIS Y SISTEMAS')}</p>
<ul class="benefits" style="columns:1">
<li>{L('Doctoral thesis: the transformation of negative archetypes into positive archetypes, used in therapy.', 'Tesis doctoral: la transformación de arquetipos negativos en arquetipos positivos, usada en terapia.')}</li>
<li>{L('Originator of Quantum Transformation.', 'Originador de la Transformación Cuántica.')}</li>
<li>{L('Creator of Archangelical Touch, a system of energy work.', 'Creador del Toque Arcangélico (Archangelical Touch), un sistema de trabajo energético.')}</li>
<li>{L('Cognizer of the Light Codes of the Flame Codex.', 'Cognizador de los Códigos de Luz del Códice de la Llama.')}</li>
</ul>
</div>
<figure><img class="portrait" src="{I}zuluan_library.jpg" alt="Dr. Zuluan Orion" loading="lazy"></figure>
</div></section>

<section><div class="wrap">
<h2>{L('With Ayurvedic physicians', 'Con médicos ayurvédicos')}</h2>
<p>{L('Ayurveda is a living tradition, and I share it with Ayurvedic physicians from India.', 'La Ayurveda es una tradición viva, y la comparto con médicos ayurvédicos de la India.')}</p>
<figure style="max-width:720px;margin:26px 0"><img class="portrait" src="{I}kerala_dr_reddy_kumar.jpg" alt="Dr. Reddy Kumar" loading="lazy"><figcaption>{L('Studying Ayurvedic medicine beside Dr. Reddy Kumar, University of Kerala, India.', 'Estudiando medicina ayurvédica al lado del Dr. Reddy Kumar, Universidad de Kerala, India.')}</figcaption></figure>
<div class="gallery tall" style="grid-template-columns:repeat(3,1fr);max-width:1000px">
<figure><img src="{I}with_dr_shekhar_annambhotla.jpg" alt="Dr. Shekhar Annambhotla" loading="lazy"><figcaption>{L('With Dr. Shekhar Annambhotla, BAMS, MD (Ayurveda).', 'Con el Dr. Shekhar Annambhotla, BAMS, MD (Ayurveda).')}</figcaption></figure>
<figure><img src="{I}with_dr_suresh_swarnapuri.jpg" alt="Dr. Suresh Swarnapuri" loading="lazy"><figcaption>{L('With Dr. Suresh Swarnapuri, BAMS, MD (Ayurveda).', 'Con el Dr. Suresh Swarnapuri, BAMS, MD (Ayurveda).')}</figcaption></figure>
<figure><img src="{I}with_dr_shan_lakshmanan.jpg" alt="Dr. Shan Lakshmanan" loading="lazy"><figcaption>{L('With Dr. Shan Lakshmanan, Ph.D.', 'Con el Dr. Shan Lakshmanan, Ph.D.')}</figcaption></figure>
</div>
</div></section>
'''

# ------------------------------------------------------------------ JOURNEYS
def trip(eyebrow, title, place, paras, stops):
    st = ''.join(f'<li>{s}</li>' for s in stops)
    return f'''<div class="card" style="padding:34px 32px">
<p class="eyebrow">{eyebrow}</p>
<h3 style="margin-top:4px">{title}</h3>
<p style="font-family:var(--caps);letter-spacing:.08em;font-size:14px;color:var(--gold)">{place}</p>
{''.join(f'<p>{p}</p>' for p in paras)}
<ul class="benefits" style="columns:1">{st}</ul>
</div>'''

def journeys(lang):
    L = Lx(lang)
    en = lang == 'en'
    pdf = 'Spiritual_Journey_Thailand_EN.pdf' if en else 'Viaje_Espiritual_por_Tailandia.pdf'
    grp = ''.join(f'<img src="{I}viajes/grupo_{n:02d}.jpg" alt="" loading="lazy">' for n in range(1, 27) if n not in (1, 9, 17))
    events = [(L('Miami, USA', 'Miami, EE. UU.'), L('17 May 2023', '17 de mayo de 2023')),
              ('Cuenca, Ecuador', L('12 August 2022', '12 de agosto de 2022')),
              ('Guayaquil, Ecuador', L('17 August 2022', '17 de agosto de 2022'))]
    ev = ''.join(f'<li><b>{c}</b><span>{d}</span></li>' for c, d in events)
    return f'''<section class="ba" style="padding:0;text-align:left"><div style="position:relative">
<img src="{I}viajes/grupo_01.jpg" alt="Wat Phra That Doi Suthep, Chiang Mai" style="width:100%;height:min(70vh,620px);object-fit:cover;object-position:center 35%;display:block;opacity:.5">
<div class="wrap" style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;max-width:1120px">
<p class="eyebrow" style="color:var(--gold2)">{L('THAILAND · CHIANG MAI · JUNE 2027', 'TAILANDIA · CHIANG MAI · JUNIO 2027')}</p>
<h2 style="font-size:clamp(30px,5vw,54px);margin:0 0 12px">{L('A spiritual journey through the temples and sacred places of Northern Thailand', 'Un viaje espiritual por los templos y lugares sagrados del Norte de Tailandia')}</h2>
<p style="font-size:clamp(18px,2.2vw,24px);max-width:640px;color:#F1E9FA">{L('Temples of the Lanna tradition, mountains and waterfalls, meditation with the monks, and the healer Pakkapron, who has channeled the Medicine Buddha for more than thirty years. Places are limited.', 'Templos de la tradición Lanna, montañas y cascadas, meditación con los monjes, y la sanadora Pakkapron, que canaliza al Buda de la Medicina desde hace más de treinta años. Cupos limitados.')}</p>
<p><a class="btn solid" href="tel:+19546680348">{L('Call (954) 668-0348', 'Llamar (954) 668-0348')}</a> <a class="btn" style="background:rgba(23,19,42,.5)" href="/assets/docs/{pdf}" download>⬇ {L('Download the journey guide', 'Descargar la guía del viaje')}</a></p>
</div></div></section>

<section><div class="narrow">
<p class="lead">{L('For almost two decades I lived and studied in Asia: twelve and a half years in India and eight in Thailand. Those lands shaped my path: the temples, the masters, the healers, the silence. Now I open those doors to small groups who want to live the journey from the inside.', 'Durante casi dos décadas viví y estudié en Asia: doce años y medio en la India y ocho en Tailandia. Esas tierras formaron mi camino: los templos, los maestros, los sanadores, el silencio. Ahora abro esas puertas a grupos pequeños que quieren vivir el viaje desde adentro.')}</p>
<p>{L('These are not tourist trips. They are pilgrimages of the soul: meditation in sacred places, encounters with living traditions, Quantum Transformation along the way, and time to integrate what opens.', 'No son viajes de turismo. Son peregrinaciones del alma: meditación en lugares sagrados, encuentros con tradiciones vivas, Transformación Cuántica en el camino, y tiempo para integrar lo que se abre.')}</p>
</div></section>

<section class="alt"><div class="wrap">
<p class="eyebrow center">{L('JUNE 2027', 'JUNIO 2027')}</p><h2 class="center">{L('Upcoming journeys', 'Próximos viajes')}</h2>
<div class="grid2 top" style="margin-top:30px">
{trip(L('THAILAND · JUNE 2027', 'TAILANDIA · JUNIO 2027'), L('Holistic retreat in Chiang Mai', 'Retiro holístico en Chiang Mai'), L('Chiang Mai · Northern Thailand', 'Chiang Mai · Norte de Tailandia'),
      [L('In the mountains of northern Thailand, among Buddhist temples and forest, we live a holistic retreat of meditation, healing and inner silence.', 'En las montañas del norte de Tailandia, entre templos budistas y bosque, vivimos un retiro holístico de meditación, sanación y silencio interior.'),
       L('One of the heart moments of this journey is our visit to Pakkapron, a very special healer from Chiang Mai who has channeled the Medicine Buddha for more than thirty years, offering healing, Dharma teaching and spiritual guidance.', 'Uno de los momentos del corazón de este viaje es la visita a Pakkapron, una sanadora muy especial de Chiang Mai que canaliza al Buda de la Medicina desde hace más de treinta años, ofreciendo sanación, enseñanza del Dharma y guía espiritual.')],
      [L('Meditation in Buddhist temples', 'Meditación en templos budistas'), L('Visit to Pakkapron', 'Visita a Pakkapron'), L('Quantum Transformation sessions during the journey', 'Sesiones de Transformación Cuántica durante el viaje'), L('Thai healing traditions, nature and silence', 'Tradiciones de sanación tailandesas, naturaleza y silencio')])}
{trip(L('INDIA · JUNE 2027', 'INDIA · JUNIO 2027'), L('Pilgrimage to Northern India', 'Peregrinación al Norte de la India'), 'Vrindavan · Mathura · Agra (Taj Mahal) · Jaipur',
      [L('A journey through the sacred sites of Northern India, to have a deep spiritual experience and connect with the energy these places have held for thousands of years.', 'Un recorrido por los lugares sagrados del norte de la India, para tener una vivencia espiritual muy profunda y conectar con la energía que esos lugares han sostenido durante miles de años.'),
       L('Along the way we live the activation of the Light Codes of the Flame Codex.', 'En el camino vivimos la activación de los Códigos de Luz del Códice de la Llama.')],
      [L('Vrindavan and Mathura, the land of Krishna', 'Vrindavan y Mathura, la tierra de Krishna'), L('The Taj Mahal in Agra', 'El Taj Mahal en Agra'), L('Jaipur, the pink city', 'Jaipur, la ciudad rosa'), L('Temples, meditation and ceremonies', 'Templos, meditación y ceremonias'), L('Activation of the Light Codes', 'Activación de los Códigos de Luz')])}
</div>
<p class="center" style="margin-top:36px">{L('Places are limited. Call for more information and to reserve your place.', 'Los cupos son limitados. Llama para más información y para reservar tu lugar.')}</p>
<p class="center"><a class="btn solid" href="tel:+19546680348">{L('Call (954) 668-0348', 'Llamar (954) 668-0348')}</a> <a class="btn" href="mailto:zuluanorion@gmail.com">{L('Write to me', 'Escríbeme')}</a></p>
</div></section>

<section><div class="wrap">
<p class="eyebrow center">{L('WITH THE GROUPS', 'CON LOS GRUPOS')}</p><h2 class="center">{L('Our journeys to Thailand, 2025 and 2026', 'Nuestros viajes a Tailandia, 2025 y 2026')}</h2>
<p class="center" style="max-width:720px;margin:0 auto 30px">{L('In 2025 and 2026 we travelled to Thailand with groups who lived this experience with us: the temples and sacred places of the north, the mountains and waterfalls, the hill-tribe villages, and the healer Pakkapron.', 'En 2025 y 2026 viajamos a Tailandia con grupos que vivieron esta experiencia con nosotros: los templos y lugares sagrados del norte, las montañas y cascadas, las aldeas de las montañas y la sanadora Pakkapron.')}</p>
<div class="grid2" style="margin-bottom:40px">
<figure><img class="portrait" src="{I}viajes/th_zuluan_pakkapron.jpg" alt="Dr. Zuluan Orion with Pakkapron" style="max-height:560px;width:auto;margin:0 auto"><figcaption>{L('With Pakkapron in Chiang Mai.', 'Con Pakkapron en Chiang Mai.')}</figcaption></figure>
<div><p class="eyebrow">{L('THE HEALER OF CHIANG MAI', 'LA SANADORA DE CHIANG MAI')}</p><h3 style="margin-top:4px">Pakkapron</h3><p>{L('Born in 1946 in the village of Namjum, in the hills of Chiang Mai, Pakkapron discovered her gift when a young girl suffering from seizures arrived at her door. Since then, for more than three decades, she has channeled the energy of the Medicine Buddha to heal, to teach the Dharma and to offer spiritual guidance, freely, to thousands of people from around the world.', 'Nacida en 1946 en el pueblo de Namjum, en las montañas de Chiang Mai, Pakkapron descubrió su don cuando una niña que sufría convulsiones llegó a su puerta. Desde entonces, por más de tres décadas, canaliza la energía del Buda de la Medicina para sanar, enseñar el Dharma y ofrecer guía espiritual, sin costo, a miles de personas de todo el mundo.')}</p></div>
</div>
<div class="gallery tall" style="grid-template-columns:repeat(2,1fr);max-width:900px;margin:0 auto">
<figure><img src="{I}viajes/th_monje_incorrupto.jpg" alt="" loading="lazy" style="aspect-ratio:4/3"><figcaption>{L('An incorruptible monk of Northern Thailand.', 'Un monje incorrupto del Norte de Tailandia.')}</figcaption></figure>
<figure><img src="{I}viajes/th_monjes_vistiendo.jpg" alt="" loading="lazy" style="aspect-ratio:4/3"><figcaption>{L('Monks caring for the body of an incorruptible master.', 'Monjes cuidando el cuerpo de un maestro incorrupto.')}</figcaption></figure>
</div>
<h3 class="center" style="margin-top:50px">{L('Our groups in Thailand, 2025 and 2026', 'Nuestros grupos en Tailandia, 2025 y 2026')}</h3>
<div class="gallery" style="margin-top:20px">{grp}</div>
<div class="center" style="margin-top:40px"><a class="btn solid" style="font-size:16px;padding:18px 34px" href="/assets/docs/{pdf}" download>⬇ {L('DOWNLOAD THE THAILAND JOURNEY GUIDE (PDF)', 'DESCARGAR LA GUÍA DEL VIAJE A TAILANDIA (PDF)')}</a><p class="note" style="margin-top:12px">PDF · {'9' if en else '18'} MB</p></div>
</div></section>

<section class="alt"><div class="wrap grid2">
<div>
<p class="eyebrow">{L('GATHERINGS AND TALKS', 'ENCUENTROS Y CONFERENCIAS')}</p>
<h2>{L('Meeting in person', 'Encontrarnos en persona')}</h2>
<p>{L('Over the years I have shared meditations and talks with many people in different cities, in the United States and in Latin America. Some of those gatherings:', 'A lo largo de los años he compartido meditaciones y conferencias con muchas personas en distintas ciudades, en los Estados Unidos y en Latinoamérica. Algunos de esos encuentros:')}</p>
<ul class="evlist">{ev}</ul>
<p>{L('New dates will be announced here and on my social media.', 'Las nuevas fechas se anunciarán aquí y en mis redes sociales.')}</p>
<p><a class="btn" href="https://www.youtube.com/channel/UCM42zxWtUt1xK4cp1bLl1uw">YouTube ↗</a> <a class="btn" href="https://www.instagram.com/drzuluanorion/">Instagram ↗</a></p>
</div>
<figure><img class="portrait" src="{I}press_tv_studio_01.jpg" alt="" loading="lazy"><figcaption>{L('Presenting <em>Deshojando el Corazón de la Eternidad</em> on television in Miami.', 'Presentando <em>Deshojando el Corazón de la Eternidad</em> en televisión, en Miami.')}</figcaption></figure>
</div></section>
'''

# ------------------------------------------------------------------ CONTACT
def contact(lang):
    L = Lx(lang)
    return f'''<section><div class="narrow center">
<h2>{L('Write to me', 'Escríbeme')}</h2>
<p class="lead">{L('For the teaching, the books, satsang, the journeys, talks and interviews:', 'Para la enseñanza, los libros, el satsang, los viajes, las conferencias y las entrevistas:')}</p>
<div class="btns"><a class="btn solid" href="mailto:zuluanorion@gmail.com">zuluanorion@gmail.com</a><a class="btn" href="tel:+19546680348">(954) 668-0348</a></div>
<div class="cinfo">
<div><p class="eyebrow">{L('OFFICE', 'CONSULTORIO')}</p><p>1565 North Park Drive, Suite 101<br>Weston, Florida 33326</p></div>
<div><p class="eyebrow">{L('SOCIAL MEDIA', 'REDES SOCIALES')}</p><p><a href="https://www.instagram.com/drzuluanorion/">Instagram</a> · <a href="https://www.facebook.com/zuluanorion/">Facebook</a> · <a href="https://www.youtube.com/channel/UCM42zxWtUt1xK4cp1bLl1uw">YouTube</a></p></div>
</div>
</div></section>
<section class="dark"><div class="wrap">
<div class="doors">
<a class="door" href="{ext(SB, lang)}"><div><p class="eyebrow">{L('THERAPY AND PERSONAL WORK', 'TERAPIAS Y TRABAJO PERSONAL')}</p><h3>Spiritual Balance</h3><p>{L('Sessions, Ayurveda and Quantum Transformation in Weston, Florida.', 'Sesiones, Ayurveda y Transformación Cuántica en Weston, Florida.')}</p><span class="more">{L('VISIT ↗', 'VISITAR ↗')}</span></div></a>
<a class="door" href="{ext(FC, lang)}"><div><p class="eyebrow">{L('THE SACRED LANGUAGE', 'EL LENGUAJE SAGRADO')}</p><h3>{L('The Flame Codex', 'El Códice de la Llama')}</h3><p>{L('The keys, the Light Code meditation, and the retreats and initiations of the Flame.', 'Las llaves, la meditación de Códigos de Luz, y los retiros e iniciaciones de la Llama.')}</p><span class="more">{L('VISIT ↗', 'VISITAR ↗')}</span></div></a>
<a class="door" href="{url(lang, 'journeys')}"><div><p class="eyebrow">{L('JUNE 2027', 'JUNIO 2027')}</p><h3>{L('Journeys', 'Viajes')}</h3><p>{L('Thailand and India, in small groups.', 'Tailandia y la India, en grupos pequeños.')}</p><span class="more">{L('SEE →', 'VER →')}</span></div></a>
</div>
</div></section>
'''

# ------------------------------------------------------------------ assemble
for lang, B in (('en', BODY['en']), ('es', BODY['es'])):
    L = Lx(lang)
    B[''] = home(lang)
    B['story'] = hero(L('My Story', 'Mi historia'), L('From Bogotá to India and Thailand, and from the awakening to the Descent', 'De Bogotá a la India y Tailandia, y del despertar al Descenso')) + story(lang)
    B['illumination'] = hero(L('Illumination', 'Iluminación'), L('The nondual teaching', 'La enseñanza no dual')) + illumination(lang)
    B['recognition'] = hero(L('Recognition and Studies', 'Reconocimientos y formación'), L('Ayurveda, natural and quantum medicine', 'Ayurveda, medicina natural y cuántica')) + recognition(lang)
    B['books'] = hero(L('Books', 'Libros'), L('By Dr. Zuluan Orion', 'Del Dr. Zuluan Orion')) + shelf(lang)
    B['journeys'] = hero(L('Journeys and Retreats', 'Viajes y retiros'), L('Thailand and India with Dr. Zuluan Orion', 'Tailandia y la India con el Dr. Zuluan Orion')) + journeys(lang)
    B['contact'] = hero(L('Contact', 'Contacto'), L('Everything always begins with a simple question', 'Todo siempre empieza con una simple pregunta')) + contact(lang)

# ------------------------------------------------------------------ blog
POSTPAGES = {}
for lang in ('en', 'es'):
    BODY[lang]['blog'] = blog.index_page(lang)
    POSTPAGES[lang] = blog.pages(lang)
