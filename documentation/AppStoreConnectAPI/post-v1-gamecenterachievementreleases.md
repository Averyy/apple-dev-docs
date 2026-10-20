# Create a game center achievement release

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a release for an achievement and a Game Center detail.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterAchievementReleases`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterAchievementReleaseCreateRequest`

## Responses

- `201` Created (`GameCenterAchievementReleaseResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Game Center achievement releases
- [List achievement releases](./get-v1-gamecenterdetails-_id_-achievementreleases.md)
  Read information about the achievement releases for specific Game Center detail.
- [List achievement release IDs for a Game Center detail](./get-v1-gamecenterdetails-_id_-relationships-achievementreleases.md)
- [Read Release Information for an Achievement](./get-v1-gamecenterachievements-_id_-releases.md)
  Read the state of an achievement release and related information.
- [List release IDs for a Game Center achievement](./get-v1-gamecenterachievements-_id_-relationships-releases.md)
- [Read game center achievement release information](./get-v1-gamecenterachievementreleases-_id_.md)
  Read the state of a specific achievement release.
- [Delete a game center achievement release](./delete-v1-gamecenterachievementreleases-_id_.md)
  Delete a release of an achievement or Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenterachievementreleases)*