# Get Catalog Search Hints

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch the search term results for a hint.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `results` object contains a single `terms` array. This array contains a list of possible valid search queries determined from the search hint. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

These results are autocompletion options for the hint and are potential search terms. For more information, see [`Search for Catalog Resources`](search-for-catalog-resources-(by-type).md).

##### Example

## See Also

- [object SearchHintsResponse](searchhintsresponse.md)
  The response to a request for search hints.
- [Search for Catalog Resources](search-for-catalog-resources-(by-type).md)
  Search the catalog by using a query.
- [Get Catalog Search Suggestions](get-catalog-search-suggesions.md)
  Fetch the search suggestions for a provided term input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-catalog-search-hints)*