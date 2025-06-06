# Get a Library Music Video

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a library music video by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

## See Also

- [object LibraryMusicVideos](librarymusicvideos.md)
  A resource object that represents a library music video.
- [object LibraryMusicVideosResponse](librarymusicvideosresponse.md)
  The response to a library music videos request.
- [Get a Library Music Video's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-419dz.md)
  Fetch a library music video’s relationship by using its identifier.
- [Get Multiple Library Music Videos](get-multiple-library-music-videos.md)
  Fetch one or more library music videos by using their identifiers.
- [Get All Library Music Videos](get-all-library-music-videos.md)
  Fetch all the library music videos in alphabetical order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-library-music-video)*