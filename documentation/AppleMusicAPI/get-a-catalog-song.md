# Get a Catalog Song

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a song by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

## See Also

- [object Songs](songs.md)
  A resource object that represents a song.
- [object SongsResponse](songsresponse.md)
  The response to a songs request.
- [Get a Catalog Song's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-56rq7.md)
  Fetch a song’s relationship by using its identifier.
- [Get Multiple Catalog Songs by ID](get-multiple-catalog-songs-by-id.md)
  Fetch one or more songs by using their identifiers.
- [Get Multiple Catalog Songs by ISRC](get-multiple-catalog-songs-by-isrc.md)
  Fetch one or more songs by using their International Standard Recording Code (ISRC) values.
- [Get Equivalent Catalog Songs by ID](get-equivalent-ids-for-the-albums-3ce20.md)
  Fetch the equivalent, available content in the storefront for the provided songs’ identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-catalog-song)*