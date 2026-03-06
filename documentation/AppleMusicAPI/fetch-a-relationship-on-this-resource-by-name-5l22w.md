# Get a Library Playlist's Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a library playlist’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/library/playlists/p.ldvAAZ3C3Qmop9/tracks
```

**Response**:

```json
{
    "data": [
        {
            "id": "a.1542568135",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1542568135",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Music124/v4/8c/8f/8a/8c8f8a29-8810-feb8-7091-18191ca2768a/886448619161.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Dirk Maassen",
                "discNumber": 2,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 169813,
                "releaseDate": "2020-12-18",
                "name": "Diaries (From Home)",
                "hasLyrics": false,
                "albumName": "Echoes",
                "playParams": {
                    "id": "a.1542568135",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1542568135"
                },
                "trackNumber": 3
            }
        },
        {
            "id": "a.472229257",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.472229257",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music/da/c8/4f/mzi.zuduxsnk.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Chad Lawson",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 362353,
                "releaseDate": "2011-10-09",
                "name": "Nocturne in a Minor",
                "hasLyrics": false,
                "albumName": "The Piano",
                "playParams": {
                    "id": "a.472229257",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "472229257"
                },
                "trackNumber": 2
            }
        },
        {
            "id": "a.1572874447",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1572874447",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music115/v4/e0/cf/6a/e0cf6a88-88a7-d11c-8df4-a8afc7935ffb/21UMGIM01753.rgb.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Víkingur Ólafsson",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 186542,
                "releaseDate": "2021-09-03",
                "name": "Piano Sonata No. 34 in C Minor: I. Larghetto",
                "hasLyrics": false,
                "albumName": "Mozart & Contemporaries",
                "playParams": {
                    "id": "a.1572874447",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1572874447"
                },
                "trackNumber": 16
            }
        },
        {
            "id": "a.1506251363",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1506251363",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Music114/v4/1d/fd/29/1dfd2927-03e8-19bc-ca44-fc3c07bc851b/886448387602.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Dirk Maassen",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 276795,
                "releaseDate": "2014-04-05",
                "name": "To the Sky (Moderate)",
                "hasLyrics": false,
                "albumName": "Piano Music at Home",
                "playParams": {
                    "id": "a.1506251363",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1506251363"
                },
                "trackNumber": 6
            }
        },
        {
            "id": "a.1566632114",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1566632114",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/6d/cd/d3/6dcdd3d9-89ca-52cb-87bc-b634270c6fef/190296721298.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Matteo Myderwyk",
                "discNumber": 1,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 145940,
                "releaseDate": "2021-09-17",
                "name": "Aria",
                "hasLyrics": false,
                "albumName": "Notes of Longing",
                "playParams": {
                    "id": "a.1566632114",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1566632114"
                },
                "trackNumber": 6
            }
        },
        {
            "id": "a.1394076347",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1394076347",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Music115/v4/ba/f2/b6/baf2b6f4-f81f-12d8-576b-175fed011a4f/886446990347.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Alexis Ffrench",
                "discNumber": 1,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 213645,
                "releaseDate": "2018-06-08",
                "name": "Moments",
                "hasLyrics": false,
                "albumName": "Evolution",
                "playParams": {
                    "id": "a.1394076347",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1394076347"
                },
                "trackNumber": 3
            }
        },
        {
            "id": "a.1559739419",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1559739419",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Music124/v4/64/dd/03/64dd030b-9425-2a06-5c01-d95fd1a56fc8/21UMGIM16975.rgb.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Ludovico Einaudi",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 291680,
                "releaseDate": "2006-11-07",
                "name": "Ascolta",
                "hasLyrics": false,
                "albumName": "Cinema",
                "playParams": {
                    "id": "a.1559739419",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1559739419"
                },
                "trackNumber": 13
            }
        },
        {
            "id": "a.1579486668",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1579486668",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music115/v4/23/d2/4e/23d24e8a-6209-aebf-d365-fd1c10d3bc40/21UMGIM64346.rgb.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Stephan Moccio",
                "discNumber": 1,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 313973,
                "releaseDate": "2021-08-25",
                "name": "Le Jardin de Monsieur Monet",
                "hasLyrics": false,
                "albumName": "Lionheart",
                "playParams": {
                    "id": "a.1579486668",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1579486668"
                },
                "trackNumber": 8
            }
        },
        {
            "id": "a.1580933859",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1580933859",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music115/v4/af/c6/36/afc6365b-1aaa-c32e-a52e-6375a0a10776/196292260564.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Belle Chen",
                "discNumber": 1,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 212800,
                "releaseDate": "2021-09-10",
                "name": "Lullaby for Edward",
                "hasLyrics": false,
                "albumName": "We Shall Meet Again, Under The Moon - EP",
                "playParams": {
                    "id": "a.1580933859",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1580933859"
                },
                "trackNumber": 1
            }
        },
        {
            "id": "a.1542568125",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1542568125",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Music124/v4/8c/8f/8a/8c8f8a29-8810-feb8-7091-18191ca2768a/886448619161.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Dirk Maassen",
                "discNumber": 1,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 281044,
                "releaseDate": "2021-02-12",
                "name": "In Another Life",
                "hasLyrics": false,
                "albumName": "Echoes",
                "playParams": {
                    "id": "a.1542568125",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1542568125"
                },
                "trackNumber": 8
            }
        },
        {
            "id": "a.1568819429",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1568819429",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/a1/29/93/a1299346-6de3-8a91-3a0a-baa3bd846cab/886448706922.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Igor Levit",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 131840,
                "releaseDate": "2021-08-20",
                "name": "24 Preludes and Fugues, Op. 87: Fugue No. 7 in A Major",
                "hasLyrics": false,
                "albumName": "On DSCH",
                "playParams": {
                    "id": "a.1568819429",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1568819429"
                },
                "trackNumber": 14
            }
        },
        {
            "id": "a.1578540545",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1578540545",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/0b/95/2b/0b952bc7-90e8-bb05-2d9d-3e503db31bfa/21UMGIM63637.rgb.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Jean-Yves Thibaudet",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 66573,
                "releaseDate": "2021-09-10",
                "name": "Pride & Prejudice Suite: Leaving Netherfield",
                "hasLyrics": false,
                "albumName": "Carte Blanche",
                "playParams": {
                    "id": "a.1578540545",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1578540545"
                },
                "trackNumber": 2
            }
        },
        {
            "id": "a.1563679335",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1563679335",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Music125/v4/26/46/67/26466778-712b-9cc3-1d1e-e651be7574f8/886449185856.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Olivia Belli",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 207141,
                "releaseDate": "2021-05-07",
                "name": "As I Was",
                "hasLyrics": false,
                "albumName": "As I Was - Single",
                "playParams": {
                    "id": "a.1563679335",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1563679335"
                },
                "trackNumber": 1
            }
        },
        {
            "id": "a.1337873731",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1337873731",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Music128/v4/83/70/f1/8370f148-1f5b-54de-7027-7ceab8be96a8/886446684017.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Florian Christl",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 214573,
                "releaseDate": "2018-03-23",
                "name": "Moments",
                "hasLyrics": false,
                "albumName": "Inspiration",
                "playParams": {
                    "id": "a.1337873731",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1337873731"
                },
                "trackNumber": 3
            }
        },
        {
            "id": "a.1481832458",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1481832458",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Music123/v4/ed/03/b1/ed03b1a1-530f-3c75-cff6-16f795d3d0f2/5059366399667_cover.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Steingrimur Thorhallsson",
                "discNumber": 1,
                "genreNames": [
                    "Easy Listening"
                ],
                "durationInMillis": 152000,
                "releaseDate": "2019-10-10",
                "name": "A Quarter To Ten",
                "hasLyrics": false,
                "albumName": "A Quarter To Ten - Single",
                "playParams": {
                    "id": "a.1481832458",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1481832458"
                },
                "trackNumber": 1
            }
        },
        {
            "id": "a.1578540843",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1578540843",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/0b/95/2b/0b952bc7-90e8-bb05-2d9d-3e503db31bfa/21UMGIM63637.rgb.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Jean-Yves Thibaudet",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 155867,
                "releaseDate": "2021-09-03",
                "name": "Waltz No. 19 in A Minor, Op. Posth., B. 150",
                "hasLyrics": false,
                "albumName": "Carte Blanche",
                "playParams": {
                    "id": "a.1578540843",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1578540843"
                },
                "trackNumber": 9
            }
        },
        {
            "id": "a.1572874450",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1572874450",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music115/v4/e0/cf/6a/e0cf6a88-88a7-d11c-8df4-a8afc7935ffb/21UMGIM01753.rgb.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Víkingur Ólafsson",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 242811,
                "releaseDate": "2021-09-03",
                "name": "Ave verum corpus, K. 618 (Transcr. Liszt for Solo Piano)",
                "hasLyrics": false,
                "albumName": "Mozart & Contemporaries",
                "playParams": {
                    "id": "a.1572874450",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1572874450"
                },
                "trackNumber": 21
            }
        },
        {
            "id": "a.1577661242",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1577661242",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Music115/v4/25/64/47/2564472b-273c-8a85-36b1-24fef278d6c7/198000295240.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Isle’r",
                "discNumber": 1,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 228693,
                "releaseDate": "2021-04-23",
                "name": "The Path and the Rain",
                "hasLyrics": false,
                "albumName": "Memoried",
                "playParams": {
                    "id": "a.1577661242",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1577661242"
                },
                "trackNumber": 3
            }
        },
        {
            "id": "a.1440790593",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1440790593",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music115/v4/d8/16/09/d81609a0-501a-8053-bcf0-ba4611865c47/00028947971979.rgb.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Joep Beving",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 173413,
                "releaseDate": "2015-04-28",
                "name": "The Light She Brings",
                "hasLyrics": false,
                "albumName": "Solipsism",
                "playParams": {
                    "id": "a.1440790593",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1440790593"
                },
                "trackNumber": 9
            }
        },
        {
            "id": "a.1506251530",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1506251530",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Music114/v4/1d/fd/29/1dfd2927-03e8-19bc-ca44-fc3c07bc851b/886448387602.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Dirk Maassen",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 270485,
                "releaseDate": "2014-11-30",
                "name": "La Mer",
                "hasLyrics": false,
                "albumName": "Piano Music at Home",
                "playParams": {
                    "id": "a.1506251530",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1506251530"
                },
                "trackNumber": 16
            }
        },
        {
            "id": "a.1582173172",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1582173172",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Music115/v4/3d/b2/ac/3db2ac38-a83f-a1e2-df8c-ce81a3c160ce/cover.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Laurence Ipsum",
                "discNumber": 1,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 156142,
                "releaseDate": "2021-09-17",
                "name": "Closer",
                "hasLyrics": false,
                "albumName": "Filigree Works of Sound, Vol. 2",
                "playParams": {
                    "id": "a.1582173172",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1582173172"
                },
                "trackNumber": 1
            }
        },
        {
            "id": "a.1545906169",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1545906169",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Music114/v4/d0/f2/df/d0f2df2d-3bbe-db76-1776-b905b3ed4949/3663729144409_cover.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Nils Frahm",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 165558,
                "releaseDate": "2016-03-28",
                "name": "Because This Must Be",
                "hasLyrics": false,
                "albumName": "Because This Must Be - Single",
                "playParams": {
                    "id": "a.1545906169",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1545906169"
                },
                "trackNumber": 1
            }
        },
        {
            "id": "a.1573421732",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1573421732",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Music115/v4/7d/f6/b7/7df6b7c1-cb24-1d97-13c8-39a03d4338f4/886449058617.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Lucas Debargue",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 117237,
                "releaseDate": "2021-07-09",
                "name": "Nostalgie du pays, extrait des Miniatures polonaises",
                "hasLyrics": false,
                "albumName": "Zal - The Music of Miłosz Magin",
                "playParams": {
                    "id": "a.1573421732",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1573421732"
                },
                "trackNumber": 9
            }
        },
        {
            "id": "a.1577793875",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1577793875",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music125/v4/59/4f/a8/594fa861-e9a0-8db8-c39b-6e2c0cc35870/19UM1IM14434.rgb.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Daniil Trifonov",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 258520,
                "releaseDate": "2021-08-27",
                "name": "Herz und Mund und Tat und Leben, Cantata BWV 147: Jesu, Joy of Man’s Desiring (Transcr. Hess for Piano)",
                "hasLyrics": false,
                "albumName": "BACH: The Art of Life",
                "playParams": {
                    "id": "a.1577793875",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1577793875"
                },
                "trackNumber": 57
            }
        },
        {
            "id": "a.957451796",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.957451796",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Music5/v4/58/15/56/5815567d-2f7b-ded5-ddb3-295ca2b2ea42/859713932418_cover.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Steingrimur Thorhallsson",
                "discNumber": 1,
                "genreNames": [
                    "Instrumental"
                ],
                "durationInMillis": 237000,
                "releaseDate": "2014-12-24",
                "name": "Lauds",
                "hasLyrics": false,
                "albumName": "December Hours",
                "playParams": {
                    "id": "a.957451796",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "957451796"
                },
                "trackNumber": 2
            }
        },
        {
            "id": "a.767432654",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.767432654",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Music115/v4/52/5a/87/525a8768-6c5a-00bb-4825-34edce4bf5cc/880918216935.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Otto A. Totland",
                "discNumber": 1,
                "genreNames": [
                    "Modern Era"
                ],
                "durationInMillis": 165995,
                "releaseDate": "2014-01-31",
                "name": "Pinô",
                "hasLyrics": false,
                "albumName": "Pinô",
                "playParams": {
                    "id": "a.767432654",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "767432654"
                },
                "trackNumber": 7
            }
        },
        {
            "id": "a.1474949205",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1474949205",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Music115/v4/d1/57/0d/d1570d66-ddd4-6f32-c2d5-f82de44e719c/19UMGIM66727.rgb.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Ola Gjeilo",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 142333,
                "releaseDate": "2020-01-24",
                "name": "Still",
                "hasLyrics": false,
                "albumName": "Night",
                "playParams": {
                    "id": "a.1474949205",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1474949205"
                },
                "trackNumber": 3
            }
        },
        {
            "id": "a.1194668612",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1194668612",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Music124/v4/47/13/6b/47136b0e-514f-6eb0-ccff-f1411a0114a7/cover.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Fabrizio Paterlini",
                "discNumber": 1,
                "genreNames": [
                    "Contemporary Era"
                ],
                "durationInMillis": 148205,
                "releaseDate": "2014-02-04",
                "name": "Wind Song",
                "hasLyrics": false,
                "albumName": "The Art of the Piano",
                "playParams": {
                    "id": "a.1194668612",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1194668612"
                },
                "trackNumber": 8
            }
        },
        {
            "id": "a.1584268630",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1584268630",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music125/v4/e9/75/fc/e975fc57-a015-378e-2628-7915464fa22f/21UMGIM67990.rgb.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Federico Albanese",
                "discNumber": 1,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 135369,
                "releaseDate": "2021-09-17",
                "name": "Silenzio",
                "hasLyrics": false,
                "albumName": "Silenzio - Single",
                "playParams": {
                    "id": "a.1584268630",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1584268630"
                },
                "trackNumber": 1
            }
        },
        {
            "id": "a.1478320679",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1478320679",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music125/v4/a2/01/d5/a201d5ec-e2a4-9b9d-ec9f-4edc52a9fea8/886447706299.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Dirk Maassen",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 237627,
                "releaseDate": "2019-09-13",
                "name": "Two Skies",
                "hasLyrics": false,
                "albumName": "Ocean",
                "playParams": {
                    "id": "a.1478320679",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1478320679"
                },
                "trackNumber": 9
            }
        },
        {
            "id": "a.1452619570",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1452619570",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Music124/v4/1b/77/8c/1b778cf7-414c-216c-a2d2-7f9b8a4ad01f/00827590363250.rgb.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Jean-Michel Blais",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 346813,
                "releaseDate": "2018-02-02",
                "name": "roses",
                "hasLyrics": false,
                "albumName": "roses - Single",
                "playParams": {
                    "id": "a.1452619570",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1452619570"
                },
                "trackNumber": 1
            }
        },
        {
            "id": "a.1542568132",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1542568132",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Music124/v4/8c/8f/8a/8c8f8a29-8810-feb8-7091-18191ca2768a/886448619161.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Dirk Maassen",
                "discNumber": 2,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 126893,
                "releaseDate": "2021-03-05",
                "name": "Air (From Home)",
                "hasLyrics": false,
                "albumName": "Echoes",
                "playParams": {
                    "id": "a.1542568132",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1542568132"
                },
                "trackNumber": 2
            }
        },
        {
            "id": "a.1550204253",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1550204253",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Music114/v4/62/9a/00/629a00a9-4c47-5f32-5baf-d1fc0523ec72/886448970200.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Eydís Evensen",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 195193,
                "releaseDate": "2021-01-29",
                "name": "Brotin",
                "hasLyrics": false,
                "albumName": "Brotin - Single",
                "playParams": {
                    "id": "a.1550204253",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1550204253"
                },
                "trackNumber": 1
            }
        },
        {
            "id": "a.1165107675",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1165107675",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Music71/v4/75/47/ad/7547adff-9052-23f0-f174-64e070a0252c/859718500582_cover.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Alexis Ffrench",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 169617,
                "releaseDate": "2016-10-17",
                "name": "A Time of Wonder",
                "hasLyrics": false,
                "albumName": "The Piano Whisperer",
                "playParams": {
                    "id": "a.1165107675",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1165107675"
                },
                "trackNumber": 3
            }
        },
        {
            "id": "a.1560605348",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1560605348",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Music124/v4/6d/52/6f/6d526fa4-f643-59da-655c-4908d09471aa/886449185252.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Olivia Belli",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 180270,
                "releaseDate": "2021-04-16",
                "name": "Visions to Come",
                "hasLyrics": false,
                "albumName": "Belli: Visions to Come - Single",
                "playParams": {
                    "id": "a.1560605348",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1560605348"
                },
                "trackNumber": 1
            }
        },
        {
            "id": "a.989431055",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.989431055",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music7/v4/dd/a2/b7/dda2b706-96ba-b138-2489-be565590d67e/859714604628_cover.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Ed Haydon",
                "discNumber": 1,
                "genreNames": [
                    "Soundtrack"
                ],
                "durationInMillis": 235500,
                "releaseDate": "2015-05-09",
                "name": "Hope",
                "hasLyrics": false,
                "albumName": "Heart Strings",
                "playParams": {
                    "id": "a.989431055",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "989431055"
                },
                "trackNumber": 3
            }
        },
        {
            "id": "a.1375632646",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1375632646",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music115/v4/ab/ca/82/abca82cb-31a3-582a-180c-46912abc8d0d/cover.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Dirk Maassen",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 249645,
                "releaseDate": "2018-07-13",
                "name": "Falling Stars",
                "hasLyrics": false,
                "albumName": "Avalanche",
                "playParams": {
                    "id": "a.1375632646",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1375632646"
                },
                "trackNumber": 6
            }
        },
        {
            "id": "a.1440762223",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1440762223",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music125/v4/ea/44/86/ea448600-257f-670f-7f06-332e02b42abc/06UMGIM59381.rgb.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Ludovico Einaudi",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 229827,
                "releaseDate": "2004-09-06",
                "name": "Dietro Casa",
                "hasLyrics": false,
                "albumName": "Una Mattina",
                "playParams": {
                    "id": "a.1440762223",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1440762223"
                },
                "trackNumber": 7
            }
        },
        {
            "id": "a.1053971369",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1053971369",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music114/v4/7f/5c/2c/7f5c2c3b-a2c8-e795-c60f-06142f96a6f8/mzm.egfcslyw.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Federico Albanese",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 234464,
                "releaseDate": "2016-01-15",
                "name": "Shadow Land, Pt. 1",
                "hasLyrics": false,
                "albumName": "The Blue Hour",
                "playParams": {
                    "id": "a.1053971369",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1053971369"
                },
                "trackNumber": 4
            }
        },
        {
            "id": "a.1092653570",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1092653570",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Music124/v4/d6/e0/29/d6e029f4-1b5e-1be4-4502-65737eafaefe/5051083097284.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Ilya Beshevli",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 273013,
                "releaseDate": "2016-05-27",
                "name": "Covenant",
                "hasLyrics": false,
                "albumName": "Wanderer",
                "playParams": {
                    "id": "a.1092653570",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1092653570"
                },
                "trackNumber": 4
            }
        },
        {
            "id": "a.1574554100",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1574554100",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Music115/v4/09/cc/91/09cc91b6-b75e-4da6-4dc8-5830b5510d38/886449375806.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Dirk Maassen",
                "discNumber": 1,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 235579,
                "releaseDate": "2021-07-23",
                "name": "Fragile",
                "hasLyrics": false,
                "albumName": "Re:Visions",
                "playParams": {
                    "id": "a.1574554100",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1574554100"
                },
                "trackNumber": 3
            }
        },
        {
            "id": "a.1177210673",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1177210673",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music125/v4/5a/29/78/5a2978d9-ca90-890c-3708-1578b5d89d1e/886446216874.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Dustin O’Halloran & Hauschka",
                "discNumber": 1,
                "genreNames": [
                    "Soundtrack"
                ],
                "durationInMillis": 118747,
                "releaseDate": "2016-11-25",
                "name": "Lion Theme",
                "hasLyrics": false,
                "albumName": "Lion (Original Motion Picture Soundtrack)",
                "playParams": {
                    "id": "a.1177210673",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1177210673"
                },
                "trackNumber": 2
            }
        },
        {
            "id": "a.693364434",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.693364434",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Music124/v4/4d/ba/b8/4dbab8b3-7634-bd5c-9f04-4723365cf857/0724359235356_1401x1401_300dpi.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Yann Tiersen",
                "discNumber": 1,
                "genreNames": [
                    "Pop"
                ],
                "durationInMillis": 104800,
                "releaseDate": "2003-02-03",
                "name": "Childhood (2)",
                "hasLyrics": false,
                "albumName": "Goodbye Lenin!",
                "playParams": {
                    "id": "a.693364434",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "693364434"
                },
                "trackNumber": 9
            }
        },
        {
            "id": "a.1579271930",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1579271930",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Music125/v4/cd/40/98/cd40983c-392a-0965-5599-4a51335002eb/886449380015.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Rewired88",
                "discNumber": 1,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 176143,
                "releaseDate": "2021-08-20",
                "name": "Sapphires",
                "hasLyrics": false,
                "albumName": "Sapphires - Single",
                "playParams": {
                    "id": "a.1579271930",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1579271930"
                },
                "trackNumber": 1
            }
        },
        {
            "id": "a.1478320133",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1478320133",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music125/v4/a2/01/d5/a201d5ec-e2a4-9b9d-ec9f-4edc52a9fea8/886447706299.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Dirk Maassen",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 264010,
                "releaseDate": "2019-11-29",
                "name": "Peace of Mind",
                "hasLyrics": false,
                "albumName": "Ocean",
                "playParams": {
                    "id": "a.1478320133",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1478320133"
                },
                "trackNumber": 3
            }
        },
        {
            "id": "a.16750361",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.16750361",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Features/v4/f7/7a/76/f77a7627-f673-54b7-5f35-ee7810503855/dj.buyrqmih.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "David Nevue",
                "discNumber": 1,
                "genreNames": [
                    "Christian"
                ],
                "durationInMillis": 184573,
                "releaseDate": "1997-01-01",
                "name": "Ascending With Angels",
                "hasLyrics": false,
                "albumName": "The Last Waking Moment",
                "playParams": {
                    "id": "a.16750361",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "16750361"
                },
                "trackNumber": 8
            }
        },
        {
            "id": "a.1579066864",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1579066864",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music125/v4/98/80/0c/98800cc3-eb7c-e726-d73c-e6ffaaf9010b/886449436675.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Olga Scheps",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 152419,
                "releaseDate": "2021-08-13",
                "name": "Morning Mood Variation (Arr. for Piano from Peer Gynt Suite No. 1, Op. 36 by Ketan & Vivan Bhatti)",
                "hasLyrics": false,
                "albumName": "Morning Mood Variation (Arr. for Piano from Peer Gynt Suite No. 1, Op. 36 by Ketan & Vivan Bhatti) - Single",
                "playParams": {
                    "id": "a.1579066864",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1579066864"
                },
                "trackNumber": 1
            }
        },
        {
            "id": "a.1489661837",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1489661837",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music124/v4/83/74/36/83743652-f517-9913-db64-f87020f2c634/rls00077657.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Martin Herzberg",
                "discNumber": 1,
                "genreNames": [
                    "Electronic"
                ],
                "durationInMillis": 265033,
                "releaseDate": "2013-12-01",
                "name": "Lifelines",
                "hasLyrics": false,
                "albumName": "Lifelines of Music",
                "playParams": {
                    "id": "a.1489661837",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1489661837"
                },
                "trackNumber": 2
            }
        },
        {
            "id": "a.1506251373",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1506251373",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Music114/v4/1d/fd/29/1dfd2927-03e8-19bc-ca44-fc3c07bc851b/886448387602.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Dirk Maassen",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 257110,
                "releaseDate": "2016-07-19",
                "name": "Saltare (Somewhere at the Baltic Sea)",
                "hasLyrics": false,
                "albumName": "Piano Music at Home",
                "playParams": {
                    "id": "a.1506251373",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1506251373"
                },
                "trackNumber": 12
            }
        },
        {
            "id": "a.1390704156",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1390704156",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/74/16/18/74161878-065f-8d9b-0c1d-6225ef887634/00602567687504.rgb.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Ólafur Arnalds",
                "discNumber": 1,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 131923,
                "releaseDate": "2018-08-24",
                "name": "saman",
                "hasLyrics": false,
                "albumName": "re:member",
                "playParams": {
                    "id": "a.1390704156",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1390704156"
                },
                "trackNumber": 3
            }
        },
        {
            "id": "a.1558923456",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1558923456",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music124/v4/be/84/0f/be840f9d-5405-e957-f935-752e40fbe93a/886449153077.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Hugar",
                "discNumber": 1,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 116627,
                "releaseDate": "2021-03-29",
                "name": "Vísur Vatnsenda-Rósu",
                "hasLyrics": false,
                "albumName": "Þjóðlög / Folk Songs - EP",
                "playParams": {
                    "id": "a.1558923456",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1558923456"
                },
                "trackNumber": 4
            }
        },
        {
            "id": "a.1527037829",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1527037829",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Music124/v4/ad/db/d0/addbd03b-f5d1-026e-6fb2-471b51a71da1/886448700562.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Dardust",
                "discNumber": 1,
                "genreNames": [
                    "Pop"
                ],
                "durationInMillis": 205235,
                "releaseDate": "2020-08-28",
                "name": "S.A.D. (Piano Solo)",
                "hasLyrics": false,
                "albumName": "S.A.D. (Piano Solo) - EP",
                "playParams": {
                    "id": "a.1527037829",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1527037829"
                },
                "trackNumber": 5
            }
        },
        {
            "id": "a.1464980335",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1464980335",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music124/v4/80/29/c9/8029c937-246b-83b6-3fc9-e528cad954b6/190295408985.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Carlos Cipa",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 443483,
                "releaseDate": "2019-08-23",
                "name": "and she was",
                "hasLyrics": false,
                "albumName": "Cipa: Retronyms",
                "playParams": {
                    "id": "a.1464980335",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1464980335"
                },
                "trackNumber": 4
            }
        },
        {
            "id": "a.1452314593",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1452314593",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Music114/v4/47/15/f1/4715f1cc-b7e9-8f6a-b98f-476906f3ed14/00028948167432.rgb.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Sophie Hutchings",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 329107,
                "releaseDate": "2012-08-24",
                "name": "By Night",
                "hasLyrics": false,
                "albumName": "Night Sky",
                "playParams": {
                    "id": "a.1452314593",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1452314593"
                },
                "trackNumber": 6
            }
        },
        {
            "id": "a.1570081296",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1570081296",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music125/v4/26/d2/45/26d245a8-56f0-5fdb-8f63-e75326701b9a/886449315765.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Goldbæk",
                "discNumber": 1,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 202829,
                "releaseDate": "2021-06-18",
                "name": "Challen",
                "hasLyrics": false,
                "albumName": "Challen - Single",
                "playParams": {
                    "id": "a.1570081296",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1570081296"
                },
                "trackNumber": 1
            }
        },
        {
            "id": "a.724561744",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.724561744",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Music125/v4/b1/44/20/b14420f5-f047-f28d-ff10-d2a469df5147/00724383954957.rgb.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Michael Nyman",
                "discNumber": 1,
                "genreNames": [
                    "Soundtrack"
                ],
                "durationInMillis": 96560,
                "releaseDate": "1993-10-19",
                "name": "The Heart Asks Pleasure First",
                "hasLyrics": false,
                "albumName": "The Piano",
                "playParams": {
                    "id": "a.724561744",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "724561744"
                },
                "trackNumber": 4
            }
        },
        {
            "id": "a.1542568130",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1542568130",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Music124/v4/8c/8f/8a/8c8f8a29-8810-feb8-7091-18191ca2768a/886448619161.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Dirk Maassen",
                "discNumber": 2,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 168493,
                "releaseDate": "2020-12-18",
                "name": "Introspective (From Home)",
                "hasLyrics": false,
                "albumName": "Echoes",
                "playParams": {
                    "id": "a.1542568130",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1542568130"
                },
                "trackNumber": 1
            }
        },
        {
            "id": "a.862972531",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.862972531",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Music125/v4/f8/26/6a/f8266ac6-8a00-4769-aacc-fae0702d33b9/886443985216.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Khatia Buniatishvili",
                "discNumber": 1,
                "genreNames": [
                    "Classical"
                ],
                "durationInMillis": 130904,
                "releaseDate": "2014-05-16",
                "name": "Tune from the Film \"When Almonds Blossomed\",
                "hasLyrics": false,
                "albumName": "Motherland",
                "playParams": {
                    "id": "a.862972531",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "862972531"
                },
                "trackNumber": 5
            }
        },
        {
            "id": "a.1554074871",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1554074871",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Music125/v4/19/3d/dc/193ddc04-6d23-31ae-2b8c-20a2a299fc82/886448661382.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Eydís Evensen",
                "discNumber": 1,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 187200,
                "releaseDate": "2021-03-12",
                "name": "Dagdraumur",
                "hasLyrics": false,
                "albumName": "Bylur",
                "playParams": {
                    "id": "a.1554074871",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1554074871"
                },
                "trackNumber": 2
            }
        },
        {
            "id": "a.1526806490",
            "type": "library-songs",
            "href": "/v1/me/library/songs/a.1526806490",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music114/v4/7d/84/ce/7d84ceaf-f51e-45d4-b2f8-2327751672dc/886448401407.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Alexis Ffrench",
                "discNumber": 1,
                "genreNames": [
                    "Classical Crossover"
                ],
                "durationInMillis": 190309,
                "releaseDate": "2020-09-04",
                "name": "Shine (Solo Piano Version)",
                "hasLyrics": false,
                "albumName": "Shine (Solo Piano Version) - Single",
                "playParams": {
                    "id": "a.1526806490",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1526806490"
                },
                "trackNumber": 1
            }
        }
    ],
    "meta": {
        "total": 60
    }
}
```

## Endpoint

`GET https://api.music.apple.com/v1/me/library/playlists/{id}/{relationship}`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object LibraryPlaylists](libraryplaylists.md)
  A resource object that represents a library playlist.
- [object LibraryPlaylistsResponse](libraryplaylistsresponse.md)
  The response to a library playlists request.
- [Get a Library Playlist](get-a-library-playlist.md)
  Fetch a library playlist by using its identifier.
- [Get Multiple Library Playlists](get-multiple-library-playlists.md)
  Fetch one or more library playlists by using their identifiers.
- [Get All Library Playlists](get-all-library-playlists.md)
  Fetch all the library playlists in alphabetical order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-5l22w)*