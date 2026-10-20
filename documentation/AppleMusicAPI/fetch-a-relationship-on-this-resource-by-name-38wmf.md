# Get a Catalog Station's Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetch a station’s relationship using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

##### Example

**Request**:

```
https://api.music.apple.com/v1/catalog/us/stations/ra.1582049480/radio-show
```

**Response**:

```json
{    
     "data": [
        {
            "id": "1496850205",
            "type": "apple-curators",
            "href": "/v1/catalog/us/apple-curators/1496850205",
            "attributes": {
                "kind": "Show",
                "name": "Easy Hits Radio with Sabi",
                "showHostName": "Sabi",
                "editorialNotes": {
                    "name": "Easy Hits Radio with Sabi",
                    "standard": "Sometimes all it takes to turn a day around is the warm ring of a familiar tune. On Apple Music, we created a show just for that. From Fleetwood Mac's “Dreams” to John Legend's “All of Me,” Easy Hits Radio is your home for the lighter side of pop.",
                    "short": "Low-key songs to help you unwind.",
                    "tagline": "Sabi"
                },
                "artwork": {
                    "width": 1080,
                    "height": 1080,
                    "url": "https://is2-ssl.mzstatic.com/image/thumb/Features124/v4/91/1a/d8/911ad8da-6d42-6b06-e883-19ff6c7f3ba1/QkwtTVMtV1ctRWFzeUhpdHNSYWRpb19BREFNX0lEPTE0OTY4NTAyMDVfbmV3bG9nby5wbmc.png/{w}x{h}bb.jpg",
                    "bgColor": "f4f4f4",
                    "textColor1": "090909",
                    "textColor2": "131212",
                    "textColor3": "2a2a2a",
                    "textColor4": "353434"
                },
                "shortName": "Easy Hits Radio",
                "url": "https://music.apple.com/us/curator/easy-hits-radio-with-sabi/1496850205"
            }
        }
    ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/stations/{id}/{relationship}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the station.
- `relationship` (string) *(required)*: The name of the relationship you want to fetch for the resource.

  **Allowed Values**: `radio-show`
- `storefront` (string) *(required)*: An iTunes Store territory, specified by an ISO 3166 alpha-2 country code. The possible values are the `id` attributes of `Storefront` objects.

### Query Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.
- `limit` (integer): The maximum number of related resources from the relationship.

## Responses

- `200` OK (`RelationshipResponse`, `application/json`): The request was successful.
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`): A response indicating an incorrect `Authorization` header.
- `500` Internal Server Error (`ErrorsResponse`, `application/json`): A response indicating an error occurred on the server.

## See Also

### Related Documentation
- [object Stations](./stations.md)
  A resource object that represents a station.
- [object StationsResponse](./stationsresponse.md)
  The response to a stations request.
### Requesting a Catalog Station
- [Get a Catalog Station](./get-a-catalog-station.md)
  Fetch a station by using its identifier.
- [Get Multiple Catalog Stations](./get-multiple-catalog-stations.md)
  Fetch one or more stations by using their identifiers.
- [Get the Apple Music Live Radio Stations](./get-the-apple-music-live-radio-stations.md)
  Fetch the Apple Music live radio stations for the storefront.
- [Get the User's Personal Apple Music Station](./get-the-users-personal-apple-music-station.md)
  Fetch the current user’s personal Apple Music station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-38wmf)*