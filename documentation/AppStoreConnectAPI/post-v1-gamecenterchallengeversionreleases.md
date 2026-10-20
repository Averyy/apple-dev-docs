# Add a Challenge Version Release

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a version release for a specific Game Center challenge version.

**Availability**:
- App Store Connect API 4.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Mentions

- [Configuring Game Center challenges](./configuring-game-center-challenges.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterChallengeVersionReleases`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterChallengeVersionReleaseCreateRequest`

## Responses

- `201` Created (`GameCenterChallengeVersionReleaseResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing version releases
- [Read Challenge Version Release Information](./get-v1-gamecenterchallengeversionreleases-_id_.md)
  Get information for a specific Game Center challenge version release.
- [Delete a Challenge Version Release](./delete-v1-gamecenterchallengeversionreleases-_id_.md)
  Remove a specific version release from a Game Center challenge version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenterchallengeversionreleases)*