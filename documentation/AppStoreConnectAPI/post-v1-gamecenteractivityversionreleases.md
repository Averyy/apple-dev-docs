# Add an Activity Version Release

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a version release for a specific Game Center activity.

**Availability**:
- App Store Connect API 4.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Mentions

- [Configuring Game center activities](./configuring-game-center-activities.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterActivityVersionReleases`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterActivityVersionReleaseCreateRequest`

## Responses

- `201` Created (`GameCenterActivityVersionReleaseResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Read, create, and update Game Center activity versions
- [Read Activity Version Release Information](./get-v1-gamecenteractivityversionreleases-_id_.md)
  Get information for a specific Game Center activity version release.
- [Delete an Activity Version Release](./delete-v1-gamecenteractivityversionreleases-_id_.md)
  Remove a specific version release from a Game Center activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenteractivityversionreleases)*