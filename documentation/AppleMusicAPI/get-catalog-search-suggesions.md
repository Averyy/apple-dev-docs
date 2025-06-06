# Get Catalog Search Suggestions

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch the search suggestions for a provided term input.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `results` object contains a single `terms` array. This array contains a list of possible valid search queries determined from the search hint. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

## See Also

- [object SearchSuggestionsResponse](searchsuggestionsresponse.md)
  The response to a request for search suggestions.
- [Search for Catalog Resources](search-for-catalog-resources-(by-type).md)
  Search the catalog by using a query.
- [Get Catalog Search Hints](get-catalog-search-hints.md)
  Fetch the search term results for a hint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-catalog-search-suggesions)*