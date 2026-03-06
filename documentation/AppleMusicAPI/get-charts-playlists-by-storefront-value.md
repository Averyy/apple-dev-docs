# Get Charts Playlists by Storefront Value

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more Charts Playlists by using their Storefront value.

**Availability**:
- Apple Music 1.0+

#### Discussion

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/playlists?filter[storefront-chart]=us
```

**Response**:

```json
{
  "data": [
    {
      "id": "pl.606afcbb70264d2eb2b51d8dbcfa6a12",
      "type": "playlists",
      "href": "/v1/catalog/us/playlists/pl.606afcbb70264d2eb2b51d8dbcfa6a12",
      "attributes": {
        "artwork": {
          "width": 4320,
          "height": 1080,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Features124/v4/a9/f9/c4/a9f9c49d-63ea-d93a-4920-924f684bc574/U0MtTVMtV1ctVG9wXzEwMF9VU0EtQURBTV9JRD0xNDEyNDQ2MTczLnBuZw.png/{w}x{h}cc.jpg",
          "bgColor": "f5f0e6",
          "textColor1": "000000",
          "textColor2": "400026",
          "textColor3": "372164",
          "textColor4": "5f2646"
        },
        "isChart": true,
        "url": "https://music.apple.com/us/playlist/top-100-usa/pl.606afcbb70264d2eb2b51d8dbcfa6a12",
        "lastModifiedDate": "2022-04-13T07:00:29Z",
        "name": "Top 100: USA",
        "playlistType": "editorial",
        "curatorName": "Apple Music",
        "playParams": {
          "id": "pl.606afcbb70264d2eb2b51d8dbcfa6a12",
          "kind": "playlist",
          "versionHash": "bf1e3a5d6e4dde22a96dadd00e7f62fb8b05728693fe1ec126a6d1710febb08b"
        },
        "description": {
          "standard": "The most-played songs in the United States, updated every day."
        }
      },
      "relationships": {
        "tracks": {
          "href": "/v1/catalog/us/playlists/pl.606afcbb70264d2eb2b51d8dbcfa6a12/tracks",
          "data": [
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
              "id": "1618153473",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1618153473",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/2c/3f/6e/2c3f6e34-69ca-7874-f2c6-79ebd72532cd/mzaf_11649324804628938442.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/56/6d/ce/566dceeb-e2ea-24ff-f601-1c18497b87f8/22UMGIM37903.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "060606",
                  "textColor1": "fefefe",
                  "textColor2": "d3d3d3",
                  "textColor3": "cccccc",
                  "textColor4": "aaaaaa"
                },
                "artistName": "Lil Baby",
                "url": "https://music.apple.com/us/album/right-on/1618153462?i=1618153473",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 213976,
                "releaseDate": "2022-04-08",
                "isAppleDigitalMaster": true,
                "name": "Right On",
                "isrc": "USUG12200031",
                "hasLyrics": true,
                "albumName": "Right On - Single",
                "playParams": {
                  "id": "1618153473",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Dominique Jones & Jacob Canady",
                "contentRating": "explicit"
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
              "id": "1611056020",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611056020",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/4c/66/97/4c66979b-8bb0-3271-a969-4f9e3cc4ca9d/mzaf_17821700581209805848.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/ahhh-ha/1611055823?i=1611056020",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 186538,
                "releaseDate": "2022-02-22",
                "isAppleDigitalMaster": false,
                "name": "AHHH HA",
                "isrc": "USQX92200794",
                "hasLyrics": true,
                "albumName": "7220",
                "playParams": {
                  "id": "1611056020",
                  "kind": "song"
                },
                "trackNumber": 3,
                "composerName": "Durk Banks, Joshua Luellen, Bryan Lamar Simmons, Lesidney Ragland, Konstantinos Latos & Brian Roke",
                "contentRating": "explicit"
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
              "id": "1617332889",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617332889",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/26/97/5a/26975a4d-171f-17c3-e406-72ad28b5a357/mzaf_3428418767810485524.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3600,
                  "height": 3600,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/6c/08/18/6c08184c-61f2-6777-88d4-c08580e09205/22UMGIM33673.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "565656",
                  "textColor1": "fcfcfc",
                  "textColor2": "f2f2f2",
                  "textColor3": "dbdbdb",
                  "textColor4": "d3d3d3"
                },
                "artistName": "42 Dugg & EST Gee",
                "url": "https://music.apple.com/us/album/thump-shit/1617332701?i=1617332889",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 226362,
                "releaseDate": "2022-04-05",
                "isAppleDigitalMaster": true,
                "name": "Thump Shit",
                "isrc": "USUM72202010",
                "hasLyrics": true,
                "albumName": "Last Ones Left",
                "playParams": {
                  "id": "1617332889",
                  "kind": "song"
                },
                "trackNumber": 2,
                "composerName": "Dion Hayes, George Stone III, Sterling White Jr., Papa Abdou Fall, Jared Brown, Isaiah Brown, Khaya Gilika & John Scherer",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1611056032",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611056032",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/28/62/c6/2862c645-dfdc-0bd8-b5d4-94d939994e59/mzaf_7689015035267016845.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/petty-too-feat-future/1611055823?i=1611056032",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 159927,
                "releaseDate": "2022-03-11",
                "isAppleDigitalMaster": false,
                "name": "Petty Too (feat. Future)",
                "isrc": "USQX92200950",
                "hasLyrics": true,
                "albumName": "7220",
                "playParams": {
                  "id": "1611056032",
                  "kind": "song"
                },
                "trackNumber": 7,
                "composerName": "Durk Banks, Nayvadius Wilburn, Roderick Hughey, Broderick Hughey & Adarsh Mani",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1584281787",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1584281787",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/e4/fe/bb/e4febb0a-fff9-0dd0-05e6-9e7e5177e42a/mzaf_16317235683639158681.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/11/36/38/1136384a-eebc-697a-c005-d890e41c0854/21UM1IM07518.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "ffffff",
                  "textColor1": "070707",
                  "textColor2": "1a1631",
                  "textColor3": "383838",
                  "textColor4": "47455a"
                },
                "artistName": "Drake",
                "url": "https://music.apple.com/us/album/knife-talk-feat-21-savage-project-pat/1584281467?i=1584281787",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 242966,
                "releaseDate": "2021-09-03",
                "isAppleDigitalMaster": true,
                "name": "Knife Talk (feat. 21 Savage & Project Pat)",
                "isrc": "USUG12104409",
                "hasLyrics": true,
                "albumName": "Certified Lover Boy",
                "playParams": {
                  "id": "1584281787",
                  "kind": "song"
                },
                "trackNumber": 13,
                "composerName": "Aubrey Drake Graham, S. Bin Abraham-Joseph, L. Wayne, P. Houston, J. Houston, R. Mayers & P. Johnson",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1609794347",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1609794347",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/10/c9/92/10c99225-6f73-9abe-ef6e-5f76c3456e37/mzaf_11440978917850088667.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 1400,
                  "height": 1400,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/0a/51/d7/0a51d787-399d-5f22-d667-1e219755e7e8/850039440106.jpg/{w}x{h}bb.jpg",
                  "bgColor": "0d0d0d",
                  "textColor1": "68b0f6",
                  "textColor2": "3773fb",
                  "textColor3": "568fc7",
                  "textColor4": "2f5ecb"
                },
                "artistName": "Gunna",
                "url": "https://music.apple.com/us/album/banking-on-me/1609794346?i=1609794347",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 200000,
                "releaseDate": "2022-01-07",
                "isAppleDigitalMaster": true,
                "name": "Banking On Me",
                "isrc": "QMCE32200098",
                "hasLyrics": true,
                "albumName": "Banking On Me - Single",
                "playParams": {
                  "id": "1609794347",
                  "kind": "song"
                },
                "trackNumber": 1,
                "contentRating": "explicit"
              }
            },
            {
              "id": "1611056031",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611056031",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/47/a7/89/47a789c4-a84c-a411-3657-41c9b0eaaf9c/mzaf_3094845008323043258.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/no-interviews/1611055823?i=1611056031",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 179806,
                "releaseDate": "2022-03-11",
                "isAppleDigitalMaster": false,
                "name": "No Interviews",
                "isrc": "USQX92200952",
                "hasLyrics": true,
                "albumName": "7220",
                "playParams": {
                  "id": "1611056031",
                  "kind": "song"
                },
                "trackNumber": 6,
                "composerName": "Durk Banks, Trenton Turner & Henri Velasco",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1604945199",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1604945199",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/ec/b2/0c/ecb20cac-fc2c-038a-904c-99f76fcae1b9/mzaf_5205292766664616532.plus.aac.p.m4a"
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
                "artistName": "Gunna",
                "url": "https://music.apple.com/us/album/p-power-feat-drake/1604944424?i=1604945199",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 193347,
                "releaseDate": "2022-01-13",
                "isAppleDigitalMaster": true,
                "name": "P power (feat. Drake)",
                "isrc": "QMCE32200042",
                "hasLyrics": true,
                "albumName": "DRIP SEASON 4EVER",
                "playParams": {
                  "id": "1604945199",
                  "kind": "song"
                },
                "trackNumber": 6,
                "composerName": "Aubrey Drake Graham, Barry Manilow, Leland Wayne & Sergio Kitchens",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1600722156",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1600722156",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/ad/49/f4/ad49f45b-e096-119d-a42c-099fc3fc9de6/mzaf_4802328967878109211.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/6f/73/de/6f73de5d-9bd5-05f1-ebbc-0e053afea88d/886449812868.jpg/{w}x{h}bb.jpg",
                  "bgColor": "2b0754",
                  "textColor1": "fefcff",
                  "textColor2": "bbbcc4",
                  "textColor3": "d3cadc",
                  "textColor4": "9e98ad"
                },
                "artistName": "Lil Durk",
                "url": "https://music.apple.com/us/album/broadway-girls-feat-morgan-wallen/1600721938?i=1600722156",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 185600,
                "releaseDate": "2021-12-19",
                "isAppleDigitalMaster": false,
                "name": "Broadway Girls (feat. Morgan Wallen)",
                "isrc": "USQX92105926",
                "hasLyrics": true,
                "albumName": "Broadway Girls (feat. Morgan Wallen) - Single",
                "playParams": {
                  "id": "1600722156",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Morgan Wallen, Durk Banks, Ryan Vojtesak, Ernest Keith Smith, Rocky Block, Grady Block, J. Reeves & Alexander Izquierdo"
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
              "id": "1611845611",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611845611",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/bb/d7/ed/bbd7edd7-497a-0ca2-66d7-8dc442b83774/mzaf_6481992821617648177.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 1400,
                  "height": 1400,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/35/51/14/355114e5-89cd-7758-44a8-3a195289333a/075679754301.jpg/{w}x{h}bb.jpg",
                  "bgColor": "1a1b1d",
                  "textColor1": "f3f6f4",
                  "textColor2": "f0e6e1",
                  "textColor3": "c8cac9",
                  "textColor4": "c5beba"
                },
                "artistName": "YoungBoy Never Broke Again",
                "url": "https://music.apple.com/us/album/i-hate-youngboy/1611845602?i=1611845611",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 261818,
                "releaseDate": "2022-02-22",
                "isAppleDigitalMaster": false,
                "name": "I Hate YoungBoy",
                "isrc": "USAT22201682",
                "hasLyrics": true,
                "albumName": "I Hate YoungBoy - Single",
                "playParams": {
                  "id": "1611845611",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Jason Goldberg & Kentrell Gaulden",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1615089001",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1615089001",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/79/1d/b2/791db2b9-f02a-7765-51b7-2edf8790f196/mzaf_18275308850715319878.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/19/8e/a3/198ea386-8697-ce57-b33e-10498877eb2d/22UMGIM30737.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "fcfcfc",
                  "textColor1": "090909",
                  "textColor2": "232324",
                  "textColor3": "3a3a3a",
                  "textColor4": "4e4e4f"
                },
                "artistName": "SleazyWorld Go",
                "url": "https://music.apple.com/us/album/sleazy-flow/1615088986?i=1615089001",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 111484,
                "releaseDate": "2021-10-15",
                "isAppleDigitalMaster": false,
                "name": "Sleazy Flow",
                "isrc": "QZNWT2199125",
                "hasLyrics": true,
                "albumName": "Sleazy Flow - Single",
                "playParams": {
                  "id": "1615089001",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Joseph Isaac & Robert Lavar McCoy Jr.",
                "contentRating": "explicit"
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
              "id": "1597172274",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1597172274",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/43/47/94/4347947d-c186-f7b1-6cd4-171ead29782d/mzaf_1890639554222357497.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/70/6f/f9/706ff924-34a1-d3a4-eceb-70162f73d6c6/886449754113.jpg/{w}x{h}bb.jpg",
                  "bgColor": "151515",
                  "textColor1": "fefefe",
                  "textColor2": "d6d6d6",
                  "textColor3": "cfcfcf",
                  "textColor4": "b0b0b0"
                },
                "artistName": "Nardo Wick",
                "url": "https://music.apple.com/us/album/me-or-sum-feat-future-lil-baby/1597172268?i=1597172274",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 225664,
                "releaseDate": "2021-12-01",
                "isAppleDigitalMaster": false,
                "name": "Me or Sum (feat. Future & Lil Baby)",
                "isrc": "USRC12103471",
                "hasLyrics": true,
                "albumName": "Me or Sum (feat. Future & Lil Baby) - Single",
                "playParams": {
                  "id": "1597172274",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Horace Walls, Juan Guerrieri-Maril, Nayvadius Wilburn & Dominique' Jones",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1617353572",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617353572",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/97/ff/61/97ff6152-c10e-ea4e-a9a1-9cb314205865/mzaf_4619734619069466904.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 4500,
                  "height": 4500,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/58/57/64/5857645e-c2a5-717a-f86e-19157ab0aed3/22UMGIM31111.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "060604",
                  "textColor1": "ffffff",
                  "textColor2": "ec7d59",
                  "textColor3": "cdcdcc",
                  "textColor4": "be6548"
                },
                "artistName": "Muni Long",
                "url": "https://music.apple.com/us/album/hrs-hrs/1617353567?i=1617353572",
                "discNumber": 1,
                "genreNames": [
                  "R&B/Soul",
                  "Music"
                ],
                "durationInMillis": 204317,
                "releaseDate": "2021-11-19",
                "isAppleDigitalMaster": true,
                "name": "Hrs & Hrs",
                "isrc": "QZAKB2136210",
                "hasLyrics": true,
                "albumName": "Public Displays Of Affection",
                "playParams": {
                  "id": "1617353572",
                  "kind": "song"
                },
                "trackNumber": 5,
                "composerName": "Priscilla Renea, Kuk Harrell, Hamadi Aaabi, Dylan Graham, Justin Nathaniel Zim, ISAAC WRISTON & Brandon John-Baptiste",
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
              "id": "1617161814",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617161814",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/2d/15/15/2d1515b6-8de9-a0a3-78e2-a51d293ad284/mzaf_15025730616976297303.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/66/a0/fd/66a0fdf7-8b80-06cb-06d1-84b2ccee2765/196589062345.jpg/{w}x{h}bb.jpg",
                  "bgColor": "050409",
                  "textColor1": "dbdcd6",
                  "textColor2": "c5c5c2",
                  "textColor3": "b0b1ad",
                  "textColor4": "9e9e9d"
                },
                "artistName": "Fivio Foreign, Kanye West & Alicia Keys",
                "url": "https://music.apple.com/us/album/city-of-gods/1617161806?i=1617161814",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 256000,
                "releaseDate": "2022-02-11",
                "isAppleDigitalMaster": true,
                "name": "City of Gods",
                "isrc": "USSM12201246",
                "hasLyrics": true,
                "albumName": "B.I.B.L.E.",
                "playParams": {
                  "id": "1617161814",
                  "kind": "song"
                },
                "trackNumber": 4,
                "composerName": "Fivio Foreign, Kanye West, Andrew Taggart, Delacey, Dwayne Abernathy Jr, MIKE DEAN, Allan Lopez, Aswad Asif, Malik Piper, Hamza Hamaal, Cristian Dejesus Tejada, Mark Williams & Raul Cubina",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1611056036",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611056036",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/26/92/b5/2692b5b0-8c1b-46c9-1210-7a060e7caa3c/mzaf_13248173897065423646.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/barbarian/1611055823?i=1611056036",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 149244,
                "releaseDate": "2022-03-11",
                "isAppleDigitalMaster": false,
                "name": "Barbarian",
                "isrc": "USQX92200953",
                "hasLyrics": true,
                "albumName": "7220",
                "playParams": {
                  "id": "1611056036",
                  "kind": "song"
                },
                "trackNumber": 8,
                "composerName": "Durk Banks, John Lam, David McDowell & Roland Hannah",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1611056028",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611056028",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/d9/fd/59/d9fd5964-0783-5cb7-502f-28221184934f/mzaf_12487766867004034334.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/golden-child/1611055823?i=1611056028",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 114580,
                "releaseDate": "2022-03-10",
                "isAppleDigitalMaster": false,
                "name": "Golden Child",
                "isrc": "USQX92200949",
                "hasLyrics": true,
                "albumName": "7220",
                "playParams": {
                  "id": "1611056028",
                  "kind": "song"
                },
                "trackNumber": 5,
                "composerName": "Durk Banks, Christian Ward, Kevin Gomringer, Tim Gomringer, Christopher Pearson & Jorres Nelson",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1617162047",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617162047",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/d7/2a/15/d72a1592-4480-314d-d92b-76c37a33bb53/mzaf_12750717764224200676.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/66/a0/fd/66a0fdf7-8b80-06cb-06d1-84b2ccee2765/196589062345.jpg/{w}x{h}bb.jpg",
                  "bgColor": "050409",
                  "textColor1": "dbdcd6",
                  "textColor2": "c5c5c2",
                  "textColor3": "b0b1ad",
                  "textColor4": "9e9e9d"
                },
                "artistName": "Fivio Foreign",
                "url": "https://music.apple.com/us/album/changed-on-me-feat-vory-polo-g/1617161806?i=1617162047",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 241644,
                "releaseDate": "2022-04-08",
                "isAppleDigitalMaster": true,
                "name": "Changed On Me (feat. Vory & Polo G)",
                "isrc": "USSM12203054",
                "hasLyrics": true,
                "albumName": "B.I.B.L.E.",
                "playParams": {
                  "id": "1617162047",
                  "kind": "song"
                },
                "trackNumber": 13,
                "composerName": "Fivio Foreign, MIKE DEAN, Tavoris Javon Hollins Jr., Taurus Bartlett, Aswad Asif & Kevin Da Silva",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1611056174",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611056174",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/3f/96/cb/3f96cb21-5cec-7543-0e91-771dc6c5b0c2/mzaf_14477534070618867870.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/smoking-thinking/1611055823?i=1611056174",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 147392,
                "releaseDate": "2022-03-11",
                "isAppleDigitalMaster": false,
                "name": "Smoking & Thinking",
                "isrc": "USQX92200956",
                "hasLyrics": true,
                "albumName": "7220",
                "playParams": {
                  "id": "1611056174",
                  "kind": "song"
                },
                "trackNumber": 11,
                "composerName": "Durk Banks, Maliki Decampos, Devonte Richmond, Gabriel Kerr & Cameron Hubler",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1617161815",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617161815",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/9e/2b/73/9e2b7344-d5d4-1f41-9e87-87a0ae5b514b/mzaf_6508174425010683693.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/66/a0/fd/66a0fdf7-8b80-06cb-06d1-84b2ccee2765/196589062345.jpg/{w}x{h}bb.jpg",
                  "bgColor": "050409",
                  "textColor1": "dbdcd6",
                  "textColor2": "c5c5c2",
                  "textColor3": "b0b1ad",
                  "textColor4": "9e9e9d"
                },
                "artistName": "Fivio Foreign & Queen Naija",
                "url": "https://music.apple.com/us/album/whats-my-name-feat-coi-leray/1617161806?i=1617161815",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 201399,
                "releaseDate": "2022-04-08",
                "isAppleDigitalMaster": true,
                "name": "What's My Name (feat. Coi Leray)",
                "isrc": "USSM12203043",
                "hasLyrics": true,
                "albumName": "B.I.B.L.E.",
                "playParams": {
                  "id": "1617161815",
                  "kind": "song"
                },
                "trackNumber": 5,
                "composerName": "Fivio Foreign, Queen Naija Bulls, Coi Collins, Aswad Asif, Luis Campozano, Brendan Walsh, Drü Oliver, Jade Amar, Adrian Lau, Jason L. Patterson, Beyoncé, Lashawn Daniels, Fred Jerkins III, Rodney Jerkins, Kelendria Rowland, LaTavia Roberson & LeToya Luckett",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1617332704",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617332704",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/8a/c1/62/8ac1621c-29d9-bd9b-a1a4-7ea650fd185c/mzaf_16841405227402209904.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3600,
                  "height": 3600,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/6c/08/18/6c08184c-61f2-6777-88d4-c08580e09205/22UMGIM33673.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "565656",
                  "textColor1": "fcfcfc",
                  "textColor2": "f2f2f2",
                  "textColor3": "dbdbdb",
                  "textColor4": "d3d3d3"
                },
                "artistName": "42 Dugg & EST Gee",
                "url": "https://music.apple.com/us/album/ice-talk/1617332701?i=1617332704",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 151422,
                "releaseDate": "2022-04-08",
                "isAppleDigitalMaster": true,
                "name": "Ice Talk",
                "isrc": "USUM72201999",
                "hasLyrics": true,
                "albumName": "Last Ones Left",
                "playParams": {
                  "id": "1617332704",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Dion Hayes, George Stone III & Martin McCurtis",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1617332912",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617332912",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/c7/37/c5/c737c5d5-962e-53f8-9f8b-2526fa6643c3/mzaf_13703778849944624336.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3600,
                  "height": 3600,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/6c/08/18/6c08184c-61f2-6777-88d4-c08580e09205/22UMGIM33673.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "565656",
                  "textColor1": "fcfcfc",
                  "textColor2": "f2f2f2",
                  "textColor3": "dbdbdb",
                  "textColor4": "d3d3d3"
                },
                "artistName": "42 Dugg & EST Gee",
                "url": "https://music.apple.com/us/album/everybody-shooters-too/1617332701?i=1617332912",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 112560,
                "releaseDate": "2022-03-30",
                "isAppleDigitalMaster": true,
                "name": "Everybody Shooters Too",
                "isrc": "USUM72202005",
                "hasLyrics": true,
                "albumName": "Last Ones Left",
                "playParams": {
                  "id": "1617332912",
                  "kind": "song"
                },
                "trackNumber": 12,
                "composerName": "Dion Hayes, George Stone III & MARLON LAFAYETTE BROWN JR",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1618137577",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1618137577",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/e0/6c/14/e06c14ea-aeae-f066-5c2a-3af175ae57a6/mzaf_798812291997874498.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/nail-tech/1618136433?i=1618137577",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 206385,
                "releaseDate": "2022-02-18",
                "isAppleDigitalMaster": false,
                "name": "Nail Tech",
                "isrc": "USAT22200223",
                "hasLyrics": true,
                "albumName": "Come Home The Kids Miss You",
                "playParams": {
                  "id": "1618137577",
                  "kind": "song"
                },
                "trackNumber": 14,
                "composerName": "Amir Sims, Douglas Ford, Jack Harlow, Jahaan Sweet, Jose Velazquez, Matthew Samuels, Montez Dewayne Jones, Roget Chahayed & Scotty Lavell Coleman",
                "contentRating": "explicit"
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
              "id": "1611056227",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611056227",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/40/8e/d1/408ed11a-011b-4c94-1af9-0d2d88b57cee/mzaf_18277615590565193888.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/difference-is-feat-summer-walker/1611055823?i=1611056227",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 193396,
                "releaseDate": "2022-03-11",
                "isAppleDigitalMaster": false,
                "name": "Difference Is (feat. Summer Walker)",
                "isrc": "USQX92200959",
                "hasLyrics": true,
                "albumName": "7220",
                "playParams": {
                  "id": "1611056227",
                  "kind": "song"
                },
                "trackNumber": 13,
                "composerName": "Summer Walker, Durk Banks, Jocelyn Donald, Trenton Turner & Thomas Moore",
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
              "id": "1556670532",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1556670532",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview125/v4/3e/81/15/3e811549-6565-0fba-f5e5-1562cf558b98/mzaf_16245449060790865093.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/63/2a/34/632a3488-d104-3ff1-dc02-4ed86f58ed05/21UMGIM18577.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "101729",
                  "textColor1": "e0e7fa",
                  "textColor2": "b1b9dd",
                  "textColor3": "b6bdd0",
                  "textColor4": "9099b9"
                },
                "artistName": "Drake",
                "url": "https://music.apple.com/us/album/wants-and-needs-feat-lil-baby/1556669854?i=1556670532",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 192956,
                "releaseDate": "2021-03-05",
                "isAppleDigitalMaster": true,
                "name": "Wants and Needs (feat. Lil Baby)",
                "isrc": "USUG12101042",
                "hasLyrics": true,
                "albumName": "Scary Hours 2",
                "playParams": {
                  "id": "1556670532",
                  "kind": "song"
                },
                "trackNumber": 2,
                "composerName": "Aubrey Drake Graham, Dominique Jones, Ronald LaTour, Dylan Cleary-Krell & Noah Shebib",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1600766436",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1600766436",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/dc/67/7b/dc677bac-af4b-6b3b-87ba-9e981e59c0f2/mzaf_9465112466347853788.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/92/b9/62/92b9624d-e9fb-0e4f-f14b-6f1f96c0a3e0/21UM1IM54414.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "263121",
                  "textColor1": "d0d0d0",
                  "textColor2": "b1c9e9",
                  "textColor3": "aeb0ad",
                  "textColor4": "95aac1"
                },
                "artistName": "J. Cole",
                "url": "https://music.apple.com/us/album/no-role-modelz/1600766204?i=1600766436",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 292799,
                "releaseDate": "2014-12-09",
                "isAppleDigitalMaster": true,
                "name": "No Role Modelz",
                "isrc": "USQX91402598",
                "hasLyrics": true,
                "albumName": "2014 Forest Hills Drive",
                "playParams": {
                  "id": "1600766436",
                  "kind": "song"
                },
                "trackNumber": 9,
                "composerName": "J. Cole, Darius Barnes, Marvin Whitemon, Paul Beauregard, Jordan Houston, Tenina Stevens, Earl Stevens, Danell Stevens & Brandt Jones",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1617171589",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617171589",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/a7/d9/9d/a7d99d95-2f59-9cd2-02f7-e10fd1fd6f3d/mzaf_9775747674511223537.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 2000,
                  "height": 2000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/4d/54/ec/4d54eccd-8e71-4217-cb81-445adc77136b/075679750006.jpg/{w}x{h}bb.jpg",
                  "bgColor": "000000",
                  "textColor1": "fafeff",
                  "textColor2": "dddce3",
                  "textColor3": "c7cbcb",
                  "textColor4": "b0b0b5"
                },
                "artistName": "YoungBoy Never Broke Again",
                "url": "https://music.apple.com/us/album/wagwan/1617170958?i=1617171589",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 149333,
                "releaseDate": "2022-04-01",
                "isAppleDigitalMaster": false,
                "name": "Wagwan",
                "isrc": "USAT22203146",
                "hasLyrics": true,
                "albumName": "The Last Slimeto",
                "playParams": {
                  "id": "1617171589",
                  "kind": "song"
                },
                "trackNumber": 24,
                "composerName": "Adnan Khan, Francis Lopez Varela, Jason Goldberg & Kentrell Gaulden",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1574378625",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1574378625",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview125/v4/c2/73/76/c27376ee-77bf-4408-fa67-49d66cf578df/mzaf_14194545279247312737.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/e8/eb/cc/e8ebcc8d-6293-6e7f-7cc5-defa2bdbd4bd/886449399895.jpg/{w}x{h}bb.jpg",
                  "bgColor": "121317",
                  "textColor1": "bcf1fc",
                  "textColor2": "9ae4f0",
                  "textColor3": "9ac4ce",
                  "textColor4": "7fbac4"
                },
                "artistName": "The Kid LAROI & Justin Bieber",
                "url": "https://music.apple.com/us/album/stay/1574378620?i=1574378625",
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
                "albumName": "STAY - Single",
                "playParams": {
                  "id": "1574378625",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Justin Bieber, Charlton Howard, Blake Slatkin, Omer Fedi, Charlie Puth, Magnus Høiberg, Michael Mule, Isaac DeBoni & Subhaan Rahmaan",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1611056176",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611056176",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/c5/48/e6/c548e690-d140-c7aa-f993-8bff5386dd28/mzaf_12440298012776702194.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/blocklist/1611055823?i=1611056176",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 126653,
                "releaseDate": "2022-03-11",
                "isAppleDigitalMaster": false,
                "name": "Blocklist",
                "isrc": "USQX92200957",
                "hasLyrics": true,
                "albumName": "7220",
                "playParams": {
                  "id": "1611056176",
                  "kind": "song"
                },
                "trackNumber": 12,
                "composerName": "Durk Banks, Maliki Decampos, Devonte Richmond & Jarvis Adams Jr.",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1607880044",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1607880044",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/49/ae/69/49ae6921-8b32-42ac-7873-0002020b8396/mzaf_5381259366480931791.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/6f/0c/0a/6f0c0ab2-e0a7-3051-e0c4-b5ec0ab243be/194690707285_cover.jpg/{w}x{h}bb.jpg",
                  "bgColor": "030504",
                  "textColor1": "faf8fd",
                  "textColor2": "f1391a",
                  "textColor3": "c9c7cb",
                  "textColor4": "c12e16"
                },
                "artistName": "King Von & 21 Savage",
                "url": "https://music.apple.com/us/album/dont-play-that/1607880039?i=1607880044",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 133613,
                "releaseDate": "2022-02-04",
                "isAppleDigitalMaster": false,
                "name": "Don't Play That",
                "isrc": "USUYG1402387",
                "hasLyrics": true,
                "albumName": "Don't Play That - Single",
                "playParams": {
                  "id": "1607880044",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Dayvon Bennet & She'yaa Bin Abraham-Joseph",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1584281770",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1584281770",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview125/v4/fa/33/35/fa3335c1-d7e8-621b-efb9-89e5f8078b23/mzaf_14949164923463134807.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/11/36/38/1136384a-eebc-697a-c005-d890e41c0854/21UM1IM07518.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "ffffff",
                  "textColor1": "070707",
                  "textColor2": "1a1631",
                  "textColor3": "383838",
                  "textColor4": "47455a"
                },
                "artistName": "Drake",
                "url": "https://music.apple.com/us/album/way-2-sexy-feat-future-young-thug/1584281467?i=1584281770",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 257605,
                "releaseDate": "2021-09-03",
                "isAppleDigitalMaster": true,
                "name": "Way 2 Sexy (feat. Future & Young Thug)",
                "isrc": "USUG12104403",
                "hasLyrics": true,
                "albumName": "Certified Lover Boy",
                "playParams": {
                  "id": "1584281770",
                  "kind": "song"
                },
                "trackNumber": 7,
                "composerName": "Aubrey Drake Graham, N. Wilburn, J. Williams, B. Simmons, L. Ragland, R. Fairbrass, F. Fairbrass & R. Manzoli",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1613977158",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1613977158",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/f3/70/a3/f370a374-b3b9-34ae-38fb-d69f3aa2f54b/mzaf_10408424559370595737.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/ae/82/c5/ae82c5f9-b544-4cca-a1fc-78dae6040905/886449998067.jpg/{w}x{h}bb.jpg",
                  "bgColor": "161616",
                  "textColor1": "f4f5f9",
                  "textColor2": "4aa3da",
                  "textColor3": "c7c8cb",
                  "textColor4": "3f87b3"
                },
                "artistName": "Lil Tjay",
                "url": "https://music.apple.com/us/album/in-my-head/1613977157?i=1613977158",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 135264,
                "releaseDate": "2022-04-01",
                "isAppleDigitalMaster": false,
                "name": "In My Head",
                "isrc": "USSM12202421",
                "hasLyrics": true,
                "albumName": "In My Head - Single",
                "playParams": {
                  "id": "1613977158",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Lil Tjay, Theron Thomas, Tim Thomas, Jason Desrouleaux, Jonathan Rotem, kisean paul anderson & Keidran Jones",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1440766784",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1440766784",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview125/v4/04/d7/ab/04d7abc5-358b-eac3-da65-8ab33042aaaa/mzaf_3819037996539775303.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 1500,
                  "height": 1500,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/04/f8/63/04f863fc-2852-604f-c910-a97ac069506b/12UMGIM40339.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "f37520",
                  "textColor1": "030202",
                  "textColor2": "0f0d0e",
                  "textColor3": "331908",
                  "textColor4": "3d2212"
                },
                "artistName": "Frank Ocean",
                "url": "https://music.apple.com/us/album/lost/1440765580?i=1440766784",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 234093,
                "releaseDate": "2012-07-10",
                "isAppleDigitalMaster": false,
                "name": "Lost",
                "isrc": "USUM71207186",
                "hasLyrics": true,
                "albumName": "channel ORANGE",
                "playParams": {
                  "id": "1440766784",
                  "kind": "song"
                },
                "trackNumber": 11,
                "composerName": "Micah Otano, Lonnie Breaux, Paul Shelton & J. Ho",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1611056023",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611056023",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/d9/62/f0/d962f043-c58f-09fa-9806-9605edb3a436/mzaf_9461939648521770152.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/shootout-my-crib/1611055823?i=1611056023",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 153813,
                "releaseDate": "2022-03-11",
                "isAppleDigitalMaster": false,
                "name": "Shootout @ My Crib",
                "isrc": "USQX92200967",
                "hasLyrics": true,
                "albumName": "7220",
                "playParams": {
                  "id": "1611056023",
                  "kind": "song"
                },
                "trackNumber": 4,
                "composerName": "Durk Banks, Maliki Decampos, Devonte Richmond & Jarvis Adams Jr.",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1617171580",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617171580",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/1e/48/6d/1e486d12-1bf8-f063-0506-fad45494d193/mzaf_10029231014080545036.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 2000,
                  "height": 2000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/4d/54/ec/4d54eccd-8e71-4217-cb81-445adc77136b/075679750006.jpg/{w}x{h}bb.jpg",
                  "bgColor": "000000",
                  "textColor1": "fafeff",
                  "textColor2": "dddce3",
                  "textColor3": "c7cbcb",
                  "textColor4": "b0b0b5"
                },
                "artistName": "YoungBoy Never Broke Again",
                "url": "https://music.apple.com/us/album/loner-life/1617170958?i=1617171580",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 133333,
                "releaseDate": "2022-04-01",
                "isAppleDigitalMaster": false,
                "name": "Loner Life",
                "isrc": "USAT22203014",
                "hasLyrics": true,
                "albumName": "The Last Slimeto",
                "playParams": {
                  "id": "1617171580",
                  "kind": "song"
                },
                "trackNumber": 22,
                "composerName": "Aaron Gilfenbain, Brian Mitchell, Ethan Hayes, Jason Goldberg, Kentrell Gaulden & Vilyam Vardumyan",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1611056172",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611056172",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/e0/d3/5d/e0d35dbe-c7c1-cd7c-baad-f18c2889fa45/mzaf_3184567054496209151.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/grow-up-keep-it-on-speaker/1611055823?i=1611056172",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 196341,
                "releaseDate": "2022-03-11",
                "isAppleDigitalMaster": false,
                "name": "Grow Up/Keep It On Speaker",
                "isrc": "USQX92200955",
                "hasLyrics": true,
                "albumName": "7220",
                "playParams": {
                  "id": "1611056172",
                  "kind": "song"
                },
                "trackNumber": 10,
                "composerName": "Durk Banks, David Morse, Daniel Ivy, Julian Davis, William Byrd, Ridge Williams & Dominic Brooks",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1614870427",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1614870427",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/07/b5/3c/07b53ccb-96d2-cce2-93b6-743b1e5c0be8/mzaf_11026711619326345299.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/29/ba/71/29ba719b-9dfc-3693-ec8e-c80d518063d2/196589019684.jpg/{w}x{h}bb.jpg",
                  "bgColor": "0b0b0b",
                  "textColor1": "e3e3e3",
                  "textColor2": "c6c6c6",
                  "textColor3": "b8b8b8",
                  "textColor4": "a1a1a1"
                },
                "artistName": "Lil Durk",
                "url": "https://music.apple.com/us/album/computer-murderers/1614870185?i=1614870427",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 139533,
                "releaseDate": "2022-03-18",
                "isAppleDigitalMaster": false,
                "name": "Computer Murderers",
                "isrc": "USQX92201462",
                "hasLyrics": true,
                "albumName": "7220 (Reloaded)",
                "playParams": {
                  "id": "1614870427",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Durk Banks, Trenton Turner & Marko Cervantes",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1611056017",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611056017",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/5d/a9/bc/5da9bc86-cc7c-d787-f260-fe394a7a2e12/mzaf_5755043997493813693.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/headtaps/1611055823?i=1611056017",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 173880,
                "releaseDate": "2022-03-11",
                "isAppleDigitalMaster": false,
                "name": "Headtaps",
                "isrc": "USQX92200965",
                "hasLyrics": true,
                "albumName": "7220",
                "playParams": {
                  "id": "1611056017",
                  "kind": "song"
                },
                "trackNumber": 2,
                "composerName": "Durk Banks, Trenton Turner & David Morse",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1582024384",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1582024384",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview125/v4/9b/1b/28/9b1b2845-0daa-e1a6-1f19-e4efd7536428/mzaf_5651024574799424106.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/8b/4d/54/8b4d545d-feee-c91c-992c-cecd16677f6e/093624879381.jpg/{w}x{h}bb.jpg",
                  "bgColor": "9da5a7",
                  "textColor1": "000e09",
                  "textColor2": "2c1e13",
                  "textColor3": "202c28",
                  "textColor4": "423931"
                },
                "artistName": "Cody Johnson",
                "url": "https://music.apple.com/us/album/til-you-cant/1582024378?i=1582024384",
                "discNumber": 1,
                "genreNames": [
                  "Country",
                  "Music"
                ],
                "durationInMillis": 224213,
                "releaseDate": "2021-06-11",
                "isAppleDigitalMaster": true,
                "name": "'Til You Can't",
                "isrc": "QMCQK1900137",
                "hasLyrics": true,
                "albumName": "Human: The Double Album",
                "playParams": {
                  "id": "1582024384",
                  "kind": "song"
                },
                "trackNumber": 4,
                "composerName": "Ben Stennis & Matt Rogers"
              }
            },
            {
              "id": "1617171907",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617171907",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/ef/79/20/ef792082-40c3-d6e7-958d-ee32a2adc605/mzaf_14896052997739904723.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 2000,
                  "height": 2000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/4d/54/ec/4d54eccd-8e71-4217-cb81-445adc77136b/075679750006.jpg/{w}x{h}bb.jpg",
                  "bgColor": "000000",
                  "textColor1": "fafeff",
                  "textColor2": "dddce3",
                  "textColor3": "c7cbcb",
                  "textColor4": "b0b0b5"
                },
                "artistName": "YoungBoy Never Broke Again",
                "url": "https://music.apple.com/us/album/i-got-the-bag/1617170958?i=1617171907",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 138262,
                "releaseDate": "2022-04-01",
                "isAppleDigitalMaster": false,
                "name": "I Got The Bag",
                "isrc": "USAT22203016",
                "hasLyrics": true,
                "albumName": "The Last Slimeto",
                "playParams": {
                  "id": "1617171907",
                  "kind": "song"
                },
                "trackNumber": 28,
                "composerName": "Daniel Lebrun, Jason Goldberg, Kentrell Gaulden & Thomas Mkrtchyan",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1576552565",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1576552565",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview125/v4/63/c5/9a/63c59a18-6610-173c-5a78-65a06fb251cc/mzaf_9849876950553161459.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/79/d7/66/79d7669f-36ff-46fb-16cb-b86fd321ef25/886449403912.jpg/{w}x{h}bb.jpg",
                  "bgColor": "e2e2fa",
                  "textColor1": "030a0d",
                  "textColor2": "2a1616",
                  "textColor3": "2f353d",
                  "textColor4": "4f3e43"
                },
                "artistName": "Lil Nas X & Jack Harlow",
                "url": "https://music.apple.com/us/album/industry-baby/1576552540?i=1576552565",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music",
                  "Pop"
                ],
                "durationInMillis": 212000,
                "releaseDate": "2021-07-23",
                "isAppleDigitalMaster": false,
                "name": "INDUSTRY BABY",
                "isrc": "USSM12104539",
                "hasLyrics": true,
                "albumName": "INDUSTRY BABY - Single",
                "playParams": {
                  "id": "1576552565",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Jack Harlow, Montero Hill, Kanye West, Denzel Baptiste, Nick Lee & David Biral",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1606715703",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1606715703",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/1b/16/54/1b1654ad-4b14-2d84-e9d0-a80c03ee1301/mzaf_10334518247162914165.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 1425,
                  "height": 1425,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/20/57/aa/2057aa6a-6a71-f9da-2cc3-106377a9e2b7/075679758903.jpg/{w}x{h}bb.jpg",
                  "bgColor": "161d29",
                  "textColor1": "e0eae6",
                  "textColor2": "c0c7cd",
                  "textColor3": "b7c1c0",
                  "textColor4": "9ea5ac"
                },
                "artistName": "Gucci Mane",
                "url": "https://music.apple.com/us/album/rumors-feat-lil-durk/1606715689?i=1606715703",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 185856,
                "releaseDate": "2022-01-25",
                "isAppleDigitalMaster": true,
                "name": "Rumors (feat. Lil Durk)",
                "isrc": "USAT22200226",
                "hasLyrics": true,
                "albumName": "Rumors (feat. Lil Durk) - Single",
                "playParams": {
                  "id": "1606715703",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Brytavious Lakeith Chambers, Demetrius Moore, Durk Banks, Meech & Radric Davis",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1542103620",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1542103620",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/9c/2b/40/9c2b40da-0554-23d2-3c2f-e3daddebadcf/mzaf_2322621263265654526.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/64/70/1c/64701cff-71ed-912f-ce62-71d409f5e6ad/195497640560.jpg/{w}x{h}bb.jpg",
                  "bgColor": "1a182e",
                  "textColor1": "ffeded",
                  "textColor2": "f26240",
                  "textColor3": "d1c2c6",
                  "textColor4": "c7533c"
                },
                "artistName": "Bad Bunny & Jhay Cortez",
                "url": "https://music.apple.com/us/album/d%C3%A1kiti/1542102907?i=1542103620",
                "discNumber": 1,
                "genreNames": [
                  "Urbano latino",
                  "Music",
                  "Latin"
                ],
                "durationInMillis": 205090,
                "releaseDate": "2020-10-30",
                "isAppleDigitalMaster": false,
                "name": "DÁKITI",
                "isrc": "QMFME2004132",
                "hasLyrics": true,
                "albumName": "EL ÚLTIMO TOUR DEL MUNDO",
                "playParams": {
                  "id": "1542103620",
                  "kind": "song"
                },
                "trackNumber": 11,
                "composerName": "Benito A. Martinez Ocasio & Gabriel Mora",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1584281482",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1584281482",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/e6/d1/bc/e6d1bc6b-7fc5-febc-6867-cfe277c0c713/mzaf_10267840951443724018.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/11/36/38/1136384a-eebc-697a-c005-d890e41c0854/21UM1IM07518.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "ffffff",
                  "textColor1": "070707",
                  "textColor2": "1a1631",
                  "textColor3": "383838",
                  "textColor4": "47455a"
                },
                "artistName": "Drake",
                "url": "https://music.apple.com/us/album/girls-want-girls-feat-lil-baby/1584281467?i=1584281482",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 221980,
                "releaseDate": "2021-09-03",
                "isAppleDigitalMaster": true,
                "name": "Girls Want Girls (feat. Lil Baby)",
                "isrc": "USUG12104399",
                "hasLyrics": true,
                "albumName": "Certified Lover Boy",
                "playParams": {
                  "id": "1584281482",
                  "kind": "song"
                },
                "trackNumber": 3,
                "composerName": "Aubrey Drake Graham, D. Jones, O. Yildirim & Mathias Liyew",
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
              "id": "1611056228",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611056228",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/1e/f9/c1/1ef9c1c6-c47e-2a0a-d440-f1c12ad200b4/mzaf_6294324421361901499.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/federal-nightmares/1611055823?i=1611056228",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 151340,
                "releaseDate": "2022-03-11",
                "isAppleDigitalMaster": false,
                "name": "Federal Nightmares",
                "isrc": "USQX92200961",
                "hasLyrics": true,
                "albumName": "7220",
                "playParams": {
                  "id": "1611056228",
                  "kind": "song"
                },
                "trackNumber": 14,
                "composerName": "Durk Banks, Trenton Turner, Tahj Vaughn & Braylen Rembert",
                "contentRating": "explicit"
              }
            },
            {
              "id": "661233781",
              "type": "songs",
              "href": "/v1/catalog/us/songs/661233781",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/9b/ea/54/9bea54a3-5e6d-184a-a005-07824ff4f146/mzaf_17676248724426858768.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 1425,
                  "height": 1425,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music2/v4/3c/c7/1b/3cc71b82-fd61-1418-a48b-087cde1ed8d9/075679951953.jpg/{w}x{h}bb.jpg",
                  "bgColor": "121212",
                  "textColor1": "eaeaea",
                  "textColor2": "cdcdcd",
                  "textColor3": "bfbfbf",
                  "textColor4": "a7a7a7"
                },
                "artistName": "Kevin Gates",
                "url": "https://music.apple.com/us/album/thinking-with-my-dick-feat-juicy-j/661233401?i=661233781",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music",
                  "Gangsta Rap",
                  "Rock",
                  "Rap",
                  "Dirty South",
                  "Hardcore Rap"
                ],
                "durationInMillis": 165315,
                "releaseDate": "2013-07-16",
                "isAppleDigitalMaster": false,
                "name": "Thinking With My Dick (feat. Juicy J)",
                "isrc": "USAT21301797",
                "hasLyrics": true,
                "albumName": "Stranger Than Fiction",
                "playParams": {
                  "id": "661233781",
                  "kind": "song"
                },
                "trackNumber": 8,
                "composerName": "Jeremy McArthur, Jordan Houston, Kevin Gates & Tevin Thompson",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1617332891",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617332891",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/15/c2/5b/15c25b2a-5dd9-1b31-845b-4e40f40ad43c/mzaf_11268420285666544072.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3600,
                  "height": 3600,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/6c/08/18/6c08184c-61f2-6777-88d4-c08580e09205/22UMGIM33673.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "565656",
                  "textColor1": "fcfcfc",
                  "textColor2": "f2f2f2",
                  "textColor3": "dbdbdb",
                  "textColor4": "d3d3d3"
                },
                "artistName": "42 Dugg & EST Gee",
                "url": "https://music.apple.com/us/album/spin/1617332701?i=1617332891",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 141457,
                "releaseDate": "2022-04-08",
                "isAppleDigitalMaster": true,
                "name": "Spin",
                "isrc": "USUM72202007",
                "hasLyrics": true,
                "albumName": "Last Ones Left",
                "playParams": {
                  "id": "1617332891",
                  "kind": "song"
                },
                "trackNumber": 4,
                "composerName": "Dion Hayes, George Stone III, Jeffrey Lynn Jones Jr, Aaron Butler & Oscar Braojos Garcia",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1611055835",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611055835",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/34/a5/58/34a5582b-edfc-1564-ff1a-184bd7d26658/mzaf_10782684702036674622.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/started-from/1611055823?i=1611055835",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 121060,
                "releaseDate": "2022-03-11",
                "isAppleDigitalMaster": false,
                "name": "Started From",
                "isrc": "USQX92200951",
                "hasLyrics": true,
                "albumName": "7220",
                "playParams": {
                  "id": "1611055835",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Durk Banks, Trenton Turner & Ethan Hayes",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1584281493",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1584281493",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/80/49/4d/80494d0e-d6e6-08aa-db68-c87a6b9a9af7/mzaf_9981093986552058080.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/11/36/38/1136384a-eebc-697a-c005-d890e41c0854/21UM1IM07518.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "ffffff",
                  "textColor1": "070707",
                  "textColor2": "1a1631",
                  "textColor3": "383838",
                  "textColor4": "47455a"
                },
                "artistName": "Drake",
                "url": "https://music.apple.com/us/album/fair-trade-feat-travis-scott/1584281467?i=1584281493",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 291175,
                "releaseDate": "2021-09-03",
                "isAppleDigitalMaster": true,
                "name": "Fair Trade (feat. Travis Scott)",
                "isrc": "USUG12104402",
                "hasLyrics": true,
                "albumName": "Certified Lover Boy",
                "playParams": {
                  "id": "1584281493",
                  "kind": "song"
                },
                "trackNumber": 6,
                "composerName": "Aubrey Drake Graham, J. Webster II, O. Yildirim, J Sweet, E. Oshunrinde, R.S. Antoine, C. Day Wilson, K. Edmonds, T. Halm, V. Wade, E. Dernst II, B Banks, M. Gordon, K. Mosovich & M. Reddick",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1610618872",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1610618872",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/b2/57/0b/b2570b78-b469-d34f-fc30-586d3968475b/mzaf_16127562533043897928.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 1425,
                  "height": 1425,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/07/c3/aa/07c3aa6f-33fd-92c3-dd03-1e8ff6ba9bbc/075679756992.jpg/{w}x{h}bb.jpg",
                  "bgColor": "984628",
                  "textColor1": "f1f0eb",
                  "textColor2": "e8dbd9",
                  "textColor3": "dfcec4",
                  "textColor4": "d8bdb5"
                },
                "artistName": "GAYLE",
                "url": "https://music.apple.com/us/album/abcdefu/1610618866?i=1610618872",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 168552,
                "releaseDate": "2021-08-13",
                "isAppleDigitalMaster": true,
                "name": "abcdefu",
                "isrc": "USAT22103652",
                "hasLyrics": true,
                "albumName": "a study of the human experience volume one - EP",
                "playParams": {
                  "id": "1610618872",
                  "kind": "song"
                },
                "trackNumber": 2,
                "composerName": "David Pittenger, GAYLE & Sara Davis",
                "contentRating": "explicit"
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
              "id": "1617171584",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617171584",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/63/9e/c2/639ec2cd-6349-0d45-07a8-224cde19942e/mzaf_12676035163869961511.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 2000,
                  "height": 2000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/4d/54/ec/4d54eccd-8e71-4217-cb81-445adc77136b/075679750006.jpg/{w}x{h}bb.jpg",
                  "bgColor": "000000",
                  "textColor1": "fafeff",
                  "textColor2": "dddce3",
                  "textColor3": "c7cbcb",
                  "textColor4": "b0b0b5"
                },
                "artistName": "YoungBoy Never Broke Again",
                "url": "https://music.apple.com/us/album/acclaimed-emotions/1617170958?i=1617171584",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 180454,
                "releaseDate": "2022-04-01",
                "isAppleDigitalMaster": false,
                "name": "Acclaimed Emotions",
                "isrc": "USAT22203145",
                "hasLyrics": true,
                "albumName": "The Last Slimeto",
                "playParams": {
                  "id": "1617171584",
                  "kind": "song"
                },
                "trackNumber": 23,
                "composerName": "Daniel Lebrun, Gineau Johan, Jason Goldberg, Kentrell Gaulden, Lukas Payne & Sterling Reynolds",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1608990811",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1608990811",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/73/b7/c7/73b7c751-2ed8-9934-365f-321e36943086/mzaf_10063189383910135911.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/8e/f3/aa/8ef3aa07-081c-edec-c037-c9a20da4d3e5/dj.cbtqyobo.jpg/{w}x{h}bb.jpg",
                  "bgColor": "2a0a1b",
                  "textColor1": "d2bf9b",
                  "textColor2": "de7576",
                  "textColor3": "b09b81",
                  "textColor4": "ba5f64"
                },
                "artistName": "ERNEST",
                "url": "https://music.apple.com/us/album/flower-shops-feat-morgan-wallen/1608990805?i=1608990811",
                "discNumber": 1,
                "genreNames": [
                  "Country",
                  "Music"
                ],
                "durationInMillis": 214406,
                "releaseDate": "2021-12-31",
                "isAppleDigitalMaster": false,
                "name": "Flower Shops (feat. Morgan Wallen)",
                "isrc": "QZ22S2100091",
                "hasLyrics": true,
                "albumName": "FLOWER SHOPS (THE ALBUM)",
                "playParams": {
                  "id": "1608990811",
                  "kind": "song"
                },
                "trackNumber": 6,
                "composerName": "Ernest Keith Smith, Ben Burgess & Mark Holman"
              }
            },
            {
              "id": "1540314624",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1540314624",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/0b/7d/42/0b7d4235-347a-0a94-6460-86349e71c4d5/mzaf_4153755297687545971.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/10/a2/39/10a239bc-0f25-69d2-52df-b1fe755dcf19/20UM1IM03632.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "15272e",
                  "textColor1": "f3e3dc",
                  "textColor2": "bdc5bf",
                  "textColor3": "c7beb9",
                  "textColor4": "9ba5a2"
                },
                "artistName": "Morgan Wallen",
                "url": "https://music.apple.com/us/album/wasted-on-you/1540314609?i=1540314624",
                "discNumber": 1,
                "genreNames": [
                  "Country",
                  "Music"
                ],
                "durationInMillis": 178520,
                "releaseDate": "2021-01-08",
                "isAppleDigitalMaster": true,
                "name": "Wasted On You",
                "isrc": "USUG12004194",
                "hasLyrics": true,
                "albumName": "Dangerous: The Double Album",
                "playParams": {
                  "id": "1540314624",
                  "kind": "song"
                },
                "trackNumber": 2,
                "composerName": "Morgan Wallen, Ernest Keith Smith, Josh Thompson & Ryan Vojtesak"
              }
            },
            {
              "id": "1571169194",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1571169194",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview125/v4/f5/66/33/f5663339-03a9-5970-1ef5-b40a46d8d9de/mzaf_14919954981643236207.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/need-to-know/1571168930?i=1571169194",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music"
                ],
                "durationInMillis": 210560,
                "releaseDate": "2021-06-11",
                "isAppleDigitalMaster": true,
                "name": "Need To Know",
                "isrc": "USRC12101120",
                "hasLyrics": true,
                "albumName": "Planet Her",
                "playParams": {
                  "id": "1571169194",
                  "kind": "song"
                },
                "trackNumber": 5,
                "composerName": "Amala Zandile Dlamini & Lukasz Gottwald",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1590036021",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1590036021",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/75/28/56/75285676-dbce-d91d-7b36-070084a3546b/mzaf_5286200244455841527.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/73/6d/7c/736d7cfb-c79d-c9a9-4170-5e71d008dea1/886449666430.jpg/{w}x{h}bb.jpg",
                  "bgColor": "2d4b53",
                  "textColor1": "eaebe2",
                  "textColor2": "dfd1b4",
                  "textColor3": "c4cbc5",
                  "textColor4": "bcb6a1"
                },
                "artistName": "Adele",
                "url": "https://music.apple.com/us/album/easy-on-me/1590035691?i=1590036021",
                "discNumber": 1,
                "genreNames": [
                  "Pop",
                  "Music",
                  "Vocal",
                  "Vocal Pop"
                ],
                "durationInMillis": 224695,
                "releaseDate": "2021-10-14",
                "isAppleDigitalMaster": false,
                "name": "Easy On Me",
                "isrc": "USSM12105970",
                "hasLyrics": true,
                "albumName": "30",
                "playParams": {
                  "id": "1590036021",
                  "kind": "song"
                },
                "trackNumber": 2,
                "composerName": "Adele Adkins & Greg Kurstin"
              }
            },
            {
              "id": "1604945223",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1604945223",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/b7/5b/01/b75b019c-66b9-091b-6403-02e2dd8d4c58/mzaf_2822453882986831618.plus.aac.p.m4a"
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
                "artistName": "Gunna",
                "url": "https://music.apple.com/us/album/25k-jacket-feat-lil-baby/1604944424?i=1604945223",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 120000,
                "releaseDate": "2022-01-07",
                "isAppleDigitalMaster": true,
                "name": "25k jacket (feat. Lil Baby)",
                "isrc": "QMCE32200048",
                "hasLyrics": true,
                "albumName": "DRIP SEASON 4EVER",
                "playParams": {
                  "id": "1604945223",
                  "kind": "song"
                },
                "trackNumber": 12,
                "composerName": "Nik Dean, Sergio Kitchens & Wesley Glass",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1470146813",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1470146813",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/1c/cc/17/1ccc1766-c057-3192-c6f4-0bc556d20a78/mzaf_17540950830075325311.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/e1/2a/37/e12a370c-d8a1-ce39-367b-cd64ca234724/19UMGIM55524.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "020205",
                  "textColor1": "e8f5f3",
                  "textColor2": "03caeb",
                  "textColor3": "bac5c3",
                  "textColor4": "03a2bd"
                },
                "artistName": "J Balvin & Bad Bunny",
                "url": "https://music.apple.com/us/album/la-canci%C3%B3n/1470146332?i=1470146813",
                "discNumber": 1,
                "genreNames": [
                  "Urbano latino",
                  "Music",
                  "Latin"
                ],
                "durationInMillis": 242573,
                "releaseDate": "2019-08-02",
                "isAppleDigitalMaster": true,
                "name": "LA CANCIÓN",
                "isrc": "USUM71911618",
                "hasLyrics": true,
                "albumName": "OASIS",
                "playParams": {
                  "id": "1470146813",
                  "kind": "song"
                },
                "trackNumber": 5,
                "composerName": "J Balvin, Bad Bunny, José Nicael Arroyo, Gilbert Rodriguez Marte & Alejandro Ramirez"
              }
            },
            {
              "id": "1617162041",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617162041",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/0c/96/ab/0c96ab9b-b5e7-4b97-89ae-ee6ae280abfe/mzaf_15098416412364487168.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/66/a0/fd/66a0fdf7-8b80-06cb-06d1-84b2ccee2765/196589062345.jpg/{w}x{h}bb.jpg",
                  "bgColor": "050409",
                  "textColor1": "dbdcd6",
                  "textColor2": "c5c5c2",
                  "textColor3": "b0b1ad",
                  "textColor4": "9e9e9d"
                },
                "artistName": "Fivio Foreign",
                "url": "https://music.apple.com/us/album/world-watching-feat-lil-tjay-yung-bleu/1617161806?i=1617162041",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 211064,
                "releaseDate": "2022-04-08",
                "isAppleDigitalMaster": true,
                "name": "World Watching (feat. Lil Tjay & Yung Bleu)",
                "isrc": "USSM12203055",
                "hasLyrics": true,
                "albumName": "B.I.B.L.E.",
                "playParams": {
                  "id": "1617162041",
                  "kind": "song"
                },
                "trackNumber": 11,
                "composerName": "Fivio Foreign, Lil Tjay, Jeremy Biddle, Jonathan Perry, Richard Stannard, Ellie Goulding & Ash Howes",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1521889285",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1521889285",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/76/9a/2d/769a2d58-21c3-122e-3000-8c33f3f56763/mzaf_16254970509770785442.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/1c/ed/39/1ced39e0-c34d-52b0-021c-ff967f21f5bf/20UMGIM55833.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "000000",
                  "textColor1": "ffffff",
                  "textColor2": "dddddd",
                  "textColor3": "cbcbcb",
                  "textColor4": "b0b0b0"
                },
                "artistName": "Pop Smoke",
                "url": "https://music.apple.com/us/album/for-the-night-feat-lil-baby-dababy/1521889004?i=1521889285",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 190476,
                "releaseDate": "2020-07-03",
                "isAppleDigitalMaster": true,
                "name": "For The Night (feat. Lil Baby & DaBaby)",
                "isrc": "USUM72013355",
                "hasLyrics": true,
                "albumName": "Shoot For The Stars Aim For The Moon",
                "playParams": {
                  "id": "1521889285",
                  "kind": "song"
                },
                "trackNumber": 3,
                "composerName": "Bashar Jackson, Alex Petit, Christoffer Buchardt Marcussen, Cédric Leutwyler, Dominique Jones & Jonathan Kirk",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1617171598",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617171598",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/29/d6/d5/29d6d53b-31c1-0623-f158-311312afd893/mzaf_11934021057930256648.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 2000,
                  "height": 2000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/4d/54/ec/4d54eccd-8e71-4217-cb81-445adc77136b/075679750006.jpg/{w}x{h}bb.jpg",
                  "bgColor": "000000",
                  "textColor1": "fafeff",
                  "textColor2": "dddce3",
                  "textColor3": "c7cbcb",
                  "textColor4": "b0b0b5"
                },
                "artistName": "YoungBoy Never Broke Again",
                "url": "https://music.apple.com/us/album/holy/1617170958?i=1617171598",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 117551,
                "releaseDate": "2022-04-01",
                "isAppleDigitalMaster": false,
                "name": "Holy",
                "isrc": "USAT22203015",
                "hasLyrics": true,
                "albumName": "The Last Slimeto",
                "playParams": {
                  "id": "1617171598",
                  "kind": "song"
                },
                "trackNumber": 27,
                "composerName": "Aaron Gilfenbain, Jason Goldberg, Jonathan gabor, Kentrell Gaulden & Nicolas Simon Schmidt",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1588439297",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1588439297",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/4d/71/70/4d71700d-3abd-88d3-0f49-1881abae24d5/mzaf_2423531812414431149.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/e6/5c/29/e65c2965-93f6-cbed-febe-4cb6c8479bad/886449255443.jpg/{w}x{h}bb.jpg",
                  "bgColor": "08080a",
                  "textColor1": "c8cecc",
                  "textColor2": "b6c4c2",
                  "textColor3": "a2a6a5",
                  "textColor4": "939e9d"
                },
                "artistName": "Nardo Wick",
                "url": "https://music.apple.com/us/album/who-want-smoke-feat-g-herbo-lil-durk-21-savage/1588439290?i=1588439297",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 279853,
                "releaseDate": "2021-10-08",
                "isAppleDigitalMaster": false,
                "name": "Who Want Smoke?? (feat. G Herbo, Lil Durk & 21 Savage)",
                "isrc": "USRC12101071",
                "hasLyrics": true,
                "albumName": "Who Want Smoke?? (feat. G Herbo, Lil Durk & 21 Savage) - Single",
                "playParams": {
                  "id": "1588439297",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Horace Walls, She'yaa Bin Abraham-Joseph, Mark Läpple Onokey, Durk Banks, Dominique' Jones & Carlos Pfersdorf",
                "contentRating": "explicit"
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
              "id": "1617332890",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617332890",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/78/3a/cd/783acd9c-fbce-4c4c-4505-34def0dc2589/mzaf_17504572091771348921.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3600,
                  "height": 3600,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/6c/08/18/6c08184c-61f2-6777-88d4-c08580e09205/22UMGIM33673.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "565656",
                  "textColor1": "fcfcfc",
                  "textColor2": "f2f2f2",
                  "textColor3": "dbdbdb",
                  "textColor4": "d3d3d3"
                },
                "artistName": "42 Dugg & EST Gee",
                "url": "https://music.apple.com/us/album/i-never-judged-you/1617332701?i=1617332890",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 114390,
                "releaseDate": "2022-04-08",
                "isAppleDigitalMaster": true,
                "name": "I Never Judged You",
                "isrc": "USUM72202003",
                "hasLyrics": true,
                "albumName": "Last Ones Left",
                "playParams": {
                  "id": "1617332890",
                  "kind": "song"
                },
                "trackNumber": 3,
                "composerName": "Dion Hayes, George Stone III, Jeffrey Lynn Jones Jr & Pepijn Baltus",
                "contentRating": "explicit"
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
              "id": "1583678164",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1583678164",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview125/v4/52/5c/8e/525c8eb4-4372-6e72-63ca-827fec3ad52e/mzaf_5901309229950545535.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/21/9a/b2/219ab295-469c-f0f9-1369-60c9af11c6f2/21008.jpg/{w}x{h}bb.jpg",
                  "bgColor": "121210",
                  "textColor1": "d5d6d9",
                  "textColor2": "d4c1bd",
                  "textColor3": "aeafb0",
                  "textColor4": "ad9e9a"
                },
                "artistName": "Yeat",
                "url": "https://music.apple.com/us/album/mon%C3%ABy-so-big/1583678146?i=1583678164",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 160052,
                "releaseDate": "2021-09-10",
                "isAppleDigitalMaster": false,
                "name": "Monëy so big",
                "isrc": "USLD91734275",
                "hasLyrics": true,
                "albumName": "Up 2 Më",
                "playParams": {
                  "id": "1583678164",
                  "kind": "song"
                },
                "trackNumber": 18,
                "contentRating": "explicit"
              }
            },
            {
              "id": "1440111980",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1440111980",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/d6/08/bc/d608bcf3-d23d-1efe-7da5-6f786d93c1b1/mzaf_18392403041853942040.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/ac/f5/19/acf51942-e001-2d6e-e0e6-49b3fd09cac4/842812106569_01_img001.jpg/{w}x{h}bb.jpg",
                  "bgColor": "2f2e2a",
                  "textColor1": "e0dad5",
                  "textColor2": "d5cbc1",
                  "textColor3": "bcb7b3",
                  "textColor4": "b3aca3"
                },
                "artistName": "Morgan Wallen",
                "url": "https://music.apple.com/us/album/whiskey-glasses/1440111976?i=1440111980",
                "discNumber": 1,
                "genreNames": [
                  "Country",
                  "Music"
                ],
                "durationInMillis": 234347,
                "releaseDate": "2016-01-01",
                "isAppleDigitalMaster": false,
                "name": "Whiskey Glasses",
                "isrc": "QZ22S1500059",
                "hasLyrics": true,
                "albumName": "If I Know Me",
                "playParams": {
                  "id": "1440111980",
                  "kind": "song"
                },
                "trackNumber": 4,
                "composerName": "Ben Burgess & Kevin Kadish"
              }
            },
            {
              "id": "1617332892",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617332892",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/f9/ff/af/f9ffaff9-759c-a285-20d1-f1e4b7f9ce8d/mzaf_16443043866378236012.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3600,
                  "height": 3600,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/6c/08/18/6c08184c-61f2-6777-88d4-c08580e09205/22UMGIM33673.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "565656",
                  "textColor1": "fcfcfc",
                  "textColor2": "f2f2f2",
                  "textColor3": "dbdbdb",
                  "textColor4": "d3d3d3"
                },
                "artistName": "42 Dugg & EST Gee",
                "url": "https://music.apple.com/us/album/skcretch-sum/1617332701?i=1617332892",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 145395,
                "releaseDate": "2022-04-08",
                "isAppleDigitalMaster": true,
                "name": "Skcretch Sum",
                "isrc": "USUM72202008",
                "hasLyrics": true,
                "albumName": "Last Ones Left",
                "playParams": {
                  "id": "1617332892",
                  "kind": "song"
                },
                "trackNumber": 5,
                "composerName": "Dion Hayes, George Stone III, Jeffrey Lynn Jones Jr & David Morse",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1570323056",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1570323056",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/2f/93/9d/2f939dab-2435-212a-997d-a03fb93ed4ba/mzaf_16349653155058740859.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/b6/12/da/b612daba-6c68-c2ab-7492-fb2e079074d5/196006829308.jpg/{w}x{h}bb.jpg",
                  "bgColor": "e3d9d7",
                  "textColor1": "070b0b",
                  "textColor2": "0b100e",
                  "textColor3": "333434",
                  "textColor4": "363836"
                },
                "artistName": "Bad Bunny",
                "url": "https://music.apple.com/us/album/yonaguni/1570323047?i=1570323056",
                "discNumber": 1,
                "genreNames": [
                  "Urbano latino",
                  "Music",
                  "Latin"
                ],
                "durationInMillis": 206710,
                "releaseDate": "2021-06-03",
                "isAppleDigitalMaster": false,
                "name": "Yonaguni",
                "isrc": "QM6P42169803",
                "hasLyrics": true,
                "albumName": "Yonaguni - Single",
                "playParams": {
                  "id": "1570323056",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Benito A. Martinez",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1617161812",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617161812",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/ab/e0/11/abe011be-460f-e7cc-66a9-da3284dcc27e/mzaf_4775011961024438750.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/66/a0/fd/66a0fdf7-8b80-06cb-06d1-84b2ccee2765/196589062345.jpg/{w}x{h}bb.jpg",
                  "bgColor": "050409",
                  "textColor1": "dbdcd6",
                  "textColor2": "c5c5c2",
                  "textColor3": "b0b1ad",
                  "textColor4": "9e9e9d"
                },
                "artistName": "Fivio Foreign",
                "url": "https://music.apple.com/us/album/through-the-fire-feat-quavo/1617161806?i=1617161812",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 205288,
                "releaseDate": "2022-04-08",
                "isAppleDigitalMaster": true,
                "name": "Through the Fire (feat. Quavo)",
                "isrc": "USSM12203050",
                "hasLyrics": true,
                "albumName": "B.I.B.L.E.",
                "playParams": {
                  "id": "1617161812",
                  "kind": "song"
                },
                "trackNumber": 2,
                "composerName": "Fivio Foreign, Quavious Marshall, Cristian Dejesus Tejada, Bigram Zayas, Aswad Asif, Omari Clarke, Adrian Lau, Luis Campozano, Brendan Walsh, Joshua Scruggs & John Carlton White",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1617171578",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617171578",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/b9/31/44/b93144d4-785c-2bfa-1464-a2b2faff40c4/mzaf_2144528317460028960.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 2000,
                  "height": 2000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/4d/54/ec/4d54eccd-8e71-4217-cb81-445adc77136b/075679750006.jpg/{w}x{h}bb.jpg",
                  "bgColor": "000000",
                  "textColor1": "fafeff",
                  "textColor2": "dddce3",
                  "textColor3": "c7cbcb",
                  "textColor4": "b0b0b5"
                },
                "artistName": "YoungBoy Never Broke Again",
                "url": "https://music.apple.com/us/album/the-north-bleeding/1617170958?i=1617171578",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 207241,
                "releaseDate": "2022-04-01",
                "isAppleDigitalMaster": false,
                "name": "The North Bleeding",
                "isrc": "USAT22203144",
                "hasLyrics": true,
                "albumName": "The Last Slimeto",
                "playParams": {
                  "id": "1617171578",
                  "kind": "song"
                },
                "trackNumber": 21,
                "composerName": "Jason Goldberg, Kentrell Gaulden, Leonardo Mateus & Malik",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1564531202",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1564531202",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/d6/6f/58/d66f58c4-50ad-4978-971c-b19c022a440b/mzaf_3392528453380582564.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/2d/f3/c9/2df3c9fd-e0eb-257c-c035-b04f05a66580/21UMGIM36691.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "6d4d3a",
                  "textColor1": "fcfbf9",
                  "textColor2": "ead3b5",
                  "textColor3": "e0d8d3",
                  "textColor4": "d1b89c"
                },
                "artistName": "Billie Eilish",
                "url": "https://music.apple.com/us/album/happier-than-ever/1564530719?i=1564531202",
                "discNumber": 1,
                "genreNames": [
                  "Alternative",
                  "Music"
                ],
                "durationInMillis": 298899,
                "releaseDate": "2021-07-30",
                "isAppleDigitalMaster": true,
                "name": "Happier Than Ever",
                "isrc": "USUM72105936",
                "hasLyrics": true,
                "albumName": "Happier Than Ever",
                "playParams": {
                  "id": "1564531202",
                  "kind": "song"
                },
                "trackNumber": 15,
                "composerName": "Billie Eilish & FINNEAS",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1511793607",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1511793607",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/92/b2/a4/92b2a474-86b8-8e03-e474-1081e8543211/mzaf_11808379545918554724.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/a6/89/c8/a689c864-9a82-0c8f-e37a-21ead3a29ac6/886448463481.jpg/{w}x{h}bb.jpg",
                  "bgColor": "101010",
                  "textColor1": "fbfbfb",
                  "textColor2": "cecece",
                  "textColor3": "cccccc",
                  "textColor4": "a8a8a8"
                },
                "artistName": "Polo G",
                "url": "https://music.apple.com/us/album/martin-gina/1511793475?i=1511793607",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 132833,
                "releaseDate": "2020-05-15",
                "isAppleDigitalMaster": false,
                "name": "Martin & Gina",
                "isrc": "USQX92002595",
                "hasLyrics": true,
                "albumName": "THE GOAT",
                "playParams": {
                  "id": "1511793607",
                  "kind": "song"
                },
                "trackNumber": 3,
                "composerName": "Taurus Bartlett, Tahj Vaughn, Kyre Trask & Hagan Lange",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1617332897",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617332897",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview112/v4/12/ea/f5/12eaf5ff-b4c7-f22f-da03-30983a8e01cd/mzaf_16368579352944571970.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3600,
                  "height": 3600,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/6c/08/18/6c08184c-61f2-6777-88d4-c08580e09205/22UMGIM33673.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "565656",
                  "textColor1": "fcfcfc",
                  "textColor2": "f2f2f2",
                  "textColor3": "dbdbdb",
                  "textColor4": "d3d3d3"
                },
                "artistName": "42 Dugg & EST Gee",
                "url": "https://music.apple.com/us/album/free-the-shiners/1617332701?i=1617332897",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 125017,
                "releaseDate": "2022-03-22",
                "isAppleDigitalMaster": true,
                "name": "Free The Shiners",
                "isrc": "USUM72202000",
                "hasLyrics": true,
                "albumName": "Last Ones Left",
                "playParams": {
                  "id": "1617332897",
                  "kind": "song"
                },
                "trackNumber": 6,
                "composerName": "Ceary Veon, Dion Hayes, George Stone III & Khaya Gilika",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1614549001",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1614549001",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/69/d4/8f/69d48f4e-f799-39d0-38ce-544f208640e8/mzaf_13397897337525034641.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/52/79/95/5279954e-eb45-478e-7749-4deb0e5fc3ca/21UMGIM86227.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "e9e9e7",
                  "textColor1": "000000",
                  "textColor2": "2e2e27",
                  "textColor3": "2f2f2e",
                  "textColor4": "53544d"
                },
                "artistName": "Pusha T",
                "url": "https://music.apple.com/us/album/neck-wrist-feat-jay-z-pharrell-williams/1614548999?i=1614549001",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 209315,
                "releaseDate": "2022-04-06",
                "isAppleDigitalMaster": true,
                "name": "Neck & Wrist (feat. JAY-Z & Pharrell Williams)",
                "isrc": "USUM72121118",
                "hasLyrics": true,
                "albumName": "Neck & Wrist (feat. JAY-Z & Pharrell Williams) - Single",
                "playParams": {
                  "id": "1614549001",
                  "kind": "song"
                },
                "trackNumber": 1,
                "composerName": "Terrence Thornton, Pharrell Williams & Shawn Carter",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1585883847",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1585883847",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/1e/39/c3/1e39c343-bf01-59ae-0b14-7ce268ba999f/mzaf_11262237549309107690.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 1425,
                  "height": 1425,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/3a/4d/ee/3a4deeb4-9555-4bef-3836-185a913b0b20/075679769602.jpg/{w}x{h}bb.jpg",
                  "bgColor": "99dffe",
                  "textColor1": "000000",
                  "textColor2": "0c342a",
                  "textColor3": "1e2c32",
                  "textColor4": "285654"
                },
                "artistName": "Meek Mill",
                "url": "https://music.apple.com/us/album/sharing-locations-feat-lil-baby-lil-durk/1585883836?i=1585883847",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 161053,
                "releaseDate": "2021-08-27",
                "isAppleDigitalMaster": false,
                "name": "Sharing Locations (feat. Lil Baby & Lil Durk)",
                "isrc": "USAT22105014",
                "hasLyrics": true,
                "albumName": "Expensive Pain",
                "playParams": {
                  "id": "1585883847",
                  "kind": "song"
                },
                "trackNumber": 4,
                "composerName": "Alexander Papamitrou, Dominik Svoroboric, Dominique Jones, Durk Banks, Nii Tetteh, Nikolas Papamitrou & Robert Williams",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1440111985",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1440111985",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/74/a9/17/74a91705-b2a1-0153-2f69-ab666a8e7009/mzaf_3330231804450688681.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/ac/f5/19/acf51942-e001-2d6e-e0e6-49b3fd09cac4/842812106569_01_img001.jpg/{w}x{h}bb.jpg",
                  "bgColor": "2f2e2a",
                  "textColor1": "e0dad5",
                  "textColor2": "d5cbc1",
                  "textColor3": "bcb7b3",
                  "textColor4": "b3aca3"
                },
                "artistName": "Morgan Wallen",
                "url": "https://music.apple.com/us/album/chasin-you/1440111976?i=1440111985",
                "discNumber": 1,
                "genreNames": [
                  "Country",
                  "Music"
                ],
                "durationInMillis": 205453,
                "releaseDate": "2018-04-27",
                "isAppleDigitalMaster": false,
                "name": "Chasin' You",
                "isrc": "QZ22S1800006",
                "hasLyrics": true,
                "albumName": "If I Know Me",
                "playParams": {
                  "id": "1440111985",
                  "kind": "song"
                },
                "trackNumber": 9,
                "composerName": "Morgan Wallen, Jamie Moore & Craig Wiseman"
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
              "id": "1617171576",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617171576",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/f0/11/f3/f011f3bc-b026-e036-01a3-fb3fd2d8b815/mzaf_4253237894645848676.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 2000,
                  "height": 2000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/4d/54/ec/4d54eccd-8e71-4217-cb81-445adc77136b/075679750006.jpg/{w}x{h}bb.jpg",
                  "bgColor": "000000",
                  "textColor1": "fafeff",
                  "textColor2": "dddce3",
                  "textColor3": "c7cbcb",
                  "textColor4": "b0b0b5"
                },
                "artistName": "YoungBoy Never Broke Again",
                "url": "https://music.apple.com/us/album/4kt-baby/1617170958?i=1617171576",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 137143,
                "releaseDate": "2022-04-01",
                "isAppleDigitalMaster": false,
                "name": "4KT Baby",
                "isrc": "USAT22203143",
                "hasLyrics": true,
                "albumName": "The Last Slimeto",
                "playParams": {
                  "id": "1617171576",
                  "kind": "song"
                },
                "trackNumber": 20,
                "composerName": "BJondatrakk, Daniel Lebrun, duhvinci, Jason Goldberg, Kentrell Gaulden & Traevon Walker",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1440924420",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1440924420",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview125/v4/c3/ef/ed/c3efedf2-89d1-2c40-3496-6141dcf6063a/mzaf_23268240071252276.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/de/9f/34/de9f3425-74fc-dc5b-5288-63d4755650e8/00854078006309.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "343434",
                  "textColor1": "dae8cf",
                  "textColor2": "e3dbd2",
                  "textColor3": "b9c4b0",
                  "textColor4": "c0bab2"
                },
                "artistName": "WILLOW",
                "url": "https://music.apple.com/us/album/wait-a-minute/1440923499?i=1440924420",
                "discNumber": 1,
                "genreNames": [
                  "Alternative",
                  "Music"
                ],
                "durationInMillis": 196520,
                "releaseDate": "2015-12-11",
                "isAppleDigitalMaster": true,
                "name": "Wait a Minute!",
                "isrc": "QMJMT1500801",
                "hasLyrics": true,
                "albumName": "ARDIPITHECUS",
                "playParams": {
                  "id": "1440924420",
                  "kind": "song"
                },
                "trackNumber": 13,
                "composerName": "Willow Smith & James Chul Rim"
              }
            },
            {
              "id": "1437955726",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1437955726",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/08/9d/b1/089db15c-8bd3-e9e2-3a6e-c2bfe7ae9266/mzaf_10659803182361164407.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/e9/08/8f/e9088fcd-f2b2-cf94-03ff-927977219869/00602577108037.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "1f1f1f",
                  "textColor1": "ededed",
                  "textColor2": "d4d4d4",
                  "textColor3": "c4c4c4",
                  "textColor4": "b0b0b0"
                },
                "artistName": "Lil Baby & Gunna",
                "url": "https://music.apple.com/us/album/drip-too-hard/1437955279?i=1437955726",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 145543,
                "releaseDate": "2018-09-12",
                "isAppleDigitalMaster": true,
                "name": "Drip Too Hard",
                "isrc": "USUG11801811",
                "hasLyrics": true,
                "albumName": "Drip Harder",
                "playParams": {
                  "id": "1437955726",
                  "kind": "song"
                },
                "trackNumber": 12,
                "composerName": "Dominique Jones, Sergio Kitchens & Chandler Durham",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1565443631",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1565443631",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/a1/60/20/a16020f3-cc18-7e56-2d8a-5209d492c07e/mzaf_16633133816764317393.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/5f/13/2b/5f132b68-1e45-36c3-452a-2a68ffb6aab5/886448654483.jpg/{w}x{h}bb.jpg",
                  "bgColor": "161304",
                  "textColor1": "9ad8fe",
                  "textColor2": "bbde4c",
                  "textColor3": "80b1cc",
                  "textColor4": "9ab53e"
                },
                "artistName": "DJ Khaled",
                "url": "https://music.apple.com/us/album/every-chance-i-get-feat-lil-baby-lil-durk/1565443380?i=1565443631",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 236524,
                "releaseDate": "2021-04-30",
                "isAppleDigitalMaster": false,
                "name": "EVERY CHANCE I GET (feat. Lil Baby & Lil Durk)",
                "isrc": "USSM12102263",
                "hasLyrics": true,
                "albumName": "KHALED KHALED",
                "playParams": {
                  "id": "1565443631",
                  "kind": "song"
                },
                "trackNumber": 2,
                "composerName": "DJ Khaled, Dominique' Jones, Durk Banks & Brytavious Chambers",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1611056232",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1611056232",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview126/v4/f8/02/5f/f8025f7f-51eb-d828-ce02-36e8cefad0f8/mzaf_16217240250989246727.plus.aac.p.m4a"
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
                "url": "https://music.apple.com/us/album/pissed-me-off/1611055823?i=1611056232",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 123077,
                "releaseDate": "2021-10-15",
                "isAppleDigitalMaster": false,
                "name": "Pissed Me Off",
                "isrc": "USQX92104791",
                "hasLyrics": true,
                "albumName": "7220",
                "playParams": {
                  "id": "1611056232",
                  "kind": "song"
                },
                "trackNumber": 16,
                "composerName": "Durk Banks & Matthew Fontanilla Manuel",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1617171590",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617171590",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/96/23/d0/9623d00f-3ae6-2c36-cd53-6e2f4183877d/mzaf_13757501383815381132.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 2000,
                  "height": 2000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/4d/54/ec/4d54eccd-8e71-4217-cb81-445adc77136b/075679750006.jpg/{w}x{h}bb.jpg",
                  "bgColor": "000000",
                  "textColor1": "fafeff",
                  "textColor2": "dddce3",
                  "textColor3": "c7cbcb",
                  "textColor4": "b0b0b5"
                },
                "artistName": "YoungBoy Never Broke Again",
                "url": "https://music.apple.com/us/album/ghost/1617170958?i=1617171590",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 135385,
                "releaseDate": "2022-04-01",
                "isAppleDigitalMaster": false,
                "name": "Ghost",
                "isrc": "USAT22203012",
                "hasLyrics": true,
                "albumName": "The Last Slimeto",
                "playParams": {
                  "id": "1617171590",
                  "kind": "song"
                },
                "trackNumber": 25,
                "composerName": "Aaron Hill, Daniel Lebrun, Jason Goldberg, Kentrell Gaulden & Michael Roberge",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1384782182",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1384782182",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview115/v4/c9/0a/0b/c90a0b22-6b07-536c-c3a0-70e281cf4b0e/mzaf_8255416011221709921.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/d6/fb/ab/d6fbabd0-1253-1340-aff9-9fe271deb6a5/00602567713999.rgb.jpg/{w}x{h}bb.jpg",
                  "bgColor": "e4e4e4",
                  "textColor1": "161616",
                  "textColor2": "282828",
                  "textColor3": "3f3f3f",
                  "textColor4": "4d4d4d"
                },
                "artistName": "Lil Baby & Drake",
                "url": "https://music.apple.com/us/album/yes-indeed/1384782173?i=1384782182",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 142273,
                "releaseDate": "2018-05-15",
                "isAppleDigitalMaster": true,
                "name": "Yes Indeed",
                "isrc": "USUM71806749",
                "hasLyrics": true,
                "albumName": "Harder Than Ever",
                "playParams": {
                  "id": "1384782182",
                  "kind": "song"
                },
                "trackNumber": 5,
                "composerName": "Dominique Jones, Aubrey Drake Graham & Wesley Glass",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1617161818",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1617161818",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview116/v4/ce/5a/c9/ce5ac906-d064-e8a1-eb52-521dbc56e54a/mzaf_5049423941112458155.plus.aac.p.m4a"
                  }
                ],
                "artwork": {
                  "width": 3000,
                  "height": 3000,
                  "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/66/a0/fd/66a0fdf7-8b80-06cb-06d1-84b2ccee2765/196589062345.jpg/{w}x{h}bb.jpg",
                  "bgColor": "050409",
                  "textColor1": "dbdcd6",
                  "textColor2": "c5c5c2",
                  "textColor3": "b0b1ad",
                  "textColor4": "9e9e9d"
                },
                "artistName": "Fivio Foreign",
                "url": "https://music.apple.com/us/album/for-nothin/1617161806?i=1617161818",
                "discNumber": 1,
                "genreNames": [
                  "Hip-Hop/Rap",
                  "Music"
                ],
                "durationInMillis": 127552,
                "releaseDate": "2022-04-08",
                "isAppleDigitalMaster": true,
                "name": "For Nothin",
                "isrc": "USSM12202701",
                "hasLyrics": true,
                "albumName": "B.I.B.L.E.",
                "playParams": {
                  "id": "1617161818",
                  "kind": "song"
                },
                "trackNumber": 6,
                "composerName": "Fivio Foreign, Rick Vilsaint, Martin Targett & Tarik Hemeci",
                "contentRating": "explicit"
              }
            },
            {
              "id": "1594677759",
              "type": "songs",
              "href": "/v1/catalog/us/songs/1594677759",
              "attributes": {
                "previews": [
                  {
                    "url": "https://audio-ssl.itunes.apple.com/itunes-itms8-assets/AudioPreview122/v4/eb/61/ca/eb61ca54-5a3b-10d5-1ab0-7080a1563262/mzaf_12169689915012476224.plus.aac.p.m4a"
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
                "artistName": "Jessica Darrow",
                "url": "https://music.apple.com/us/album/surface-pressure/1594677532?i=1594677759",
                "discNumber": 1,
                "genreNames": [
                  "Soundtrack",
                  "Music"
                ],
                "durationInMillis": 202227,
                "releaseDate": "2021-11-19",
                "isAppleDigitalMaster": true,
                "name": "Surface Pressure",
                "isrc": "USWD12112914",
                "hasLyrics": true,
                "albumName": "Encanto (Original Motion Picture Soundtrack)",
                "playParams": {
                  "id": "1594677759",
                  "kind": "song"
                },
                "trackNumber": 3,
                "composerName": "Lin-Manuel Miranda"
              }
            }
          ]
        },
        "curator": {
          "href": "/v1/catalog/us/playlists/pl.606afcbb70264d2eb2b51d8dbcfa6a12/curator",
          "data": [

          ]
        }
      }
    }
  ],
  "meta": {
    "filters": {
      "storefront-chart": {
        "us": [
          {
            "id": "pl.606afcbb70264d2eb2b51d8dbcfa6a12",
            "type": "playlists",
            "href": "/v1/catalog/us/playlists/pl.606afcbb70264d2eb2b51d8dbcfa6a12"
          }
        ]
      }
    }
  }
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/playlists`

## Parameters

- `extend` ([string]): A list of attribute extensions to apply to resources in the response.
- `filter[storefront-chart]` ([string]) *(required)*: A filter to apply to the request.
- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.

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
- [Get Multiple Catalog Playlists](get-multiple-catalog-playlists.md)
  Fetch one or more playlists by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-charts-playlists-by-storefront-value)*