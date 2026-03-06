# Get the User's Personal Apple Music Station

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch the current user’s personal Apple Music station.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/stations?filter[identity]=personal
```

**Response**:

```json
{
    "data": [
        {
            "id": "ra.u-741b035f6f0a85c81abb70ff757aa95f",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.u-741b035f6f0a85c81abb70ff757aa95f",
            "attributes": {
                "artwork": {
                    "width": 2400,
                    "height": 2400,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Features124/v4/7b/1d/f0/7b1df048-0017-8ac0-98c9-735f14849606/mza_7507996640781423701.png/{w}x{h}bb.jpg"
                },
                "name": "My Station",
                "mediaKind": "audio",
                "playParams": {
                    "id": "ra.u-741b035f6f0a85c81abb70ff757aa95f",
                    "kind": "radioStation",
                    "format": "tracks",
                    "stationHash": "CgoIByIGCPeqnL8HEAE",
                    "hasDrm": false,
                    "mediaType": 0
                },
                "url": "https: //music.apple.com/us/station/grace-lis-station/ra.u-741b035f6f0a85c81abb70ff757aa95f",
                "isLive": false
            }
        }
    ],
    "meta": {
        "filters": {
            "identity": {
                "personal": [
                    {
                        "id": "ra.u-741b035f6f0a85c81abb70ff757aa95f",
                        "type": "stations",
                        "href": "/v1/catalog/us/stations/ra.u-741b035f6f0a85c81abb70ff757aa95f"
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

- `filter[identity]` ([string]) *(required)*: A filter to apply to the request.
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
- [Get the Apple Music Live Radio Stations](get-the-apple-music-live-radio-stations.md)
  Fetch the Apple Music live radio stations for the storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-the-user's-personal-apple-music-station)*