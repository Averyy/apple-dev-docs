# Get a Station Genre

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a station genre by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/station-genres/1149486336
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

`GET https://api.music.apple.com/v1/catalog/{storefront}/station-genres/{id}`

## Parameters

- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object StationGenres](stationgenres.md)
  A resource object that represents a station genre.
- [object StationGenresResponse](stationgenresresponse.md)
  The response to a specific station genres resource request.
- [Get a Station Genre’s Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-i4r0.md)
  Fetch a station genre’s relationship by using its identifier.
- [Get Multiple Stations Genres](get-multiple-stations-genres.md)
  Fetch one or more station genres by using their identifiers.
- [Get All Station Genres](get-all-station-genres.md)
  Fetch all station genres for a given storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-station-genre)*