# Get a Library Artist

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a library artist by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

## See Also

- [object LibraryArtists](libraryartists.md)
  A resource object that represents an artist present in a user’s library.
- [object LibraryArtistsResponse](libraryartistsresponse.md)
  The response to a library artists request.
- [Get a Library Artist's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-9dsoc.md)
  Fetch a library artist’s relationship by using its identifier.
- [Get Multiple Library Artists](get-multiple-library-artists.md)
  Fetch one or more library artists by using their identifiers.
- [Get All Library Artists](get-all-library-artists.md)
  Fetch all the library artists in alphabetical order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-library-artist)*