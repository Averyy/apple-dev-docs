# Get Multiple Catalog Stations

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more stations by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/stations?ids=ra.1498157166
```

**Response**:

```json
{
    "data": [
        {
            "id": "ra.1498157166",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.1498157166",
            "attributes": {
                "playParams": {
                    "id": "ra.1498157166",
                    "kind": "radioStation",
                    "format": "stream",
                    "stationHash": "CgkIBRoF7qCwygUQBA",
                    "hasDrm": true,
                    "mediaType": 0
                },
                "editorialNotes": {
                    "name": "Apple Music Country",
                    "short": "Where it sounds like home.",
                    "tagline": "Where it sounds like home."
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
                "isLive": true,
                "mediaKind": "audio",
                "url": "https: //music.apple.com/us/station/apple-music-country/ra.1498157166",
                "name": "Apple Music Country"
            }
        }
    ]
}

```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/stations`

## Parameters

- `ids` ([string]) *(required)*: The unique identifiers for the stations. The maximum fetch limit is 100.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
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
- [Get the Apple Music Live Radio Stations](get-the-apple-music-live-radio-stations.md)
  Fetch the Apple Music live radio stations for the storefront.
- [Get the User's Personal Apple Music Station](get-the-user's-personal-apple-music-station.md)
  Fetch the current user’s personal Apple Music station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-catalog-stations)*