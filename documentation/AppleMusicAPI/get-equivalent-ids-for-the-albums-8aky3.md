# Get Equivalent Catalog Albums by ID

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch the equivalent, available content in the storefront for the provided albums’ identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/ly/albums?filter[equivalents]=1616728060
```

**Response**:

```json
{
    "data": [
        {
            "id": "1620500261",
            "type": "albums",
            "href": "/v1/catalog/ly/albums/1620500261",
            "attributes": {
                "copyright": "A 10 Summers/Interscope Records Release; ℗ 2022 10 Summers Records, LLC",
                "genreNames": [
                    "R&B/Soul",
                    "Music"
                ],
                "releaseDate": "2022-05-06",
                "isMasteredForItunes": true,
                "upc": "00602445868162",
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
                "url": "https://music.apple.com/ly/album/heart-on-my-sleeve/1620500261",
                "playParams": {
                    "id": "1620500261",
                    "kind": "album"
                },
                "recordLabel": "10 Summers/Interscope Records",
                "trackCount": 15,
                "isCompilation": false,
                "isSingle": false,
                "name": "Heart On My Sleeve",
                "artistName": "Ella Mai",
                "contentRating": "clean",
                "isComplete": false
            },
            "relationships": {
                "artists": {
                    "href": "/v1/catalog/ly/albums/1620500261/artists",
                    "data": [
                        {
                            "id": "1160482144",
                            "type": "artists",
                            "href": "/v1/catalog/ly/artists/1160482144"
                        }
                    ]
                },
                "tracks": {
                    "href": "/v1/catalog/ly/albums/1620500261/tracks",
                    "data": [
                        {
                            "id": "1620500269",
                            "type": "songs",
                            "href": "/v1/catalog/ly/songs/1620500269",
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
                                "playParams": {
                                    "id": "1620500269",
                                    "kind": "song"
                                },
                                "url": "https://music.apple.com/ly/album/trying/1620500261?i=1620500269",
                                "discNumber": 1,
                                "isAppleDigitalMaster": true,
                                "hasLyrics": true,
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
                            "href": "/v1/catalog/ly/songs/1620500271",
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
                                "playParams": {
                                    "id": "1620500271",
                                    "kind": "song"
                                },
                                "url": "https://music.apple.com/ly/album/not-another-love-song/1620500261?i=1620500271",
                                "discNumber": 1,
                                "isAppleDigitalMaster": true,
                                "hasLyrics": true,
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
                            "href": "/v1/catalog/ly/songs/1620500272",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 3,
                                "durationInMillis": 245650,
                                "releaseDate": "2022-05-06",
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
                                "url": "https://music.apple.com/ly/album/didnt-say-feat-latto/1620500261?i=1620500272",
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
                            "href": "/v1/catalog/ly/songs/1620500277",
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
                                "playParams": {
                                    "id": "1620500277",
                                    "kind": "song"
                                },
                                "url": "https://music.apple.com/ly/album/break-my-heart/1620500261?i=1620500277",
                                "discNumber": 1,
                                "isAppleDigitalMaster": true,
                                "hasLyrics": true,
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
                            "href": "/v1/catalog/ly/songs/1620500280",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 5,
                                "durationInMillis": 261811,
                                "releaseDate": "2022-05-06",
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
                                "playParams": {
                                    "id": "1620500280",
                                    "kind": "song"
                                },
                                "url": "https://music.apple.com/ly/album/fallen-angel/1620500261?i=1620500280",
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
                            "href": "/v1/catalog/ly/songs/1620500284",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 6,
                                "durationInMillis": 218317,
                                "releaseDate": "2022-05-06",
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
                                "playParams": {
                                    "id": "1620500284",
                                    "kind": "song"
                                },
                                "url": "https://music.apple.com/ly/album/how-feat-roddy-ricch/1620500261?i=1620500284",
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
                            "href": "/v1/catalog/ly/songs/1620500648",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 7,
                                "durationInMillis": 198795,
                                "releaseDate": "2022-05-06",
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
                                "playParams": {
                                    "id": "1620500648",
                                    "kind": "song"
                                },
                                "url": "https://music.apple.com/ly/album/pieces/1620500261?i=1620500648",
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
                            "href": "/v1/catalog/ly/songs/1620500652",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 8,
                                "durationInMillis": 197517,
                                "releaseDate": "2022-01-28",
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
                                "url": "https://music.apple.com/ly/album/dfmu/1620500261?i=1620500652",
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
                            "href": "/v1/catalog/ly/songs/1620500653",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 9,
                                "durationInMillis": 208119,
                                "releaseDate": "2022-05-06",
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
                                "url": "https://music.apple.com/ly/album/hide/1620500261?i=1620500653",
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
                            "href": "/v1/catalog/ly/songs/1620500657",
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
                                "playParams": {
                                    "id": "1620500657",
                                    "kind": "song"
                                },
                                "url": "https://music.apple.com/ly/album/power-of-a-woman/1620500261?i=1620500657",
                                "discNumber": 1,
                                "isAppleDigitalMaster": true,
                                "hasLyrics": true,
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
                            "href": "/v1/catalog/ly/songs/1620500663",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 11,
                                "durationInMillis": 233794,
                                "releaseDate": "2022-05-06",
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
                                "url": "https://music.apple.com/ly/album/a-mess-feat-lucky-daye/1620500261?i=1620500663",
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
                            "href": "/v1/catalog/ly/songs/1620500674",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 12,
                                "durationInMillis": 199909,
                                "releaseDate": "2022-05-06",
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
                                "url": "https://music.apple.com/ly/album/feels-like/1620500261?i=1620500674",
                                "playParams": {
                                    "id": "1620500674",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "isAppleDigitalMaster": true,
                                "hasLyrics": false,
                                "name": "Feels Like",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/14/e2/ab/14e2ab3d-fd88-ec13-681b-29cf46b21414/mzaf_8155293122708882028.plus.aac.p.m4a"
                                    }
                                ],
                                "contentRating": "clean",
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1620500770",
                            "type": "songs",
                            "href": "/v1/catalog/ly/songs/1620500770",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 13,
                                "durationInMillis": 209136,
                                "releaseDate": "2022-04-02",
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
                                "url": "https://music.apple.com/ly/album/leave-you-alone/1620500261?i=1620500770",
                                "playParams": {
                                    "id": "1620500770",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "isAppleDigitalMaster": true,
                                "hasLyrics": true,
                                "name": "Leave You Alone",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/3b/bd/95/3bbd9588-7359-3764-c30d-e4ee9abf5b07/mzaf_16785343148441517892.plus.aac.p.m4a"
                                    }
                                ],
                                "contentRating": "clean",
                                "artistName": "Ella Mai"
                            }
                        },
                        {
                            "id": "1620500773",
                            "type": "songs",
                            "href": "/v1/catalog/ly/songs/1620500773",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 14,
                                "durationInMillis": 234613,
                                "releaseDate": "2022-05-06",
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
                                "playParams": {
                                    "id": "1620500773",
                                    "kind": "song"
                                },
                                "url": "https://music.apple.com/ly/album/sink-or-swim/1620500261?i=1620500773",
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
                            "href": "/v1/catalog/ly/songs/1620500780",
                            "attributes": {
                                "albumName": "Heart On My Sleeve",
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "trackNumber": 15,
                                "durationInMillis": 214882,
                                "releaseDate": "2022-05-06",
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
                                "url": "https://music.apple.com/ly/album/fading-out/1620500261?i=1620500780",
                                "playParams": {
                                    "id": "1620500780",
                                    "kind": "song"
                                },
                                "discNumber": 1,
                                "isAppleDigitalMaster": true,
                                "hasLyrics": true,
                                "name": "Fading Out",
                                "previews": [
                                    {
                                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/e2/d8/d5/e2d8d53b-3dd1-a1d5-0c71-aa6431ba160d/mzaf_14489967022318346201.plus.aac.p.m4a"
                                    }
                                ],
                                "contentRating": "clean",
                                "artistName": "Ella Mai"
                            }
                        }
                    ]
                }
            }
        }
    ],
    "meta": {
        "filters": {
            "equivalents": {
                "1616728060": [
                    {
                        "id": "1620500261",
                        "type": "albums",
                        "href": "/v1/catalog/ly/albums/1620500261"
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

- `filter[equivalents]` ([string]) *(required)*: A filter to apply to the request.
- `include` ([string]): A list of relationship names to include for resources in the response.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `restrict` ([string]): A set of restrictions (for example, to restrict explicit content).
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

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
- [Get Multiple Catalog Albums by UPC](get-multiple-catalog-albums-by-upc.md)
  Fetch one or more albums by using their UPC values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-equivalent-ids-for-the-albums-8aky3)*