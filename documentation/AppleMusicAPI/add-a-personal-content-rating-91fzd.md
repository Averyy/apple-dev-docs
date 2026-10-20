# Add a Personal Library Playlist Rating

**Framework**: Apple Music API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a user’s library playlist rating by using the library playlist’s identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

This endpoint requires a music user token. For more information, see [User Authentication for MusicKit](./user-authentication-for-musickit.md).

A rating indicates whether a user likes `(1)` or dislikes `(-1)` the playlist. These are the only two ratings supported.

For a particular playlist, the personal ratings for that playlist’s catalog ID and library ID (if the playlist is in the library) stay synced.

##### Example

**Request**:

```
https://api.music.apple.com/v1/me/ratings/library-playlists/p.MoGJYM3CYXW09B

{
    "type":"rating",
    "attributes":{
        "value":1
    }
}
```

**Response**:

```json
{
   "data":[
      {
         "id":"p.MoGJYM3CYXW09B",
         "type":"ratings",
         "href":"/v1/me/ratings/library-playlists/p.MoGJYM3CYXW09B",
         "attributes":{
            "value":1
         }
      }
   ]
}
```

## Endpoint

`PUT https://api.music.apple.com/v1/me/ratings/library-playlists/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the library playlist.

### Query Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.

## Request Body

**Content-Type**: `application/json`  
**Type**: `RatingRequest`

A dictionary that includes the type and attributes of the resource rating.

## Responses

- `200` OK (`RatingsResponse`, `application/json`): The request was successful.
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`): A response indicating an incorrect `Authorization` header.
- `403` Forbidden (`ForbiddenResponse`, `application/json`): A response indicating invalid or insufficient authentication.
- `500` Internal Server Error (`ErrorsResponse`, `application/json`): A response indicating an error occurred on the server.

## See Also

### Related Documentation
- [object Ratings](./ratings.md)
  An object that represents a rating for a resource.
- [object RatingsResponse](./ratingsresponse.md)
  The response to a request for a rating.
### Adding Library Ratings
- [Add a Personal Library Album Rating](./add-a-personal-content-rating-98xt0.md)
  Add a user’s content rating by using the content’s identifier.
- [Add a Personal Library Music Video Rating](./add-a-personal-content-rating-58x8v.md)
  Add a user’s library music video rating by using the library music video’s identifier.
- [Add a Personal Library Song Rating](./add-a-personal-content-rating-8z1fn.md)
  Add a user’s library song rating by using the library song’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/add-a-personal-content-rating-91fzd)*