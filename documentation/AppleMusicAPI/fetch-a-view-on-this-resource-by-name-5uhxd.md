# Get a Catalog Record Label’s Relationship View Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch related resources for a single record label’s relationship view.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single [`RecordLabels.Views`](recordlabels/views-data.dictionary.md) object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/record-labels/1543990853/view/top-releases
```

**Response**:

```json
{
  "next": "/v1/catalog/us/record-labels/1543990853/view/top-releases?offset=10",
  "data": [
    {
      "id": "1169245868",
      "type": "albums",
      "href": "/v1/catalog/us/albums/1169245868",
      "attributes": {
        "artwork": {
          "width": 3000,
          "height": 3000,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/be/f1/d0/bef1d063-ed73-bd7d-3899-2217762cdcda/5054429005721.png/{w}x{h}bb.jpg",
          "bgColor": "36311b",
          "textColor1": "ebebf3",
          "textColor2": "c9e1ef",
          "textColor3": "c7c6c8",
          "textColor4": "abbdc4"
        },
        "artistName": "Bonobo",
        "isSingle": false,
        "url": "https://music.apple.com/us/album/migration/1169245868",
        "isComplete": true,
        "genreNames": [
          "Electronic",
          "Music"
        ],
        "trackCount": 12,
        "isMasteredForItunes": true,
        "releaseDate": "2017-01-13",
        "name": "Migration",
        "recordLabel": "Ninja Tune",
        "upc": "5054429005721",
        "copyright": "℗ 2017 Ninja Tune",
        "playParams": {
          "id": "1169245868",
          "kind": "album"
        },
        "editorialNotes": {
          "standard": "Contemplative, colorful electronica from the UK producer. On his sixth album, Simon Green explores the theme of migration through global sounds. His references are subtle, but not overly serious; he drifts from old-school Brandy samples (“Kerala”) to Moroccan Gnawa musicians (“Bambro Koyo Ganda”) with signature restraint (“Outlier”). There are a few high-profile guests along the way, including Nicole Miglis (Hundred Waters) and Nick Murphy (Chet Faker), but they’re not the main attraction—this LP is about the ride.",
          "short": "Contemplative, colorful electronica featuring Nick Murphy and more."
        },
        "isCompilation": false
      }
    },
    {
      "id": "416292276",
      "type": "albums",
      "href": "/v1/catalog/us/albums/416292276",
      "attributes": {
        "artwork": {
          "width": 2362,
          "height": 2362,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/d2/19/d2/d219d28f-682b-63c6-a4e9-0d205b71b797/5021392584195.png/{w}x{h}bb.jpg",
          "bgColor": "0a0b10",
          "textColor1": "dbf3f0",
          "textColor2": "afe0d6",
          "textColor3": "b1c4c3",
          "textColor4": "8eb5af"
        },
        "artistName": "Bonobo",
        "isSingle": false,
        "url": "https://music.apple.com/us/album/black-sands/416292276",
        "isComplete": true,
        "genreNames": [
          "Electronic",
          "Music",
          "Jazz",
          "Big Band",
          "Bop",
          "Rock",
          "Alternative",
          "Downtempo"
        ],
        "trackCount": 12,
        "isMasteredForItunes": false,
        "releaseDate": "2010-03-29",
        "name": "Black Sands",
        "recordLabel": "Ninja Tune",
        "upc": "5021392584195",
        "copyright": "℗ 2010 Ninja Tune",
        "playParams": {
          "id": "416292276",
          "kind": "album"
        },
        "editorialNotes": {
          "standard": "The tension between lush instrumental arrangements and digital trickery energizes every iota of Bonobo’s fourth album, in which broken beats and sampler-assisted jazz frequently blossom into flickering electronic futurism. The Eastern-tinged melody of the opening “Prelude” shows how far the UK downtempo producer’s horizons have expanded here, as he delves into Latin grooves on “We Could Forever” and turns the hip-hop beats of “Kong” into a dynamic play of electro-acoustic textures. Andreya Triana shines on “Eyesdown,” transforming Bonobo’s moody collage work into full-fledged modern soul.",
          "short": "Lush, broken-beat soul and flickering electronic futurism."
        },
        "isCompilation": false
      }
    },
    {
      "id": "1586070259",
      "type": "albums",
      "href": "/v1/catalog/us/albums/1586070259",
      "attributes": {
        "artwork": {
          "width": 6000,
          "height": 6000,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/3c/22/7d/3c227d89-9ab2-b556-b8f4-c9ce588c2d91/5054429151442.png/{w}x{h}bb.jpg",
          "bgColor": "754b20",
          "textColor1": "ebf5f1",
          "textColor2": "d4e8f7",
          "textColor3": "d4d3c8",
          "textColor4": "c1c8cc"
        },
        "artistName": "Black Country, New Road",
        "isSingle": false,
        "url": "https://music.apple.com/us/album/ants-from-up-there/1586070259",
        "isComplete": true,
        "genreNames": [
          "Alternative",
          "Music"
        ],
        "trackCount": 10,
        "isMasteredForItunes": false,
        "releaseDate": "2022-02-04",
        "name": "Ants From Up There",
        "recordLabel": "Ninja Tune",
        "upc": "5054429151442",
        "copyright": "℗ 2022 Ninja Tune",
        "playParams": {
          "id": "1586070259",
          "kind": "album"
        },
        "editorialNotes": {
          "standard": "Traditionally, a band releases their debut album and heads out for an extended stretch on the road, honing their live chops, twisting their songs into new shapes. But when Black Country, New Road released <i>For the First Time</i> in February 2021, that route was blocked off by the pandemic. Instead, the London-based band set out to tweak and tamper with their experimental post-rock sound for a transformative second album. They might not have been able to travel, but their music could. “By the time the first album came out, those songs had existed for so long that we were very keen to change the way we wrote music,” bassist Tyler Hyde tells Apple Music. The material that makes up their second record, <i>Ants From Up There</i>, soon came to life, the group using the labyrinthine “Basketball Shoes,” which had been around before their debut, as a springboard. “We wanted to explore the themes we’d created on that song,” says Hyde. “It’s essentially three songs within one, all of which relatively cover the emotions and moods that are on the album. It’s hopeful and light, but still looks at some of the darker sides that the first album showed.”<br />\nThe resultant record sees the band hit hypnotic new peaks. <i>Ants From Up There</i>, recorded before the departure of singer Isaac Wood in January 2022, is less reliant on jerky, rhythmic U-turns than their debut (although there is some of that), with expansive, Godspeed You! Black Emperor-ish atmospherics emerging in their place. “Fundamentally, we relearned an entirely new style of playing with each other,” says drummer Charlie Wayne. “We learned a lot about how to express ourselves just for each other rather than for anything else going on externally.” Here Hyde, Wayne, and saxophonist Lewis Evans take us through it, track by track.<br />\n<b>“Intro”</b>\nLewis Evans: “This uses the theme from ’Basketball Shoes,’ compressed into these little micro cells and repeated over and over again. It’s just a straight-up, impactful welcome to the album.”<br />\n<b>“Chaos Space Marine”</b>\nTyler Hyde: “In this song, we allowed ourselves to get out all the stupid, funny joke style of playing. It was just our way of saying yes to everything. There are many things across the album—and in previous songs from the last album—that are seemingly good ideas, but they’ve come about through a joke. I think the rest of the album is much more considered than that. It’s our silly song. It’s a voyage. It’s a sea shanty. It’s a space trip.”<br />\n<b>“Concorde”</b>\nCharlie Wayne: “I love how it follows the same chord progression the whole way through, and it’s driven but very soft. It’s got real moments of delicacy, and it’s a song that we all thought quite a lot about when we were getting it together. When you’re restricted to that one-chord sequence, you want it to feel as though it’s going somewhere and progressing, so the peaks and troughs have to be considered.”<br />\n<b>“Bread Song”</b>\nLE: “It’s like two different songs in one. You’ve got this really quite flowing and free track in a melodic and conventional harmonic way, but rhythmically free and flowing accompaniment to Isaac’s vocals. It feels quite orchestral, and the way that we all play together on this recording is so in sync with each other. We were listening to each other so much, so the swells that one person starts making, people start responding to, and everybody is swelling at the same time and getting quieter at the same time. Then it turns into this almost Soweto, kind of township-style pop tune at the end. It’s a really fun ending to an intense, emotional tune.”<br />\n<b>“Good Will Hunting”</b>\nLE: “This is another slightly silly one, and it’s got a really silly ending which actually never made the cut on the album, but it’s heavily driven by the riff on the guitars. I think at the time we were listening to quite a bit of Kurt Vile, especially rhythmically. I can remember a conversation about when we wanted the drums to come in and to be super straight, super driven. Then for the choruses, rhythmically, to completely flip and not feel like they were big at all. So for both the choruses, the drums are just tiny.”<br />\n<b>“Haldern”</b>\nTH: “We were playing at Haldern Pop Festival in north Germany during lockdown. We’d just been allowed to fly for work purposes, and we were doing this session. We did two performances there, and the second one was a livestream, and we weren’t allowed to play songs that weren’t released. At the time, that left us with not very much that we weren’t already bored with, so we decided to do some improv. It was a very lucky day where we were all very in sync with one another. So ‘Haldern’ was totally from improv, which is not how we write ever.”<br />\n<b>“Mark’s Theme”</b>\nLE: “This is a tune written kind of for my uncle who passed away from COVID in 2021. I wrote it on my tenor saxophone as soon as I found out. I just started playing and wrote that. It’s a reflection on him and my feelings towards him passing away and everything being really bleak. He was a massive fan and supporter of the band, so it felt right to put that on the album and to have his name remembered with our music.”<br />\n<b>“The Place Where He Inserted the Blade”</b>\nCW: “For me, this is about as far away as we went from the first album. Aesthetically, where the first album has moments of real dissonance and apathy, ‘The Place Where He Inserted the Blade’ is very warm and rich and quite uplifting. I think it strikes right to the heart of what the album is for me, which is fundamentally being in the room, making music with my friends.”<br />\n<b>“Snow Globes”</b>\nLE: “This is another tune where we really thought about what we wanted from it before we wrote it. We had examples of things we liked, and one of them was Frank Ocean’s ‘White Ferrari.’ We liked the idea of it almost being like two different bands [playing] at the same time. So you’ve got this quite simple but quite heart-wrenching, fugal-sounding arrangement of all the instruments with a drum solo that is just crazy and doesn’t really relate too much to what is going on in the other instruments. We react to the drum solo, but he doesn’t react to us. It’s that kind of idea.”<br />\n<b>“Basketball Shoes”</b>\nTH: “It’s essentially a medley of the whole album. It’s got literal musical motifs that are repeated on different songs in the album. It touches on all the themes that we’ve been exploring, and it’s the most climactic song on the album. It wouldn’t really make sense to not finish with it, it’s so exhausting. It’s such a journey. I think you just wouldn’t be able to pay much attention to anything that followed it because you’d be so wiped out after listening to it.”",
          "short": "“It’s hopeful and light but still looks at some darker sides.”"
        },
        "isCompilation": false
      }
    },
    {
      "id": "1506713751",
      "type": "albums",
      "href": "/v1/catalog/us/albums/1506713751",
      "attributes": {
        "artwork": {
          "width": 6000,
          "height": 6000,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music113/v4/5d/cd/14/5dcd1469-7b0a-b32b-4f95-59d674485a8c/dj.kdudhsln.png/{w}x{h}bb.jpg",
          "bgColor": "000000",
          "textColor1": "e8e8e8",
          "textColor2": "f7dc02",
          "textColor3": "b9b9b9",
          "textColor4": "c6b001"
        },
        "artistName": "BRONSON",
        "isSingle": false,
        "url": "https://music.apple.com/us/album/bronson/1506713751",
        "isComplete": true,
        "genreNames": [
          "Electronic",
          "Music",
          "Rock",
          "Dance"
        ],
        "trackCount": 10,
        "isMasteredForItunes": false,
        "releaseDate": "2020-08-07",
        "name": "BRONSON",
        "recordLabel": "Ninja Tune",
        "upc": "5054429141849",
        "copyright": "℗ 2020 Foreign Family Collective LLC & Ninja Tune",
        "playParams": {
          "id": "1506713751",
          "kind": "album"
        },
        "editorialNotes": {
          "standard": "“It happened really naturally over time,” Harrison Mills tells Apple Music of BRONSON, a collaboration between Seattle duo ODESZA (Mills alongside Clayton Knight) and Sydney producer Golden Features (Tom Stell). “We were just friends. The first time we came to Australia, Tom was the first Australian person we met that we instantly started getting along with and we just got to know each other really well.” The project has been in production for years, with the bulk of it written in 2018, both online and during a weeklong recording trip to Berry, New South Wales. The resulting album is a rush to explore. More than blending elements of each artist’s sound, it was a collaboration in the truest sense, with each member working off one another, challenging their processes and experimenting beyond their typical boundaries. “I sent a melody [to ODESZA],” says Stell, “and they sent me back this incredible almost-finished song. They’d added these drums that I never would have picked, this bass that I never would have picked. That was the beauty of the whole project. Ideas that usually get a red light, where we’d normally be like, ‘This doesn't sound like ODESZA’ or ‘This doesn't sound like Golden Features,’ got a green light.” Mills adds: “It felt like we were all very open-minded. There weren’t any limitations; we weren't trying to put ourselves in a box. We were always learning.” Below, all three members of BRONSON break down each track on their debut album.<br />\n<b>FOUNDATION</b>\nMills: “This was one of the final songs we wrote, and ironically, it became the first track on the album. We’ve always been fans of the concept of having an intro to an album, and set out to do that here. We wanted something that set the tone for the record and invited the listener into the world of BRONSON. We wanted to make sure we gave the right first impression. Something that lived between dark and euphoric.”<br />\n<b>HEART ATTACK (feat. lau.ra)</b>\nMills: “lau.ra first sent a bunch of gibberish melodies over the demo and we ended up looping one section. It was so catchy and hypnotic. Her delivery was so intimate—it felt gorgeous yet dark, uplifting yet melancholy.”\nStell: “It was the first vocal track we worked on for the record. It was one of those ideas that came together really quickly and felt very natural while writing with lau.ra. It was a confluence between the distinctive sounds of ODESZA and Golden Features, and served as a turning point for the album.”<br />\n<b>BLINE</b>\nKnight: “The first version of this tune felt more laidback, but it didn’t seem to keep our attention—at least not enough to make it on the record. We kept experimenting with different leads until we found a melody that gave it a driving sound, which ultimately cranked the song up to a much higher energy level than we were initially intending. We focused a lot on using different analog elements and constantly modulating them to add layers to the song, inherently making it feel alive.”<br />\n<b>KNOW ME (feat. Gallant)</b>\nMills: “We’ve always been fans of Gallant’s work, so we reached out to him and tried setting up a studio session together in LA. When we did finally meet up, we ended up really hitting it off. He’s such a natural talent—it was incredible watching him work to a simple demo loop we had put together that he really connected to. During that session, we talked about the lyrical content—about someone you love never really knowing who you are and finally coming to the realization they never truly knew you. As a result, he matched the emotive R&B sound and tone we were going for perfectly; it really elevated the entire message of the song to an entirely different level of depth.”<br />\n<b>VAULTS</b>\nStell: “It was one of the earlier instrumentals we completed, and it acted as a cornerstone to the overall sound design and aesthetic. The track really proved a departure from each of our separate projects’ styles and set a definitive change in direction for the BRONSON project. We knew we had something special here and it served as a guiding light for the rest of the record.”<br />\n<b>TENSE</b>\nStell: “This was the first track we started as BRONSON and most likely the reason it’s so heavy. It really felt like a breakout of sorts from the worlds of ODESZA and Golden Features. It fueled us as a source of inspiration to keep working on the project. We wanted to make a heater, and hopefully we did.”<br />\n<b>CALL OUT</b>\nMills: “This track started with us just messing around with ’80s sounds and being inspired by that era’s energy. Eventually, after a few glasses of wine, we started singing over it...you can hear both myself and Tom in the vocals, which was certainly a departure from the norm.”<br />\n<b>CONTACT</b>\nKnight: “‘CONTACT’ is the most distorted tune on our record. We wanted to make a dance song and then run it through amps, distortion, and saturation to give a chaotic feel. To us, it’s such a frenetic and charged moment on the album, which we wanted to fully embrace. We took a lot of risks in the writing process of this entire album and pushed the envelope, so to speak, which felt good.”\nMills: “We were just really trying to make a distorted dance song. We had these cool elements, but the hard part was making all of that stay interesting for the full three minutes. We just wanted to keep your ears perked up throughout the whole song.”<br />\n<b>KEEP MOVING</b>\nMills: “This song is really about pushing through and the inner dialogue you have with yourself when facing an obstacle or opponent. Instrumentally and lyrically, we wanted to convey that intense emotion and the experience of channeling all of your energy to conquer whatever you’re facing. One interesting element of this track is that we sampled an army marching to give it this pulsing, percussive drive at its core. It just grew from there.”<br />\n<b>DAWN (feat. Totally Enormous Extinct Dinosaurs)</b>\nMills: “TEED has been someone we've been trying to work with for a long time. We showed him a couple of tracks, talked about the themes of the album. He went in a corner for literally 20 minutes and came back with this incredible lyrical content and melody. From there we just expanded it. It was pretty awesome to watch him work. I mean, it was done and written in three or four hours, which is insane.”\nKnight: “Creatively, we respect Orlando [TEED] so much. Not only do the lyrics provide this renewed sense of hope, but his vocals complement the tone and energy of the song perfectly. ‘DAWN’ is a song meant to take you on a journey and explore various concepts and emotions of the record. We couldn’t think of a more fitting song to end the album with.”",
          "short": "ODESZA + Golden Features = Even more than the sum of its parts."
        },
        "isCompilation": false
      }
    },
    {
      "id": "1584968878",
      "type": "albums",
      "href": "/v1/catalog/us/albums/1584968878",
      "attributes": {
        "artwork": {
          "width": 6000,
          "height": 6000,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/dc/a8/30/dca830e9-9ebd-6702-395c-0284e1ac6f87/dj.njmgrfro.png/{w}x{h}bb.jpg",
          "bgColor": "000710",
          "textColor1": "e36f9f",
          "textColor2": "ed6a61",
          "textColor3": "b65a82",
          "textColor4": "bd5650"
        },
        "artistName": "Bonobo",
        "isSingle": false,
        "url": "https://music.apple.com/us/album/fragments/1584968878",
        "isComplete": true,
        "genreNames": [
          "Electronic",
          "Music"
        ],
        "trackCount": 12,
        "isMasteredForItunes": false,
        "releaseDate": "2022-01-14",
        "name": "Fragments",
        "recordLabel": "Ninja Tune",
        "upc": "5054429151855",
        "copyright": "℗ 2022 Ninja Tune",
        "playParams": {
          "id": "1584968878",
          "kind": "album"
        },
        "editorialNotes": {
          "standard": "During the disorienting first few months of the pandemic, Simon Green hit a creative block. The British electronic musician, better known as Bonobo, felt trapped and isolated working out of his home in east Los Angeles, starved for live music and human interaction. “I desperately needed to get into a different headspace,” he tells Apple Music. “Really, I needed to get out of the house.” Green began taking solo camping trips into the area’s remote mountains and deserts in an effort to get his creative juices flowing. “Exploring California was a great way of breaking the monotony of being indoors all day,” he says. “During this time of zero stimulation, I felt like I had to make it for myself.” <i>Fragments</i>, his moody seventh album, born from these adventures, is a tribute to the West Coast’s wide-open spaces. A laidback mix of mesmerizing techno, orchestral instrumentation, and hushed R&B balladry, the project is as sprawling, peaceful, and varied as the landscape itself. Here, he takes us inside the making of each track.<br /> \n<b>“Polyghost” (feat. Miguel Atwood-Ferguson)</b>\n“This began as a long, drawn-out, seven-minute techno track that didn’t make the final cut. But it was built on top of two important thematic elements: harp, which is played by Lara Somogyi, who I recorded and then sampled, and strings, which are played by Miguel Atwood-Ferguson. In the end, I decided to keep just those two parts because they weave throughout the rest of the record and drew everything together. The minute I did that, it became the obvious opener.”<br />\n<b>“Shadows” (feat. Jordan Rakei)</b>\n“Back in 2019, before I even started assembling this album, I was working on a track that felt like a reference to guys like Theo Parrish and Moodymann—that swingy, old-school Detroit sound. I had been listening to that Andrew Ashong song ‘Flowers’ and felt like, with a vocalist, this could be in that same area. I reached out to Jordan, who helped me work out the structure—a bit of tension and release—and it wound up being one of the first tracks I had in place for this project. I’ve been sitting on it for almost three years.”<br />\n<b>“Rosewood”</b> \n“A good ways into making this album, I started to feel like I had the record but I didn’t have a proper single. So I went through my iPhone notes and voice memos and found a little piano loop that jumped out at me. I pulled it into Ableton and put a little kick drum under it and immediately felt like it could be the seeds of something. For the hook, I found this R&B a cappella on YouTube that had this little lyric of ‘I won't leave you.’ And I knew that was it.”<br /> \n<b>“Otomo” (feat. O’Flynn)</b>\n“This features an archived folk recording of a Bulgarian bagpipe choir that, to me, feels like a huge sample. It’s this big, droning, ethereal, cathedral-y thing, and I hadn’t heard anything like it before. I felt like it deserved to have some big <i>moments</i> around it, so I reached out to my friend O'Flynn, who does that so well—switching between tuneful melodies and percussive muscle. He wound up building an entire section for it, without even me prompting him, and it was perfect. It’s definitely the track that’s going to get played out in the club.”<br />\n<b>“Tides” (feat. Jamila Woods)</b>\n“I’d been talking to Jamila and a few other vocalists about doing some collaborations, but nobody was feeling particularly motivated—it was too early into the pandemic. But then, in 2021, people came to life. Jamila texted me that she was going into the studio to record something, and it wound up being a demo that’s on the record. Hearing it really kick-started my creative energy. I remember when she first sent it to me, I was heading out for the night and was like, ‘I'm going to wait to listen to this until I get home, when I can really give it my full attention.' When I got back, I'd had a couple glasses of wine, so I was in the perfect state. I hit play, and I was just...overcome. I almost cried. It was like suddenly there was an emotional centerpiece to the record. It changed everything.”<br />\n<b>“Elysian”</b>\n“This one is named after Elysian Park, which is very close to where I live in LA. Because it was the pandemic and most things were closed, I spent a lot of time in the park, going for walks, cycling up to Angels Point, and so on. As this song came together, I listened to it while walking around in Elysian, so the tribute felt appropriate. It’s the midway point of the record, and felt like a good place to have a nice acoustic interlude. A moment of pause.”<br />\n<b>“Closer”</b>\n“I was digging around in my archives and stumbled upon an old session recording with Andreya Triana, a singer-songwriter who I’d worked with back in 2009. I produced her debut album, <i>Lost Where I Belong</i>, in my apartment in London. I pulled some vocals from this one track ‘Far Closer,’ and it worked really well. I hit her up and was like, ‘Hey! Remember this vocal? I've started sampling it again on this other thing.’ She got a kick out of it.” <br />\n<b>“Age of Phase”</b>\n“Throughout this whole process, I was playing a lot with modular synths. It was a way of keeping the process exciting, to learn how to use different technology. ‘Age of Phase’ is basically exclusively modular synths, apart from the vocals, and that was a new thing for me. I wanted to create all these interweaving melodies and vocals and have everything reach this chaotic peak, before diving down into something really lush. I'm going to try to deconstruct it for the live show and see how far I can push that idea.”<br />\n<b>“From You” (feat. Joji)</b>\n“This one seems like it’s a bit of a curveball for some people. Maybe myself as well. But I was trying to do something that sounded a bit more like contemporary hip-hop and R&B. I was listening to Kehlani, SZA, slowthai, even some James Blake, and was really inspired by that blended sound. I'd always wanted to work with Joji, because I think he's a really interesting musician, and when the parts all came together I was like, ‘Wow, okay, this is kind of a pop song. And I'm kind of into that.’”<br /> \n<b>“Counterpart”</b>\n“This song came together early on and was exactly the mix of sounds I was looking for—a little bit techno, but quite melodic, with lots of modular synths. It was so fun to make that I was sad when I finished it, so now I’m working on a live version as well. I think it’s going to have multiple lives.”<br />\n<b>“Sapien”</b>\n“This is my throwback to early-'90s rave—artists like Mike Paradinas, Rephlex, and Future Sound of London, that era of melodic, ravey breakbeats. I sent the piano part into a modular so I could get all those choppy synth parts that are actually from a Rhodes piano, and then I went apeshit on drum programming at the end as a way to hearken back to that era of frenetic drum breaks. It’s one of the more abrasive moments on the record, which I really like.”<br />\n<b>“Day by Day” (feat. Kadhja Bonet)</b>\n“This is a straight R&B jam, really. I had spoken to Kadhja for ages and we'd sent demos back and forth. And the thing I like about this one is that it references earlier stuff of mine. It feels like it could be from the <i>Black Sands</i> era, which makes me feel like I’ve come full circle. I also like that it has a sense of optimism as the album closer, serving as a reminder that everything’s going to be all right.”",
          "short": "A rich tribute to California that’s as sprawling and varied as the landscape."
        },
        "isCompilation": false
      }
    },
    {
      "id": "611171778",
      "type": "albums",
      "href": "/v1/catalog/us/albums/611171778",
      "attributes": {
        "artwork": {
          "width": 2362,
          "height": 2362,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/e8/66/f6/e866f673-a3c7-f705-645c-c5b42bd9c7d4/5021392806198.jpg/{w}x{h}bb.jpg",
          "bgColor": "08232f",
          "textColor1": "93d3a0",
          "textColor2": "7bd1c6",
          "textColor3": "77b089",
          "textColor4": "64aea8"
        },
        "artistName": "Bonobo",
        "isSingle": false,
        "url": "https://music.apple.com/us/album/the-north-borders/611171778",
        "isComplete": true,
        "genreNames": [
          "Electronic",
          "Music",
          "Dance",
          "Rock",
          "Jazz",
          "Big Band",
          "Bop"
        ],
        "trackCount": 13,
        "isMasteredForItunes": true,
        "releaseDate": "2013-03-21",
        "name": "The North Borders",
        "recordLabel": "Ninja Tune",
        "upc": "5021392806198",
        "copyright": "℗ 2013 Ninja Tune",
        "playParams": {
          "id": "611171778",
          "kind": "album"
        },
        "editorialNotes": {
          "standard": "While the fifth studio album from producer Simon Green (a.k.a. Bonobo) continues to soothe the eardrums with his signature style of soulful downbeat, <i>The North Borders</i> is also rife with previously unheard nuances. Over a more studied mix of acoustic and electronic textures, Bonobo mixes in some salient guest vocal parts—with Erykah Badu’s the most alluring. She sounds almost robotic in \"Heaven for the Sinner” as her phrasing matches the deliberately stuttered rhythms pulsing over a delicate tangle of horns, harps, strings, and woodwinds. Grey Reverend sets a mellow vibe in the opening “First Fires,” where his smoky inflections recall moments from Terry Callier’s 1972 opus <i>What Color Is Love</i>. Similarly, the creamy inflections of electronica soul singer Szjerdene are a perfect fit the ethereal “Towers,” which nicely balances the rich resonance of wooden percussion with the slow percolation of drum-machine beats and what sounds like vintage analog synth tones. She turns up again in the more spatial “Transits,” which has a dusty-vinyl effect that approximates the warm crackles and pops of playing an old record.",
          "short": "Soulful downtempo furnished with the finest materials."
        },
        "isCompilation": false
      }
    },
    {
      "id": "1494326872",
      "type": "albums",
      "href": "/v1/catalog/us/albums/1494326872",
      "attributes": {
        "artwork": {
          "width": 6000,
          "height": 6000,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/84/d6/c2/84d6c2e9-1894-d3d2-6093-4b2eb35ad955/dj.zznyrtzk.png/{w}x{h}bb.jpg",
          "bgColor": "110000",
          "textColor1": "00cfc6",
          "textColor2": "e48311",
          "textColor3": "03a59f",
          "textColor4": "ba690d"
        },
        "artistName": "Little Dragon",
        "isSingle": false,
        "url": "https://music.apple.com/us/album/new-me-same-us/1494326872",
        "isComplete": true,
        "genreNames": [
          "Electronic",
          "Music"
        ],
        "trackCount": 11,
        "isMasteredForItunes": false,
        "releaseDate": "2020-03-27",
        "name": "New Me, Same Us",
        "recordLabel": "Ninja Tune",
        "upc": "5054429140514",
        "copyright": "℗ 2020 Ninja Tune",
        "playParams": {
          "id": "1494326872",
          "kind": "album"
        },
        "editorialNotes": {
          "standard": "After five studio albums, Little Dragon has established a reputation for genre-blending experimentation, trance-inducing ’80s pop, and downtempo ’90s R&B. For five albums, the band remained faithful to their signature breathy, dreamy dance club sound, but in the three years since the Swedish quartet released <i>Season High</i>, the band has matured lyrically. The subject matter on <i>New Me, Same Us</i> ranges from commentary on the monotony of life to coping with loss of loved ones. “It definitely feels like a personal album for us,” lead singer Yukimi Nagano tells Apple Music during a track-by-track interview for the band’s latest record.<br />\n<b>Hold On</b>\n“It started very much as a house track, actually. The demo version of it really reminded me of ‘Unfinished Sympathy’ by Massive Attack, which is a band that has been a huge influence for us. The song has a deeper meaning about accepting change, which can go for a lot of the other tracks as well. That one in particular is about being able to let go of a former part of yourself and accept the new you in a way. And not being ready to let go of that part of you, the older part of you.”<br />\n<b>Rush</b>\n“‘Rush’ is basically just a song about this feeling of our modern lives and everything moving as a whirlwind, really hectically, and not being able to really reflect on your inner self. In the midst of just being this arrow moving forwards in life, you're filled with feelings of fear and the separation anxiety and all these kinds of things that you maybe can't even deal with properly. It’s about that frenzy of modern-day life.”<br />\n<b>Another Lover</b>\n“I had this beat from the guys and I really loved it. I had a melody that I was working on and I was just sort of a bit stuck. It was my birthday and I had a mushroom, a magic mushroom. I just had to lay down and close my eyes and embrace what was happening. I just felt this huge amount of pain and sorrow for a person that I had not been able to feel any empathy for. And as I felt all those things, I was like, ‘Okay, let me snap out of this. I really want to write this song.’ So in the midst of that, I sort of wrote the song. It just felt very genuine and like my heart was wide open. I sort of recorded the vocals straight after that with snot running out of my nose and tears flowing. I was just like, oh. My voice was so groggy and hoarse. So actually we recorded it the next day.”<br />\n<b>Kids</b>\n“‘Kids’ is one of our tracks that was very playful and experimental. It's kind of dark and hopeful at the same time. It's definitely a reflection on just this time of individualism. Everyone sort of being the star of their own story and kids growing up into this madness. It has an angelic vibe to it with the synth, but it also has the darkness. It has a lot of mixed emotions, and it kind of was one of those tracks that we felt the album needed. It wasn't that single or anything, but it had that experimental vibe that we love and that we've tried to keep in the band and that's important to us.”<br />\n<b>Every Rain</b>\n “The fact that we're all from this earth, this planet, this universe together. In that sense, we're every rain, we're the clouds, we're the sky, we're everything here together, but we change form.”<br />\n<b> New Fiction</b>\n“That started with Fred [Källgren Wallin] singing the chorus and messing with sort of the demo version. I recall him saying that he went out to a party and he kind of just felt like he was seeing it as a very shallow experience where everyone was trying to be something. Sometimes you just feel misplaced in that and you feel like everyone's almost playing roles and following some kind of an invisible curriculum in a way. We need new fantasies to live up to that are more epic than this. My favorite part of that song is the piano solo in the end, because we have a grand piano in the studio right now. We've never had it on any song. Fred had a bit of anxiety because it's not a cheap instrument. It takes all this space and it has this aura around it that is just very serious. He got so excited about having the piano that once it arrived, it put on a big pressure. We were very happy to lighten that pressure by having him sort of let go on that track.”<br />\n<b>Sadness</b>\n“Sadness is the space of transition; it can truly lead to something beautiful. So it's kind of a portal where you can heal yourself, where your tears are something that can be something beautiful and helpful. It's something that I've always enjoyed, when the music has a certain emotion and the lyrics kind of contradict that.”<br />\n<b>Are You Feeling Sad?</b> \n“We have a lot of songs that didn't end up on the album, but 'Are You Feeling Sad?' was just a beat that felt infectious to us and fun. So I didn't have any deep thoughts about it. I didn't sit and explode my brain on what to write on that. It was just sort of freestyling, going into the booth and putting some vocals in. I kind of liked the idea of a dancing song kind of also being a soothing lullaby-ish kind of song, you know? Then with the Kali [Uchis] feature, we were really excited because I just really love her verse on it, so it added something definitely to the whole song. Lifted it up.”<br />\n<b>Where You Belong</b>\n“It started just guitar and vocals. Not typical Little Dragon, just crazy beat from somebody's computer. The song is about the feeling of losing somebody and when you still have their number in your phone and you want to hear their voice or you want to talk to that person. There's that realization of them not being there, but they're always with you, you know? You close your eyes, you know that they're with you no matter what.”<br />\n<b>Stay Right Here</b>\n“‘Stay Right Here’ is a love song. Every album is a sort of reflection of where we are in our lives at the moment. I met somebody in my life, someone now that means so much to me. It's kind of literal, even in the lyrics.”<br />\n<b>Water</b>\n“‘Water’ is also a song that really changed from the demo. It started very electronic and kind of became in the end a song that sounded almost a little country. It's written in a shattered way—I usually just write different sentences that I feel at the moment. It's about time passing and sitting, becoming older and looking out. I wanted to get that sort of feeling of a journey of life, starting somewhere and then ending in another space. You start out in the desert and then you kind of end out in the water.”",
          "short": "“It definitely feels like a personal album for us.”"
        },
        "isCompilation": false
      }
    },
    {
      "id": "1323229946",
      "type": "albums",
      "href": "/v1/catalog/us/albums/1323229946",
      "attributes": {
        "artwork": {
          "width": 3000,
          "height": 3000,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music118/v4/bb/e1/02/bbe10295-370f-a9de-76c0-8b889f7bde02/5054429131970.png/{w}x{h}bb.jpg",
          "bgColor": "000000",
          "textColor1": "9ec4c4",
          "textColor2": "90c7c1",
          "textColor3": "7e9c9c",
          "textColor4": "739f9a"
        },
        "artistName": "Young Fathers",
        "isSingle": false,
        "url": "https://music.apple.com/us/album/cocoa-sugar/1323229946",
        "isComplete": true,
        "genreNames": [
          "Alternative",
          "Music",
          "Electronic",
          "Hip-Hop/Rap",
          "Alternative Rap",
          "Rap"
        ],
        "trackCount": 12,
        "isMasteredForItunes": true,
        "releaseDate": "2018-03-09",
        "name": "Cocoa Sugar",
        "recordLabel": "Ninja Tune",
        "upc": "5054429131970",
        "copyright": "℗ 2018 Ninja Tune",
        "playParams": {
          "id": "1323229946",
          "kind": "album"
        },
        "editorialNotes": {
          "standard": "The Edinburgh trio continues its explorative, pastiche approach, using R&B, hip-hop, dub, gospel, post-punk, and spontaneity as tools. Feeling, not riffs or grooves, is their North Star on “Turn” and “Fee Fi.” They invoke biblical themes on “Holy Ghost” and “Lord,” one pristine and glistening, the other raw oratory, both uplifting. “In My View” comes with a rare hook. Are Young Fathers embracing more traditional methods? Possibly, but <i>Cocoa Sugar</i> is a staggeringly creative listen, soaked with ingenuity and catharsis.",
          "short": "The Edinburgh trio continues to paint outside the lines."
        },
        "isCompilation": false,
        "contentRating": "explicit"
      }
    },
    {
      "id": "416319613",
      "type": "albums",
      "href": "/v1/catalog/us/albums/416319613",
      "attributes": {
        "artwork": {
          "width": 3684,
          "height": 3825,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/83/42/e8/8342e8ba-c32a-49c4-528e-da245abf932f/mzi.jnrfihbz.jpg/{w}x{h}bb.jpg",
          "bgColor": "121d12",
          "textColor1": "fdfffc",
          "textColor2": "ebf2fa",
          "textColor3": "ced1cd",
          "textColor4": "bfc7cb"
        },
        "artistName": "Bonobo",
        "isSingle": false,
        "url": "https://music.apple.com/us/album/days-to-come/416319613",
        "isComplete": true,
        "genreNames": [
          "Electronic",
          "Music",
          "Jazz",
          "Bop",
          "Big Band"
        ],
        "trackCount": 18,
        "isMasteredForItunes": false,
        "releaseDate": "2006-10-02",
        "name": "Days To Come",
        "recordLabel": "Ninja Tune",
        "upc": "5051083020695",
        "copyright": "℗ 2006 Ninja Tune",
        "playParams": {
          "id": "416319613",
          "kind": "album"
        },
        "editorialNotes": {
          "standard": "A bridge between the globetrotting boom-bap of <i>Dial 'M' for Monkey</i> and the more intricate <i>Black Sands</i>, <i>Days To Come</i> is a low-key delight where jazz, funk, and soul are boiled down into a potent concentrate. The singer Bajka provides a slow-burning center of gravity on four songs, and Fink gives \"If You Stayed Over\" a folky tinge. But songs like the cello-infused \"Recurring\" prove that Bonobo doesn't need vocalists to make music that's deeply lyrical and delightfully intimate.",
          "short": "Soulful downtempo enriched by jazzy licks and spellbinding vocal features."
        },
        "isCompilation": false
      }
    },
    {
      "id": "1257093380",
      "type": "albums",
      "href": "/v1/catalog/us/albums/1257093380",
      "attributes": {
        "artwork": {
          "width": 3000,
          "height": 3000,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/a7/cf/d9/a7cfd9bb-334d-e1cf-b9c3-542437965829/dj.qzeopjzm.jpg/{w}x{h}bb.jpg",
          "bgColor": "e29936",
          "textColor1": "121212",
          "textColor2": "2d1a01",
          "textColor3": "3b2d19",
          "textColor4": "51340c"
        },
        "artistName": "Jordan Rakei",
        "isSingle": false,
        "url": "https://music.apple.com/us/album/wallflower/1257093380",
        "isComplete": true,
        "genreNames": [
          "R&B/Soul",
          "Music"
        ],
        "trackCount": 11,
        "isMasteredForItunes": false,
        "releaseDate": "2017-09-22",
        "name": "Wallflower",
        "recordLabel": "Ninja Tune",
        "upc": "5054429119657",
        "copyright": "℗ 2017 Ninja Tune",
        "playParams": {
          "id": "1257093380",
          "kind": "album"
        },
        "editorialNotes": {
          "standard": "Moving to London after the success of 2014’s <i>Groove Curse</i> EP forced New Zealand-born, Brisbane-raised Jordan Rakei to confront his introversion and anxiety. He taps into that experience on this album of warm, inventive soul. With a voice that switches gracefully from velvety longing to Jeff Buckley-like fragility, he picks over his insecurity on the gentle funk of “Nerve” and sighs about an “unnecessary goodbye” on the fluid, string-mottled “Goodbyes.” “Clues Blues” offers the best showcase of Rakei’s skill and versatility, moulding electronic R&B, dub, and jazz into a cohesive soundtrack for his absorbing introspection.",
          "short": "Introversion and introspection fuel an album of inventive soul."
        },
        "isCompilation": false
      }
    }
  ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/record-labels/{id}/view/{view}`

## Parameters

- `extend` ([string]): A list of attribute extensions to apply to resources in the response.
- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `with` ([string]): A list of modifications to apply to the request.

## See Also

- [object RecordLabels](recordlabels.md)
  A resource object that represents a record label.
- [object RecordLabelsResponse](recordlabelsresponse.md)
  The response to a request for record labels.
- [Get a Catalog Record Label](get-a-record-label.md)
  Fetch a record label by using its identifier.
- [Get Multiple Record Labels](get-multiple-record-labels.md)
  Fetch one or more record labels by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-view-on-this-resource-by-name-5uhxd)*