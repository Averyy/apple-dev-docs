# Get Multiple Library Songs

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more library songs by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

## See Also

- [object LibrarySongs](librarysongs.md)
  A resource object that represents a library song.
- [object LibrarySongsResponse](librarysongsresponse.md)
  The response to a library songs request.
- [Get a Library Song](get-a-library-song.md)
  Fetch a library song by using its identifier.
- [Get a Library Song's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-9xvg6.md)
  Fetch a library song’s relationship by using its identifier.
- [Get All Library Songs](get-all-library-songs.md)
  Fetch all the library songs in alphabetical order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-library-songs)*