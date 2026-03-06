# Get All Station Genres

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch all station genres for a given storefront.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/station-genres
```

**Response**:

```json
{
    "data": [
        {
            "id": "1149486245",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486245",
            "attributes": {
                "name": "Electronic"
            }
        },
        {
            "id": "1149486314",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486314",
            "attributes": {
                "name": "Latin"
            }
        },
        {
            "id": "1149486325",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486325",
            "attributes": {
                "name": "Metal"
            }
        },
        {
            "id": "1149486238",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486238",
            "attributes": {
                "name": "Dance"
            }
        },
        {
            "id": "1149486299",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486299",
            "attributes": {
                "name": "Jazz"
            }
        },
        {
            "id": "1149486336",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486336",
            "attributes": {
                "name": "Pop"
            }
        },
        {
            "id": "1149486287",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486287",
            "attributes": {
                "name": "Hip-Hop/R&B"
            }
        },
        {
            "id": "1149486381",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486381",
            "attributes": {
                "name": "Workout"
            }
        },
        {
            "id": "1149486231",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486231",
            "attributes": {
                "name": "Country"
            }
        },
        {
            "id": "1184713285",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1184713285",
            "attributes": {
                "name": "Holiday"
            }
        },
        {
            "id": "1149484144",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149484144",
            "attributes": {
                "name": "Alternative & Indie"
            }
        },
        {
            "id": "1149486361",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486361",
            "attributes": {
                "name": "Reggae"
            }
        },
        {
            "id": "1149486377",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486377",
            "attributes": {
                "name": "Singer/Songwriter"
            }
        },
        {
            "id": "1149486281",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486281",
            "attributes": {
                "name": "From Around the World"
            }
        },
        {
            "id": "1149486223",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486223",
            "attributes": {
                "name": "Christian"
            }
        },
        {
            "id": "1154291546",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1154291546",
            "attributes": {
                "name": "Hits by Decade"
            }
        },
        {
            "id": "1149486227",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486227",
            "attributes": {
                "name": "Classical"
            }
        },
        {
            "id": "1149486306",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486306",
            "attributes": {
                "name": "Kids & Family"
            }
        },
        {
            "id": "1149486365",
            "type": "station-genres",
            "href": "/v1/catalog/us/station-genres/1149486365",
            "attributes": {
                "name": "Rock"
            }
        }
    ]
}

```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/station-genres`

## Parameters

- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `offset` (string): The offset to use for a paginated request.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object StationGenres](stationgenres.md)
  A resource object that represents a station genre.
- [object StationGenresResponse](stationgenresresponse.md)
  The response to a specific station genres resource request.
- [Get a Station Genre](get-a-station-genre.md)
  Fetch a station genre by using its identifier.
- [Get a Station Genre’s Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-i4r0.md)
  Fetch a station genre’s relationship by using its identifier.
- [Get Multiple Stations Genres](get-multiple-stations-genres.md)
  Fetch one or more station genres by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-all-station-genres)*