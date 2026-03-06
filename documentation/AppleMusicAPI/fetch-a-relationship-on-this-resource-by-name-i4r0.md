# Get a Station Genre’s Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a station genre’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/station-genres/1149486336/stations
```

**Response**:

```json
{
    "data": [
        {
            "id": "ra.686227433",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.686227433",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Features125/v4/e0/cd/18/e0cd1802-fca9-22a7-5b8f-899c9fa99380/U0MtTVMtV1ctUG9wLUFEQU1fSUQ9Njg2MjI3NDMzLnBuZw.png/{w}x{h}sr.jpg",
                    "bgColor": "d23676",
                    "textColor1": "ffffff",
                    "textColor2": "110c0e",
                    "textColor3": "2e131e",
                    "textColor4": "2e131e"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Pop Station",
                    "standard": "If it’s hot, it’s here.",
                    "short": "Apple Music Pop",
                    "tagline": "Apple Music Pop"
                },
                "playParams": {
                    "id": "ra.686227433",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoF6f-bxwIQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/pure-pop/ra.686227433",
                "name": "Pop Station",
                "isLive": false
            }
        },
        {
            "id": "ra.985480047",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.985480047",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Features125/v4/9f/d8/42/9fd84207-7614-9114-010f-19f17a36e07a/U0MtTVMtV1ctSGl0cy1BREFNX0lEPTE0OTgxNTU1NDgucG5n.png/{w}x{h}sr.jpg",
                    "bgColor": "dda208",
                    "textColor1": "ffffff",
                    "textColor2": "110f09",
                    "textColor3": "302506",
                    "textColor4": "302608"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Hits Station",
                    "standard": "The hottest tracks on the planet.",
                    "short": "Apple Music Hits",
                    "tagline": "Apple Music Hits"
                },
                "playParams": {
                    "id": "ra.985480047",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoF7_b01QMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/hits-station/ra.985480047",
                "name": "Hits Station",
                "isLive": false
            }
        },
        {
            "id": "ra.1266190007",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.1266190007",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Features125/v4/c0/82/1f/c0821f3f-c6ef-950a-9e88-679728f898f7/U0MtTVMtV1ctMjAxMHNfSGl0cy1BREFNX0lEPTEyNjYxOTAwMDcucG5n.png/{w}x{h}sr.jpg",
                    "bgColor": "401cbc",
                    "textColor1": "000000",
                    "textColor2": "e9e5f8",
                    "textColor3": "ccc2ee",
                    "textColor4": "c4b9ec"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "2010s Hits Station",
                    "standard": "Nothing but bangers.",
                    "short": "Apple Music Hits",
                    "tagline": "Apple Music Hits"
                },
                "playParams": {
                    "id": "ra.1266190007",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFt43i2wQQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/2010s-hits-station/ra.1266190007",
                "name": "2010s Hits Station",
                "isLive": false
            }
        },
        {
            "id": "ra.991200508",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.991200508",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Features125/v4/13/6c/a0/136ca06b-e76f-1c4a-291e-12631447f148/U0MtTVMtV1ctU29mdF9Qb3AtQURBTV9JRD05OTEyMDA1MDgucG5n.png/{w}x{h}sr.jpg",
                    "bgColor": "fc81b7",
                    "textColor1": "ffffff",
                    "textColor2": "120e10",
                    "textColor3": "352029",
                    "textColor4": "352029"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Soft Pop Station",
                    "standard": "The gentle side of pop.",
                    "short": "Apple Music Pop",
                    "tagline": "Apple Music Pop"
                },
                "playParams": {
                    "id": "ra.991200508",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoF_InS2AMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/soft-pop-station/ra.991200508",
                "name": "Soft Pop Station",
                "isLive": false
            }
        },
        {
            "id": "ra.1055198656",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.1055198656",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Features115/v4/11/6c/db/116cdb8c-d19a-1ab3-5193-0be449b448bd/U0MtTVMtV1ctMjAwMHNfSGl0cy1BREFNX0lEPTEwNTUxOTg2NTYucG5n.png/{w}x{h}sr.jpg",
                    "bgColor": "3b8de8",
                    "textColor1": "000000",
                    "textColor2": "0c0f11",
                    "textColor3": "122232",
                    "textColor4": "132232"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "2000s Hits Station",
                    "standard": "Outkast. Timberlake. Coldplay.",
                    "short": "Apple Music Hits",
                    "tagline": "Apple Music Hits"
                },
                "playParams": {
                    "id": "ra.1055198656",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFwJuU9wMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/2000s-hits-station/ra.1055198656",
                "name": "2000s Hits Station",
                "isLive": false
            }
        },
        {
            "id": "ra.1055198674",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.1055198674",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Features115/v4/b3/06/69/b30669d9-e04f-bd63-04a1-4d8af91a3b6c/U0MtTVMtV1ctOTBzX0hpdHMtQURBTV9JRD0xMDU1MTk4Njc0LnBuZw.png/{w}x{h}sr.jpg",
                    "bgColor": "c43f33",
                    "textColor1": "000000",
                    "textColor2": "100c0b",
                    "textColor3": "2b1411",
                    "textColor4": "2c1512"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "’90s Hits Station",
                    "standard": "Kurt Cobain to Britney Spears.",
                    "short": "Apple Music Hits",
                    "tagline": "Apple Music Hits"
                },
                "playParams": {
                    "id": "ra.1055198674",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoF0puU9wMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/90s-hits-station/ra.1055198674",
                "name": "’90s Hits Station",
                "isLive": false
            }
        },
        {
            "id": "ra.1055200360",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.1055200360",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Features115/v4/39/8e/03/398e038c-2491-1a55-0cce-a541f571e5a8/U0MtTVMtV1ctODBzX0hpdHMtQURBTV9JRD0xMDU1MjAwMzYwLnBuZw.png/{w}x{h}sr.jpg",
                    "bgColor": "b123a7",
                    "textColor1": "000000",
                    "textColor2": "100b0f",
                    "textColor3": "280f26",
                    "textColor4": "281027"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "’80s Hits Station",
                    "standard": "Prince, Madonna, and Wham!",
                    "short": "Apple Music Hits",
                    "tagline": "Apple Music Hits"
                },
                "playParams": {
                    "id": "ra.1055200360",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoF6KiU9wMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/80s-hits-station/ra.1055200360",
                "name": "’80s Hits Station",
                "isLive": false
            }
        },
        {
            "id": "ra.1055200655",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.1055200655",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Features125/v4/61/26/21/612621ad-e21d-47d3-650e-4906f8d14822/U0MtTVMtV1ctNzBzX0hpdHMtQURBTV9JRD0xMDU1MjAwNjU1LnBuZw.png/{w}x{h}sr.jpg",
                    "bgColor": "6317a9",
                    "textColor1": "000000",
                    "textColor2": "eee5f6",
                    "textColor3": "d6c1ea",
                    "textColor4": "d0b7e6"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "’70s Hits Station",
                    "standard": "Stevie, Elton, and more.",
                    "short": "Apple Music Hits",
                    "tagline": "Apple Music Hits"
                },
                "playParams": {
                    "id": "ra.1055200655",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFj6uU9wMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/70s-hits-station/ra.1055200655",
                "name": "’70s Hits Station",
                "isLive": false
            }
        },
        {
            "id": "ra.1055201459",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.1055201459",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Features115/v4/5d/60/2b/5d602b5d-0120-958d-7cf2-9a4946c006a5/U0MtTVMtV1ctNjBzX0hpdHMtQURBTV9JRD0xMDU1MjAxNDU5LnBuZw.png/{w}x{h}sr.jpg",
                    "bgColor": "e66336",
                    "textColor1": "000000",
                    "textColor2": "110d0b",
                    "textColor3": "311a12",
                    "textColor4": "311b13"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "’60s Hits Station",
                    "standard": "Aretha, The Beatles, and more.",
                    "short": "Apple Music Hits",
                    "tagline": "Apple Music Hits"
                },
                "playParams": {
                    "id": "ra.1055201459",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFs7GU9wMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/60s-hits-station/ra.1055201459",
                "name": "’60s Hits Station",
                "isLive": false
            }
        },
        {
            "id": "ra.985499979",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.985499979",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Features115/v4/a2/3a/a8/a23aa822-4f97-5f55-8f47-afdd4caf858d/U0MtTVMtV1ctT2xkaWVzLUFEQU1fSUQ9OTg1NDk5OTc5LnBuZw.png/{w}x{h}sr.jpg",
                    "bgColor": "eda538",
                    "textColor1": "ffffff",
                    "textColor2": "12100d",
                    "textColor3": "322613",
                    "textColor4": "332714"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Oldies Station",
                    "standard": "Happy days.",
                    "short": "Apple Music Oldies",
                    "tagline": "Apple Music Oldies"
                },
                "playParams": {
                    "id": "ra.985499979",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFy5L21QMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/oldies-station/ra.985499979",
                "name": "Oldies Station",
                "isLive": false
            }
        },
        {
            "id": "ra.985498974",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.985498974",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Features115/v4/13/a6/08/13a608a1-b9b2-37c6-f737-8d1ef7ac5afa/U0MtTVMtV1ctTGF0aW5fUG9wIFN0YXRpb24tQURBTV9JRD05ODU0OTg5NzQucG5n.png/{w}x{h}sr.jpg",
                    "bgColor": "ea644c",
                    "textColor1": "ffffff",
                    "textColor2": "110d0c",
                    "textColor3": "321b17",
                    "textColor4": "321b17"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Latin Pop Station",
                    "standard": "J Balvin, Jennifer Lopez, and more.",
                    "short": "Apple Music Latin",
                    "tagline": "Apple Music Latin"
                },
                "playParams": {
                    "id": "ra.985498974",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoF3or21QMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/latin-pop-station/ra.985498974",
                "name": "Latin Pop Station",
                "isLive": false
            }
        },
        {
            "id": "ra.991157822",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.991157822",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Features115/v4/ae/33/92/ae33924f-f523-1e6f-fd30-f43eec2e54ca/U0MtTVMtV1ctQnJhemlsaWFuX1BvcC1BREFNX0lEPTk5MTE1NzgyMi5wbmc.png/{w}x{h}sr.jpg",
                    "bgColor": "6b9817",
                    "textColor1": "000000",
                    "textColor2": "0d0f0a",
                    "textColor3": "1b240b",
                    "textColor4": "1c240c"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Brazilian Pop Station",
                    "standard": "From Rio and beyond.",
                    "short": "Apple Music Brazilian Pop",
                    "tagline": "Apple Music Brazilian Pop"
                },
                "playParams": {
                    "id": "ra.991157822",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFvrzP2AMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/brazilian-pop-station/ra.991157822",
                "name": "Brazilian Pop Station",
                "isLive": false
            }
        },
        {
            "id": "ra.991194759",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.991194759",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Features125/v4/04/df/bc/04dfbc83-8b36-35b0-2da6-2860e06cc4b8/U0MtTVMtV1ctSXJpc2hfSGl0cy1BREFNX0lEPTk5MTE5NDc1OS5wbmc.png/{w}x{h}sr.jpg",
                    "bgColor": "71b117",
                    "textColor1": "ffffff",
                    "textColor2": "0e100a",
                    "textColor3": "1d280b",
                    "textColor4": "1d280c"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Irish Hits Station",
                    "standard": "Anthems of the Emerald Isle.",
                    "short": "Apple Music Hits",
                    "tagline": "Apple Music Hits"
                },
                "playParams": {
                    "id": "ra.991194759",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFh93R2AMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/irish-hits-station/ra.991194759",
                "name": "Irish Hits Station",
                "isLive": false
            }
        },
        {
            "id": "ra.991162438",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.991162438",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Features115/v4/9b/d9/3a/9bd93a17-d8ce-c625-dbac-4280aeeaa253/U0MtTVMtV1ctRGV1dHNjaHBvcC1BREFNX0lEPTk5MTE2MjQzOC5wbmc.png/{w}x{h}sr.jpg",
                    "bgColor": "a642a1",
                    "textColor1": "ffffff",
                    "textColor2": "0f0c0f",
                    "textColor3": "271526",
                    "textColor4": "271526"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Deutschpop Station",
                    "standard": "Germany’s biggest tracks.",
                    "short": "Apple Music Deutschpop",
                    "tagline": "Apple Music Deutschpop"
                },
                "playParams": {
                    "id": "ra.991162438",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFxuDP2AMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/deutschpop-station/ra.991162438",
                "name": "Deutschpop Station",
                "isLive": false
            }
        },
        {
            "id": "ra.991160214",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.991160214",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Features115/v4/fa/0c/16/fa0c16bf-8290-c641-d498-ccab78c7d417/U0MtTVMtV1ctRnJlbmNoX1BvcC1BREFNX0lEPTk5MTE2MDIxNC5wbmc.png/{w}x{h}sr.jpg",
                    "bgColor": "113790",
                    "textColor1": "ffffff",
                    "textColor2": "5a91fa",
                    "textColor3": "5d8ce4",
                    "textColor4": "497de4"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "French Pop Station",
                    "standard": "Current and recent hits.",
                    "short": "Apple Music French Pop",
                    "tagline": "Apple Music French Pop"
                },
                "playParams": {
                    "id": "ra.991160214",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFls_P2AMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/french-pop-station/ra.991160214",
                "name": "French Pop Station",
                "isLive": false
            }
        },
        {
            "id": "ra.991158061",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.991158061",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Features115/v4/16/54/97/16549755-a20e-c166-11f7-01ad8475e1ef/U0MtTVMtV1ctQ2FuYWRpYW5fQ2xhc3NpY3MtQURBTV9JRD05OTExNTgwNjEucG5n.png/{w}x{h}sr.jpg",
                    "bgColor": "c23f2e",
                    "textColor1": "000000",
                    "textColor2": "100c0b",
                    "textColor3": "2b1410",
                    "textColor4": "2b1511"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Canadian Classics Station",
                    "standard": "A selection of unforgettable songs.",
                    "short": "Apple Music Canadian Music",
                    "tagline": "Apple Music Canadian Music"
                },
                "playParams": {
                    "id": "ra.991158061",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFrb7P2AMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/canadian-classics-station/ra.991158061",
                "name": "Canadian Classics Station",
                "isLive": false
            }
        },
        {
            "id": "ra.991158858",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.991158858",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Features115/v4/c8/6d/22/c86d227e-8a6f-ee32-37d5-6a9f366650e5/U0MtTVMtV1ctQ2FuYWRpYW5fSGl0cy1BREFNX0lEPTk5MTE1ODg1OC5wbmc.png/{w}x{h}sr.jpg",
                    "bgColor": "fc7c31",
                    "textColor1": "000000",
                    "textColor2": "120f0c",
                    "textColor3": "351f12",
                    "textColor4": "352013"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Canadian Hits Station",
                    "standard": "The songs that rule the charts.",
                    "short": "Apple Music Hits",
                    "tagline": "Apple Music Hits"
                },
                "playParams": {
                    "id": "ra.991158858",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFysTP2AMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/canadian-hits-station/ra.991158858",
                "name": "Canadian Hits Station",
                "isLive": false
            }
        },
        {
            "id": "ra.991160003",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.991160003",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Features125/v4/4a/5a/e0/4a5ae073-667e-eecd-9c48-3c8dd9a00d0e/U0MtTVMtV1ctRnJhbmNvcGhvbmVfSGl0cy1BREFNX0lEPTk5MTE2MDAwMy5wbmc.png/{w}x{h}sr.jpg",
                    "bgColor": "44b7d5",
                    "textColor1": "000000",
                    "textColor2": "0c1011",
                    "textColor3": "15292e",
                    "textColor4": "15292e"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Francophone Hits Station",
                    "standard": "The best French-Canadian pop.",
                    "short": "Apple Music Canadian",
                    "tagline": "Apple Music Canadian"
                },
                "playParams": {
                    "id": "ra.991160003",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFw83P2AMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/francophone-hits-station/ra.991160003",
                "name": "Francophone Hits Station",
                "isLive": false
            }
        },
        {
            "id": "ra.991159841",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.991159841",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Features125/v4/51/9b/45/519b4527-88f1-b5c1-9e6f-bfa6cd6e5f55/U0MtTVMtV1ctRnJhbmNvcGhvbmVfQ2xhc3NpY3MtQURBTV9JRD05OTExNTk4NDEucG5n.png/{w}x{h}sr.jpg",
                    "bgColor": "1932b5",
                    "textColor1": "000000",
                    "textColor2": "e3e8f7",
                    "textColor3": "bec9ed",
                    "textColor4": "b4c0ea"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Francophone Classics Station",
                    "standard": "Timeless favorites.",
                    "short": "Apple Music Canadian",
                    "tagline": "Apple Music Canadian"
                },
                "playParams": {
                    "id": "ra.991159841",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFoczP2AMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/francophone-classics-station/ra.991159841",
                "name": "Francophone Classics Station",
                "isLive": false
            }
        },
        {
            "id": "ra.992731732",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.992731732",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Features125/v4/d1/f4/bd/d1f4bd0f-76f2-85bd-4baf-4d69c7c9e96e/U0MtTVMtV1ctS19Qb3AtQURBTV9JRD05OTI3MzE3MzIucG5n.png/{w}x{h}sr.jpg",
                    "bgColor": "30bcd1",
                    "textColor1": "ffffff",
                    "textColor2": "0b1011",
                    "textColor3": "102a2e",
                    "textColor4": "112a2e"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "K-Pop Station",
                    "standard": "Chart-dominating hits from Korea.",
                    "short": "Apple Music K-Pop",
                    "tagline": "Apple Music K-Pop"
                },
                "playParams": {
                    "id": "ra.992731732",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoF1MSv2QMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/k-pop-station/ra.992731732",
                "name": "K-Pop Station",
                "isLive": false
            }
        },
        {
            "id": "ra.991655669",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.991655669",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Features115/v4/b2/a8/b0/b2a8b031-a37f-c6aa-c8bd-951a6c95eb2a/U0MtTVMtV1ctSl9Qb3AtQURBTV9JRD05OTE2NTU2NjkucG5n.png/{w}x{h}sr.jpg",
                    "bgColor": "d23fa8",
                    "textColor1": "ffffff",
                    "textColor2": "110c0f",
                    "textColor3": "2e1527",
                    "textColor4": "2e1527"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "J-Pop Station",
                    "standard": "Japanese pop from then to now.",
                    "short": "Apple Music J-Pop",
                    "tagline": "Apple Music J-Pop"
                },
                "playParams": {
                    "id": "ra.991655669",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoF9e3t2AMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/j-pop-station/ra.991655669",
                "name": "J-Pop Station",
                "isLive": false
            }
        },
        {
            "id": "ra.991168637",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.991168637",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Features115/v4/b4/a9/f3/b4a9f3ac-b78d-9a10-4b02-378b2f657cb6/U0MtTVMtV1ctQ2FudG9wb3AtQURBTV9JRD05OTExNjg2MzcucG5n.png/{w}x{h}sr.jpg",
                    "bgColor": "fd9710",
                    "textColor1": "ffffff",
                    "textColor2": "120f0a",
                    "textColor3": "352309",
                    "textColor4": "35240b"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Cantopop Station",
                    "standard": "Pop music from Hong Kong.",
                    "short": "Apple Music Cantopop",
                    "tagline": "Apple Music Cantopop"
                },
                "playParams": {
                    "id": "ra.991168637",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoF_ZDQ2AMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/cantopop-station/ra.991168637",
                "name": "Cantopop Station",
                "isLive": false
            }
        },
        {
            "id": "ra.991169024",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.991169024",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Features115/v4/a6/29/1d/a6291d17-c558-6b84-d339-dbd700edb0a9/U0MtTVMtV1ctTWFuZG9wb3AtQURBTV9JRD05OTExNjkwMjQucG5n.png/{w}x{h}sr.jpg",
                    "bgColor": "de6346",
                    "textColor1": "ffffff",
                    "textColor2": "110d0c",
                    "textColor3": "301b16",
                    "textColor4": "301b16"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Mandopop Station",
                    "standard": "Recent hits performed in Mandarin.",
                    "short": "Apple Music Mandopop",
                    "tagline": "Apple Music Mandopop"
                },
                "playParams": {
                    "id": "ra.991169024",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFgJTQ2AMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/mandopop-station/ra.991169024",
                "name": "Mandopop Station",
                "isLive": false
            }
        },
        {
            "id": "ra.1147496342",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.1147496342",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Features125/v4/3e/1a/5c/3e1a5c9f-2404-72af-4207-a4df6c9a1dbf/U0MtTVMtV1ctVGhhaV9Qb3AtQURBTV9JRD0xMTQ3NDk2MzQyLnBuZw.png/{w}x{h}sr.jpg",
                    "bgColor": "7f2142",
                    "textColor1": "ffffff",
                    "textColor2": "f892b7",
                    "textColor3": "de799d",
                    "textColor4": "de799d"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Thai Pop Station",
                    "standard": "Today’s mainstream Thai hits.",
                    "short": "Apple Music Thai Music",
                    "tagline": "Apple Music Thai Music"
                },
                "playParams": {
                    "id": "ra.1147496342",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFls-VowQQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/thai-pop-station/ra.1147496342",
                "name": "Thai Pop Station",
                "isLive": false
            }
        },
        {
            "id": "ra.991163466",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.991163466",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Features115/v4/98/fe/23/98fe23c5-bd8f-bf8f-600c-d566b8154e62/U0MtTVMtV1ctUG9wX0l0YWxpYW5vLUFEQU1fSUQ9OTkxMTYzNDY2LnBuZw.png/{w}x{h}sr.jpg",
                    "bgColor": "3b90de",
                    "textColor1": "ffffff",
                    "textColor2": "0c0f11",
                    "textColor3": "122230",
                    "textColor4": "132330"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Pop Italiano Station",
                    "standard": "Rock, pop, and dance hits.",
                    "short": "Apple Music Pop Italiano",
                    "tagline": "Apple Music Pop Italiano"
                },
                "playParams": {
                    "id": "ra.991163466",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFyujP2AMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/pop-italiano/ra.991163466",
                "name": "Pop Italiano Station",
                "isLive": false
            }
        },
        {
            "id": "ra.991172490",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.991172490",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Features115/v4/f5/97/52/f5975222-cef9-75a1-78f7-f93d582ecc97/U0MtTVMtV1ctVHVya2lzaF9Qb3AtQURBTV9JRD05OTExNzI0OTAucG5n.png/{w}x{h}sr.jpg",
                    "bgColor": "d53c1f",
                    "textColor1": "ffffff",
                    "textColor2": "110c0a",
                    "textColor3": "2e130d",
                    "textColor4": "2e140e"
                },
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Turkish Pop Station",
                    "standard": "Current stars and new favorites.",
                    "short": "Apple Music Pop",
                    "tagline": "Apple Music Pop"
                },
                "playParams": {
                    "id": "ra.991172490",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFiq_Q2AMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/turkish-pop-station/ra.991172490",
                "name": "Turkish Pop Station",
                "isLive": false
            }
        }
    ]
}

```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/station-genres/{id}/{relationship}`

## Parameters

- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object StationGenres](stationgenres.md)
  A resource object that represents a station genre.
- [object StationGenresResponse](stationgenresresponse.md)
  The response to a specific station genres resource request.
- [Get a Station Genre](get-a-station-genre.md)
  Fetch a station genre by using its identifier.
- [Get Multiple Stations Genres](get-multiple-stations-genres.md)
  Fetch one or more station genres by using their identifiers.
- [Get All Station Genres](get-all-station-genres.md)
  Fetch all station genres for a given storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-i4r0)*