# Get the Apple Music Live Radio Stations

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch the Apple Music live radio stations for the storefront.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/stations?filter[featured]=apple-music-live-radio
```

**Response**:

```json
{
    "data": [
        {
            "id": "ra.978194965",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.978194965",
            "attributes": {
                "isLive": true,
                "url": "https: //music.apple.com/us/station/apple-music-1/ra.978194965",
                "editorialNotes": {
                    "name": "Apple Music 1",
                    "short": "The new music that matters.",
                    "tagline": "The new music that matters."
                },
                "playParams": {
                    "id": "ra.978194965",
                    "kind": "radioStation",
                    "format": "stream",
                    "stationHash": "CgkIBRoFlaS40gMQBA",
                    "hasDrm": true,
                    "mediaType": 0
                },
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Features114/v4/bd/c4/aa/bdc4aa17-bbe4-ccb0-c005-1514160727d2/U0MtTVMtV1ctQU1fMS5wbmc.png/{w}x{h}sr.jpg",
                    "bgColor": "f4f4f4",
                    "textColor1": "000000",
                    "textColor2": "120509",
                    "textColor3": "332628",
                    "textColor4": "33272a"
                },
                "supportedDrms": [
                    "fairplay",
                    "playready",
                    "widevine"
                ],
                "name": "Apple Music 1",
                "mediaKind": "audio"
            }
        },
        {
            "id": "ra.1498155548",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.1498155548",
            "attributes": {
                "isLive": true,
                "url": "https: //music.apple.com/us/station/apple-music-hits/ra.1498155548",
                "editorialNotes": {
                    "name": "Apple Music Hits",
                    "short": "Songs you know and love.",
                    "tagline": "Songs you know and love."
                },
                "playParams": {
                    "id": "ra.1498155548",
                    "kind": "radioStation",
                    "format": "stream",
                    "stationHash": "CgkIBRoFnJSwygUQBA",
                    "hasDrm": true,
                    "mediaType": 0
                },
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Features114/v4/af/5f/6c/af5f6c79-5784-e57c-5202-531ece00e73b/U0MtTVMtV1ctQU1fSGl0cy5wbmc.png/{w}x{h}sr.jpg",
                    "bgColor": "f4f4f4",
                    "textColor1": "000000",
                    "textColor2": "10185f",
                    "textColor3": "292b34",
                    "textColor4": "323b7a"
                },
                "supportedDrms": [
                    "fairplay",
                    "playready",
                    "widevine"
                ],
                "name": "Apple Music Hits",
                "mediaKind": "audio"
            }
        },
        {
            "id": "ra.1498157166",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.1498157166",
            "attributes": {
                "isLive": true,
                "url": "https: //music.apple.com/us/station/apple-music-country/ra.1498157166",
                "editorialNotes": {
                    "name": "Apple Music Country",
                    "short": "Where it sounds like home.",
                    "tagline": "Where it sounds like home."
                },
                "playParams": {
                    "id": "ra.1498157166",
                    "kind": "radioStation",
                    "format": "stream",
                    "stationHash": "CgkIBRoF7qCwygUQBA",
                    "hasDrm": true,
                    "mediaType": 0
                },
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Features114/v4/89/e2/66/89e266ee-454e-87e7-e108-dea53c54da6a/U0MtTVMtV1ctQU1fQ291bnRyeS5wbmc.png/{w}x{h}sr.jpg",
                    "bgColor": "f4f4f4",
                    "textColor1": "000000",
                    "textColor2": "142234",
                    "textColor3": "3a412d",
                    "textColor4": "364354"
                },
                "supportedDrms": [
                    "fairplay",
                    "playready",
                    "widevine"
                ],
                "name": "Apple Music Country",
                "mediaKind": "audio"
            }
        }
    ],
    "meta": {
        "filters": {
            "featured": {
                "apple-music-live-radio": [
                    {
                        "id": "ra.978194965",
                        "type": "stations",
                        "href": "/v1/catalog/us/stations/ra.978194965"
                    },
                    {
                        "id": "ra.1498155548",
                        "type": "stations",
                        "href": "/v1/catalog/us/stations/ra.1498155548"
                    },
                    {
                        "id": "ra.1498157166",
                        "type": "stations",
                        "href": "/v1/catalog/us/stations/ra.1498157166"
                    }
                ]
            }
        }
    }
}

```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/stations`

## Parameters

- `filter[featured]` ([string]) *(required)*: A filter to apply to the request. The maximum fetch limit is 1.
- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Stations](stations.md)
  A resource object that represents a station.
- [object StationsResponse](stationsresponse.md)
  The response to a stations request.
- [Get a Catalog Station](get-a-catalog-station.md)
  Fetch a station by using its identifier.
- [Get a Catalog Station's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-38wmf.md)
  Fetch a station’s relationship using its identifier.
- [Get Multiple Catalog Stations](get-multiple-catalog-stations.md)
  Fetch one or more stations by using their identifiers.
- [Get the User's Personal Apple Music Station](get-the-user's-personal-apple-music-station.md)
  Fetch the current user’s personal Apple Music station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-the-apple-music-live-radio-stations)*