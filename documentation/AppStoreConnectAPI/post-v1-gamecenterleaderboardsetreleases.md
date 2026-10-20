# Create a Leaderboard Set Release

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a new leaderboard set release.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardSetReleases`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterLeaderboardSetReleaseCreateRequest`

## Responses

- `201` Created (`GameCenterLeaderboardSetReleaseResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing leaderboard set releases
- [Read Leaderboard Set Release Information](./get-v1-gamecenterleaderboardsetreleases-_id_.md)
  Get information about a leaderboard set release.
- [Delete a Leaderboard Set Release](./delete-v1-gamecenterleaderboardsetreleases-_id_.md)
  Delete a new leaderboard set release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenterleaderboardsetreleases)*