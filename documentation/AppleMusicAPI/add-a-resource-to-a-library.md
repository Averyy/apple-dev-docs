# Add a Resource to a Library

**Framework**: Apple Music API  
**Kind**: httpRequest

Add a catalog resource to a user’s iCloud Music Library.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 202 (Accepted) and there is no response body. For requested IDs that can’t be added to a user’s library, Apple Music Library ignores those IDs. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

> **Note**:  There may be a delay before a new resource appears in a user’s library.

 There may be a delay before a new resource appears in a user’s library.

##### Example

## See Also

- [object Resource](resource.md)
  A resource—such as an album, song, or playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/add-a-resource-to-a-library)*