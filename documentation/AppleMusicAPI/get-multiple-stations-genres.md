# Get Multiple Stations Genres

**Framework**: Apple Music API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetch one or more station genres by using their identifiers.

**Availability**:
- Apple Music 1.0+

## Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [Handling Requests and Responses](./handling-requests-and-responses.md).

### Example

**Request**:

```
https://api.music.apple.com/v1/catalog/us/station-genres?ids=1149486336
```

**Response**:

```json
{
    "data": [
        {
            "id": "1149486336",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486336",
            "attributes": {
                "name": "Pop"
            }
        }
    ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/station-genres`

## Parameters

### Path Parameters

- `storefront` (string) *(required)*: An iTunes Store territory, specified by an ISO 3166 alpha-2 country code. The possible values are the `id` attributes of `Storefront` objects.

### Query Parameters

- `ids` ([string]) *(required)*: The unique identifiers for the station genres.
- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## Responses

- `200` OK (`StationGenresResponse`, `application/json`): The request was successful.
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`): A response indicating an incorrect `Authorization` header.
- `500` Internal Server Error (`ErrorsResponse`, `application/json`): A response indicating an error occurred on the server.

## See Also

### Related Documentation
- [object StationGenres](./stationgenres.md)
  A resource object that represents a station genre.
- [object StationGenresResponse](./stationgenresresponse.md)
  The response to a specific station genres resource request.
### Requesting a Catalog Station Genre
- [Get a Station Genre](./get-a-station-genre.md)
  Fetch a station genre by using its identifier.
- [Get a Station Genre’s Relationship Directly by Name](./fetch-a-relationship-on-this-resource-by-name-i4r0.md)
  Fetch a station genre’s relationship by using its identifier.
- [Get All Station Genres](./get-all-station-genres.md)
  Fetch all station genres for a given storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-stations-genres)*