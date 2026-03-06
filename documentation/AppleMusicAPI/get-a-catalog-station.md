# Get a Catalog Station

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a station by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/stations/ra.1498157166
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
                "mediaKind": "audio",
                "isLive": true,
                "name": "Apple Music Country",
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
                "editorialNotes": {
                    "name": "Apple Music Country",
                    "short": "Where it sounds like home.",
                    "tagline": "Where it sounds like home."
                },
                "url": "https: //music.apple.com/us/station/apple-music-country/ra.1498157166"
            }
        }
    ]
}

```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/stations/{id}`

## Parameters

- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Stations](stations.md)
  A resource object that represents a station.
- [object StationsResponse](stationsresponse.md)
  The response to a stations request.
- [Get a Catalog Station's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-38wmf.md)
  Fetch a station’s relationship using its identifier.
- [Get Multiple Catalog Stations](get-multiple-catalog-stations.md)
  Fetch one or more stations by using their identifiers.
- [Get the Apple Music Live Radio Stations](get-the-apple-music-live-radio-stations.md)
  Fetch the Apple Music live radio stations for the storefront.
- [Get the User's Personal Apple Music Station](get-the-user's-personal-apple-music-station.md)
  Fetch the current user’s personal Apple Music station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-catalog-station)*