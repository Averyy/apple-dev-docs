# Search for Catalog Resources

**Framework**: Apple Music API  
**Kind**: httpRequest

Search the catalog by using a query.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `results` contains a map of search results. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

## See Also

- [object SearchResponse](searchresponse.md)
  The response to a search request.
- [Get Catalog Search Hints](get-catalog-search-hints.md)
  Fetch the search term results for a hint.
- [Get Catalog Search Suggestions](get-catalog-search-suggesions.md)
  Fetch the search suggestions for a provided term input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/search-for-catalog-resources-(by-type))*