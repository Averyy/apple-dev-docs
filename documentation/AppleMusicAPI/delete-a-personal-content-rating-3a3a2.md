# Delete a Personal Song Rating

**Framework**: Apple Music API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Remove a user’s song rating by using the song’s identifier.

**Availability**:
- Apple Music 1.0+

## Discussion

This endpoint requires a music user token. For more information, see [User Authentication for MusicKit](./user-authentication-for-musickit.md).

A rating indicates whether a user likes `(1)` or dislikes `(-1)` the song. These are the only two ratings supported.

For a particular song, the personal ratings for that son’s catalog ID and library ID (if the playlist is in the library) stay synced.

### Example

**Request**:

```
https://api.music.apple.com/v1/me/ratings/songs/907242702
```

**Response**:

```json
No response body.
```

## Endpoint

`DELETE https://api.music.apple.com/v1/me/ratings/songs/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the song.

### Query Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.

## Responses

- `204` No Content (`EmptyBodyResponse`, `application/json`): The modification was successful, but there’s no content in the response.
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`): A response indicating an incorrect `Authorization` header.
- `403` Forbidden (`ForbiddenResponse`, `application/json`): A response indicating invalid or insufficient authentication.
- `500` Internal Server Error (`ErrorsResponse`, `application/json`): A response indicating an error occurred on the server.

## See Also

### Related Documentation
- [object Ratings](./ratings.md)
  An object that represents a rating for a resource.
### Deleting Catalog Ratings
- [Delete a Personal Album Rating](./delete-a-personal-content-rating-863sx.md)
  Remove a user’s album rating by using the album’s identifier.
- [Delete a Personal Music Video Rating](./delete-a-personal-content-rating-9xd3d.md)
  Remove a user’s music video rating by using the music video’s identifier.
- [Delete a Personal Playlist Rating](./delete-a-personal-content-rating-mv3a.md)
  Remove a user’s playlist rating by using the playlist’s identifier.
- [Delete a Personal Station Rating](./delete-a-personal-content-rating-7pbcr.md)
  Remove a user’s station rating by using the station’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/delete-a-personal-content-rating-3a3a2)*