# Add resource to favorites

**Framework**: Apple Music API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add the user’s resource to favorites.

**Availability**:
- Apple Music 1.0+

#### Discussion

This endpoint allows the user to favorite a resource. For example, if a customer favorites a song, the song is added to their `favorite songs` playlist. If they like an album or playlist, they can filter on `favorited album` in their library view.

If successful, the HTTP status code is 202 (Accepted) and there’s no response body. For requested IDs that the system can’t add to a user’s library, Apple Music Library ignores those IDs. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

> **Note**: Bulk additions of heterogenous types are permitted.

## Endpoint

`POST https://api.music.apple.com/v1/me/favorites`

## Parameters

### Query Parameters

- `ids` ([string]) *(required)*: The ids of the specific type.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object that `storefront` specifies. Otherwise, the default is `defaultLanguageTag` in `Storefront`.

## Responses

- `202` Accepted (`EmptyBodyResponse`, `application/json`): Request accepted.
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`): A response indicating an incorrect `Authorization` header.
- `403` Forbidden (`ForbiddenResponse`, `application/json`): A response indicating invalid or insufficient authentication.
- `500` Internal Server Error (`ErrorsResponse`, `application/json`): A response indicating an error occurred on the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/add-resource-to-favorites)*