# Delete a Personal Library Song Rating

**Framework**: Apple Music API  
**Kind**: httpRequest

Remove a user’s library song rating by using the library song’s identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

A rating indicates whether a user likes `(1`) or dislikes `(-1)` the song. These are the only two ratings supported.

For a particular song, the personal ratings for that song’s catalog ID and library ID (if the song is in the library) stay synced.

##### Example

## See Also

- [object Ratings](ratings.md)
  An object that represents a rating for a resource.
- [Delete a Personal Library Album Rating](delete-a-personal-content-rating-32o8r.md)
  Remove a user’s content rating by using the content’s identifier.
- [Delete a Personal Library Music Video Rating](delete-a-personal-content-rating-1vj60.md)
  Remove a user’s library music video rating by using the library music video’s identifier.
- [Delete a Personal Library Playlist Rating](delete-a-personal-content-rating-7vxs6.md)
  Remove a user’s library playlist rating by using the library playlist’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/delete-a-personal-content-rating-2k02e)*