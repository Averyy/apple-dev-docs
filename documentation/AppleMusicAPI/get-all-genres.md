# Get Catalog Top Charts Genres

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch all genres for the current top charts.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains an array of `Genre` objects. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

## See Also

- [object Genres](genres.md)
  A resource object that represents a music genre.
- [object GenresResponse](genresresponse.md)
  The response to a genres request.
- [Get a Catalog Genre](get-a-genre.md)
  Fetch a genre by using its identifier.
- [Get Multiple Catalog Genres](get-multiple-genres.md)
  Fetch one or more genres for a specific storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-all-genres)*