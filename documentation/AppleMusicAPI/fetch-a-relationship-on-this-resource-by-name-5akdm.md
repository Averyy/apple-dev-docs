# Get a Catalog Artist's Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch an artist’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/artists/1147783278/albums
```

**Response**:

```json
{
    "data": [
        {
            "id": "1482041821",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1482041821",
            "attributes": {
                "copyright": "℗ 2019 Mom+Pop",
                "genreNames": [
                    "Alternative",
                    "Music"
                ],
                "releaseDate": "2020-02-14",
                "upc": "858275058666",
                "isMasteredForItunes": false,
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music125/v4/0b/b2/52/0bb2524d-ecfc-1bae-9c1e-218c978d7072/Honeymoon_3K.jpg/{w}x{h}bb.jpg",
                    "bgColor": "fffaa9",
                    "textColor1": "030005",
                    "textColor2": "363240",
                    "textColor3": "353226",
                    "textColor4": "5e5a55"
                },
                "url": "https://music.apple.com/us/album/honeymoon/1482041821",
                "playParams": {
                    "id": "1482041821",
                    "kind": "album"
                },
                "recordLabel": "Mom+Pop",
                "isCompilation": false,
                "trackCount": 9,
                "isSingle": false,
                "name": "Honeymoon",
                "artistName": "Beach Bunny",
                "editorialNotes": {
                    "standard": "With “Prom Queen”—the homespun breakthrough from her 2018 EP of the same name—Beach Bunny’s Lili Trifilio became a sort of Liz Phair for the TikTok generation, inspiring a wealth of fan-made videos that speak to the sheer relatability and emotional charge in every line, no matter how ordinary. (“Shut up, count your calories/I never looked good in mom jeans,” she sings, amid a grid of power chords. “Wish I was like you/Blue-eyed blondie, perfect body.”) On <i>Honeymoon</i>, her Chicago outfit’s first full-length, she sounds like a songwriter quickly coming into her own, even as her best songs capture what it is to feel forever inadequate. Trifilio has a natural way with melody, and everything here sparkles—from quiet-LOUD slow-burns (“Rearview”) to jangly love letters (“Dream Boy”) and well-disguised anthems (“Ms. California”)...",
                    "short": "The Chicago indie outfit follows “Prom Queen” with a debut LP just as honest."
                },
                "isComplete": true
            }
        },
        {
            "id": "1613600183",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1613600183",
            "attributes": {
                "copyright": "℗ 2022 Mom+Pop",
                "genreNames": [
                    "Alternative",
                    "Music"
                ],
                "releaseDate": "2022-07-22",
                "upc": "810090090962",
                "isMasteredForItunes": true,
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/df/4e/68/df4e6833-9828-51d7-cdeb-71ecf6d3a23d/810090090962.png/{w}x{h}bb.jpg",
                    "bgColor": "202020",
                    "textColor1": "aea6f6",
                    "textColor2": "b68ef6",
                    "textColor3": "918bcb",
                    "textColor4": "9878cb"
                },
                "url": "https://music.apple.com/us/album/emotional-creature/1613600183",
                "playParams": {
                    "id": "1613600183",
                    "kind": "album"
                },
                "recordLabel": "Mom+Pop",
                "isCompilation": false,
                "trackCount": 12,
                "isSingle": false,
                "name": "Emotional Creature",
                "artistName": "Beach Bunny",
                "editorialNotes": {
                    "standard": "There’s something they don’t tell you about virality: It never seems to last. Beach Bunny, the Chicago-based indie-rock band fronted by Lili Trifilio, blew up on TikTok when the songs “Prom Queen” and “Cloud 9” (the latter from their 2020 debut LP, <i>Honeymoon</i>) made the rounds. But this is a band of pop songwriters—led by Trifilio’s undeniable ability to write a hook—and so, on Beach Bunny’s sophomore LP, they’re out to make a more permanent name for themselves.\n\nBacked by Fall Out Boy producer Sean O’Keefe, <i>Emotional Creature</i> is all “emotional experiences,” says Trifilio. “And viewing them in a positive, empowering light or feeling deeply shameful—it ties into a greater theme of how we, as humans, feel things,” and how social relationships influence those feelings, be it the Y2K Disney pop of “Entropy,” the rush of a crush on “Fire Escape,” or the proggy sci-fi synth detours of “Gravity” and “Scream.” “I hope it brings relatability,” Trifilio says of the album, “and maybe acts as a cathartic experience for people going through similar things as me. Music’s healing in that way, if you find tracks that resonate.” Below, Trifilio walks Apple Music through <i>Emotional Creature</i>, track by track.\n\n<b>“Entropy”</b>\n“There’s one Jonas Brothers song called ‘Burnin’ Up,’ and it has this transitional lead into the song. It kind of fades in, in a cool way. And with Kelly Clarkson and Avril or any of the big acts of the time, I think I was pulling from a vibe more than trying to mimic anything. The song has a late-’90s, early-2000s feel. I was leaning into that and trying things and seeing what worked and would fit that vibe.”\n\n<b>“Oxygen”</b> \n“I wanted to separate the verses and the choruses, and make the verses have that anxiety undertone—not just lyrically. I wanted the guitar riff a little more chaotic. The choruses are the breakthrough moment in this song where these reflections come together and it’s like, ‘OK, everything’s fine. Don’t stress out so much.’ It took me a while to write, just because it’s quite wordy. It was this ongoing poem, notes in my phone. Once it flowed, I was like, ‘OK, this is a pretty good song. We can put this on the album. It’s not just chaotic word vomit.’”\n\n<b>“Deadweight”</b>\n“‘Deadweight’ feels like a sequel to some <i>Honeymoon</i> tracks. It was 2019, and I was feeling very passionate. I wrote it in 10 minutes; it was super fast, like getting out my therapy session emotions. But I didn’t actually know how to end the song. I procrastinated till we got to the studio and then revealed to everyone that I didn’t have an ending. It reminds me of Vampire Weekend a little bit. And to fill you in on some Midwest history: There’s this place called the Wisconsin Dells, a chaotic water park land. It’s super corny, and they also love cheese. It’s just a really weird place. All of the resorts have really weird theme songs, and I feel like, listening back, we were like, ‘Oh my god, that sounds just like the Kalahari Resort’s theme song.’”\n\n<b>“Gone”</b>\n“The best time I write is if I’m feeling something pretty intense. It’s when, instead of journaling or calling my mom, I’m like, ‘All right, let’s try to get some lyrics out of this situation first.’ Other times, it’s just a bunch of notes on my phone that are all related. I just wanted it to sound aggressive, but also simple at the same time. It’s a straightforward punk song. I like that the chords have some dissonance to them. And the contents of the song are about being stuck in a situation and wanting out, not being sure what the right thing to do is.”\n\n<b>“Eventually”</b>\n“It’s about having panic attacks, but also finding love and how that can be so healing in those moments—to have loved ones. I think I wrote this right after having a panic attack, and I was like, ‘I don’t really know who to talk to about this, but I feel like I need to get this out of my system. I need to reflect on it somehow.’ There’s something bittersweet about it, this sad undertone.“\n\n<b>“Fire Escape”</b>\n“‘I was excited about a trip that was coming up in a couple weeks with my boyfriend. We were long-distance, and I was so excited for this trip that I wrote a fantasy song about what it would be like. I did add some lyrics after the trip, too, capturing the entire event. I’ve always loved New York, and it’s funny because Chicago is, in a lot of ways, similar. It’s not the craziest transition when I’m there, but it still has such a magical mysticism to it. Things were getting a little bit better in my personal life, and I just wanted to write something happy.”\n\n<b>“Weeds”</b>\n“‘Weeds’ was one of the first songs I wrote for the album. It is one of my favorite songs on the record because it deviates from a lot of the breakup-angled songs I have. Those are super self-deprecating, and this was written from the perspective of being my own best friend. It’s me giving myself an intervention, almost. And musically, I think I took a lot of risks—experimenting and trying synths, stuff that isn’t as common on Beach Bunny things.”\n\n<b>“Gravity”</b>\n“A lot of this interlude was improvised. Sean was like, ‘Yeah, you want to do that? OK. We’re going to go get Starbucks or something. We’ll be back in a sec. You work on that.’ With the theme of the album being this salute to old sci-fi, in my head, it’s a movie-soundtrack moment.“\n\n<b>“Scream”</b>\n“‘Scream’ was, by far, the hardest to write. The guitar was fleshed out, but it was very difficult to jam on. With my bandmates, if I bring them a song, we’ll do some trial and error. They just pick up on the vibe, and we know the direction of music. It usually works out pretty easily. But ‘Scream,’ for some reason, it felt like we were all very disjointed. It is so different from other Beach Bunny stuff; it was just difficult for everybody to figure out. Everyone saw that I was getting frustrated, so they left me alone with a bunch of synths, and I tried a bunch of stuff until it finally clicked. I don’t remember how long it took, but I remember after that day, everyone was exhausted and pissed but also happy that it was just done.”\n\n<b>“Infinity Room”</b>\n“There’s this UK artist. His name’s Tom Rosenthal. His songs make me cry all the time. They’re these really sweet, acoustic songs. He’s an amazing lyricist. And there was one song where he sampled bird sounds, and that blew my mind. I wrote it down long before I went to the studio. I was like, ‘I want to put birds on the record. I don’t know where, and I don’t know if that’s going to be weird, but I’m going to bring it up and see what people think.’ It ended up working really well. ‘Infinity Room’ reminds me of being in a greenhouse. It’s ambient nature vibes. The song’s lyrics, in themselves, are ethereal.”\n\n<b>“Karaoke”</b>\n“‘Karaoke’ was written early in the pandemic or right before the pandemic. I feel like that song is, in very simple terms, just about having a crush. It doesn’t have maybe that much depth to it, but it just has a lightheartedness about when you connect with someone cool. Sonically, it’s one of the more laidback songs on the record.”\n\n<b>“Love Song”</b>\n“As soon as this song was written, I was like, ‘OK, I want this album to have a happy ending.’ It really is just a sweet love song that I wanted to write with intention. It’s this big moment and that ties in all the themes. ‘Love Song’ feels like a reflection on all of the hard moments [in a relationship], but at the end, love perseveres and everything’s OK.”",
                    "short": "The indie rockers’ sophomore album is here in Spatial Audio."
                },
                "isComplete": true
            }
        },
        {
            "id": "1476463573",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1476463573",
            "attributes": {
                "copyright": "℗ 2019 Mom+Pop",
                "genreNames": [
                    "Alternative",
                    "Music"
                ],
                "releaseDate": "2018-08-10",
                "isMasteredForItunes": false,
                "upc": "858275058062",
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music114/v4/d0/1b/9f/d01b9f8a-fd47-4428-ef15-e5f23860e988/Prom_Queen_Art.jpg/{w}x{h}bb.jpg",
                    "bgColor": "af7db8",
                    "textColor1": "080008",
                    "textColor2": "221424",
                    "textColor3": "29192b",
                    "textColor4": "3e2942"
                },
                "playParams": {
                    "id": "1476463573",
                    "kind": "album"
                },
                "url": "https://music.apple.com/us/album/prom-queen-ep/1476463573",
                "recordLabel": "Mom+Pop",
                "isCompilation": false,
                "trackCount": 5,
                "isSingle": false,
                "name": "Prom Queen - EP",
                "artistName": "Beach Bunny",
                "isComplete": true
            }
        },
        {
            "id": "1476463541",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1476463541",
            "attributes": {
                "copyright": "℗ 2019 Mom+Pop",
                "genreNames": [
                    "Alternative",
                    "Music"
                ],
                "releaseDate": "2018-01-01",
                "isMasteredForItunes": false,
                "upc": "858275058048",
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music114/v4/c6/82/63/c682635e-f2b6-6183-e4ce-c950f88dcf5a/Sports_Art.jpg/{w}x{h}bb.jpg",
                    "bgColor": "59c2c6",
                    "textColor1": "000808",
                    "textColor2": "33242f",
                    "textColor3": "122d2e",
                    "textColor4": "3a434d"
                },
                "playParams": {
                    "id": "1476463541",
                    "kind": "album"
                },
                "url": "https://music.apple.com/us/album/sports-single/1476463541",
                "recordLabel": "Mom+Pop",
                "isCompilation": false,
                "trackCount": 1,
                "isSingle": true,
                "name": "Sports - Single",
                "artistName": "Beach Bunny",
                "isComplete": true
            }
        },
        {
            "id": "1537898980",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1537898980",
            "attributes": {
                "copyright": "℗ 2020 Mom+Pop",
                "genreNames": [
                    "Alternative",
                    "Music"
                ],
                "releaseDate": "2021-01-15",
                "upc": "858275061680",
                "isMasteredForItunes": false,
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is5-ssl.mzstatic.com/image/thumb/Music124/v4/3d/6f/fd/3d6ffd53-bff6-ab67-c8f3-612a82754cf6/858275061680.png/{w}x{h}bb.jpg",
                    "bgColor": "2f40fb",
                    "textColor1": "feffff",
                    "textColor2": "fa9dc2",
                    "textColor3": "d4d8fe",
                    "textColor4": "d18bcd"
                },
                "url": "https://music.apple.com/us/album/blame-game-ep/1537898980",
                "playParams": {
                    "id": "1537898980",
                    "kind": "album"
                },
                "recordLabel": "Mom+Pop",
                "isCompilation": false,
                "trackCount": 4,
                "isSingle": false,
                "name": "Blame Game - EP",
                "contentRating": "explicit",
                "artistName": "Beach Bunny",
                "isComplete": true
            }
        },
        {
            "id": "1147798746",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1147798746",
            "attributes": {
                "copyright": "℗ 2016 626987 Records DK",
                "genreNames": [
                    "Alternative",
                    "Music",
                    "Pop"
                ],
                "releaseDate": "2016-08-25",
                "upc": "840096230420",
                "isMasteredForItunes": false,
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is4-ssl.mzstatic.com/image/thumb/Music62/v4/4c/44/f4/4c44f4d1-95ec-f4fd-9e64-6ece52416f89/artwork.jpg/{w}x{h}bb.jpg",
                    "bgColor": "74ccf7",
                    "textColor1": "22241b",
                    "textColor2": "262e37",
                    "textColor3": "324547",
                    "textColor4": "354e5d"
                },
                "url": "https://music.apple.com/us/album/pool-party-ep/1147798746",
                "playParams": {
                    "id": "1147798746",
                    "kind": "album"
                },
                "recordLabel": "626987 Records DK",
                "isCompilation": false,
                "trackCount": 5,
                "isSingle": false,
                "name": "Pool Party - EP",
                "artistName": "Beach Bunny",
                "isComplete": true
            }
        },
        {
            "id": "1147782780",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1147782780",
            "attributes": {
                "copyright": "℗ 2016 626987 Records DK",
                "genreNames": [
                    "Alternative",
                    "Music",
                    "Pop"
                ],
                "releaseDate": "2016-08-25",
                "isMasteredForItunes": false,
                "upc": "840096230567",
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music62/v4/e0/e6/83/e0e683c6-d08f-3e08-1e4a-6257228ffe99/artwork.jpg/{w}x{h}bb.jpg",
                    "bgColor": "000000",
                    "textColor1": "f59bff",
                    "textColor2": "d96ee2",
                    "textColor3": "c37bcb",
                    "textColor4": "ad58b5"
                },
                "playParams": {
                    "id": "1147782780",
                    "kind": "album"
                },
                "url": "https://music.apple.com/us/album/animalism-ep/1147782780",
                "recordLabel": "626987 Records DK",
                "isCompilation": false,
                "trackCount": 5,
                "isSingle": false,
                "name": "Animalism - EP",
                "artistName": "Beach Bunny",
                "isComplete": true
            }
        },
        {
            "id": "1445627459",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1445627459",
            "attributes": {
                "copyright": "℗ 2018 Audiotree Music",
                "genreNames": [
                    "Indie Rock",
                    "Music",
                    "Alternative"
                ],
                "releaseDate": "2018-12-13",
                "isMasteredForItunes": false,
                "upc": "192641231230",
                "artwork": {
                    "width": 1400,
                    "height": 1400,
                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music118/v4/86/d0/50/86d050d7-d127-eaed-a787-bbde664cb793/192641231230_Cover.jpg/{w}x{h}bb.jpg",
                    "bgColor": "1a1b16",
                    "textColor1": "fefdf8",
                    "textColor2": "df9e08",
                    "textColor3": "d0d0cb",
                    "textColor4": "b7840b"
                },
                "playParams": {
                    "id": "1445627459",
                    "kind": "album"
                },
                "url": "https://music.apple.com/us/album/beach-bunny-on-audiotree-live-ep/1445627459",
                "recordLabel": "Audiotree Music",
                "isCompilation": false,
                "trackCount": 6,
                "isSingle": false,
                "name": "Beach Bunny on Audiotree Live - EP",
                "artistName": "Beach Bunny",
                "isComplete": true
            }
        },
        {
            "id": "1589473324",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1589473324",
            "attributes": {
                "copyright": "℗ 2021 Mom+Pop",
                "genreNames": [
                    "Alternative",
                    "Music"
                ],
                "releaseDate": "2021-10-27",
                "isMasteredForItunes": true,
                "upc": "810090090610",
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is4-ssl.mzstatic.com/image/thumb/Music112/v4/36/47/7c/36477c67-0ad4-f71d-1c94-a164682d0d9e/810090090610.png/{w}x{h}bb.jpg",
                    "bgColor": "111a15",
                    "textColor1": "f0f0f0",
                    "textColor2": "f9b4ae",
                    "textColor3": "c3c5c4",
                    "textColor4": "cb958f"
                },
                "playParams": {
                    "id": "1589473324",
                    "kind": "album"
                },
                "url": "https://music.apple.com/us/album/oxygen-single/1589473324",
                "recordLabel": "Mom+Pop",
                "isCompilation": false,
                "trackCount": 1,
                "isSingle": true,
                "name": "Oxygen - Single",
                "artistName": "Beach Bunny",
                "isComplete": true
            }
        },
        {
            "id": "1509311498",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1509311498",
            "attributes": {
                "copyright": "℗ 2018 Audiotree Music",
                "genreNames": [
                    "Indie Rock",
                    "Music",
                    "Alternative"
                ],
                "releaseDate": "2018-12-13",
                "isMasteredForItunes": false,
                "upc": "192641231230",
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is5-ssl.mzstatic.com/image/thumb/Music123/v4/24/3e/5f/243e5f2e-955d-9cc1-a068-6e7be660b88b/192641231230.png/{w}x{h}bb.jpg",
                    "bgColor": "1c1d18",
                    "textColor1": "e8a411",
                    "textColor2": "d89913",
                    "textColor3": "bf8912",
                    "textColor4": "b28014"
                },
                "playParams": {
                    "id": "1509311498",
                    "kind": "album"
                },
                "url": "https://music.apple.com/us/album/beach-bunny-on-audiotree-live-ep/1509311498",
                "recordLabel": "Audiotree Music",
                "isCompilation": false,
                "trackCount": 6,
                "isSingle": false,
                "name": "Beach Bunny on Audiotree Live - EP",
                "artistName": "Beach Bunny",
                "isComplete": true
            }
        },
        {
            "id": "1562419539",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1562419539",
            "attributes": {
                "copyright": "℗ 2021 Mom+Pop",
                "genreNames": [
                    "Alternative",
                    "Music"
                ],
                "releaseDate": "2021-04-16",
                "isMasteredForItunes": false,
                "upc": "858275062441",
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is5-ssl.mzstatic.com/image/thumb/Music124/v4/15/9b/62/159b62d6-0585-047b-94d4-96c5d133d278/858275062441.png/{w}x{h}bb.jpg",
                    "bgColor": "c4e3c4",
                    "textColor1": "000000",
                    "textColor2": "161716",
                    "textColor3": "272d27",
                    "textColor4": "394039"
                },
                "playParams": {
                    "id": "1562419539",
                    "kind": "album"
                },
                "url": "https://music.apple.com/us/album/cloud-9-feat-tegan-and-sara-single/1562419539",
                "recordLabel": "Mom+Pop",
                "isCompilation": false,
                "trackCount": 1,
                "isSingle": true,
                "name": "Cloud 9 (feat. Tegan and Sara) - Single",
                "artistName": "Beach Bunny",
                "isComplete": true
            }
        },
        {
            "id": "1243697430",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1243697430",
            "attributes": {
                "copyright": "℗ 2017 626987 Records DK",
                "genreNames": [
                    "Alternative",
                    "Music",
                    "Punk"
                ],
                "releaseDate": "2017-06-01",
                "upc": "840094855403",
                "isMasteredForItunes": false,
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is4-ssl.mzstatic.com/image/thumb/Music117/v4/93/04/07/930407ea-4ca7-b915-d93f-a59b8f1cbf7b/artwork.jpg/{w}x{h}bb.jpg",
                    "bgColor": "e99fdc",
                    "textColor1": "120b13",
                    "textColor2": "251121",
                    "textColor3": "3d283b",
                    "textColor4": "4c2d46"
                },
                "url": "https://music.apple.com/us/album/crybaby-single/1243697430",
                "playParams": {
                    "id": "1243697430",
                    "kind": "album"
                },
                "recordLabel": "626987 Records DK",
                "isCompilation": false,
                "trackCount": 3,
                "isSingle": false,
                "name": "Crybaby - Single",
                "artistName": "Beach Bunny",
                "isComplete": true
            }
        },
        {
            "id": "1590556925",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1590556925",
            "attributes": {
                "copyright": "℗ 2021 Atlantic Recording Corporation",
                "genreNames": [
                    "Pop",
                    "Music"
                ],
                "releaseDate": "2021-10-20",
                "isMasteredForItunes": true,
                "upc": "075679766687",
                "artwork": {
                    "width": 1425,
                    "height": 1425,
                    "url": "https://is5-ssl.mzstatic.com/image/thumb/Music115/v4/33/27/24/33272445-ab79-7a8d-be36-eabb754cd258/075679766687.jpg/{w}x{h}bb.jpg",
                    "bgColor": "343f43",
                    "textColor1": "ebeff8",
                    "textColor2": "8196eb",
                    "textColor3": "c6ccd4",
                    "textColor4": "7184c9"
                },
                "playParams": {
                    "id": "1590556925",
                    "kind": "album"
                },
                "url": "https://music.apple.com/us/album/i-love-you-but-i-love-me-more-feat-beach-bunny-single/1590556925",
                "recordLabel": "Atlantic Records",
                "isCompilation": false,
                "trackCount": 1,
                "isSingle": true,
                "name": "I Love You But I Love Me More (feat. Beach Bunny) - Single",
                "contentRating": "explicit",
                "artistName": "MARINA",
                "isComplete": true
            }
        },
        {
            "id": "1596358408",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1596358408",
            "attributes": {
                "copyright": "℗ 2021 Mom+Pop",
                "genreNames": [
                    "Alternative",
                    "Music"
                ],
                "releaseDate": "2021-10-26",
                "upc": "810090090887",
                "isMasteredForItunes": false,
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is4-ssl.mzstatic.com/image/thumb/Music126/v4/04/e2/21/04e22122-caed-0060-42b7-27932f8b44a4/dj.ygwfwpym.png/{w}x{h}bb.jpg",
                    "bgColor": "f2f3ee",
                    "textColor1": "000000",
                    "textColor2": "00344f",
                    "textColor3": "30302f",
                    "textColor4": "305a6f"
                },
                "url": "https://music.apple.com/us/album/christmas-caller-single/1596358408",
                "playParams": {
                    "id": "1596358408",
                    "kind": "album"
                },
                "recordLabel": "Mom+Pop",
                "isCompilation": false,
                "trackCount": 1,
                "isSingle": true,
                "name": "Christmas Caller - Single",
                "artistName": "Beach Bunny",
                "isComplete": true
            }
        }
    ]
}

```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/artists/{id}/{relationship}`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Artists](artists.md)
  A resource object that represents the artist of an album where an artist can be one or more people.
- [object ArtistsResponse](artistsresponse.md)
  The response to an artists request.
- [Get a Catalog Artist](get-a-catalog-artist.md)
  Fetch an artist by using the artist’s identifier.
- [Get a Catalog Artist’s Relationship View Directly by Name](fetch-a-view-on-this-resource-by-name-4kow5.md)
  Fetch related resources for a single artist’s relationship view.
- [Get Multiple Catalog Artists](get-multiple-catalog-artists.md)
  Fetch one or more artists by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-5akdm)*