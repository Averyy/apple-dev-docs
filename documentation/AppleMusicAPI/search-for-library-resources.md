# Search for Library Resources

**Framework**: Apple Music API  
**Kind**: httpRequest

Search the library by using a query.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `results` contains a map of search results. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

## See Also

- [object LibrarySearchResponse](librarysearchresponse.md)
  The response to a request for a library search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/search-for-library-resources)*