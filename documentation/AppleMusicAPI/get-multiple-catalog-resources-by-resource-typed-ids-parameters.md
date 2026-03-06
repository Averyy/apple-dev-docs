# Get Multiple Catalog Resources Using Resource-Typed ID Parameters

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more catalog resources by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us?ids[songs]=1564531202&ids[albums]=1577502911
```

**Response**:

```json
{
    "data": [
        {
            "id": "1577502911",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1577502911",
            "attributes": {
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/2f/50/32/2f5032ef-2481-019a-0310-70942dace8c9/886449464326.jpg/{w}x{h}bb.jpg",
                    "bgColor": "e1b73e",
                    "textColor1": "0d0d0c",
                    "textColor2": "232323",
                    "textColor3": "382f16",
                    "textColor4": "494128"
                },
                "artistName": "Leon Bridges",
                "isSingle": false,
                "url": "https: //music.apple.com/us/album/gold-diggers-sound-apple-music-edition/1577502911",
                "isComplete": false,
                "genreNames": [
                    "R&B/Soul",
                    "Music"
                ],
                "trackCount": 12,
                "isMasteredForItunes": false,
                "releaseDate": "2021-07-23",
                "name": "Gold-Diggers Sound (Apple Music Edition)",
                "recordLabel": "Columbia",
                "upc": "886449464326",
                "copyright": "℗ 2021 LisaSawyer63, Inc. under license to Columbia Records, a Division of Sony Music Entertainment",
                "playParams": {
                    "id": "1577502911",
                    "kind": "album"
                },
                "editorialNotes": {
                    "standard": "When Leon Bridges set out to make his third album, he wanted it to be different this time around. "We felt like the only way to unlock a unique sound was to create this immersive experience and find a place that was aesthetically inspiring," he tells Apple Music. He landed on Gold-Diggers in East Hollywood, a three-in-one bar, hotel, and recording studio that allowed the Texas-bred singer to tap into his sound the way he hears it in his head, free from the expectations of others. "It definitely felt the most liberating to me," he says of the process. "I was just able to be myself and let go of any inhibitions and create without any boundaries." <br />\nThe songs born of those sessions—produced by Ricky Reed and Nate Mercereau—became <i>Gold-Diggers Sound</i> and some of Bridges’ most refined work. He rose to fame through his ’50s and ’60s soul stylings, but the R&B contained within this album situates its nostalgia in a more modern context, bridging ’80s and ’90s R&B with lush, jazz-inspired live instrumentation...",
                    "short": "The singer-songwriter’s new album has arrived, along with a short film."
                },
                "isCompilation": false
            },
            "relationships": {
                "artists": {
                    "href": "/v1/catalog/us/albums/1577502911/artists",
                    "data": [
                        {
                            "id": "961252454",
                            "type": "artists",
                            "href": "/v1/catalog/us/artists/961252454"
                        }
                    ]
                },
                "tracks": {
                    "href": "/v1/catalog/us/albums/1577502911/tracks",
                    "data": [
                        {
                            "id": "1577502916",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1577502916",
                            "attributes": {
                                "previews": [
                                    {
                                        "url": "https: //audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/4b/39/8e/4b398e81-bc8f-9e95-0dd6-8b6653fccd17/mzaf_5139253780411774906.plus.aac.p.m4a"
                                    }
                                ],
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/2f/50/32/2f5032ef-2481-019a-0310-70942dace8c9/886449464326.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "e1b73e",
                                    "textColor1": "0d0d0c",
                                    "textColor2": "232323",
                                    "textColor3": "382f16",
                                    "textColor4": "494128"
                                },
                                "artistName": "Leon Bridges & Robert Glasper",
                                "url": "https: //music.apple.com/us/album/born-again/1577502911?i=1577502916",
                                "discNumber": 1,
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "durationInMillis": 223248,
                                "releaseDate": "2021-07-23",
                                "name": "Born Again",
                                "isrc": "USSM12101509",
                                "hasLyrics": true,
                                "albumName": "Gold-Diggers Sound (Apple Music Edition)",
                                "playParams": {
                                    "id": "1577502916",
                                    "kind": "song"
                                },
                                "trackNumber": 1,
                                "composerName": "Robert Glasper, Todd Bridges, Eric Frederic, Daniel Stanfill & Lemar Guillary"
                            }
                        },
                        {
                            "id": "1577502919",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1577502919",
                            "attributes": {
                                "previews": [
                                    {
                                        "url": "https: //audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/69/3f/fd/693ffd2c-25b8-f43a-363d-7325fcaedf6e/mzaf_11844597036568859006.plus.aac.p.m4a"
                                    }
                                ],
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/2f/50/32/2f5032ef-2481-019a-0310-70942dace8c9/886449464326.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "e1b73e",
                                    "textColor1": "0d0d0c",
                                    "textColor2": "232323",
                                    "textColor3": "382f16",
                                    "textColor4": "494128"
                                },
                                "artistName": "Leon Bridges",
                                "url": "https: //music.apple.com/us/album/motorbike/1577502911?i=1577502919",
                                "discNumber": 1,
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "durationInMillis": 188617,
                                "releaseDate": "2021-05-14",
                                "name": "Motorbike",
                                "isrc": "USSM12101510",
                                "hasLyrics": true,
                                "albumName": "Gold-Diggers Sound (Apple Music Edition)",
                                "playParams": {
                                    "id": "1577502919",
                                    "kind": "song"
                                },
                                "trackNumber": 2,
                                "composerName": "Todd Bridges, Paris Strother, Eric Frederic, Nate Mercereau & Dan Wilson"
                            }
                        },
                        {
                            "id": "1577502922",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1577502922",
                            "attributes": {
                                "previews": [
                                    {
                                        "url": "https: //audio-ssl.itunes.apple.com/itunes-assets/AudioPreview125/v4/2b/7a/bf/2b7abf62-1e0d-f672-8bbf-97b62137a38c/mzaf_1605009830699058501.plus.aac.p.m4a"
                                    }
                                ],
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/2f/50/32/2f5032ef-2481-019a-0310-70942dace8c9/886449464326.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "e1b73e",
                                    "textColor1": "0d0d0c",
                                    "textColor2": "232323",
                                    "textColor3": "382f16",
                                    "textColor4": "494128"
                                },
                                "artistName": "Leon Bridges",
                                "url": "https: //music.apple.com/us/album/steam/1577502911?i=1577502922",
                                "discNumber": 1,
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "durationInMillis": 203091,
                                "releaseDate": "2021-07-23",
                                "name": "Steam",
                                "isrc": "USSM12101511",
                                "hasLyrics": true,
                                "albumName": "Gold-Diggers Sound (Apple Music Edition)",
                                "playParams": {
                                    "id": "1577502922",
                                    "kind": "song"
                                },
                                "trackNumber": 3,
                                "composerName": "Todd Bridges, Nate Mercereau, Eric Frederic, Antoine Katz, Jordan Blackmon, Justin Tranter, Trevor Lawrence & Atia Boggs"
                            }
                        },
                        {
                            "id": "1577502928",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1577502928",
                            "attributes": {
                                "previews": [
                                    {
                                        "url": "https: //audio-ssl.itunes.apple.com/itunes-assets/AudioPreview125/v4/f9/3b/3a/f93b3aba-18bd-476b-d6c5-698d309a958e/mzaf_17811488500143850689.plus.aac.p.m4a"
                                    }
                                ],
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/2f/50/32/2f5032ef-2481-019a-0310-70942dace8c9/886449464326.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "e1b73e",
                                    "textColor1": "0d0d0c",
                                    "textColor2": "232323",
                                    "textColor3": "382f16",
                                    "textColor4": "494128"
                                },
                                "artistName": "Leon Bridges",
                                "url": "https: //music.apple.com/us/album/why-dont-you-touch-me/1577502911?i=1577502928",
                                "discNumber": 1,
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "durationInMillis": 197746,
                                "releaseDate": "2021-06-18",
                                "name": "Why Don’t You Touch Me",
                                "isrc": "USSM12101512",
                                "hasLyrics": true,
                                "albumName": "Gold-Diggers Sound (Apple Music Edition)",
                                "playParams": {
                                    "id": "1577502928",
                                    "kind": "song"
                                },
                                "trackNumber": 4,
                                "composerName": "Todd Bridges, Kim \"Kaydence\" Krysiuk, Eric Frederic, Jeff Baranowski & Luke Milano"
                            }
                        },
                        {
                            "id": "1577502935",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1577502935",
                            "attributes": {
                                "previews": [
                                    {
                                        "url": "https: //audio-ssl.itunes.apple.com/itunes-assets/AudioPreview125/v4/16/45/6b/16456bd4-da84-0f9d-ee53-27bdd31e31f4/mzaf_8973081954505739791.plus.aac.p.m4a"
                                    }
                                ],
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/2f/50/32/2f5032ef-2481-019a-0310-70942dace8c9/886449464326.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "e1b73e",
                                    "textColor1": "0d0d0c",
                                    "textColor2": "232323",
                                    "textColor3": "382f16",
                                    "textColor4": "494128"
                                },
                                "artistName": "Leon Bridges",
                                "url": "https: //music.apple.com/us/album/magnolias/1577502911?i=1577502935",
                                "discNumber": 1,
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "durationInMillis": 202676,
                                "releaseDate": "2021-07-23",
                                "name": "Magnolias",
                                "isrc": "USSM12101513",
                                "hasLyrics": true,
                                "albumName": "Gold-Diggers Sound (Apple Music Edition)",
                                "playParams": {
                                    "id": "1577502935",
                                    "kind": "song"
                                },
                                "trackNumber": 5,
                                "composerName": "Todd Bridges, Nate Mercereau, Eric Frederic, Steve Wyreman, Steven Cheung, Jerome Castille, Michael Neil & Atia Boggs"
                            }
                        },
                        {
                            "id": "1577503208",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1577503208",
                            "attributes": {
                                "previews": [
                                    {
                                        "url": "https: //audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/a4/8d/9c/a48d9c76-f551-c132-4f86-3dbe577596ee/mzaf_13723421321501701849.plus.aac.p.m4a"
                                    }
                                ],
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/2f/50/32/2f5032ef-2481-019a-0310-70942dace8c9/886449464326.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "e1b73e",
                                    "textColor1": "0d0d0c",
                                    "textColor2": "232323",
                                    "textColor3": "382f16",
                                    "textColor4": "494128"
                                },
                                "artistName": "Leon Bridges",
                                "url": "https: //music.apple.com/us/album/gold-diggers-juniors-fanfare/1577502911?i=1577503208",
                                "discNumber": 1,
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "durationInMillis": 41945,
                                "releaseDate": "2021-07-23",
                                "name": "Gold-Diggers (Junior’s Fanfare)",
                                "isrc": "USSM12101514",
                                "hasLyrics": false,
                                "albumName": "Gold-Diggers Sound (Apple Music Edition)",
                                "playParams": {
                                    "id": "1577503208",
                                    "kind": "song"
                                },
                                "trackNumber": 6,
                                "composerName": "Lemar Guillary"
                            }
                        },
                        {
                            "id": "1577503214",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1577503214",
                            "attributes": {
                                "previews": [
                                    {
                                        "url": "https: //audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/e5/74/ea/e574ea35-5d6d-56d0-73b0-abe24a2fcf00/mzaf_16881033463858329452.plus.aac.p.m4a"
                                    }
                                ],
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/2f/50/32/2f5032ef-2481-019a-0310-70942dace8c9/886449464326.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "e1b73e",
                                    "textColor1": "0d0d0c",
                                    "textColor2": "232323",
                                    "textColor3": "382f16",
                                    "textColor4": "494128"
                                },
                                "artistName": "Leon Bridges",
                                "url": "https: //music.apple.com/us/album/details/1577502911?i=1577503214",
                                "discNumber": 1,
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "durationInMillis": 196510,
                                "releaseDate": "2021-07-23",
                                "name": "Details",
                                "isrc": "USSM12101515",
                                "hasLyrics": true,
                                "albumName": "Gold-Diggers Sound (Apple Music Edition)",
                                "playParams": {
                                    "id": "1577503214",
                                    "kind": "song"
                                },
                                "trackNumber": 7,
                                "composerName": "Todd Bridges, Nate Mercereau, Eric Frederic & Amber Strother"
                            }
                        },
                        {
                            "id": "1577503219",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1577503219",
                            "attributes": {
                                "previews": [
                                    {
                                        "url": "https: //audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/cd/78/e3/cd78e3ac-6853-b9e6-ef1f-f317199188da/mzaf_1275235105385100189.plus.aac.p.m4a"
                                    }
                                ],
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/2f/50/32/2f5032ef-2481-019a-0310-70942dace8c9/886449464326.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "e1b73e",
                                    "textColor1": "0d0d0c",
                                    "textColor2": "232323",
                                    "textColor3": "382f16",
                                    "textColor4": "494128"
                                },
                                "artistName": "Leon Bridges",
                                "url": "https: //music.apple.com/us/album/sho-nuff/1577502911?i=1577503219",
                                "discNumber": 1,
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "durationInMillis": 187500,
                                "releaseDate": "2021-07-23",
                                "name": "Sho Nuff",
                                "isrc": "USSM12101516",
                                "hasLyrics": true,
                                "albumName": "Gold-Diggers Sound (Apple Music Edition)",
                                "playParams": {
                                    "id": "1577503219",
                                    "kind": "song"
                                },
                                "trackNumber": 8,
                                "composerName": "Todd Bridges, Steve Wyreman, Eric Frederic, Nate Mercereau, Atia Boggs, Ian Fitchuk, Daniel Tashian, Austin Jenkins & Jerome Castille"
                            }
                        },
                        {
                            "id": "1577503222",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1577503222",
                            "attributes": {
                                "previews": [
                                    {
                                        "url": "https: //audio-ssl.itunes.apple.com/itunes-assets/AudioPreview125/v4/3b/b9/6e/3bb96ea9-1f60-a38f-fb8d-8882bb4b75e2/mzaf_14349022360643129259.plus.aac.p.m4a"
                                    }
                                ],
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/2f/50/32/2f5032ef-2481-019a-0310-70942dace8c9/886449464326.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "e1b73e",
                                    "textColor1": "0d0d0c",
                                    "textColor2": "232323",
                                    "textColor3": "382f16",
                                    "textColor4": "494128"
                                },
                                "artistName": "Leon Bridges",
                                "url": "https: //music.apple.com/us/album/sweeter-feat-terrace-martin/1577502911?i=1577503222",
                                "discNumber": 1,
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "durationInMillis": 168465,
                                "releaseDate": "2021-05-14",
                                "name": "Sweeter (feat. Terrace Martin)",
                                "isrc": "USSM12003777",
                                "hasLyrics": true,
                                "albumName": "Gold-Diggers Sound (Apple Music Edition)",
                                "playParams": {
                                    "id": "1577503222",
                                    "kind": "song"
                                },
                                "trackNumber": 9,
                                "composerName": "Terrace Martin, Todd Bridges, Nate Mercereau, Eric Frederic, Dan Wilson, Rome Castille, Jerome Castille, Zach Cooper & Vic Dimotsis"
                            }
                        },
                        {
                            "id": "1577503225",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1577503225",
                            "attributes": {
                                "previews": [
                                    {
                                        "url": "https: //audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/fd/d1/2d/fdd12d48-ef66-dcc3-275e-32761bdc31fa/mzaf_2727147849979860138.plus.aac.p.m4a"
                                    }
                                ],
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/2f/50/32/2f5032ef-2481-019a-0310-70942dace8c9/886449464326.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "e1b73e",
                                    "textColor1": "0d0d0c",
                                    "textColor2": "232323",
                                    "textColor3": "382f16",
                                    "textColor4": "494128"
                                },
                                "artistName": "Leon Bridges",
                                "url": "https: //music.apple.com/us/album/dont-worry-feat-ink/1577502911?i=1577503225",
                                "discNumber": 1,
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "durationInMillis": 401075,
                                "releaseDate": "2021-07-23",
                                "name": "Don’t Worry (feat. Ink)",
                                "isrc": "USSM12101517",
                                "hasLyrics": true,
                                "albumName": "Gold-Diggers Sound (Apple Music Edition)",
                                "playParams": {
                                    "id": "1577503225",
                                    "kind": "song"
                                },
                                "trackNumber": 10,
                                "composerName": "Todd Bridges, Steve Wyreman, Eric Frederic, Nate Mercereau, Atia Boggs, Josh Crumbly, Amber Strother & Jerome Castille"
                            }
                        },
                        {
                            "id": "1577503229",
                            "type": "songs",
                            "href": "/v1/catalog/us/songs/1577503229",
                            "attributes": {
                                "previews": [
                                    {
                                        "url": "https: //audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/c9/f5/b2/c9f5b2de-bb99-c208-ac7e-e8b8821d850b/mzaf_10634358777372585227.plus.aac.p.m4a"
                                    }
                                ],
                                "artwork": {
                                    "width": 3000,
                                    "height": 3000,
                                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music125/v4/2f/50/32/2f5032ef-2481-019a-0310-70942dace8c9/886449464326.jpg/{w}x{h}bb.jpg",
                                    "bgColor": "e1b73e",
                                    "textColor1": "0d0d0c",
                                    "textColor2": "232323",
                                    "textColor3": "382f16",
                                    "textColor4": "494128"
                                },
                                "artistName": "Leon Bridges",
                                "url": "https: //music.apple.com/us/album/blue-mesas/1577502911?i=1577503229",
                                "discNumber": 1,
                                "genreNames": [
                                    "R&B/Soul",
                                    "Music"
                                ],
                                "durationInMillis": 195682,
                                "releaseDate": "2021-07-23",
                                "name": "Blue Mesas",
                                "isrc": "USSM12101518",
                                "hasLyrics": true,
                                "albumName": "Gold-Diggers Sound (Apple Music Edition)",
                                "playParams": {
                                    "id": "1577503229",
                                    "kind": "song"
                                },
                                "trackNumber": 11,
                                "composerName": "Todd Bridges, Eric Frederic, Daniel Stanfill, Harold Lilly & Olivia Salas"
                            }
                        },
                        {
                            "id": "1577503231",
                            "type": "music-videos",
                            "href": "/v1/catalog/us/music-videos/1577503231",
                            "attributes": {
                                "previews": [
                                    {
                                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video125/v4/fa/38/69/fa386910-c911-1bb7-dda2-91099d95b4ad/mzvf_15088007543490493136.720w.h264lc.U.p.m4v",
                                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1577503231&id=313573229&l=en&aec=HD",
                                        "artwork": {
                                            "width": 3840,
                                            "height": 2160,
                                            "url": "https: //is5-ssl.mzstatic.com/image/thumb/Video125/v4/f5/fb/af/f5fbafce-7139-89cc-7328-929cd363d1f9/Jobbacf1bd3-0b33-4c37-8272-0367b63ca55a-118200244-PreviewImage_preview_image_287000_video_sdr-Time1627466696100.png/{w}x{h}bb.jpg",
                                            "bgColor": "000000",
                                            "textColor1": "f2f2f2",
                                            "textColor2": "e5e5e5",
                                            "textColor3": "c1c1c1",
                                            "textColor4": "b7b7b7"
                                        }
                                    }
                                ],
                                "artwork": {
                                    "width": 3840,
                                    "height": 2160,
                                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Video115/v4/b4/64/a1/b464a19e-4fcb-dd48-54fe-013307c05f06/dj.njuuqwhg.jpg/{w}x{h}mv.jpg",
                                    "bgColor": "0a0a0a",
                                    "textColor1": "f1f1f1",
                                    "textColor2": "d9d9d9",
                                    "textColor3": "c3c3c3",
                                    "textColor4": "b0b0b0"
                                },
                                "artistName": "Leon Bridges",
                                "url": "https: //music.apple.com/us/music-video/for-it-shall-perish-and-never-leave-us-again/1577503231",
                                "genreNames": [
                                    "R&B/Soul"
                                ],
                                "has4K": true,
                                "durationInMillis": 1196755,
                                "releaseDate": "2021-07-23",
                                "name": "For It Shall Perish And Never Leave us Again",
                                "isrc": "USSM22101764",
                                "albumName": "Gold-Diggers Sound (Apple Music Edition)",
                                "playParams": {
                                    "id": "1577503231",
                                    "kind": "musicVideo"
                                },
                                "trackNumber": 12,
                                "hasHDR": false
                            }
                        }
                    ]
                }
            }
        },
        {
            "id": "1564531202",
            "type": "songs",
            "href": "/v1/catalog/us/songs/1564531202",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/d6/6f/58/d66f58c4-50ad-4978-971c-b19c022a440b/mzaf_3392528453380582564.plus.aac.p.m4a"
                    }
                ],
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music115/v4/2d/f3/c9/2df3c9fd-e0eb-257c-c035-b04f05a66580/21UMGIM36691.rgb.jpg/{w}x{h}bb.jpg",
                    "bgColor": "6d4d3a",
                    "textColor1": "fcfbf9",
                    "textColor2": "ead3b5",
                    "textColor3": "e0d8d3",
                    "textColor4": "d1b89c"
                },
                "artistName": "Billie Eilish",
                "url": "https: //music.apple.com/us/album/happier-than-ever/1564530719?i=1564531202",
                "discNumber": 1,
                "genreNames": [
                    "Alternative",
                    "Music"
                ],
                "durationInMillis": 298899,
                "releaseDate": "2021-07-30",
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
            },
            "relationships": {
                "albums": {
                    "href": "/v1/catalog/us/songs/1564531202/albums",
                    "data": [
                        {
                            "id": "1564530719",
                            "type": "albums",
                            "href": "/v1/catalog/us/albums/1564530719"
                        }
                    ]
                },
                "artists": {
                    "href": "/v1/catalog/us/songs/1564531202/artists",
                    "data": [
                        {
                            "id": "1065981054",
                            "type": "artists",
                            "href": "/v1/catalog/us/artists/1065981054"
                        }
                    ]
                }
            }
        }
    ]
}

```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}`

## Parameters

- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.
- `ids[stations]` ([string]): The unique identifiers for the stations.
- `ids[station-genres]` ([string]): The unique identifiers for the station genres.
- `ids[songs]` ([string]): The unique identifiers for the songs.
- `ids[record-labels]` ([string]): The unique identifiers for the record labels.
- `ids[ratings]` ([string]): The unique identifiers for the ratings.
- `ids[playlists]` ([string]): The unique identifiers for the playlists.
- `ids[music-videos]` ([string]): The unique identifiers for the music videos.
- `ids[genres]` ([string]): The unique identifiers for the genres.
- `ids[curators]` ([string]): The unique identifiers for the curators.
- `ids[artists]` ([string]): The unique identifiers for the artists.
- `ids[apple-curators]` ([string]): The unique identifiers for the Apple Music curators.
- `ids[albums]` ([string]): The unique identifiers for the albums.
- `ids[activities]` ([string]): The unique identifiers for the activities.

## See Also

- [object Resource](resource.md)
  A resource—such as an album, song, or playlist.
- [Get Multiple Library Resources Using Resource-Typed ID Parameters](get-multiple-library-resources-by-resource-typed-ids-parameters.md)
  Fetch one or more library resources by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-catalog-resources-by-resource-typed-ids-parameters)*