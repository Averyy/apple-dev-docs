# Delete a Personal Music Video Rating

**Framework**: Apple Music API  
**Kind**: httpRequest

Remove a user’s music video rating by using the music video’s identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

A rating indicates whether a user likes `(1)` or dislikes `(-1)` the music video. These are the only two ratings supported.

For a particular music video, the personal ratings for that video’s catalog ID and library ID (if the video is in the library) stay synced.

##### Example

## See Also

- [object Ratings](ratings.md)
  An object that represents a rating for a resource.
- [Delete a Personal Album Rating](delete-a-personal-content-rating-863sx.md)
  Remove a user’s album rating by using the album’s identifier.
- [Delete a Personal Playlist Rating](delete-a-personal-content-rating-mv3a.md)
  Remove a user’s playlist rating by using the playlist’s identifier.
- [Delete a Personal Song Rating](delete-a-personal-content-rating-3a3a2.md)
  Remove a user’s song rating by using the song’s identifier.
- [Delete a Personal Station Rating](delete-a-personal-content-rating-7pbcr.md)
  Remove a user’s station rating by using the station’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/delete-a-personal-content-rating-9xd3d)*