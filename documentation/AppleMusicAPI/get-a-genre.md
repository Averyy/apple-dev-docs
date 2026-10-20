# Get a Catalog Genre

**Framework**: Apple Music API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetch a genre by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single `Genre` object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [Handling Requests and Responses](./handling-requests-and-responses.md).

##### Example

**Request**:

```
https://api.music.apple.com/v1/catalog/us/genres/14
```

**Response**:

```json
{
    "data": [
        {
            "attributes": {
                "name": "Pop"
            },
            "href": "/v1/catalog/us/genres/14",
            "id": "14",
            "type": "genres"
        }
    ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/genres/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the genre.
- `storefront` (string) *(required)*: An iTunes Store territory, specified by an ISO 3166 alpha-2 country code. The possible values are the `id` attributes of `Storefront` objects.

### Query Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## Responses

- `200` OK (`GenresResponse`, `application/json`): The request was successful.
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`): A response indicating an incorrect `Authorization` header.
- `500` Internal Server Error (`ErrorsResponse`, `application/json`): A response indicating an error occurred on the server.

## See Also

### Related Documentation
- [object Genres](./genres.md)
  A resource object that represents a music genre.
- [object GenresResponse](./genresresponse.md)
  The response to a genres request.
### Requesting Catalog Genres
- [Get Multiple Catalog Genres](./get-multiple-genres.md)
  Fetch one or more genres for a specific storefront.
- [Get Catalog Top Charts Genres](./get-all-genres.md)
  Fetch all genres for the current top charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-genre)*