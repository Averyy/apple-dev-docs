# Add a Resource to a Library

**Framework**: Apple Music API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a catalog resource to a user’s iCloud Music Library.

**Availability**:
- Apple Music 1.0+

## Discussion

If successful, the HTTP status code is 202 (Accepted) and there is no response body. For requested IDs that can’t be added to a user’s library, Apple Music Library ignores those IDs. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [User Authentication for MusicKit](./user-authentication-for-musickit.md).

> **Note**:  There may be a delay before a new resource appears in a user’s library.

### Example

**Request**:

```
https://api.music.apple.com/v1/me/library?ids[albums]=1577502911
```

**Response**:

```json
No response body
```

## Endpoint

`POST https://api.music.apple.com/v1/me/library`

## Parameters

### Query Parameters

- `ids` ([string]) *(required)*: The unique catalog identifiers for the resources. To indicate the type of resource to add, follow the `ids` with one of the allowed values. Add multiple types in the same request.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object that `storefront` specifies. Otherwise, the default is `defaultLanguageTag` in `Storefront`.

## Responses

- `202` Accepted (`EmptyBodyResponse`, `application/json`): Although the modification request was acceptable, it may not have completed.
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`): A response indicating an incorrect `Authorization` header.
- `403` Forbidden (`ForbiddenResponse`, `application/json`): A response indicating invalid or insufficient authentication.
- `500` Internal Server Error (`ErrorsResponse`, `application/json`): A response indicating an error occurred on the server.

## See Also

### Related Documentation
- [object Resource](./resource.md)
  A resource—such as an album, song, or playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/add-a-resource-to-a-library)*