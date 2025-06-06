# Get Multiple Personal Playlist Ratings

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch the user’s ratings for one or more playlists by using the playlists’ identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

A rating indicates whether a user likes `(1)` or dislikes `(-1)` the playlist. These are the only two ratings supported.

For a particular playlist, the personal ratings for that playlist’s catalog ID and library ID (if the playlist is in the library) stay synced.

##### Example

## See Also

- [object Ratings](ratings.md)
  An object that represents a rating for a resource.
- [object RatingRequest](ratingrequest.md)
  A request containing the data for a rating.
- [object RatingsResponse](ratingsresponse.md)
  The response to a request for a rating.
- [Get a Personal Album Rating](get-a-personal-content-rating-1q2mb.md)
  Fetch a user’s rating for an album by using the user’s identifier.
- [Get a Personal Music Video Rating](get-a-personal-content-rating-8doe0.md)
  Fetch a user’s rating for a music video by using the video’s identifier.
- [Get a Personal Playlist Rating](get-a-personal-content-rating-6wib7.md)
  Fetch a user’s rating for a playlist by using the playlist’s identifier.
- [Get a Personal Song Rating](get-a-personal-content-rating-4k9c0.md)
  Fetch a user’s rating for a song by using the song’s identifier.
- [Get a Personal Station Rating](get-a-personal-content-rating-try2.md)
  Fetch a user’s rating for a station by using the station’s identifier.
- [Get Multiple Personal Album Ratings](get-multiple-personal-content-ratings-8tjvr.md)
  Fetch the user’s ratings for one or more albums by using the albums’ identifiers.
- [Get Multiple Personal Music Video Ratings](get-multiple-personal-content-ratings-74o7x.md)
  Fetch the user’s ratings for one or more music videos by using the music videos’ identifiers.
- [Get Multiple Personal Song Ratings](get-multiple-personal-content-ratings-6wab5.md)
  Fetch the user’s ratings for one or more songs by using the songs’ identifiers.
- [Get Multiple Personal Station Ratings](get-multiple-personal-content-ratings-7ycdc.md)
  Fetch the user’s ratings for one or more stations by using the stations’ identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-personal-content-ratings-7i7bv)*