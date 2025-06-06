# Get a Catalog Genre

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a genre by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single `Genre` object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

## See Also

- [object Genres](genres.md)
  A resource object that represents a music genre.
- [object GenresResponse](genresresponse.md)
  The response to a genres request.
- [Get Multiple Catalog Genres](get-multiple-genres.md)
  Fetch one or more genres for a specific storefront.
- [Get Catalog Top Charts Genres](get-all-genres.md)
  Fetch all genres for the current top charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-genre)*