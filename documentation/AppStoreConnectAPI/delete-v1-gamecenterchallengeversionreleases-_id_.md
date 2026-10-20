# Delete a Challenge Version Release

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Remove a specific version release from a Game Center challenge version.

**Availability**:
- App Store Connect API 4.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/gameCenterChallengeVersionReleases/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing version releases
- [Add a Challenge Version Release](./post-v1-gamecenterchallengeversionreleases.md)
  Add a version release for a specific Game Center challenge version.
- [Read Challenge Version Release Information](./get-v1-gamecenterchallengeversionreleases-_id_.md)
  Get information for a specific Game Center challenge version release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecenterchallengeversionreleases-_id_)*