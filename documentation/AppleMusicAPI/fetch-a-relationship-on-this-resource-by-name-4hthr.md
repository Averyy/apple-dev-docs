# Get a Catalog Album's Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch an album’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

## See Also

- [object Albums](albums.md)
  A resource object that represents an album.
- [object AlbumsResponse](albumsresponse.md)
  The response to an albums request.
- [Get a Catalog Album](get-a-catalog-album.md)
  Fetch an album by using its identifier.
- [Get a Catalog Album’s Relationship View Directly by Name](fetch-a-view-on-this-resource-by-name-2we6l.md)
  Fetch related resources for a single album’s relationship view.
- [Get Multiple Catalog Albums](get-multiple-catalog-albums.md)
  Fetch one or more albums by using their identifiers.
- [Get Multiple Catalog Albums by UPC](get-multiple-catalog-albums-by-upc.md)
  Fetch one or more albums by using their UPC values.
- [Get Equivalent Catalog Albums by ID](get-equivalent-ids-for-the-albums-8aky3.md)
  Fetch the equivalent, available content in the storefront for the provided albums’ identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-4hthr)*