# Get Catalog Search Hints

**Framework**: Apple Music API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetch the search term results for a hint.

**Availability**:
- Apple Music 1.0+

## Discussion

If successful, the HTTP status code is 200 (OK) and the `results` object contains a single `terms` array. This array contains a list of possible valid search queries determined from the search hint. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [Handling Requests and Responses](./handling-requests-and-responses.md).

These results are autocompletion options for the hint and are potential search terms. For more information, see [`Search for Catalog Resources`](./search-for-catalog-resources-%28by-type%29.md).

### Example

**Request**:

```
https://api.music.apple.com/v1/catalog/us/search/hints?term=beach+bunny
```

**Response**:

```json
{
    "results": {
        "terms": [
            "beach bunny",
            "oxygen beach bunny",
            "cloud 9 beach bunny"
        ]
    }
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/search/hints`

## Parameters

### Path Parameters

- `storefront` (string) *(required)*: An iTunes Store territory, specified by an ISO 3166 alpha-2 country code. The possible values are the `id` attributes of `Storefront` objects.

### Query Parameters

- `term` (string) *(required)*: The entered text for the search with ‘`+`’ characters between each word, to replace spaces (for example `term=james+br`).
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.

  **Default**: `10`

## Responses

- `200` OK (`SearchHintsResponse`, `application/json`): The request was successful.
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`): A response indicating an incorrect `Authorization` header.
- `500` Internal Server Error (`ErrorsResponse`, `application/json`): A response indicating an error occurred on the server.

## See Also

### Related Documentation
- [object SearchHintsResponse](./searchhintsresponse.md)
  The response to a request for search hints.
### Searching for Catalog Resources
- [Search for Catalog Resources](./search-for-catalog-resources-%28by-type%29.md)
  Search the catalog by using a query.
- [Get Catalog Search Suggestions](./get-catalog-search-suggesions.md)
  Fetch the search suggestions for a provided term input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-catalog-search-hints)*