# Get All Library Albums

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch all the library albums in alphabetical order.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

## See Also

- [object LibraryAlbums](libraryalbums.md)
  A resource object that represents a library album.
- [object LibraryAlbumsResponse](libraryalbumsresponse.md)
  The response to a library albums request.
- [Get a Library Album](get-a-library-album.md)
  Fetch a library album by using its identifier.
- [Get a Library Album's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-165fz.md)
  Fetch a library album’s relationship by using its identifier.
- [Get Multiple Library Albums](get-multiple-library-albums.md)
  Fetch one or more library albums by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-all-library-albums)*