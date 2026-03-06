# Get Catalog Search Suggestions

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch the search suggestions for a provided term input.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `results` object contains a single `terms` array. This array contains a list of possible valid search queries determined from the search hint. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/search/suggestions?term=beach+bunny&kinds=terms
```

**Response**:

```json
{
    "results": {
        "suggestions": [
            {
                "kind": "terms",
                "searchTerm": "beach bunny",
                "displayTerm": "beach bunny"
            },
            {
                "kind": "terms",
                "searchTerm": "oxygen beach bunny",
                "displayTerm": "oxygen beach bunny"
            },
            {
                "kind": "terms",
                "searchTerm": "cloud 9 beach bunny",
                "displayTerm": "cloud 9 beach bunny"
            }
        ]
    }
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/search/suggestions`

## Parameters

- `kinds` ([string]) *(required)*: The suggestion kinds to include in the results.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `term` (string) *(required)*: The text input to use for search suggestions.
- `types` ([string]): The resource types to include in the `topResults` (has no effect on the terms).

## See Also

- [object SearchSuggestionsResponse](searchsuggestionsresponse.md)
  The response to a request for search suggestions.
- [Search for Catalog Resources](search-for-catalog-resources-(by-type).md)
  Search the catalog by using a query.
- [Get Catalog Search Hints](get-catalog-search-hints.md)
  Fetch the search term results for a hint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-catalog-search-suggesions)*