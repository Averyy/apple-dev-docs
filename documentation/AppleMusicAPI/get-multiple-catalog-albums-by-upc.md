# Get Multiple Catalog Albums by UPC

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more albums by using their UPC values.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/albums?filter[upc]=00602445868162
```

**Response**:

```json
{
    "data": [
        {
            "id": "1620500261",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1620500261",
            "attributes": {
                "copyright": "A 10 Summers/Interscope Records Release; ℗ 2022 10 Summers Records, LLC",
                "genreNames": [
                    "R&B/Soul",
                    "Music"
                ],
                "releaseDate": "2022-05-06",
                "upc": "00602445868162",
                "isMasteredForItunes": true,
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                    "bgColor": "0b1b18",
                    "textColor1": "fc977a",
                    "textColor2": "ef5429",
                    "textColor3": "cc7e66",
                    "textColor4": "c14925"
                },
                "playParams": {
                    "id": "1620500261",
                    "kind": "album"
                },
                "url": "https://music.apple.com/us/album/heart-on-my-sleeve/1620500261",
                "recordLabel": "10 Summers/Interscope Records",
                "isCompilation": false,
                "trackCount": 15,
                "isSingle": false,
                "name": "Heart On My Sleeve",
                "artistName": "Ella Mai",
                "contentRating": "clean",
                "isComplete": true
            },
            "relationships": {
                "tracks": {
                    "href": "/v1/catalog/us/albums/1620500261/tracks",
                    "data": [
                        {
                            "id": "1620500269",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1620500269",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 1,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 197314,
                                "isrc": "USUM72203653",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Charles Hinshaw Jr, Dijon McFarlane, Ella Mai Howell, NICHOLAS MATTHEW BALDING, Peter Johnson & Shah Rukh Zaman Khan",
                                "url": "https://music.apple.com/us/album/trying/1620500261?i=1620500269",
                                "playParams": {
                                    "id": "1620500269",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Trying",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/5d/ca/5e/5dca5e25-77c2-bfb2-c4ee-b626b8d85c00/mzaf_6597404571320735119.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1620500271",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1620500271",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 2,
                                "releaseDate": "2022-04-02",
                                "durationInMillis": 255013,
                                "isrc": "USUM72203647",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Jahaan Sweet, Matthew Samuels, Khristopher Riddick-Tynes, Leon Thomas III, Ella Mai Howell & Varren Wade",
                                "url": "https://music.apple.com/us/album/not-another-love-song/1620500261?i=1620500271",
                                "playParams": {
                                    "id": "1620500271",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Not Another Love Song",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/92/a4/1f/92a41fce-a3dc-07bd-34a4-2aa8ae4f2e79/mzaf_18250059380211613657.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1620500272",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1620500272",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 3,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 245650,
                                "isrc": "USUM72204963",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "alyssa michelle stephens, Dijon McFarlane, Ella Mai Howell, Shah Rukh Zaman Khan & Varren Wade",
                                "url": "https://music.apple.com/us/album/didnt-say-feat-latto/1620500261?i=1620500272",
                                "playParams": {
                                    "id": "1620500272",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Didn't Say (feat. Latto)",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/fa/0e/d3/fa0ed36f-6fe4-8249-1725-561eb1e78f85/mzaf_9334449658817450379.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "clean"
                            }
                        },
                        {
                            "id": "1620500277",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1620500277",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 4,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 194826,
                                "isrc": "USUM72203644",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Charles Hinshaw Jr, Dernst Emile II & Ella Mai Howell",
                                "url": "https://music.apple.com/us/album/break-my-heart/1620500261?i=1620500277",
                                "playParams": {
                                    "id": "1620500277",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Break My Heart",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/b8/db/02/b8db0271-baeb-e8f3-776b-3e4d2f835aea/mzaf_13116830436170401764.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1620500280",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1620500280",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 5,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 261811,
                                "isrc": "USUM72203646",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Ari Irosogie, Ella Mai Howell, Gaeten, Jahaan Akil Sweet, Jvck James, Kirk Franklin, Marco, Richard Olowaranti Mbu Isong & Wolftyla",
                                "url": "https://music.apple.com/us/album/fallen-angel/1620500261?i=1620500280",
                                "playParams": {
                                    "id": "1620500280",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Fallen Angel",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/2b/37/c4/2b37c41e-f592-1615-53ae-ca1773885ddb/mzaf_5473240690781278418.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1620500284",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1620500284",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 6,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 218317,
                                "isrc": "USUM72204964",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Bass Charity, Dijon McFarlane, Ella Mai Howell, FELICIANO ECAR, Floyd Eugene Bentley Iii, Harissis Tsakmaklis, Jorge Augusto, Luzian Tuetsch, NICHOLAS MATTHEW BALDING, Rodrick Wayne Moore & Varren Wade",
                                "url": "https://music.apple.com/us/album/how-feat-roddy-ricch/1620500261?i=1620500284",
                                "playParams": {
                                    "id": "1620500284",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "How (feat. Roddy Ricch)",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/0b/cf/f1/0bcff10c-3db5-750e-3498-142fc61deefd/mzaf_7248163605629002330.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "clean"
                            }
                        },
                        {
                            "id": "1620500648",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1620500648",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 7,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 198795,
                                "isrc": "USUM72203650",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Danny Schofield, Ella Mai Howell, Sir Nolan & Varren Wade",
                                "url": "https://music.apple.com/us/album/pieces/1620500261?i=1620500648",
                                "playParams": {
                                    "id": "1620500648",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Pieces",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/65/a9/a2/65a9a2c0-cbb7-45bf-93f5-d81fc346d53f/mzaf_13504976053002672754.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1620500652",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1620500652",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 8,
                                "releaseDate": "2022-01-28",
                                "durationInMillis": 197517,
                                "isrc": "USUM72200120",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Ella Mai Howell, Charles Hinshaw Jr, Dijon McFarlane, Daemon Landrum, Jonathan Sanders, Tyus Strickland, Donell Jones & Kyle West",
                                "url": "https://music.apple.com/us/album/dfmu/1620500261?i=1620500652",
                                "playParams": {
                                    "id": "1620500652",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "DFMU",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/60/ee/88/60ee8840-ec58-ef03-70cf-19a2d039aad3/mzaf_16082051003517237880.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "clean"
                            }
                        },
                        {
                            "id": "1620500653",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1620500653",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 9,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 208119,
                                "isrc": "USUM72203649",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Charles Hinshaw Jr, Dijon McFarlane, Ella Mai Howell & Wolftyla",
                                "url": "https://music.apple.com/us/album/hide/1620500261?i=1620500653",
                                "playParams": {
                                    "id": "1620500653",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Hide",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/78/8f/0c/788f0c51-203f-b621-afa0-660ec284140a/mzaf_11407212206678378683.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1620500657",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1620500657",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 10,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 213885,
                                "isrc": "USUM72203652",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Cam Griffin, Dijon McFarlane, Ella Mai Howell, Jason Pounds & Varren Wade",
                                "url": "https://music.apple.com/us/album/power-of-a-woman/1620500261?i=1620500657",
                                "playParams": {
                                    "id": "1620500657",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Power Of A Woman",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/42/f5/93/42f5934c-54d6-f8f2-79fb-7d28761a889f/mzaf_13405667590831158068.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1620500663",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1620500663",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 11,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 233794,
                                "isrc": "USUM72204966",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Cameron Joseph, David Brown, Ella Mai Howell, Matthew Samuels, Michael Samuels Jr., Mike McGregor & Peter Iskander",
                                "url": "https://music.apple.com/us/album/a-mess-feat-lucky-daye/1620500261?i=1620500663",
                                "playParams": {
                                    "id": "1620500663",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": false,
                                "isAppleDigitalMaster": true,
                                "name": "A Mess (feat. Lucky Daye)",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/bd/81/ca/bd81ca2e-0cc3-6a49-443a-145e1c158f43/mzaf_2477860820242782529.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "clean"
                            }
                        },
                        {
                            "id": "1620500674",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1620500674",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 12,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 199909,
                                "isrc": "USUM72204962",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Chloe George, Ella Mai Howell, Jorgen Odegard & Stephanie Nicole Jones",
                                "url": "https://music.apple.com/us/album/feels-like/1620500261?i=1620500674",
                                "playParams": {
                                    "id": "1620500674",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": false,
                                "isAppleDigitalMaster": true,
                                "name": "Feels Like",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/14/e2/ab/14e2ab3d-fd88-ec13-681b-29cf46b21414/mzaf_8155293122708882028.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "clean"
                            }
                        },
                        {
                            "id": "1620500770",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1620500770",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 13,
                                "releaseDate": "2022-04-02",
                                "durationInMillis": 209136,
                                "isrc": "USUM72204723",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Ella Mai Howell, Varren Wade, Harmony Samuels & Edgar Etienne",
                                "url": "https://music.apple.com/us/album/leave-you-alone/1620500261?i=1620500770",
                                "playParams": {
                                    "id": "1620500770",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Leave You Alone",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/3b/bd/95/3bbd9588-7359-3764-c30d-e4ee9abf5b07/mzaf_16785343148441517892.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "clean"
                            }
                        },
                        {
                            "id": "1620500773",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1620500773",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 14,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 234613,
                                "isrc": "USUM72204965",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Charles Hinshaw Jr, Dernst Emile II, Ella Mai Howell & Mary J. Blige",
                                "url": "https://music.apple.com/us/album/sink-or-swim/1620500261?i=1620500773",
                                "playParams": {
                                    "id": "1620500773",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Sink or Swim",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/aa/11/ec/aa11ec02-dd79-dca3-acb3-87b5fe37f870/mzaf_9724937243396107712.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "clean"
                            }
                        },
                        {
                            "id": "1620500780",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1620500780",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 15,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 214882,
                                "isrc": "USUM72204961",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a4/1d/a7/a41da7bd-af89-032c-2d7e-7bfb0d9d8692/22UMGIM32702.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Ella Mai Howell, Jahaan Akil Sweet & Varren Wade",
                                "url": "https://music.apple.com/us/album/fading-out/1620500261?i=1620500780",
                                "playParams": {
                                    "id": "1620500780",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Fading Out",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/e2/d8/d5/e2d8d53b-3dd1-a1d5-0c71-aa6431ba160d/mzaf_14489967022318346201.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "clean"
                            }
                        }
                    ]
                },
                "artists": {
                    "href": "/v1/catalog/us/albums/1620500261/artists",
                    "data": [
                        {
                            "id": "1160482144",
                            "type": "artists",
                            "href": "/v1/catalog/us/artists/1160482144"
                        }
                    ]
                }
            }
        },
        {
            "id": "1616728060",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1616728060",
            "attributes": {
                "copyright": "A 10 Summers/Interscope Records Release; ℗ 2022 10 Summers Records, LLC",
                "genreNames": [
                    "R&B/Soul",
                    "Music"
                ],
                "releaseDate": "2022-05-06",
                "upc": "00602445790951",
                "isMasteredForItunes": true,
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                    "bgColor": "0b1b18",
                    "textColor1": "fc977a",
                    "textColor2": "ef5429",
                    "textColor3": "cc7e66",
                    "textColor4": "c14925"
                },
                "playParams": {
                    "id": "1616728060",
                    "kind": "album"
                },
                "url": "https://music.apple.com/us/album/heart-on-my-sleeve/1616728060",
                "recordLabel": "10 Summers/Interscope Records",
                "isCompilation": false,
                "trackCount": 15,
                "isSingle": false,
                "name": "Heart On My Sleeve",
                "artistName": "Ella Mai",
                "contentRating": "explicit",
                "editorialNotes": {
                    "standard": "Ella Mai knows her way around a love song. We've known that for years—certainly since her 2017 single “Boo'd Up” proved a breakout sensation—but her second album cements her as one of R&B's preeminent heart healers. <i>Heart on My Sleeve</i> is filled with the kind of desperate pleas and resolute statements of adoration that could soften even the hardest of hearts. With a voice made of satin and honey, she sings of love in the way so many wish to feel it—vulnerable and terrified yet thoroughly convinced it's worth it.\n\nThe lead singles, “DFMU” (which stands for “don't fuck me up”) and “Leave You Alone” (“I can't leave you alone,” goes the staccato and Auto-Tune hook), were the perfect appetizers for what proves to be a buffet of tender devotion intertwined with blind infatuation. On the gorgeous “Break My Heart,” Mai welcomes the heartache if it means feeling the rush for even a second: “Face my fears, ’cause if I had to choose who could break my heart, baby, it would be you,” she confesses on the hook. “Fallen Angel” literally invokes the heavens with a cameo from a Kirk Franklin-led choir that slides seamlessly into the lament of “How,” which, despite its grievances, still manages an optimistic bent. Elsewhere, tracks like “Pieces” and “A Mess” are about leaning into a person and the feelings they stir up, even when it doesn't necessarily make sense.\n\nThe songs here aren't naive to the problems or immune to the pain, but instead reflect someone choosing love again and again. It's far too easy to keep our walls up—and in a voice note at the end of “Sink or Swim,” Mary J. Blige in fact implores us to “guard that heart” from those who don't deserve us—but <i>Heart on My Sleeve</i> also reminds us of the potential rewards that await on the other side.",
                    "short": "The singer dazzles with her second LP, a collection of lush, heartfelt R&B."
                },
                "isComplete": true
            },
            "relationships": {
                "tracks": {
                    "href": "/v1/catalog/us/albums/1616728060/tracks",
                    "data": [
                        {
                            "id": "1616728064",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1616728064",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 1,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 197314,
                                "isrc": "USUM72203653",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Charles Hinshaw Jr, Dijon McFarlane, Ella Mai Howell, NICHOLAS MATTHEW BALDING, Peter Johnson & Shah Rukh Zaman Khan",
                                "url": "https://music.apple.com/us/album/trying/1616728060?i=1616728064",
                                "playParams": {
                                    "id": "1616728064",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Trying",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/c8/99/a7/c899a79c-e0b1-68ff-ac5e-37cb41c8bc6a/mzaf_613689503757681664.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1616728065",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1616728065",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 2,
                                "releaseDate": "2022-04-02",
                                "durationInMillis": 255013,
                                "isrc": "USUM72203647",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Jahaan Sweet, Matthew Samuels, Khristopher Riddick-Tynes, Leon Thomas III, Ella Mai Howell & Varren Wade",
                                "url": "https://music.apple.com/us/album/not-another-love-song/1616728060?i=1616728065",
                                "playParams": {
                                    "id": "1616728065",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Not Another Love Song",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/c2/01/ad/c201ad8c-9597-9eae-1013-0694c393be2e/mzaf_10993214544239266867.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1616728066",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1616728066",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 3,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 245650,
                                "isrc": "USUM72203642",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "alyssa michelle stephens, Dijon McFarlane, Ella Mai Howell, Shah Rukh Zaman Khan & Varren Wade",
                                "url": "https://music.apple.com/us/album/didnt-say-feat-latto/1616728060?i=1616728066",
                                "playParams": {
                                    "id": "1616728066",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Didn't Say (feat. Latto)",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/65/46/30/65463007-33de-a809-4bcd-ea345c87a561/mzaf_15582090794019773151.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "explicit"
                            }
                        },
                        {
                            "id": "1616728067",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1616728067",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 4,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 194826,
                                "isrc": "USUM72203644",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Charles Hinshaw Jr, Dernst Emile II & Ella Mai Howell",
                                "url": "https://music.apple.com/us/album/break-my-heart/1616728060?i=1616728067",
                                "playParams": {
                                    "id": "1616728067",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Break My Heart",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/c6/db/b2/c6dbb255-5ff5-7dcf-f2c3-4abd9cfab447/mzaf_4817315313113526902.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1616728068",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1616728068",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 5,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 261811,
                                "isrc": "USUM72203646",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Ari Irosogie, Ella Mai Howell, Gaeten, Jahaan Akil Sweet, Jvck James, Kirk Franklin, Marco, Richard Olowaranti Mbu Isong & Wolftyla",
                                "url": "https://music.apple.com/us/album/fallen-angel/1616728060?i=1616728068",
                                "playParams": {
                                    "id": "1616728068",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Fallen Angel",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/10/09/3d/10093d6b-3371-0878-2abe-2a174be8db7c/mzaf_11447589703428563008.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1616728069",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1616728069",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 6,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 218317,
                                "isrc": "USUM72203645",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Bass Charity, Dijon McFarlane, Ella Mai Howell, FELICIANO ECAR, Floyd Eugene Bentley Iii, Harissis Tsakmaklis, Jorge Augusto, Luzian Tuetsch, NICHOLAS MATTHEW BALDING, Rodrick Wayne Moore & Varren Wade",
                                "url": "https://music.apple.com/us/album/how-feat-roddy-ricch/1616728060?i=1616728069",
                                "playParams": {
                                    "id": "1616728069",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "How (feat. Roddy Ricch)",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/d2/58/d2/d258d278-819b-3522-a1b9-2d6e8b3af57a/mzaf_8765703002683868492.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "explicit"
                            }
                        },
                        {
                            "id": "1616728070",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1616728070",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 7,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 198795,
                                "isrc": "USUM72203650",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Danny Schofield, Ella Mai Howell, Sir Nolan & Varren Wade",
                                "url": "https://music.apple.com/us/album/pieces/1616728060?i=1616728070",
                                "playParams": {
                                    "id": "1616728070",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Pieces",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/25/70/e4/2570e403-e886-6663-5507-61edb075afe7/mzaf_15697244584423975937.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1616728071",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1616728071",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 8,
                                "releaseDate": "2022-01-28",
                                "durationInMillis": 197517,
                                "isrc": "USUM72123679",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Ella Mai Howell, Charles Hinshaw Jr, Dijon McFarlane, Daemon Landrum, Jonathan Sanders, Tyus Strickland, Donell Jones & Kyle West",
                                "url": "https://music.apple.com/us/album/dfmu/1616728060?i=1616728071",
                                "playParams": {
                                    "id": "1616728071",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "DFMU",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/87/2b/a2/872ba250-ba86-aadc-e97e-bf840f9956cf/mzaf_5160210617366591062.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "explicit"
                            }
                        },
                        {
                            "id": "1616728074",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1616728074",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 9,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 208119,
                                "isrc": "USUM72203649",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Charles Hinshaw Jr, Dijon McFarlane, Ella Mai Howell & Wolftyla",
                                "url": "https://music.apple.com/us/album/hide/1616728060?i=1616728074",
                                "playParams": {
                                    "id": "1616728074",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Hide",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/3f/f2/50/3ff25066-b511-e1f9-a035-7bc2f554117a/mzaf_5200904665505669763.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1616728075",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1616728075",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 10,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 213885,
                                "isrc": "USUM72203652",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Cam Griffin, Dijon McFarlane, Ella Mai Howell, Jason Pounds & Varren Wade",
                                "url": "https://music.apple.com/us/album/power-of-a-woman/1616728060?i=1616728075",
                                "playParams": {
                                    "id": "1616728075",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Power Of A Woman",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/4c/2e/49/4c2e49d8-4cbe-7fb1-1d06-43e601b096a8/mzaf_1661246820128533834.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1616728080",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1616728080",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 11,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 233794,
                                "isrc": "USUM72203640",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Cameron Joseph, David Brown, Ella Mai Howell, Matthew Samuels, Michael Samuels Jr., Mike McGregor & Peter Iskander",
                                "url": "https://music.apple.com/us/album/a-mess-feat-lucky-daye/1616728060?i=1616728080",
                                "playParams": {
                                    "id": "1616728080",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "A Mess (feat. Lucky Daye)",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/d4/65/93/d46593a6-4b74-d40a-a5c9-1ff0e836e5d4/mzaf_15047800783622526169.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "explicit"
                            }
                        },
                        {
                            "id": "1616728297",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1616728297",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 12,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 199909,
                                "isrc": "USUM72203648",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Chloe George, Ella Mai Howell, Jorgen Odegard & Stephanie Nicole Jones",
                                "url": "https://music.apple.com/us/album/feels-like/1616728060?i=1616728297",
                                "playParams": {
                                    "id": "1616728297",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Feels Like",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/f6/4d/74/f64d7407-86f1-d037-6b87-014128226145/mzaf_12176941177166656131.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "explicit"
                            }
                        },
                        {
                            "id": "1616728300",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1616728300",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 13,
                                "releaseDate": "2022-04-02",
                                "durationInMillis": 209136,
                                "isrc": "USUM72203641",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Ella Mai Howell, Varren Wade, Harmony Samuels & Edgar Etienne",
                                "url": "https://music.apple.com/us/album/leave-you-alone/1616728060?i=1616728300",
                                "playParams": {
                                    "id": "1616728300",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Leave You Alone",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/4e/99/03/4e9903bc-c099-2b91-f725-5f4034930e55/mzaf_12018132630264518586.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "explicit"
                            }
                        },
                        {
                            "id": "1616728301",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1616728301",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 14,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 234613,
                                "isrc": "USUM72203651",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Charles Hinshaw Jr, Dernst Emile II, Ella Mai Howell & Mary J. Blige",
                                "url": "https://music.apple.com/us/album/sink-or-swim/1616728060?i=1616728301",
                                "playParams": {
                                    "id": "1616728301",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Sink or Swim",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/85/63/1d/85631d29-7bc9-5815-5f32-b8fa02789d23/mzaf_2125550395281668690.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "explicit"
                            }
                        },
                        {
                            "id": "1616728302",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1616728302",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 15,
                                "releaseDate": "2022-05-06",
                                "durationInMillis": 214882,
                                "isrc": "USUM72203639",
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "0b1b18",
                                    "textColor1": "fc977a",
                                    "textColor2": "ef5429",
                                    "textColor3": "cc7e66",
                                    "textColor4": "c14925"
                                },
                                "composerName": "Ella Mai Howell, Jahaan Akil Sweet & Varren Wade",
                                "url": "https://music.apple.com/us/album/fading-out/1616728060?i=1616728302",
                                "playParams": {
                                    "id": "1616728302",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "hasLyrics": true,
                                "isAppleDigitalMaster": true,
                                "name": "Fading Out",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/1d/23/8f/1d238f3b-f1d0-ef0a-aec6-a1cfda070e6c/mzaf_16442520982162034651.plus.aac.p.m4a"
                                    }
                                ],
                                "artistName": "Ella Mai",
                                "contentRating": "explicit"
                            }
                        }
                    ]
                },
                "artists": {
                    "href": "/v1/catalog/us/albums/1616728060/artists",
                    "data": [
                        {
                            "id": "1160482144",
                            "type": "artists",
                            "href": "/v1/catalog/us/artists/1160482144"
                        }
                    ]
                }
            }
        }
    ],
    "meta": {
        "filters": {
            "upc": {
                "0602445868162": [
                    {
                        "id": "1616723164",
                        "type": "albums",
                        "href": "/v1/catalog/us/albums/1616723164"
                    },
                    {
                        "id": "1620500261",
                        "type": "albums",
                        "href": "/v1/catalog/us/albums/1620500261"
                    },
                    {
                        "id": "1616728060",
                        "type": "albums",
                        "href": "/v1/catalog/us/albums/1616728060"
                    }
                ]
            }
        }
    }
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/albums`

## Parameters

- `extend` ([string]): A list of attribute extensions to apply to resources in the response.
- `filter[upc]` ([string]) *(required)*: A filter to apply to the request.
- `include` ([string]): A list of relationship names to include for resources in the response.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.

## See Also

- [object Albums](albums.md)
  A resource object that represents an album.
- [object AlbumsResponse](albumsresponse.md)
  The response to an albums request.
- [Get a Catalog Album](get-a-catalog-album.md)
  Fetch an album by using its identifier.
- [Get a Catalog Album's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-4hthr.md)
  Fetch an album’s relationship by using its identifier.
- [Get a Catalog Album’s Relationship View Directly by Name](fetch-a-view-on-this-resource-by-name-2we6l.md)
  Fetch related resources for a single album’s relationship view.
- [Get Multiple Catalog Albums](get-multiple-catalog-albums.md)
  Fetch one or more albums by using their identifiers.
- [Get Equivalent Catalog Albums by ID](get-equivalent-ids-for-the-albums-8aky3.md)
  Fetch the equivalent, available content in the storefront for the provided albums’ identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-catalog-albums-by-upc)*