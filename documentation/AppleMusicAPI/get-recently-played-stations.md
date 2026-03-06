# Get Recently Played Stations

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch recently played radio stations for the user.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains an array of `Station` objects. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/recent/radio-stations
```

**Response**:

```json
{    
    "next": "/v1/me/recent/radio-stations?offset=10",
    "data": [
        {
            "id": "ra.1498157166",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.1498157166",
            "attributes": {
                "isLive": true,
                "mediaKind": "audio",
                "name": "Apple Music Country",
                "editorialNotes": {
                    "name": "Apple Music Country",
                    "short": "Where it sounds like home.",
                    "tagline": "Where it sounds like home."
                },
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https://is5-ssl.mzstatic.com/image/thumb/Features114/v4/89/e2/66/89e266ee-454e-87e7-e108-dea53c54da6a/U0MtTVMtV1ctQU1fQ291bnRyeS5wbmc.png/{w}x{h}sr.jpg",
                    "bgColor": "f4f4f4",
                    "textColor1": "000000",
                    "textColor2": "142234",
                    "textColor3": "3a412d",
                    "textColor4": "364354"
                },
                "playParams": {
                    "id": "ra.1498157166",
                    "kind": "radioStation",
                    "format": "stream",
                    "stationHash": "CgkIBRoF7qCwygUQBA",
                    "hasDrm": true,
                    "mediaType": 0
                },
                "supportedDrms": [
                    "fairplay",
                    "playready",
                    "widevine"
                ],
                "url": "https://music.apple.com/us/station/apple-music-country/ra.1498157166"
            }
        },
        {
            "id": "ra.1498155548",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.1498155548",
            "attributes": {
                "isLive": true,
                "mediaKind": "audio",
                "name": "Apple Music Hits",
                "editorialNotes": {
                    "name": "Apple Music Hits",
                    "short": "Songs you know and love.",
                    "tagline": "Songs you know and love."
                },
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https://is4-ssl.mzstatic.com/image/thumb/Features114/v4/af/5f/6c/af5f6c79-5784-e57c-5202-531ece00e73b/U0MtTVMtV1ctQU1fSGl0cy5wbmc.png/{w}x{h}sr.jpg",
                    "bgColor": "f4f4f4",
                    "textColor1": "000000",
                    "textColor2": "10185f",
                    "textColor3": "292b34",
                    "textColor4": "323b7a"
                },
                "playParams": {
                    "id": "ra.1498155548",
                    "kind": "radioStation",
                    "format": "stream",
                    "stationHash": "CgkIBRoFnJSwygUQBA",
                    "hasDrm": true,
                    "mediaType": 0
                },
                "supportedDrms": [
                    "fairplay",
                    "playready",
                    "widevine"
                ],
                "url": "https://music.apple.com/us/station/apple-music-hits/ra.1498155548"
            }
        },
        {
            "id": "ra.978194965",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.978194965",
            "attributes": {
                "isLive": true,
                "name": "Apple Music 1",
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Apple Music 1",
                    "short": "The new music that matters.",
                    "tagline": "The new music that matters."
                },
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https://is2-ssl.mzstatic.com/image/thumb/Features114/v4/bd/c4/aa/bdc4aa17-bbe4-ccb0-c005-1514160727d2/U0MtTVMtV1ctQU1fMS5wbmc.png/{w}x{h}sr.jpg",
                    "bgColor": "f4f4f4",
                    "textColor1": "000000",
                    "textColor2": "120509",
                    "textColor3": "332628",
                    "textColor4": "33272a"
                },
                "url": "https://music.apple.com/us/station/apple-music-1/ra.978194965",
                "playParams": {
                    "id": "ra.978194965",
                    "kind": "radioStation",
                    "format": "stream",
                    "stationHash": "CgkIBRoFlaS40gMQBA",
                    "hasDrm": true,
                    "mediaType": 0
                },
                "supportedDrms": [
                    "fairplay",
                    "playready",
                    "widevine"
                ]
            }
        },
        {
            "id": "ra.985484166",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.985484166",
            "attributes": {
                "isLive": false,
                "name": "Alternative Station",
                "mediaKind": "audio",
                "editorialNotes": {
                    "name": "Alternative Station",
                    "standard": "The margins to mainstream.",
                    "short": "Apple Music Alternative",
                    "tagline": "Apple Music Alternative"
                },
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https://is5-ssl.mzstatic.com/image/thumb/Features125/v4/e6/bc/a8/e6bca8e2-29f1-2337-26f7-1b970994f45a/U0MtTVMtV1ctQWx0ZXJuYXRpdmUtQURBTV9JRD05ODU0ODQxNjYucG5n.png/{w}x{h}sr.jpg",
                    "bgColor": "4190f0",
                    "textColor1": "000000",
                    "textColor2": "0c0f12",
                    "textColor3": "152333",
                    "textColor4": "152333"
                },
                "url": "https://music.apple.com/us/station/alternative-station/ra.985484166",
                "playParams": {
                    "id": "ra.985484166",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgkIBBoFhpf11QMQAg",
                    "hasDrm": false,
                    "mediaType": 0
                }
            }
        }
    ]
}


```

## Endpoint

`GET https://api.music.apple.com/v1/me/recent/radio-stations`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `offset` (string): The offset to use for a paginated request.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Resource](resource.md)
  A resource—such as an album, song, or playlist.
- [Get Heavy Rotation Content](get-heavy-rotation-content.md)
  Fetch the resources in heavy rotation for the user.
- [Get Recently Played Resources](get-recently-played-resources.md)
  Fetch the recently played resources for the user.
- [Get Recently Played Tracks](get-v1-me-recent-played-tracks.md)
  Fetch the recently played tracks for the user.
- [Get Recently Added Resources](get-recently-added-resources.md)
  Fetch the resources recently added to the library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-recently-played-stations)*