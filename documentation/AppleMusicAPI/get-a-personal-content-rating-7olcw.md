# Get a Personal Library Song Rating

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a user’s rating for a library song by using the song’s library identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

A rating indicates whether a user likes `(1)` or dislikes `(-1)` the song. These are the only two ratings supported.

For a particular song, the personal ratings for that song’s catalog ID and library ID (if the song is in the library) stay synced.

##### Example

## See Also

- [object Ratings](ratings.md)
  An object that represents a rating for a resource.
- [object RatingRequest](ratingrequest.md)
  A request containing the data for a rating.
- [object RatingsResponse](ratingsresponse.md)
  The response to a request for a rating.
- [Get a Personal Library Album Rating](get-a-personal-content-rating-6c3b8.md)
  Fetch a user’s rating for specific content by using the content’s identifier.
- [Get a Personal Library Music Video Rating](get-a-personal-content-rating-4bir7.md)
  Fetch a user’s rating for a library music video by using the music video’s library identifier.
- [Get a Personal Library Playlist Rating](get-a-personal-content-rating-htyl.md)
  Fetch a user’s rating for a library playlist by using the playlist’s library identifier.
- [Get Multiple Personal Library Album Ratings](get-multiple-personal-content-ratings-5px7a.md)
  Fetch the user’s ratings for one or more pieces of content by using the contents’ identifiers.
- [Get Multiple Personal Library Music Video Ratings](get-multiple-personal-content-ratings-63ybs.md)
  Fetch the user’s ratings for one or more library music videos by using the library music videos’ identifiers.
- [Get Multiple Personal Library Playlist Ratings](get-multiple-personal-content-ratings-25kr7.md)
  Fetch the user’s ratings for one or more library playlists by using the library playlists’ identifiers.
- [Get Multiple Personal Library Songs Ratings](get-multiple-personal-content-ratings-1bod7.md)
  Fetch the user’s ratings for one or more library songs by using the library songs’ identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-personal-content-rating-7olcw)*