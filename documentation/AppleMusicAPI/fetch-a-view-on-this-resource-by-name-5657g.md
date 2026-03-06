# Get a Catalog Music Video’s Relationship View Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch related resources for a single music video’s relationship view.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/music-videos/1553279848/view/more-by-artist
```

**Response**:

```json
{
    "next": "/v1/catalog/us/music-videos/1553279848/view/more-by-artist?offset=15",
    "data": [
        {
            "id": "1534312182",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1534312182",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video114/v4/cd/e3/4d/cde34d6e-a191-d94e-f321-cfefee3661be/mzvf_17214298869418785195.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1534312182&id=168355308&l=en&aec=HD",
                        "artwork": {
                            "width": 1552,
                            "url": "https: //is1-ssl.mzstatic.com/image/thumb/Video114/v4/c3/48/e4/c348e4a3-1ed0-e0b4-3ffc-bd4b0cb05c07/Job80defef9-1ade-48f6-8374-4cf931e553d9-107635290-PreviewImage_preview_image_43000_video_sdr-Time1602218274065.png/{w}x{h}bb.jpeg",
                            "height": 1080,
                            "textColor3": "79a5bb",
                            "textColor2": "6fbcd2",
                            "textColor4": "5fa0b2",
                            "textColor1": "8fc3dd",
                            "bgColor": "213035",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 640,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Video114/v4/18/f2/fc/18f2fc67-dc55-3b61-fe4f-c384bf08c53b/GB1302000726.sca1.jpg/{w}x{h}mv.jpeg",
                    "height": 444,
                    "textColor3": "8daacf",
                    "textColor2": "71bae9",
                    "textColor4": "5d98be",
                    "textColor1": "aed2ff",
                    "bgColor": "0e0f13",
                    "hasP3": false
                },
                "artistName": "Dua Lipa",
                "url": "https: //music.apple.com/us/music-video/levitating-feat-dababy/1534312182",
                "genreNames": [
                    "Pop"
                ],
                "has4K": false,
                "durationInMillis": 231572,
                "releaseDate": "2020-10-02",
                "name": "Levitating (feat. DaBaby)",
                "isrc": "GB1302000726",
                "playParams": {
                    "id": "1534312182",
                    "kind": "musicVideo"
                },
                "hasHDR": false
            }
        },
        {
            "id": "1485874321",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1485874321",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video113/v4/b4/c9/35/b4c935f4-e369-9123-95cd-7a6f6e832ab0/mzvf_15588872542254245538.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1485874321&id=62715945&l=en&aec=HD",
                        "artwork": {
                            "width": 1920,
                            "url": "https: //is3-ssl.mzstatic.com/image/thumb/Video123/v4/3d/4e/44/3d4e4498-76a3-9205-7afc-eee287651534/Job89a3467f-aa4a-43fc-a773-c4fe1d7613b0-104426131-PreviewImage_preview_image_43000_video_sdr-Time1572892889041.png/{w}x{h}bb.jpeg",
                            "height": 804,
                            "textColor3": "a2a7a9",
                            "textColor2": "9ecbcb",
                            "textColor4": "7fa7ac",
                            "textColor1": "cacbc7",
                            "bgColor": "031833",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 640,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Video123/v4/89/28/f5/8928f5af-f4b0-5af6-d3b9-b0fbd9077e8a/GB1301901080.sca1.jpg/{w}x{h}mv.jpeg",
                    "height": 268,
                    "textColor3": "79aeb8",
                    "textColor2": "7dc8d6",
                    "textColor4": "65a4b6",
                    "textColor1": "97d5da",
                    "bgColor": "041533",
                    "hasP3": false
                },
                "artistName": "Dua Lipa",
                "url": "https: //music.apple.com/us/music-video/dont-start-now/1485874321",
                "genreNames": [
                    "Pop"
                ],
                "has4K": false,
                "durationInMillis": 181118,
                "releaseDate": "2019-11-01",
                "name": "Don’t Start Now",
                "isrc": "GB1301901080",
                "playParams": {
                    "id": "1485874321",
                    "kind": "musicVideo"
                },
                "hasHDR": false
            }
        },
        {
            "id": "1258705880",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1258705880",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video125/v4/02/28/01/022801d8-8e2b-b962-bf25-7f082df54a72/mzvf_5668012905540302285.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1258705880&id=53686535&l=en&aec=HD",
                        "artwork": {
                            "width": 1920,
                            "url": "https: //is2-ssl.mzstatic.com/image/thumb/Video125/v4/0b/65/32/0b6532e1-c8e1-24c8-39c7-19a425ad6119/Job83acace0-d40d-4614-b948-1de5899462ea-100149784-PreviewImage_preview_image_43000_video_sdr-Time1527547608043.png/{w}x{h}bb.jpeg",
                            "height": 1080,
                            "textColor3": "d8dbc6",
                            "textColor2": "e1eae6",
                            "textColor4": "c9cfc8",
                            "textColor1": "f4fae4",
                            "bgColor": "68604f",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 640,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Video118/v4/30/d4/7d/30d47dc5-af35-7938-02d1-799aa11ea0fc/GB1301700254.sca1.jpg/{w}x{h}mv.jpeg",
                    "height": 360,
                    "textColor3": "a7a597",
                    "textColor2": "cab9a1",
                    "textColor4": "a79986",
                    "textColor1": "cbc8b6",
                    "bgColor": "18191b",
                    "hasP3": false
                },
                "artistName": "Dua Lipa",
                "url": "https: //music.apple.com/us/music-video/new-rules/1258705880",
                "genreNames": [
                    "Pop"
                ],
                "has4K": false,
                "durationInMillis": 220607,
                "releaseDate": "2017-07-07",
                "name": "New Rules",
                "isrc": "GB1301700254",
                "playParams": {
                    "id": "1258705880",
                    "kind": "musicVideo"
                },
                "hasHDR": false
            }
        },
        {
            "id": "1504448799",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1504448799",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video113/v4/75/cb/cc/75cbcc37-16ab-2f0a-f10b-9e732677c735/mzvf_150498077082072007.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1504448799&id=65266143&l=en&aec=HD",
                        "artwork": {
                            "width": 1920,
                            "url": "https: //is3-ssl.mzstatic.com/image/thumb/Video113/v4/f8/b8/3f/f8b83fdf-69ba-f647-c33b-8cb9dbe4cdff/Jobae4e3594-bf71-4a90-815e-1da65a328945-106079657-PreviewImage_preview_image_43000_video_sdr-Time1585281754724.png/{w}x{h}bb.jpeg",
                            "height": 1080,
                            "textColor3": "a9b0a8",
                            "textColor2": "ced1c8",
                            "textColor4": "abaca6",
                            "textColor1": "cdd7ca",
                            "bgColor": "1b1621",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 640,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Video123/v4/1c/eb/38/1ceb38ed-0d5d-2649-a588-199525c474a5/GB1302000211.sca1.jpg/{w}x{h}mv.jpeg",
                    "height": 360,
                    "textColor3": "b6967d",
                    "textColor2": "d4b488",
                    "textColor4": "ab926f",
                    "textColor1": "e2b999",
                    "bgColor": "06090d",
                    "hasP3": false
                },
                "artistName": "Dua Lipa",
                "url": "https: //music.apple.com/us/music-video/break-my-heart/1504448799",
                "genreNames": [
                    "Pop"
                ],
                "has4K": false,
                "durationInMillis": 227880,
                "releaseDate": "2020-03-26",
                "name": "Break My Heart",
                "isrc": "GB1302000211",
                "playParams": {
                    "id": "1504448799",
                    "kind": "musicVideo"
                },
                "hasHDR": false
            }
        },
        {
            "id": "1333579835",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1333579835",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video125/v4/14/ad/3a/14ad3a32-a217-a772-47ef-e8fe79a1353d/mzvf_7804943013949277673.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1333579835&id=53816023&l=en&aec=HD",
                        "artwork": {
                            "width": 1920,
                            "url": "https: //is1-ssl.mzstatic.com/image/thumb/Video115/v4/a7/6e/ff/a76efffa-e21d-780b-4313-0d44daf608b4/Job18b782b3-fe2f-4ab0-8216-dd362a2f52c4-100205530-PreviewImage_preview_image_43000_video_sdr-Time1527882225533.png/{w}x{h}bb.jpeg",
                            "height": 1072,
                            "textColor3": "af95af",
                            "textColor2": "bcb8d5",
                            "textColor4": "a297b2",
                            "textColor1": "ccb6d2",
                            "bgColor": "3a1226",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 640,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Video118/v4/70/20/62/702062e9-c2ea-fab5-eafb-a87c08f0867e/GB1301700493.sca1.jpg/{w}x{h}mv.jpeg",
                    "height": 356,
                    "textColor3": "1f3c5a",
                    "textColor2": "431a1e",
                    "textColor4": "543d43",
                    "textColor1": "00183a",
                    "bgColor": "9cccdb",
                    "hasP3": false
                },
                "artistName": "Dua Lipa",
                "url": "https: //music.apple.com/us/music-video/idgaf/1333579835",
                "genreNames": [
                    "Pop"
                ],
                "has4K": false,
                "durationInMillis": 223528,
                "releaseDate": "2018-01-12",
                "name": "Idgaf",
                "isrc": "GB1301700493",
                "playParams": {
                    "id": "1333579835",
                    "kind": "musicVideo"
                },
                "hasHDR": false,
                "contentRating": "explicit"
            }
        },
        {
            "id": "1378223162",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1378223162",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video128/v4/fd/56/2e/fd562e18-aa42-a113-95d7-047c63fd5f25/mzvf_8326938850410074120.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1378223162&id=52634429&l=en&aec=HD",
                        "artwork": {
                            "width": 1920,
                            "url": "https: //is3-ssl.mzstatic.com/image/thumb/Video118/v4/3f/b2/b3/3fb2b31f-465d-e369-2064-45a9e0fbfd3a/Jobd624745b-2a58-4d66-82a3-48dd8b8c8d4d-99724041-PreviewImage_preview_image_62000_video_sdr-Time1525188874093.png/{w}x{h}bb.jpeg",
                            "height": 1080,
                            "textColor3": "cbc7b6",
                            "textColor2": "ebe1ca",
                            "textColor4": "c4c0b5",
                            "textColor1": "f5e9cc",
                            "bgColor": "273d61",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 1920,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Video128/v4/36/98/84/369884cb-6e7e-496c-2846-f5f5794cbcdd/dj.engoglnv.jpg/{w}x{h}mv.jpeg",
                    "height": 1080,
                    "textColor3": "3d2721",
                    "textColor2": "2d1719",
                    "textColor4": "4f2d25",
                    "textColor1": "171015",
                    "bgColor": "d48453",
                    "hasP3": false
                },
                "artistName": "Calvin Harris & Dua Lipa",
                "url": "https: //music.apple.com/us/music-video/one-kiss/1378223162",
                "genreNames": [
                    "Pop"
                ],
                "has4K": false,
                "durationInMillis": 223123,
                "releaseDate": "2018-05-01",
                "name": "One Kiss",
                "isrc": "GB1101800361",
                "playParams": {
                    "id": "1378223162",
                    "kind": "musicVideo"
                },
                "hasHDR": false,
                "editorialNotes": {
                    "short": "The UK stars present a kaleidoscopic pop paradise."
                }
            }
        },
        {
            "id": "1435206828",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1435206828",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video118/v4/b9/49/37/b9493760-43ef-9de8-0ecf-1a1a08d64ce2/mzvf_7507170959738994683.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1435206828&id=55816591&l=en&aec=HD",
                        "artwork": {
                            "width": 1920,
                            "url": "https: //is5-ssl.mzstatic.com/image/thumb/Video128/v4/0f/ee/93/0fee93cb-5dbc-d419-05bb-1609a5512d2b/Job26053328-d445-4e39-b632-130cb7d7a59d-101071092-PreviewImage_preview_image_70000_video_sdr-Time1536254666343.png/{w}x{h}bb.jpeg",
                            "height": 1080,
                            "textColor3": "b09c94",
                            "textColor2": "82b6d2",
                            "textColor4": "6892a7",
                            "textColor1": "dcc3b9",
                            "bgColor": "000000",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 1920,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Video118/v4/5a/2c/e0/5a2ce021-203b-7ad5-a9dd-77f6735b10da/dj.fewgpspm.jpg/{w}x{h}mv.jpeg",
                    "height": 804,
                    "textColor3": "6da1ac",
                    "textColor2": "5ac7e0",
                    "textColor4": "4ca4b8",
                    "textColor1": "82c3d1",
                    "bgColor": "171918",
                    "hasP3": false
                },
                "artistName": "Silk City & Dua Lipa",
                "url": "https: //music.apple.com/us/music-video/electricity-feat-diplo-mark-ronson/1435206828",
                "genreNames": [
                    "Dance"
                ],
                "has4K": false,
                "durationInMillis": 274110,
                "releaseDate": "2018-09-07",
                "name": "Electricity (feat. Diplo & Mark Ronson)",
                "isrc": "USQX91802378",
                "playParams": {
                    "id": "1435206828",
                    "kind": "musicVideo"
                },
                "hasHDR": false,
                "editorialNotes": {
                    "short": "Dua dances the lights on during the NYC blackout of 2003."
                }
            }
        },
        {
            "id": "1524772746",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1524772746",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video124/v4/f3/bc/06/f3bc0682-ab71-12c4-2ecc-bae07cedae45/mzvf_9732274862240429734.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1524772746&id=67981542&l=en&aec=HD",
                        "artwork": {
                            "width": 1920,
                            "url": "https: //is2-ssl.mzstatic.com/image/thumb/Video114/v4/fc/6d/81/fc6d81ac-6f10-bc7e-83ea-f95591e8e88a/Job7f8321bd-a881-4def-8386-ac83e2badb10-107053952-PreviewImage_preview_image_45000_video_sdr-Time1595557717768.png/{w}x{h}bb.jpeg",
                            "height": 1080,
                            "textColor3": "c0c0c0",
                            "textColor2": "eeeeee",
                            "textColor4": "c0c0c0",
                            "textColor1": "eeeeee",
                            "bgColor": "060606",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 1912,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Video114/v4/52/bc/9f/52bc9f70-20f2-0a86-281d-a8a26437040b/20UMGIM63975.crop.jpg/{w}x{h}mv.jpeg",
                    "height": 1072,
                    "textColor3": "373737",
                    "textColor2": "141414",
                    "textColor4": "3e3e3e",
                    "textColor1": "0c0c0c",
                    "bgColor": "e4e4e4",
                    "hasP3": false
                },
                "artistName": "J Balvin, Dua Lipa, Bad Bunny & Tainy",
                "url": "https: //music.apple.com/us/music-video/un-dia-one-day/1524772746",
                "genreNames": [
                    "Latin"
                ],
                "has4K": false,
                "durationInMillis": 249727,
                "releaseDate": "2020-07-24",
                "name": "UN DIA (ONE DAY)",
                "isrc": "QZM5U2000013",
                "playParams": {
                    "id": "1524772746",
                    "kind": "musicVideo"
                },
                "hasHDR": false
            }
        },
        {
            "id": "1540830143",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1540830143",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video124/v4/e7/cc/27/e7cc270c-e8b0-3de3-81f2-aebfad48992d/mzvf_13490001920548815146.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1540830143&id=215581996&l=en&aec=HD",
                        "artwork": {
                            "width": 1920,
                            "url": "https: //is2-ssl.mzstatic.com/image/thumb/Video114/v4/5d/fb/75/5dfb756d-4bc0-80ed-36c6-a4a19c5c3b0c/Job08d24a56-1fa3-4289-9d35-c5c50b4a2c6c-108028815-PreviewImage_preview_image_0_video_sdr-Time1605840987812.png/{w}x{h}bb.jpeg",
                            "height": 1080,
                            "textColor3": "c1c1c1",
                            "textColor2": "e5e5e5",
                            "textColor4": "b7b7b7",
                            "textColor1": "f2f2f2",
                            "bgColor": "000000",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 1920,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Video124/v4/a0/99/73/a09973e8-c775-a6e6-36d6-2e55e6c2d60e/dj.bwophdle.jpg/{w}x{h}mv.jpeg",
                    "height": 1080,
                    "textColor3": "b39382",
                    "textColor2": "d7a088",
                    "textColor4": "ac806e",
                    "textColor1": "e0b8a2",
                    "bgColor": "010006",
                    "hasP3": false
                },
                "artistName": "Miley Cyrus",
                "url": "https: //music.apple.com/us/music-video/prisoner-feat-dua-lipa/1540830143",
                "genreNames": [
                    "Pop"
                ],
                "has4K": false,
                "durationInMillis": 194195,
                "releaseDate": "2020-11-22",
                "name": "Prisoner (feat. Dua Lipa)",
                "isrc": "USRV82001748",
                "playParams": {
                    "id": "1540830143",
                    "kind": "musicVideo"
                },
                "hasHDR": false
            }
        },
        {
            "id": "1497306765",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1497306765",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video123/v4/6f/4b/68/6f4b686c-d7ab-7d28-440c-8d2db31c95e6/mzvf_1125412239751047451.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1497306765&id=64002683&l=en&aec=HD",
                        "artwork": {
                            "width": 1920,
                            "url": "https: //is2-ssl.mzstatic.com/image/thumb/Video113/v4/98/6f/53/986f5307-916a-d8c7-6449-0be2e5bdd36f/Jobe4654085-7b9d-4ac7-b890-dba9220cf30a-105246997-PreviewImage_preview_image_43000_video_sdr-Time1580760530990.png/{w}x{h}bb.jpeg",
                            "height": 1080,
                            "textColor3": "aea29d",
                            "textColor2": "b1b6cd",
                            "textColor4": "8e95a7",
                            "textColor1": "d9c7c1",
                            "bgColor": "061010",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 640,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Video123/v4/4c/67/bb/4c67bba1-f2a9-6cb8-3007-96aaad1260f0/GB1301901247.sca1.jpg/{w}x{h}mv.jpeg",
                    "height": 360,
                    "textColor3": "97cdd0",
                    "textColor2": "a9fdff",
                    "textColor4": "87ccd1",
                    "textColor1": "bdfefd",
                    "bgColor": "000c1d",
                    "hasP3": false
                },
                "artistName": "Dua Lipa",
                "url": "https: //music.apple.com/us/music-video/physical/1497306765",
                "genreNames": [
                    "Pop"
                ],
                "has4K": false,
                "durationInMillis": 239848,
                "releaseDate": "2020-01-31",
                "name": "Physical",
                "isrc": "GB1301901247",
                "playParams": {
                    "id": "1497306765",
                    "kind": "musicVideo"
                },
                "hasHDR": false
            }
        },
        {
            "id": "1570635373",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1570635373",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video125/v4/ae/66/4a/ae664a8a-33d9-5c46-1386-76f317c60832/mzvf_6538485288826784322.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1570635373&id=287967333&l=en&aec=HD",
                        "artwork": {
                            "width": 1920,
                            "url": "https: //is3-ssl.mzstatic.com/image/thumb/Video125/v4/b7/9b/2f/b79b2fcb-ee76-d7e8-79fc-87ca61a42efb/Joba225f3fe-19b7-445f-a505-38c3403146c6-114945944-PreviewImage_preview_image_43000_video_sdr-Time1623137625260.png/{w}x{h}bb.jpeg",
                            "height": 1080,
                            "textColor3": "b6a07d",
                            "textColor2": "d7a16e",
                            "textColor4": "b2865d",
                            "textColor1": "dcc196",
                            "bgColor": "1d1c18",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 640,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Video115/v4/ba/46/fb/ba46fb0c-c7fd-1f47-61ed-05f1ca301cd7/GB1302100632.sca1.jpg/{w}x{h}mv.jpeg",
                    "height": 360,
                    "textColor3": "ae8c61",
                    "textColor2": "d19756",
                    "textColor4": "a87a45",
                    "textColor1": "d8ae79",
                    "bgColor": "050503",
                    "hasP3": false
                },
                "artistName": "Dua Lipa",
                "url": "https: //music.apple.com/us/music-video/love-again/1570635373",
                "genreNames": [
                    "Pop"
                ],
                "has4K": false,
                "durationInMillis": 263977,
                "releaseDate": "2021-06-04",
                "name": "Love Again",
                "isrc": "GB1302100632",
                "playParams": {
                    "id": "1570635373",
                    "kind": "musicVideo"
                },
                "hasHDR": false
            }
        },
        {
            "id": "1502090282",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1502090282",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video113/v4/7d/b7/df/7db7df7f-d6e5-bc56-ac97-78df7f4b0b44/mzvf_15095912436913616268.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1502090282&id=64797066&l=en&aec=HD",
                        "artwork": {
                            "width": 1920,
                            "url": "https: //is2-ssl.mzstatic.com/image/thumb/Video123/v4/95/b3/82/95b3822f-33a9-42ad-df9f-28374389b258/Jobd7f8ccd8-f829-49a4-889b-547f1ebec271-105824865-PreviewImage_preview_image_43000_video_sdr-Time1583804699360.png/{w}x{h}bb.jpeg",
                            "height": 1080,
                            "textColor3": "2a2519",
                            "textColor2": "091a16",
                            "textColor4": "273225",
                            "textColor1": "0c0907",
                            "bgColor": "a19363",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 640,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Video124/v4/d6/02/96/d602967e-2e57-8e14-0b07-c3aa12389dba/GB1302000167.sca1.jpg/{w}x{h}mv.jpeg",
                    "height": 360,
                    "textColor3": "222519",
                    "textColor2": "161a09",
                    "textColor4": "2d321e",
                    "textColor1": "080903",
                    "bgColor": "8a9472",
                    "hasP3": false
                },
                "artistName": "Dua Lipa",
                "url": "https: //music.apple.com/us/music-video/lets-get-physical-workout-video/1502090282",
                "genreNames": [
                    "Pop"
                ],
                "has4K": false,
                "durationInMillis": 340820,
                "releaseDate": "2020-03-06",
                "name": "Let’s Get Physical Workout Video",
                "isrc": "GB1302000167",
                "playParams": {
                    "id": "1502090282",
                    "kind": "musicVideo"
                },
                "hasHDR": false
            }
        },
        {
            "id": "1580928539",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1580928539",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video115/v4/63/d4/5d/63d45d16-244a-e6c0-e5bb-40fab5dbc23b/mzvf_12268169823223188296.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1580928539&id=327369346&l=en&aec=HD",
                        "artwork": {
                            "width": 1920,
                            "url": "https: //is1-ssl.mzstatic.com/image/thumb/Video115/v4/9e/5a/76/9e5a7677-b615-502f-01f5-ac121b53aa7c/Job1e9246c7-ad41-46d3-ac6f-c0ee2261644d-120185190-PreviewImage_preview_image_45000_video_sdr-Time1628772465242.png/{w}x{h}bb.jpeg",
                            "height": 1080,
                            "textColor3": "89a098",
                            "textColor2": "1bb6d0",
                            "textColor4": "1691a6",
                            "textColor1": "abc9be",
                            "bgColor": "040001",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 1912,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Video115/v4/b2/3b/6a/b23b6a39-90c0-3f7d-c137-9498d0ff7466/21UMGIM68485.crop.jpg/{w}x{h}mv.jpeg",
                    "height": 1072,
                    "textColor3": "a9c7ce",
                    "textColor2": "f0e2e9",
                    "textColor4": "c0b4bd",
                    "textColor1": "d4f9ff",
                    "bgColor": "00000e",
                    "hasP3": false
                },
                "artistName": "Elton John & Dua Lipa",
                "url": "https: //music.apple.com/us/music-video/cold-heart-pnau-remix/1580928539",
                "genreNames": [
                    "Pop"
                ],
                "has4K": false,
                "durationInMillis": 254163,
                "releaseDate": "2021-08-13",
                "name": "Cold Heart (PNAU Remix)",
                "isrc": "GBUV72101411",
                "playParams": {
                    "id": "1580928539",
                    "kind": "musicVideo"
                },
                "hasHDR": false
            }
        },
        {
            "id": "1527754332",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1527754332",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video114/v4/78/a7/d1/78a7d162-3b05-a50c-2a65-b684a6b670c5/mzvf_7639738791763961074.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1527754332&id=68420029&l=en&aec=HD",
                        "artwork": {
                            "width": 1920,
                            "url": "https: //is1-ssl.mzstatic.com/image/thumb/Video114/v4/c5/be/7e/c5be7eb3-ad9d-997b-7362-7445d8c8ee82/Jobfd8592d3-6107-4a6c-96b0-c59e149249c5-107229955-PreviewImage_preview_image_43000_video_sdr-Time1597719243204.png/{w}x{h}bb.jpeg",
                            "height": 960,
                            "textColor3": "7da3d7",
                            "textColor2": "7ab1fb",
                            "textColor4": "6393d5",
                            "textColor1": "9ac4fe",
                            "bgColor": "081c3f",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 640,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Video114/v4/0e/f4/70/0ef470e9-1de6-5ec9-ba02-e0e36a98066f/GB1302000681.sca1.jpg/{w}x{h}mv.jpeg",
                    "height": 320,
                    "textColor3": "8458cc",
                    "textColor2": "875af9",
                    "textColor4": "7948c9",
                    "textColor1": "956efc",
                    "bgColor": "41000d",
                    "hasP3": false
                },
                "artistName": "Dua Lipa",
                "url": "https: //music.apple.com/us/music-video/levitating-feat-madonna-and-missy-elliott-the/1527754332",
                "genreNames": [
                    "Dance"
                ],
                "has4K": false,
                "durationInMillis": 256212,
                "releaseDate": "2020-08-14",
                "name": "Levitating (feat. Madonna and Missy Elliott) [The Blessed Madonna Remix
                ]",
                "isrc": "GB1302000681",
                "playParams": {
                    "id": "1527754332",
                    "kind": "musicVideo"
                },
                "hasHDR": false
            }
        },
        {
            "id": "1578870784",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1578870784",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video115/v4/cc/25/fc/cc25fc92-6628-24c3-c3e7-0b72155c9f62/mzvf_14183539230858555894.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1578870784&id=314437555&l=en&aec=HD",
                        "artwork": {
                            "width": 1920,
                            "url": "https: //is3-ssl.mzstatic.com/image/thumb/Video125/v4/82/ff/b1/82ffb165-6881-5bb6-d422-28829925996f/Job5ac31fdf-9d2e-4d8e-b596-9bf8736c3fc2-118338577-PreviewImage_preview_image_45000_video_sdr-Time1627558942458.png/{w}x{h}bb.jpeg",
                            "height": 752,
                            "textColor3": "c08548",
                            "textColor2": "cea06f",
                            "textColor4": "b0845b",
                            "textColor1": "e3a157",
                            "bgColor": "35150a",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 1912,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Video115/v4/de/70/0e/de700ef0-d6f7-7804-0598-e8757c2d10b2/21UMGIM68780.crop.jpg/{w}x{h}mv.jpeg",
                    "height": 746,
                    "textColor3": "b99569",
                    "textColor2": "d2a14f",
                    "textColor4": "b28844",
                    "textColor1": "dbb17e",
                    "bgColor": "362418",
                    "hasP3": false
                },
                "artistName": "Pop Smoke",
                "url": "https: //music.apple.com/us/music-video/demeanor-feat-dua-lipa/1578870784",
                "genreNames": [
                    "Hip-Hop/Rap"
                ],
                "has4K": false,
                "durationInMillis": 211240,
                "releaseDate": "2021-07-29",
                "name": "Demeanor (feat. Dua Lipa)",
                "isrc": "USUV72104298",
                "playParams": {
                    "id": "1578870784",
                    "kind": "musicVideo"
                },
                "hasHDR": false,
                "contentRating": "explicit"
            }
        }
    ]
}

```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/music-videos/{id}/view/{view}`

## Parameters

- `extend` ([string]): A list of attribute extensions to apply to resources in the response.
- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `with` ([string]): A list of modifications to apply to the request.

## See Also

- [object MusicVideos](musicvideos.md)
  A resource object that represents a music video.
- [object MusicVideosResponse](musicvideosresponse.md)
  The response to a music videos request.
- [Get a Catalog Music Video](get-a-catalog-music-video.md)
  Fetch a music video by using its identifier.
- [Get a Catalog Music Video's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-4z79l.md)
  Fetch a music video’s relationship by using its identifier.
- [Get Multiple Catalog Music Videos by ID](get-multiple-catalog-music-videos-by-id.md)
  Fetch one or more music videos by using their identifiers.
- [Get Multiple Catalog Music Videos by ISRC](get-multiple-catalog-music-videos-by-isrc.md)
  Fetch one or more music videos by using their International Standard Recording Code (ISRC) values.
- [Get Equivalent Catalog Music Videos by ID](get-equivalent-ids-for-the-albums-8tp4l.md)
  Fetch the equivalent, available content in the storefront for the provided music videos’ identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-view-on-this-resource-by-name-5657g)*