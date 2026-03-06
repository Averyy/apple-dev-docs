# Add a Personal Album Rating

**Framework**: Apple Music API  
**Kind**: httpRequest

Add a user’s album rating by using the album’s identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

A rating indicates whether a user likes `(1)` or dislikes `(-1)` the album. These are the only two ratings supported.

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/ratings/albums/1138988512

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
            "id":"1138988512",
            "type":"ratings",
            "href":"/v1/me/ratings/albums/1138988512",
            "attributes":{
                "value":1
            }
        }
    ]
}
```

## Endpoint

`PUT https://api.music.apple.com/v1/me/ratings/albums/{id}`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.

## Request Body

A dictionary that includes the type and attributes of the resource rating.

## See Also

- [object Ratings](ratings.md)
  An object that represents a rating for a resource.
- [object RatingsResponse](ratingsresponse.md)
  The response to a request for a rating.
- [Add a Personal Music Video Rating](add-a-personal-content-rating-8hke5.md)
  Add a user’s music video rating by using the music video’s identifier.
- [Add a Personal Playlist Rating](add-a-personal-content-rating-76n4r.md)
  Add a user’s playlist rating by using the playlist’s identifier.
- [Add a Personal Song Rating](add-a-personal-content-rating-33dop.md)
  Add a user’s song rating by using the song’s identifier.
- [Add a Personal Station Rating](add-a-personal-content-rating-8zlgo.md)
  Add a user’s station rating by using the station’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/add-a-personal-content-rating-4zesn)*