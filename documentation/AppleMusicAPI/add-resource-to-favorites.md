# Add resource to favorites

**Framework**: Apple Music API  
**Kind**: httpRequest

Add the user’s resource to favorites.

**Availability**:
- Apple Music 1.0+

#### Discussion

This endpoint allows the user to favorite a resource. For example, if a customer favorites a song, the song is added to their `favorite songs` playlist. If they like an album or playlist, they can filter on `favorited album` in their library view.

If successful, the HTTP status code is 202 (Accepted) and there’s no response body. For requested IDs that the system can’t add to a user’s library, Apple Music Library ignores those IDs. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

> **Note**: Bulk additions of heterogenous types are permitted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/add-resource-to-favorites)*