# Get Multiple Catalog Playlists

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more playlists by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/playlists?ids=pl.f4d106fed2bd41149aaacabb233eb5eb,pl.4b364b8b182f4115acbf6deb83bd5222
```

**Response**:

```json
{
  "data": [
    {
      "id": "pl.f4d106fed2bd41149aaacabb233eb5eb",
      "type": "playlists",
      "href": "/v1/catalog/us/playlists/pl.f4d106fed2bd41149aaacabb233eb5eb",
      "attributes": {
        "artwork": {
          "width": 1080,
          "height": 1080,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Features122/v4/cf/a6/0b/cfa60b1a-2801-d01f-43ca-32cf75b3bd52/7d2ff641-e31b-48ae-9ba8-1d95435405cf.png/{w}x{h}SC.DN01.jpg?l=en-US",
          "bgColor": "f4f4f4",
          "textColor1": "000000",
          "textColor2": "232121",
          "textColor3": "473e3b",
          "textColor4": "444243"
        },
        "isChart": false,
        "url": "https://music.apple.com/us/playlist/todays-hits/pl.f4d106fed2bd41149aaacabb233eb5eb",
        "lastModifiedDate": "2022-04-13T19:01:51Z",
        "name": "Today’s Hits",
        "playlistType": "editorial",
        "curatorName": "Apple Music Hits",
        "playParams": {
          "id": "pl.f4d106fed2bd41149aaacabb233eb5eb",
          "kind": "playlist",
          "versionHash": "993793b38a53ec95717db443e32a4f9f984ee4c7b8ca88494fa33f126a8ca317"
        },
        "description": {
          "standard": "The first taste of Harry Styles’ forthcoming third album, <I>Harry’s House</I>, has arrived. On “As It Was,” a brisk, daydreamy ballad co-written with Kid Harpoon and Tyler Johnson, the boy-band icon turned bona fide rock star laments one of life’s painful dichotomies: the temptation to look back while being forced to move on ahead. “You know it’s not the same as it was,” he sings on the hook. “In this world, it’s just us.” Add Today’s Hits to your library to stay up on the biggest songs in pop, hip-hop, R&B, and more.",
          "short": "“As It Was,” the daydreamy first single from Harry’s new album, has arrived—in Spatial."
        }
      },
      "relationships": {
        "tracks": {
          "href": "/v1/catalog/us/playlists/pl.f4d106fed2bd41149aaacabb233eb5eb/tracks",
          "data": [
            {
              "id": "1615585008",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1615585008",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/ed/6b/40/ed6b4050-43a0-7f4d-759a-1575c1ab5022/mzaf_4656295327266779662.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/2a/19/fb/2a19fb85-2f70-9e44-f2a9-82abe679b88e/886449990061.jpg/{w}x{h}bb.jpg",
                  "bgColor": "d2c8ad",
                  "textColor1": "090f12",
                  "textColor2": "3d2b16",
                  "textColor3": "313431",
                  "textColor4": "5b4a34"
                },
                "artistName": "Harry Styles",
                "url": "https://music.apple.com/us/album/as-it-was/1615584999?i=1615585008",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 167303,
                "releaseDate": "2022-03-31",
                "isAppleDigitalMaster": false,
                "name": "As It Was",
                "isrc": "USSM12200612",
                "hasLyrics": true,
                "albumName": "Harry's House",
                "playParams": {
                  "id": "1615585008",
                  "kind": "song"
                },
                "trackNumber": 4,
                "composerName": "Harry Styles, Kid Harpoon & Tyler Johnson"
              }
            },
            {
              "id": "1556175854",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1556175854",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/f1/c6/4d/f1c64de7-f813-6d3a-abf3-d980882070ab/mzaf_12341366234979933796.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/f5/7a/9e/f57a9e6a-31c8-0784-dfbd-4a0120bfd4af/21UMGIM17517.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "1b190d",
                  "textColor1": "97e8d9",
                  "textColor2": "7be9cf",
                  "textColor3": "7ebfb0",
                  "textColor4": "68c0a8"
                },
                "artistName": "Justin Bieber",
                "url": "https://music.apple.com/us/album/ghost/1556175419?i=1556175854",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 153190,
                "releaseDate": "2021-03-19",
                "isAppleDigitalMaster": true,
                "name": "Ghost",
                "isrc": "USUM72102635",
                "hasLyrics": true,
                "albumName": "Justice",
                "playParams": {
                  "id": "1556175854",
                  "kind": "song"
                },
                "trackNumber": 11,
                "composerName": "Justin Bieber, Jonathan Bellion, Jordan K. Johnson, Stefan Johnson & Michael Pollack"
              }
            },
            {
              "id": "1606052735",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1606052735",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/75/63/15/756315e7-1b13-81d3-e6ae-d9c8f216b5c6/mzaf_3834926278750257073.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/40/53/7e/40537e1e-263e-a069-a2c0-63c332180343/886449820757.jpg/{w}x{h}bb.jpg",
                  "bgColor": "f6cac9",
                  "textColor1": "060f0b",
                  "textColor2": "41311d",
                  "textColor3": "363431",
                  "textColor4": "654f3f"
                },
                "artistName": "Tate McRae",
                "url": "https://music.apple.com/us/album/shes-all-i-wanna-be/1606052727?i=1606052735",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 206772,
                "releaseDate": "2022-02-04",
                "isAppleDigitalMaster": false,
                "name": "she's all i wanna be",
                "isrc": "USRC12103120",
                "hasLyrics": true,
                "albumName": "she's all i wanna be - Single",
                "playParams": {
                  "id": "1606052735",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Tate McRae & Greg Kurstin"
              }
            },
            {
              "id": "1578986673",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1578986673",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/10/9c/1e/109c1e12-6693-4c71-6d2e-44b2026a0710/mzaf_13345609525827382020.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/ec/2f/92/ec2f929f-e7ea-b291-42d7-75081bd808a1/21UMGIM68484.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "ffffff",
                  "textColor1": "000000",
                  "textColor2": "1e1f1c",
                  "textColor3": "333333",
                  "textColor4": "4b4b4a"
                },
                "artistName": "Elton John & Dua Lipa",
                "url": "https://music.apple.com/us/album/cold-heart-pnau-remix/1578986656?i=1578986673",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 202735,
                "releaseDate": "2021-08-13",
                "isAppleDigitalMaster": true,
                "name": "Cold Heart (PNAU Remix)",
                "isrc": "GBUM72104705",
                "hasLyrics": true,
                "albumName": "Cold Heart (PNAU Remix) - Single",
                "playParams": {
                  "id": "1578986673",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Elton John, Bernie Taupin, Peter Mayes, Nicholas Littlemore & Sam Littlemore"
              }
            },
            {
              "id": "1593185593",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1593185593",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/5e/27/6c/5e276c72-8912-96c8-e172-cedcba40d6dd/mzaf_7238388583545842546.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/c5/ba/2b/c5ba2b96-ff06-5f58-35ad-1c070973cee7/190296362989.jpg/{w}x{h}bb.jpg",
                  "bgColor": "5e38cc",
                  "textColor1": "f1e2ff",
                  "textColor2": "efcdff",
                  "textColor3": "d3c0f4",
                  "textColor4": "d1aff4"
                },
                "artistName": "Anitta",
                "url": "https://music.apple.com/us/album/envolver/1593185587?i=1593185593",
                "discNumber": 1,
                "genreNames": [
                  "Pop Latino",
                  "Music",
                  "Latin"
                ],
                "durationInMillis": 193806,
                "releaseDate": "2021-11-11",
                "isAppleDigitalMaster": true,
                "name": "Envolver",
                "isrc": "USWL12100576",
                "hasLyrics": true,
                "albumName": "Envolver - Single",
                "playParams": {
                  "id": "1593185593",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Cristian Andrés Salazar, Freddy Montalvo, José Carlos Cruz, Julio Manuel González & Larissa de Macedo Machado"
              }
            },
            {
              "id": "1618136917",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1618136917",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/9d/09/be/9d09be7a-49ee-1f3c-99fc-af9d9cfb5e9c/mzaf_18446638603385210363.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 1425,
                  "height": 1425,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/e6/b8/83/e6b88344-8d5d-d353-06bc-3204d87071e6/075679759252.jpg/{w}x{h}bb.jpg",
                  "bgColor": "e5dad8",
                  "textColor1": "0b0c08",
                  "textColor2": "221c16",
                  "textColor3": "363532",
                  "textColor4": "49423d"
                },
                "artistName": "Jack Harlow",
                "url": "https://music.apple.com/us/album/first-class/1618136433?i=1618136917",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 173948,
                "releaseDate": "2022-04-08",
                "isAppleDigitalMaster": false,
                "name": "First Class",
                "isrc": "USAT22203024",
                "hasLyrics": true,
                "albumName": "Come Home The Kids Miss You",
                "playParams": {
                  "id": "1618136917",
                  "kind": "song"
                },
                "trackNumber": 4,
                "composerName": "Christopher Bridges, Douglas Ford, Elvis Williams, Jack Harlow, Jamal Jones, Jasper Lee Harris, Jose Velazquez, Micaiah Raheem, Nickie Jon Pabón, Roget Chahayed, Ryan Vojtesak, Stacy Ferguson & Will Adams",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1590438674",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1590438674",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/b0/35/ac/b035aca7-eaa0-0206-508a-1e3899ba433f/mzaf_14400031600884061270.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 1425,
                  "height": 1425,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/d4/46/bc/d446bcf7-e633-ab67-a2fe-35a95ca74a6c/075679766038.jpg/{w}x{h}bb.jpg",
                  "bgColor": "000000",
                  "textColor1": "efd26f",
                  "textColor2": "cd9f2f",
                  "textColor3": "bfa859",
                  "textColor4": "a47f26"
                },
                "artistName": "Tiësto & Ava Max",
                "url": "https://music.apple.com/us/album/the-motto/1590438335?i=1590438674",
                "discNumber": 1,
                "genreNames": [
                  "Dance",
                  "Music",
                  "Pop"
                ],
                "durationInMillis": 164819,
                "releaseDate": "2021-11-04",
                "isAppleDigitalMaster": false,
                "name": "The Motto",
                "isrc": "CYA112001070",
                "hasLyrics": true,
                "albumName": "The Motto - Single",
                "playParams": {
                  "id": "1590438674",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Amanda Ava Koci, Claudia Valentina, Pablo Bowman, Peter Rycroft, Sarah Blanchard & Tijs Verwest"
              }
            },
            {
              "id": "1618285316",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1618285316",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/4d/41/6c/4d416c8b-aa21-3fd6-3e52-3cfc3a4221df/mzaf_7499053389427491034.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/fc/1e/a5/fc1ea575-13ff-4a85-c158-962042ecdcd8/22UMGIM38834.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "353535",
                  "textColor1": "ececec",
                  "textColor2": "dcc6c6",
                  "textColor3": "c7c7c7",
                  "textColor4": "bba9a9"
                },
                "artistName": "Lil Baby",
                "url": "https://music.apple.com/us/album/in-a-minute/1618285311?i=1618285316",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 200471,
                "releaseDate": "2022-04-08",
                "isAppleDigitalMaster": true,
                "name": "In A Minute",
                "isrc": "USUG12200033",
                "hasLyrics": true,
                "albumName": "In A Minute - Single",
                "playParams": {
                  "id": "1618285316",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Dominique Jones, Kai Hasegawa, Ethan Hayes, Ellie Goulding, James Eliot & Howard New",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1617656020",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617656020",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/39/a8/23/39a82321-7688-47d9-9cec-93ee0541faef/mzaf_8527689616448923136.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music122/v4/8b/d7/1e/8bd71ea5-597c-2cfe-6b9a-9d6edd7e03ca/886449849307.jpg/{w}x{h}bb.jpg",
                  "bgColor": "ffffff",
                  "textColor1": "0d0b04",
                  "textColor2": "002e19",
                  "textColor3": "3e3c36",
                  "textColor4": "335847"
                },
                "artistName": "BIA & J. Cole",
                "url": "https://music.apple.com/us/album/london/1617656019?i=1617656020",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 250723,
                "releaseDate": "2022-04-08",
                "isAppleDigitalMaster": false,
                "name": "LONDON",
                "isrc": "USSM12200193",
                "hasLyrics": true,
                "albumName": "LONDON - Single",
                "playParams": {
                  "id": "1617656020",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Bianca Landrau, Abdul Aziz Dieng, Jon Glass, Timothy John Nihan & J. Cole",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1616190902",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1616190902",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/85/93/16/85931610-cb63-0879-d097-cd322efbd944/mzaf_15979770130176178681.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/4b/4c/2f/4b4c2f27-a28d-1707-24ef-2d9aacf7f439/22UMGIM33759.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "0b0b0b",
                  "textColor1": "1cf288",
                  "textColor2": "19de85",
                  "textColor3": "19c46f",
                  "textColor4": "16b46d"
                },
                "artistName": "Nicki Minaj",
                "url": "https://music.apple.com/us/album/we-go-up-feat-fivio-foreign/1616190898?i=1616190902",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 255189,
                "releaseDate": "2022-03-25",
                "isAppleDigitalMaster": true,
                "name": "We Go Up (feat. Fivio Foreign)",
                "isrc": "USUM72204900",
                "hasLyrics": true,
                "albumName": "We Go Up (feat. Fivio Foreign) - Single",
                "playParams": {
                  "id": "1616190902",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Onika Maraj, Joshua Goods, Anthony Woart Jr., Maxie Ryles, Szymon Świątczak & Konrad Zasada",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1508562516",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1508562516",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/d6/34/b2/d634b201-0f5f-ad53-53d9-1d234d8cb906/mzaf_4956443266741752293.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/da/8b/77/da8b7731-6f4f-eacf-5e74-8b23389eefa1/20UMGIM03371.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "ccabe7",
                  "textColor1": "0c000f",
                  "textColor2": "33003d",
                  "textColor3": "32223a",
                  "textColor4": "52225f"
                },
                "artistName": "Glass Animals",
                "url": "https://music.apple.com/us/album/heat-waves/1508562310?i=1508562516",
                "discNumber": 1,
                "genreNames": [
                  "Alternative",
                  "Music"
                ],
                "durationInMillis": 238805,
                "releaseDate": "2020-06-29",
                "isAppleDigitalMaster": true,
                "name": "Heat Waves",
                "isrc": "GBUM72000433",
                "hasLyrics": true,
                "albumName": "Dreamland",
                "playParams": {
                  "id": "1508562516",
                  "kind": "song"
                },
                "trackNumber": 14,
                "composerName": "Dave Bayley"
              }
            },
            {
              "id": "1608118905",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1608118905",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/3d/c4/bc/3dc4bc45-3a17-2fbc-63b2-c34490a8144f/mzaf_15282976483271231195.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/d9/48/6f/d9486f75-e228-26c2-9498-befd009e2a90/22UMGIM11298.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "dee3e6",
                  "textColor1": "21242d",
                  "textColor2": "32333b",
                  "textColor3": "474a52",
                  "textColor4": "54565d"
                },
                "artistName": "Machine Gun Kelly & blackbear",
                "url": "https://music.apple.com/us/album/make-up-sex/1608118564?i=1608118905",
                "discNumber": 1,
                "genreNames": [
                  "Alternative",
                  "Music"
                ],
                "durationInMillis": 122570,
                "releaseDate": "2022-03-25",
                "isAppleDigitalMaster": true,
                "name": "make up sex",
                "isrc": "USUM72112363",
                "hasLyrics": true,
                "albumName": "mainstream sellout",
                "playParams": {
                  "id": "1608118905",
                  "kind": "song"
                },
                "trackNumber": 7,
                "composerName": "Travis Barker, Omer Fedi, Colson Baker, Nick Long & Matthew Musto",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1571169191",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1571169191",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/3f/1e/20/3f1e2087-98f8-f767-e0c9-3e7a1459a1f3/mzaf_17092363549199162610.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/eb/63/fc/eb63fc4c-f36b-5981-a790-8f05c8dd2df1/886449138852.jpg/{w}x{h}bb.jpg",
                  "bgColor": "0e0e23",
                  "textColor1": "ffffff",
                  "textColor2": "8083f8",
                  "textColor3": "ceced2",
                  "textColor4": "696ccd"
                },
                "artistName": "Doja Cat",
                "url": "https://music.apple.com/us/album/get-into-it-yuh/1571168930?i=1571169191",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 138293,
                "releaseDate": "2021-06-25",
                "isAppleDigitalMaster": true,
                "name": "Get Into It (Yuh)",
                "isrc": "USRC12101535",
                "hasLyrics": true,
                "albumName": "Planet Her",
                "playParams": {
                  "id": "1571169191",
                  "kind": "song"
                },
                "trackNumber": 4,
                "composerName": "Amala Zandile Dlamini, Ari Starace & Sheldon Yu-Ting Cheung",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1610834870",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1610834870",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/8b/80/21/8b8021c3-7084-916e-426d-c93d9116f1f8/mzaf_8859912813450898243.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/b7/e3/2f/b7e32fd7-7ca3-edf6-7df8-861bfcfd6f9a/886449526772.jpg/{w}x{h}bb.jpg",
                  "bgColor": "5d5747",
                  "textColor1": "fcf9f2",
                  "textColor2": "f0d6ba",
                  "textColor3": "dcd9d0",
                  "textColor4": "d3bda3"
                },
                "artistName": "Camila Cabello",
                "url": "https://music.apple.com/us/album/psychofreak-feat-willow/1610834866?i=1610834870",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 201495,
                "releaseDate": "2022-04-08",
                "isAppleDigitalMaster": false,
                "name": "psychofreak (feat. WILLOW)",
                "isrc": "USSM12201108",
                "hasLyrics": true,
                "albumName": "Familia",
                "playParams": {
                  "id": "1610834870",
                  "kind": "song"
                },
                "trackNumber": 3,
                "composerName": "Camila Cabello, Tom Peyton, Willow Smith, Eric Frederic & Scott Harris"
              }
            },
            {
              "id": "1578326262",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1578326262",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview125/v4/0c/2e/d9/0c2ed928-bd02-72cd-b44c-9e906a594f8d/mzaf_15516520863399347490.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/9d/69/f1/9d69f15c-7bcc-24e9-0adc-ec3afd0bf5cc/886449473663.jpg/{w}x{h}bb.jpg",
                  "bgColor": "0f0818",
                  "textColor1": "d3d2e2",
                  "textColor2": "c5c7d8",
                  "textColor3": "aca9ba",
                  "textColor4": "a0a1b1"
                },
                "artistName": "The Kid LAROI & Justin Bieber",
                "url": "https://music.apple.com/us/album/stay/1578326258?i=1578326262",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 141806,
                "releaseDate": "2021-07-09",
                "isAppleDigitalMaster": false,
                "name": "STAY",
                "isrc": "USSM12103949",
                "hasLyrics": true,
                "albumName": "F*CK LOVE 3+: OVER YOU",
                "playParams": {
                  "id": "1578326262",
                  "kind": "song"
                },
                "trackNumber": 3,
                "composerName": "Justin Bieber, Charlton Howard, Blake Slatkin, Omer Fedi, Charlie Puth, Magnus Høiberg, Michael Mule, Isaac DeBoni & Subhaan Rahmaan",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1613376653",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1613376653",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/60/02/01/600201ae-efd2-dc4a-a525-2ac27ad1db83/mzaf_17279416121200249358.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 2100,
                  "height": 2100,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/9a/11/a49a118a-546b-3e7f-4112-92058392e282/850039440298.jpg/{w}x{h}bb.jpg",
                  "bgColor": "150a10",
                  "textColor1": "f0f0f2",
                  "textColor2": "e09c7c",
                  "textColor3": "c4c2c5",
                  "textColor4": "b87f66"
                },
                "artistName": "Megan Thee Stallion & Dua Lipa",
                "url": "https://music.apple.com/us/album/sweetest-pie/1613376645?i=1613376653",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music",
                  "Hip-Hop/Rap"
                ],
                "durationInMillis": 201334,
                "releaseDate": "2022-03-11",
                "isAppleDigitalMaster": true,
                "name": "Sweetest Pie",
                "isrc": "QMCE32200232",
                "hasLyrics": true,
                "albumName": "Sweetest Pie - Single",
                "playParams": {
                  "id": "1613376653",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Clarence Coffee Jr, Dua Lipa, John Walsh Homen, Joshua Isaiah Parker, Megan Pete, Nija Aisha-Alayja Charles, Sarah Hudson & Stephen Kozmeniuk",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1618287720",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1618287720",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/20/82/7a/20827a5a-9d1f-cf06-392f-13d65d7985a0/mzaf_6222343294584303248.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 1400,
                  "height": 1400,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/16/9a/7a/169a7a3f-6f6f-1dba-8d54-7d9a45f14db0/8720355633099_Cover.jpg/{w}x{h}bb.jpg",
                  "bgColor": "222220",
                  "textColor1": "dfd7c4",
                  "textColor2": "d6cbba",
                  "textColor3": "b9b3a3",
                  "textColor4": "b2a99b"
                },
                "artistName": "Yahritza Y Su Esencia",
                "url": "https://music.apple.com/us/album/soy-el-%C3%BAnico/1618287709?i=1618287720",
                "discNumber": 1,
                "genreNames": [
                  "Música Mexicana",
                  "Music",
                  "Latin"
                ],
                "durationInMillis": 214000,
                "releaseDate": "2022-03-25",
                "isAppleDigitalMaster": false,
                "name": "Soy El Único",
                "isrc": "USA2P2208434",
                "hasLyrics": true,
                "albumName": "Obsessed - EP",
                "playParams": {
                  "id": "1618287720",
                  "kind": "song"
                },
                "trackNumber": 3,
                "composerName": "Yahritza Martinez"
              }
            },
            {
              "id": "1610328930",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1610328930",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/65/bd/07/65bd077f-b7c5-c8ff-a727-a5fe60e99d85/mzaf_16293019882878690978.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 1500,
                  "height": 1500,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/37/ad/a3/37ada314-d9b3-a011-cf5a-67795df61322/4050538785609.jpg/{w}x{h}bb.jpg",
                  "bgColor": "fcfcfe",
                  "textColor1": "0d0e10",
                  "textColor2": "393031",
                  "textColor3": "3c3e3f",
                  "textColor4": "60595a"
                },
                "artistName": "5 Seconds of Summer",
                "url": "https://music.apple.com/us/album/complete-mess/1610328928?i=1610328930",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 206361,
                "releaseDate": "2022-03-02",
                "isAppleDigitalMaster": true,
                "name": "COMPLETE MESS",
                "isrc": "QMRSZ2200096",
                "hasLyrics": true,
                "albumName": "COMPLETE MESS - Single",
                "playParams": {
                  "id": "1610328930",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Ashton Irwin, Calum Hood, Luke Hemmings & Michael Clifford"
              }
            },
            {
              "id": "1609137778",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1609137778",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/ee/b8/15/eeb8153f-a9b7-043a-5d09-a9dcc71e5a95/mzaf_7072578783170473923.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/9e/9b/e6/9e9be6a5-431d-3f48-f7b8-76d0726b909e/886449885053.jpg/{w}x{h}bb.jpg",
                  "bgColor": "8696b7",
                  "textColor1": "0e0e0f",
                  "textColor2": "0e111b",
                  "textColor3": "262930",
                  "textColor4": "262c3a"
                },
                "artistName": "Becky G. & KAROL G",
                "url": "https://music.apple.com/us/album/mamiii/1609137776?i=1609137778",
                "discNumber": 1,
                "genreNames": [
                  "Latin",
                  "Music"
                ],
                "durationInMillis": 226088,
                "releaseDate": "2022-02-10",
                "isAppleDigitalMaster": false,
                "name": "MAMIII",
                "isrc": "USRC12200425",
                "hasLyrics": true,
                "albumName": "MAMIII - Single",
                "playParams": {
                  "id": "1609137778",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Rebbeca Marie Gomez, Daniel Echavarria Oviedo, Elena Rose & Carolina Giraldo Navarro"
              }
            },
            {
              "id": "1609153365",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1609153365",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/95/bc/8b/95bc8baa-e30c-e473-fc01-23e0f32a701d/mzaf_14860574255381362172.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/57/b8/6f/57b86fe3-775c-5cbb-b614-3ec30dc08e74/886449824731.jpg/{w}x{h}bb.jpg",
                  "bgColor": "261110",
                  "textColor1": "fae2b8",
                  "textColor2": "f9dcd0",
                  "textColor3": "cfb996",
                  "textColor4": "ceb3aa"
                },
                "artistName": "Mimi Webb",
                "url": "https://music.apple.com/us/album/house-on-fire/1609153361?i=1609153365",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 140803,
                "releaseDate": "2022-02-18",
                "isAppleDigitalMaster": false,
                "name": "House On Fire",
                "isrc": "USSM12109778",
                "hasLyrics": true,
                "albumName": "House On Fire - Single",
                "playParams": {
                  "id": "1609153365",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Mimi Webb, Pablo Bowman, Ines Dunn, Charlie Martin & Joe Housley"
              }
            },
            {
              "id": "1611219512",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611219512",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/36/56/16/36561657-7052-9812-b412-36c19e73474b/mzaf_12167760052759322492.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 1500,
                  "height": 1500,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/99/99/ad/9999ad82-4828-1254-4e11-2134461e174d/194690764974_cover.jpg/{w}x{h}bb.jpg",
                  "bgColor": "f7eaf1",
                  "textColor1": "3f1c2b",
                  "textColor2": "432431",
                  "textColor3": "634553",
                  "textColor4": "674c58"
                },
                "artistName": "Tyga & Doja Cat",
                "url": "https://music.apple.com/us/album/freaky-deaky/1611219510?i=1611219512",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 215281,
                "releaseDate": "2022-02-25",
                "isAppleDigitalMaster": false,
                "name": "Freaky Deaky",
                "isrc": "USUYG1414608",
                "hasLyrics": true,
                "albumName": "Freaky Deaky - Single",
                "playParams": {
                  "id": "1611219512",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Alyssa Lourdiz Cantu, Amala Dlamini, Michael Stevenson, Brandon Hamlin, Lukasz Gottwald, Mike Crook, Ryan Ogren & Suzanne Vega",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1616186939",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1616186939",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/db/3f/47/db3f47bf-4665-6f83-cf79-94059cb69fb2/mzaf_9123346230545605100.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/00/e2/c7/00e2c71b-3b7c-d9b6-7ee5-50dc7412af42/22UMGIM29279.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "1f1f15",
                  "textColor1": "e7bbdc",
                  "textColor2": "d89598",
                  "textColor3": "bf9bb4",
                  "textColor4": "b37d7e"
                },
                "artistName": "Shawn Mendes",
                "url": "https://music.apple.com/us/album/when-youre-gone/1616186935?i=1616186939",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 172267,
                "releaseDate": "2022-03-31",
                "isAppleDigitalMaster": true,
                "name": "When You're Gone",
                "isrc": "USUM72204098",
                "hasLyrics": true,
                "albumName": "When You're Gone - Single",
                "playParams": {
                  "id": "1616186939",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Shawn Mendes, Jonah Shy & Scott Harris"
              }
            },
            {
              "id": "1614337328",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1614337328",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/78/b4/95/78b4950f-35fc-db75-bdbc-4160f3185f9f/mzaf_8522342611911731563.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3627,
                  "height": 3627,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/62/f2/68/62f268ef-321f-bfb3-bccc-d1b5d98e3754/22UMGIM25438.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "040513",
                  "textColor1": "f070c4",
                  "textColor2": "43a2e1",
                  "textColor3": "c05ba1",
                  "textColor4": "3683b8"
                },
                "artistName": "Coi Leray & Nicki Minaj",
                "url": "https://music.apple.com/us/album/blick-blick/1614337202?i=1614337328",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 178413,
                "releaseDate": "2022-03-18",
                "isAppleDigitalMaster": true,
                "name": "Blick Blick",
                "isrc": "USUM72203386",
                "hasLyrics": true,
                "albumName": "Blick Blick - Single",
                "playParams": {
                  "id": "1614337328",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Coi Leray, Nicki Minaj, Lukasz Gottwald, Rocco Valdes, Ryan Ogren, Mike Crook, Randall Hammers & Asia Smith",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1613569750",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1613569750",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/b5/87/c6/b587c646-971c-4b20-f795-5a3282ce4114/mzaf_16419497482764902441.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 4000,
                  "height": 4000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/0e/f5/d7/0ef5d766-42df-7f2c-f6a5-bc7004754403/190296182464.jpg/{w}x{h}bb.jpg",
                  "bgColor": "ffffff",
                  "textColor1": "000000",
                  "textColor2": "5e0655",
                  "textColor3": "333333",
                  "textColor4": "7e3877"
                },
                "artistName": "Joel Corry, David Guetta & Bryson Tiller",
                "url": "https://music.apple.com/us/album/what-would-you-do/1613569404?i=1613569750",
                "discNumber": 1,
                "genreNames": [
                  "Dance",
                  "Music",
                  "House"
                ],
                "durationInMillis": 174215,
                "releaseDate": "2022-03-18",
                "isAppleDigitalMaster": false,
                "name": "What Would You Do?",
                "isrc": "GBAHS2200279",
                "hasLyrics": true,
                "albumName": "What Would You Do? - Single",
                "playParams": {
                  "id": "1613569750",
                  "kind": "song"
                },
                "trackNumber": 1
              }
            },
            {
              "id": "1586662253",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1586662253",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/0a/8c/6a/0a8c6ac9-659e-55f9-dc08-f5522e73ca26/mzaf_10708622331232675633.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/e7/bb/89/e7bb8947-38c3-8ad0-fb6e-6b90891af223/886449568475.jpg/{w}x{h}bb.jpg",
                  "bgColor": "884a4d",
                  "textColor1": "fae3ce",
                  "textColor2": "febf00",
                  "textColor3": "e3c4b4",
                  "textColor4": "e7a80f"
                },
                "artistName": "Lucky Daye",
                "url": "https://music.apple.com/us/album/over/1586662251?i=1586662253",
                "discNumber": 1,
                "genreNames": [
                  "R&B/Soul",
                  "Music"
                ],
                "durationInMillis": 205276,
                "releaseDate": "2021-09-22",
                "isAppleDigitalMaster": false,
                "name": "Over",
                "isrc": "USRC12102179",
                "hasLyrics": true,
                "albumName": "Over - Single",
                "playParams": {
                  "id": "1586662253",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "David Brown, Dernst Emile II, Carl Devonish, Jr., Mike “Hunnid” McGregor, Ivan Barias, Carvin Haggins, Taalib Johnson & Francis Lai",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1616261253",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1616261253",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/a6/38/f8/a638f82a-0f39-74d1-4077-89c295cd859b/mzaf_5249797436524250229.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/9b/6f/83/9b6f83ae-16b8-e873-74fb-494e4340108f/886449924967.jpg/{w}x{h}bb.jpg",
                  "bgColor": "b51f2b",
                  "textColor1": "fff3a1",
                  "textColor2": "fca059",
                  "textColor3": "f0c889",
                  "textColor4": "ee8650"
                },
                "artistName": "Latto & Mariah Carey",
                "url": "https://music.apple.com/us/album/big-energy-remix-feat-dj-khaled/1616261250?i=1616261253",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 181666,
                "releaseDate": "2022-03-28",
                "isAppleDigitalMaster": false,
                "name": "Big Energy (Remix) [feat. DJ Khaled]",
                "isrc": "USRC12200496",
                "hasLyrics": true,
                "albumName": "Big Energy (Remix) [feat. DJ Khaled] - Single",
                "playParams": {
                  "id": "1616261253",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Mariah Carey, Alyssa Stephens, Vaughn Oliver, Lukasz Gottwald, Theron Thomas, Adrian Belew, Christopher Frantz, Steven Stanley, Tina Weymouth, Randall Hammers, Jaucquez Lowe, A1 Laflare & Dave Hall",
                "contentRating": "clean"
              }
            },
            {
              "id": "1591640885",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1591640885",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/b0/d6/0d/b0d60dfb-bee9-6cd9-2549-0ec2b7bd1848/mzaf_17985568768977172877.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/76/77/08/767708a7-ec93-3b3d-3bac-40086e5a265c/21UM1IM29634.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "141a10",
                  "textColor1": "fcfef9",
                  "textColor2": "fe255c",
                  "textColor3": "cdd0ca",
                  "textColor4": "cf224c"
                },
                "artistName": "Imagine Dragons, JID & League of Legends",
                "url": "https://music.apple.com/us/album/enemy-from-the-series-arcane-league-of-legends/1591640884?i=1591640885",
                "discNumber": 1,
                "genreNames": [
                  "Alternative",
                  "Music"
                ],
                "durationInMillis": 173381,
                "releaseDate": "2021-10-28",
                "isAppleDigitalMaster": true,
                "name": "Enemy (From the series \"Arcane League of Legends\")",
                "isrc": "USUM72119916",
                "hasLyrics": true,
                "albumName": "Enemy (From the series \"Arcane League of Legends\") - Single",
                "playParams": {
                  "id": "1591640885",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Dan Reynolds, Justin Tranter, Wayne Sermon, Ben McKee, Daniel Platzman, Robin Fredriksson, Mattias Larsson & Destin Route"
              }
            },
            {
              "id": "1582660725",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1582660725",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/f9/3e/30/f93e30ce-5100-ab65-4b78-2b71b6009c06/mzaf_14575040342747165136.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/9f/cf/dc/9fcfdc19-7a61-3836-defb-35d817529b25/886449511440.jpg/{w}x{h}bb.jpg",
                  "bgColor": "286a80",
                  "textColor1": "f9eae3",
                  "textColor2": "fbeacc",
                  "textColor3": "cfd0cf",
                  "textColor4": "d1d1bc"
                },
                "artistName": "Lil Nas X",
                "url": "https://music.apple.com/us/album/thats-what-i-want/1582660720?i=1582660725",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 143901,
                "releaseDate": "2021-09-17",
                "isAppleDigitalMaster": false,
                "name": "THATS WHAT I WANT",
                "isrc": "USSM12105732",
                "hasLyrics": true,
                "albumName": "MONTERO",
                "playParams": {
                  "id": "1582660725",
                  "kind": "song"
                },
                "trackNumber": 4,
                "composerName": "Montero Hill, Omer Fedi, Blake Slatkin, Ryan Tedder & Keegan Bach",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1605027811",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1605027811",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/d8/26/38/d82638fb-45aa-7499-c5c1-43ba353b31e4/mzaf_1879488895182273923.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/bf/94/7a/bf947ab2-e9f0-5263-8a3d-d4f0ef6192d6/22UMGIM02189.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "035b91",
                  "textColor1": "f9f5eb",
                  "textColor2": "f9dfdb",
                  "textColor3": "c8d6d9",
                  "textColor4": "c8c5cc"
                },
                "artistName": "Em Beihold",
                "url": "https://music.apple.com/us/album/numb-little-bug/1605027263?i=1605027811",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 169238,
                "releaseDate": "2022-01-28",
                "isAppleDigitalMaster": true,
                "name": "Numb Little Bug",
                "isrc": "USUM72200626",
                "hasLyrics": true,
                "albumName": "Numb Little Bug - Single",
                "playParams": {
                  "id": "1605027811",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Emily Beihold, Nick Lopez & Andrew DeCaro"
              }
            },
            {
              "id": "1607918366",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1607918366",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/5c/8d/fc/5c8dfc8e-386c-94b9-5568-5803eec02f3e/mzaf_13044269597646734758.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/5b/da/8d/5bda8d04-7f2f-4417-12a0-e039dd011152/886449800193.jpg/{w}x{h}bb.jpg",
                  "bgColor": "ffffff",
                  "textColor1": "191716",
                  "textColor2": "5b1b17",
                  "textColor3": "474544",
                  "textColor4": "7c4946"
                },
                "artistName": "ROSALÍA",
                "url": "https://music.apple.com/us/album/candy/1607918350?i=1607918366",
                "discNumber": 1,
                "genreNames": [
                  "Pop Latino",
                  "Music",
                  "Latin",
                  "Pop"
                ],
                "durationInMillis": 193489,
                "releaseDate": "2022-03-18",
                "isAppleDigitalMaster": false,
                "name": "CANDY",
                "isrc": "USSM12109219",
                "hasLyrics": true,
                "albumName": "MOTOMAMI",
                "playParams": {
                  "id": "1607918366",
                  "kind": "song"
                },
                "trackNumber": 2,
                "composerName": "ROSALÍA, Pablo Diaz-Reixa, Frank Dukes, Adam Feeney, Kaan Gunesberk, David Rodriguez, William Bevan, Lashawn Daniels, Fred Jerkins III, Rodney Jerkins & William Ray Norwood, Jr."
              }
            },
            {
              "id": "1615477888",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1615477888",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/b6/76/29/b67629a8-67e8-86d5-d84a-e22164062b44/mzaf_15167415255791773183.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/91/a7/d8/91a7d82d-5416-2d72-014f-c62ed8a1e89c/22UMGIM27509.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "edf7f9",
                  "textColor1": "2c1b15",
                  "textColor2": "351a15",
                  "textColor3": "524743",
                  "textColor4": "5a4643"
                },
                "artistName": "Summer Walker, SZA & Cardi B",
                "url": "https://music.apple.com/us/album/no-love-extended-version/1615477870?i=1615477888",
                "discNumber": 1,
                "genreNames": [
                  "R&B/Soul",
                  "Music"
                ],
                "durationInMillis": 276214,
                "releaseDate": "2022-03-25",
                "isAppleDigitalMaster": true,
                "name": "No Love (Extended Version)",
                "isrc": "USUM72202839",
                "hasLyrics": true,
                "albumName": "No Love (Extended Version) - Single",
                "playParams": {
                  "id": "1615477888",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Summer Walker, Belcalis Almanzar, Charles “Prince Charlez” Hinshaw, Charles Jr Ocansey, Charles McAllister, Sean Garrett, SZA & Sony Anderson de Sousa Ramos",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1612719271",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1612719271",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/99/55/ff/9955ff93-c9cb-eb46-4f87-60785a4fb1ba/mzaf_12809413163359083637.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/8e/d0/e4/8ed0e4a9-bb96-e221-7440-002d2bb973cf/610012525073_cover.jpg/{w}x{h}bb.jpg",
                  "bgColor": "73ee17",
                  "textColor1": "161616",
                  "textColor2": "161616",
                  "textColor3": "294116",
                  "textColor4": "294116"
                },
                "artistName": "Russ",
                "url": "https://music.apple.com/us/album/handsomer-remix-feat-ktlyn/1612719268?i=1612719271",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music",
                  "R&B/Soul"
                ],
                "durationInMillis": 143415,
                "releaseDate": "2022-03-09",
                "isAppleDigitalMaster": false,
                "name": "HANDSOMER (Remix) [feat. Ktlyn]",
                "isrc": "QZQAY2239696",
                "hasLyrics": true,
                "albumName": "HANDSOMER (Remix) [feat. Ktlyn] - Single",
                "playParams": {
                  "id": "1612719271",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Ktlyn Raps & Russell Vitale",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1581087034",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1581087034",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/d8/eb/6a/d8eb6aad-0d8c-8da3-446e-005cb08e5f1c/mzaf_10141041291425116909.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 4000,
                  "height": 4000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/c5/d8/c6/c5d8c675-63e3-6632-33db-2401eabe574d/190296491412.jpg/{w}x{h}bb.jpg",
                  "bgColor": "350200",
                  "textColor1": "fed400",
                  "textColor2": "f54f35",
                  "textColor3": "d5aa00",
                  "textColor4": "cf402a"
                },
                "artistName": "Ed Sheeran",
                "url": "https://music.apple.com/us/album/shivers/1581087024?i=1581087034",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 207853,
                "releaseDate": "2021-09-09",
                "isAppleDigitalMaster": true,
                "name": "Shivers",
                "isrc": "GBAHS2100671",
                "hasLyrics": true,
                "albumName": "=",
                "playParams": {
                  "id": "1581087034",
                  "kind": "song"
                },
                "trackNumber": 2,
                "composerName": "Ed Sheeran, Johnny McDaid, Kal Lavelle & Steve Mac"
              }
            },
            {
              "id": "1597132449",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1597132449",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/9f/28/57/9f285723-1000-4552-c475-0aabddd8d260/mzaf_15032243671015376645.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 4000,
                  "height": 4000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/0c/86/8d/0c868d5a-81f4-42dd-1ce2-f6569fee0585/190296332722.jpg/{w}x{h}bb.jpg",
                  "bgColor": "aaaaaa",
                  "textColor1": "1b1a17",
                  "textColor2": "1b1b1b",
                  "textColor3": "383734",
                  "textColor4": "373737"
                },
                "artistName": "CKay",
                "url": "https://music.apple.com/us/album/emiliana/1597132174?i=1597132449",
                "discNumber": 1,
                "genreNames": [
                  "Afro-Pop",
                  "Music",
                  "African"
                ],
                "durationInMillis": 164848,
                "releaseDate": "2021-12-03",
                "isAppleDigitalMaster": false,
                "name": "Emiliana",
                "isrc": "ZA34K2100657",
                "hasLyrics": true,
                "albumName": "Emiliana - Single",
                "playParams": {
                  "id": "1597132449",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "BMH & CKay"
              }
            },
            {
              "id": "1604944757",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1604944757",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/d5/e3/11/d5e3118f-e055-ad85-9b53-c24c48cac2a0/mzaf_11972939650851221850.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 1425,
                  "height": 1425,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/e6/52/54/e6525474-f011-257e-04b7-12ecbae264e1/810043689519.jpg/{w}x{h}bb.jpg",
                  "bgColor": "9ca5ac",
                  "textColor1": "04080a",
                  "textColor2": "1d2126",
                  "textColor3": "23272b",
                  "textColor4": "363c41"
                },
                "artistName": "Gunna & Future",
                "url": "https://music.apple.com/us/album/pushin-p-feat-young-thug/1604944424?i=1604944757",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 136267,
                "releaseDate": "2022-01-07",
                "isAppleDigitalMaster": true,
                "name": "pushin P (feat. Young Thug)",
                "isrc": "QMCE32200039",
                "hasLyrics": true,
                "albumName": "DRIP SEASON 4EVER",
                "playParams": {
                  "id": "1604944757",
                  "kind": "song"
                },
                "trackNumber": 2,
                "composerName": "Jeffery Lamar Williams, Juke Wong, Nayvadius Wilburn, Sergio Kitchens & Wesley Glass",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1227451772",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1227451772",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview125/v4/01/11/8b/01118b7d-8dfd-4bda-b431-3172d0a7b09a/mzaf_11749717436518009661.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 1425,
                  "height": 1425,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music114/v4/fb/bf/6d/fbbf6d06-9a6c-9c49-c313-aed403613252/075679900180.jpg/{w}x{h}bb.jpg",
                  "bgColor": "242424",
                  "textColor1": "e4e4e4",
                  "textColor2": "cdcdcd",
                  "textColor3": "bdbdbd",
                  "textColor4": "ababab"
                },
                "artistName": "Jaymes Young",
                "url": "https://music.apple.com/us/album/infinity/1227451760?i=1227451772",
                "discNumber": 1,
                "genreNames": [
                  "Alternative",
                  "Music"
                ],
                "durationInMillis": 237655,
                "releaseDate": "2017-06-23",
                "isAppleDigitalMaster": true,
                "name": "Infinity",
                "isrc": "USAT21700938",
                "hasLyrics": true,
                "albumName": "Feel Something",
                "playParams": {
                  "id": "1227451772",
                  "kind": "song"
                },
                "trackNumber": 12,
                "composerName": "Billboard & Jaymes Young"
              }
            },
            {
              "id": "1611056166",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611056166",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/99/f6/bd/99f6bdd9-7446-764b-5fe0-489cfb754583/mzaf_2130758385325759575.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/f4/76/d0/f476d05a-9e7f-4e88-e891-9488dabe3b5f/886449944361.jpg/{w}x{h}bb.jpg",
                  "bgColor": "1a1728",
                  "textColor1": "e39c52",
                  "textColor2": "e98f92",
                  "textColor3": "ba8149",
                  "textColor4": "bf777d"
                },
                "artistName": "Lil Durk",
                "url": "https://music.apple.com/us/album/what-happened-to-virgil-feat-gunna/1611055823?i=1611056166",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 181393,
                "releaseDate": "2022-03-11",
                "isAppleDigitalMaster": false,
                "name": "What Happened To Virgil (feat. Gunna)",
                "isrc": "USQX92200954",
                "hasLyrics": true,
                "albumName": "7220",
                "playParams": {
                  "id": "1611056166",
                  "kind": "song"
                },
                "trackNumber": 9,
                "composerName": "Durk Banks, Sergio Kitchens & Darrel Jackson",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1598221453",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1598221453",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/bd/b4/b9/bdb4b98f-f719-e736-2fd9-edbf2d55ae50/mzaf_6450452364553722682.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/f6/4f/19/f64f19b7-3ab4-ad2d-5a67-ca196d278b44/886449787043.jpg/{w}x{h}bb.jpg",
                  "bgColor": "f8f8f8",
                  "textColor1": "000000",
                  "textColor2": "242731",
                  "textColor3": "313131",
                  "textColor4": "4e5058"
                },
                "artistName": "SZA",
                "url": "https://music.apple.com/us/album/i-hate-u/1598221271?i=1598221453",
                "discNumber": 1,
                "genreNames": [
                  "R&B/Soul",
                  "Music"
                ],
                "durationInMillis": 174000,
                "releaseDate": "2021-12-03",
                "isAppleDigitalMaster": false,
                "name": "I Hate U",
                "isrc": "USRC12103605",
                "hasLyrics": true,
                "albumName": "I Hate U - Single",
                "playParams": {
                  "id": "1598221453",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "SZA, Carter Lang, Robert Bisel, Cody Fayne & Dylan Patrice",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1606770075",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1606770075",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/ba/47/99/ba479934-bf11-5c81-f49e-c7a6cf810eed/mzaf_17792816694450847271.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/75/39/0b/75390bbc-2dff-f39d-e3d5-95851a98f31a/21UM1IM53248.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "f1f1f1",
                  "textColor1": "000000",
                  "textColor2": "131313",
                  "textColor3": "303030",
                  "textColor4": "404040"
                },
                "artistName": "Jax Jones & MNEK",
                "url": "https://music.apple.com/us/album/where-did-you-go/1606770074?i=1606770075",
                "discNumber": 1,
                "genreNames": [
                  "Dance",
                  "Music"
                ],
                "durationInMillis": 177689,
                "releaseDate": "2022-02-04",
                "isAppleDigitalMaster": true,
                "name": "Where Did You Go?",
                "isrc": "GBUM72108841",
                "hasLyrics": true,
                "albumName": "Where Did You Go? - Single",
                "playParams": {
                  "id": "1606770075",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Mark Ralph, Siba, Timucin Lam, Uzoechi Emenike & Wayne Hector"
              }
            },
            {
              "id": "1614925321",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1614925321",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/c1/ba/c1/c1bac15e-c5e6-454b-fcdf-c868c5244853/mzaf_1515460887422021502.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/87/2b/df/872bdf7c-193a-44fa-e254-5946a73f9d8c/22UMGIM29244.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "cbe4e1",
                  "textColor1": "0d2a3c",
                  "textColor2": "0f3347",
                  "textColor3": "334f5d",
                  "textColor4": "345765"
                },
                "artistName": "J Balvin & Ed Sheeran",
                "url": "https://music.apple.com/us/album/forever-my-love/1614925309?i=1614925321",
                "discNumber": 1,
                "genreNames": [
                  "Urbano latino",
                  "Music",
                  "Latin"
                ],
                "durationInMillis": 190601,
                "releaseDate": "2022-03-25",
                "isAppleDigitalMaster": true,
                "name": "Forever My Love",
                "isrc": "QZM5U2200344",
                "hasLyrics": true,
                "albumName": "Sigue/Forever My Love - Single",
                "playParams": {
                  "id": "1614925321",
                  "kind": "song"
                },
                "trackNumber": 2,
                "composerName": "J Balvin, Ed Sheeran, Michael Brun, Justin Quiles & Keytin"
              }
            },
            {
              "id": "1591302173",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1591302173",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/26/1f/a6/261fa6ee-5c94-66b0-082c-e54806a7def6/mzaf_1023143117711369263.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 4000,
                  "height": 4000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/b5/cc/41/b5cc41e2-e100-fd15-a179-08b928c10c88/190296388019.jpg/{w}x{h}bb.jpg",
                  "bgColor": "e0d4c6",
                  "textColor1": "091014",
                  "textColor2": "0b1013",
                  "textColor3": "343737",
                  "textColor4": "363737"
                },
                "artistName": "John Summit",
                "url": "https://music.apple.com/us/album/human-feat-echoes/1591302000?i=1591302173",
                "discNumber": 1,
                "genreNames": [
                  "Dance",
                  "Music"
                ],
                "durationInMillis": 219048,
                "releaseDate": "2021-11-24",
                "isAppleDigitalMaster": false,
                "name": "Human (feat. Echoes)",
                "isrc": "GBAYE2101411",
                "hasLyrics": true,
                "albumName": "Human (feat. Echoes) - Single",
                "playParams": {
                  "id": "1591302173",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Angel Z, Freek Geuze, John Schuster, Oliver Jacobs, Paul Clarke & Phillip Jacobs"
              }
            },
            {
              "id": "1592774398",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1592774398",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/46/ae/a2/46aea269-4890-093c-e7c8-137e844d6584/mzaf_8873314157668988966.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 1425,
                  "height": 1425,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/6b/3b/fc/6b3bfc34-cdce-b3ef-db0f-caa4b760dd0b/075679764195.jpg/{w}x{h}bb.jpg",
                  "bgColor": "000000",
                  "textColor1": "feffff",
                  "textColor2": "c2c8c7",
                  "textColor3": "cbcbcb",
                  "textColor4": "9ba09f"
                },
                "artistName": "Kodak Black",
                "url": "https://music.apple.com/us/album/super-gremlin/1592774394?i=1592774398",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 200548,
                "releaseDate": "2022-02-10",
                "isAppleDigitalMaster": true,
                "name": "Super Gremlin",
                "isrc": "USAT22107295",
                "hasLyrics": true,
                "albumName": "Sniper Gang Presents Syko Bob & Snapkatt: Nightmare Babies",
                "playParams": {
                  "id": "1592774398",
                  "kind": "song"
                },
                "trackNumber": 4,
                "composerName": "Bill K. Kapri, Jacob Canady & Maik Alexander Timmermann",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1610192494",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1610192494",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/ae/46/7f/ae467f19-98f4-efd7-8a0b-fd5818417d73/mzaf_9600752446927552100.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/1d/04/18/1d04187c-76f4-9a83-8006-d09fafb7b02b/054391906199.jpg/{w}x{h}bb.jpg",
                  "bgColor": "201e03",
                  "textColor1": "e4e5b5",
                  "textColor2": "bae0c4",
                  "textColor3": "bdbe91",
                  "textColor4": "9bba9d"
                },
                "artistName": "Omah Lay & Justin Bieber",
                "url": "https://music.apple.com/us/album/attention/1610192492?i=1610192494",
                "discNumber": 1,
                "genreNames": [
                  "R&B/Soul",
                  "Music"
                ],
                "durationInMillis": 180563,
                "releaseDate": "2022-03-03",
                "isAppleDigitalMaster": true,
                "name": "Attention",
                "isrc": "USWB12200242",
                "hasLyrics": true,
                "albumName": "Attention - Single",
                "playParams": {
                  "id": "1610192494",
                  "kind": "song"
                },
                "trackNumber": 1,
                "editorialNotes": {
                  "short": "A powerhouse collab drops at the crossroads of Afrobeats and pop."
                },
                "composerName": "Bernard Harvey, Felisha King, Justin Bieber, Stanley Omah Didia & Vincent van den Ende"
              }
            },
            {
              "id": "1611645052",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611645052",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/66/3a/33/663a337e-e4e1-6bd3-ef0e-55ca3c54b430/mzaf_15392207735980622296.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/b3/cb/0e/b3cb0e55-1998-5193-573e-135e4c92d037/886449967124.jpg/{w}x{h}bb.jpg",
                  "bgColor": "0c1b16",
                  "textColor1": "dbc1ac",
                  "textColor2": "d1b3a1",
                  "textColor3": "b1a08e",
                  "textColor4": "a99485"
                },
                "artistName": "Labrinth & Zendaya",
                "url": "https://music.apple.com/us/album/im-tired-from-euphoria-an-original-hbo-series/1611645050?i=1611645052",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 187944,
                "releaseDate": "2022-03-04",
                "isAppleDigitalMaster": false,
                "name": "I'm Tired (From \"Euphoria\" An Original HBO Series)",
                "isrc": "USQX92200588",
                "hasLyrics": true,
                "albumName": "I'm Tired (From \"Euphoria\" An Original HBO Series) - Single",
                "playParams": {
                  "id": "1611645052",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Labrinth"
              }
            },
            {
              "id": "1607400982",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1607400982",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/01/0a/65/010a658e-b01f-9076-e230-ea87d3882101/mzaf_15437112953829988947.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/f4/ea/ce/f4eace1c-fc05-dca3-b9a4-584699346fc5/dj.atfecqzn.jpg/{w}x{h}bb.jpg",
                  "bgColor": "1a121a",
                  "textColor1": "088dff",
                  "textColor2": "ff363e",
                  "textColor3": "0c74d1",
                  "textColor4": "d12e37"
                },
                "artistName": "Diplo & Miguel",
                "url": "https://music.apple.com/us/album/dont-forget-my-love/1607400716?i=1607400982",
                "discNumber": 1,
                "genreNames": [
                  "Dance",
                  "Music"
                ],
                "durationInMillis": 199091,
                "releaseDate": "2022-02-11",
                "isAppleDigitalMaster": false,
                "name": "Don't Forget My Love",
                "isrc": "USZ4V2200009",
                "hasLyrics": true,
                "albumName": "Diplo",
                "playParams": {
                  "id": "1607400982",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Thomas Wesley Pentz, Miguel Pimentel & Maximilian Jaeger"
              }
            },
            {
              "id": "1594677760",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1594677760",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/b3/5e/8f/b35e8f5f-1632-24da-a843-9720412d1be5/mzaf_18388837828824793637.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/94/4d/9a/944d9a8d-0549-f537-5706-5b083bd84a7d/21UM1IM38949.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "081828",
                  "textColor1": "fdde45",
                  "textColor2": "cbe379",
                  "textColor3": "ccb63f",
                  "textColor4": "a4bb69"
                },
                "artistName": "Carolina Gaitán - La Gaita, Mauro Castillo, Adassa, Rhenzy Feliz, Diane Guerrero, Stephanie Beatriz & Encanto - Cast",
                "url": "https://music.apple.com/us/album/we-dont-talk-about-bruno/1594677532?i=1594677760",
                "discNumber": 1,
                "genreNames": [
                  "Soundtrack",
                  "Music"
                ],
                "durationInMillis": 216120,
                "releaseDate": "2021-11-19",
                "isAppleDigitalMaster": true,
                "name": "We Don't Talk About Bruno",
                "isrc": "USWD12112915",
                "hasLyrics": true,
                "albumName": "Encanto (Original Motion Picture Soundtrack)",
                "playParams": {
                  "id": "1594677760",
                  "kind": "song"
                },
                "trackNumber": 4,
                "composerName": "Lin-Manuel Miranda"
              }
            },
            {
              "id": "1609135208",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1609135208",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/12/01/90/120190d6-fead-f50b-2eb6-7f280f43b001/mzaf_13748076138039923036.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/b9/6e/d3/b96ed3cc-0246-d518-9235-d80d96d6512e/886449914494.jpg/{w}x{h}bb.jpg",
                  "bgColor": "f3f4ec",
                  "textColor1": "050506",
                  "textColor2": "181818",
                  "textColor3": "343534",
                  "textColor4": "444442"
                },
                "artistName": "Dove Cameron",
                "url": "https://music.apple.com/us/album/boyfriend/1609135206?i=1609135208",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 153000,
                "releaseDate": "2022-02-11",
                "isAppleDigitalMaster": false,
                "name": "Boyfriend",
                "isrc": "USQX92200693",
                "hasLyrics": true,
                "albumName": "Boyfriend - Single",
                "playParams": {
                  "id": "1609135208",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Dove Cameron, Evan Blair, Delacey & Skyler Stonestreet",
                "contentRating": "explicit"
              }
            }
          ]
        },
        "curator": {
          "href": "/v1/catalog/us/playlists/pl.f4d106fed2bd41149aaacabb233eb5eb/curator",
          "data": [
            {
              "id": "1526756058",
              "type": "apple-curators",
              "href": "/v1/catalog/us/apple-curators/1526756058"
            }
          ]
        }
      }
    },
            {
              "id": "1614983835",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1614983835",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/a8/3b/6c/a83b6c47-09fa-8dd2-504f-efb63175a9a8/mzaf_4166183649105651539.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/9d/60/16/9d6016fd-63f5-eeff-34ff-9804e92f715e/22UMGIM30752.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "bdbdbb",
                  "textColor1": "0c0905",
                  "textColor2": "25231e",
                  "textColor3": "2f2d2a",
                  "textColor4": "43423d"
                },
                "artistName": "Daddy Yankee",
                "url": "https://music.apple.com/us/album/remix/1614983552?i=1614983835",
                "discNumber": 1,
                "genreNames": [
                  "Urbano latino",
                  "Music",
                  "Latin"
                ],
                "durationInMillis": 163680,
                "releaseDate": "2022-03-25",
                "isAppleDigitalMaster": true,
                "name": "REMIX",
                "isrc": "USUG12201734",
                "hasLyrics": true,
                "albumName": "LEGENDADDY",
                "playParams": {
                  "id": "1614983835",
                  "kind": "song"
                },
                "trackNumber": 3,
                "composerName": "Daddy Yankee, Hector Emmanuel Birriel Caraballo, Roberto Luis Figueroa, Ovimael Maldonado Burgos & Angel Jovian Barbosa Diaz",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1612334064",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1612334064",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/1b/73/49/1b7349f8-19d2-5643-305c-16bca4ea6c13/mzaf_7252790259494814013.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/69/11/7f/69117f16-1000-ee01-65f5-5552cebb7b62/196626550538.jpg/{w}x{h}bb.jpg",
                  "bgColor": "ad0d00",
                  "textColor1": "fcf0da",
                  "textColor2": "f69b89",
                  "textColor3": "ecc3ae",
                  "textColor4": "e77f6e"
                },
                "artistName": "Miky Woodz, Nio García & Jay Wheeler",
                "url": "https://music.apple.com/us/album/nadie/1612334057?i=1612334064",
                "discNumber": 1,
                "genreNames": [
                  "Latin",
                  "Music"
                ],
                "durationInMillis": 212000,
                "releaseDate": "2022-03-17",
                "isAppleDigitalMaster": false,
                "name": "Nadie",
                "isrc": "QM4TX2202893",
                "hasLyrics": true,
                "albumName": "Nadie - Single",
                "playParams": {
                  "id": "1612334064",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Miguel A. Rodriguez, Jose Angel Lopez Martinez & Luis Antonio Quinones-Garcia",
                "contentRating": "explicit"
              }
            }
          ]
        },
        "curator": {
          "href": "/v1/catalog/us/playlists/pl.4b364b8b182f4115acbf6deb83bd5222/curator",
          "data": [
            {
              "id": "976439549",
              "type": "apple-curators",
              "href": "/v1/catalog/us/apple-curators/976439549"
            }
          ]
        }
      }
    }
  ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/playlists`

## Parameters

- `ids` ([string]) *(required)*: The unique identifiers for the playlists. The maximum fetch limit is 25.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Playlists](playlists.md)
  A resource object that represents a playlist.
- [object PlaylistsResponse](playlistsresponse.md)
  The response to a playlists request.
- [Get a Catalog Playlist](get-a-catalog-playlist.md)
  Fetch a playlist by using its identifier.
- [Get a Catalog Playlist's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-707nb.md)
  Fetch a playlist’s relationship by using its identifier.
- [Get a Catalog Playlist’s Relationship View Directly by Name](fetch-a-view-on-this-resource-by-name-6i3ek.md)
  Fetch related resources for a single playlist’s relationship view.
- [Get Charts Playlists by Storefront Value](get-charts-playlists-by-storefront-value.md)
  Fetch one or more Charts Playlists by using their Storefront value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-catalog-playlists)*