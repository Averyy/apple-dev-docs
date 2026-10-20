# Create a Leaderboard Release

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a new leaderboard release.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardReleases`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterLeaderboardReleaseCreateRequest`

## Responses

- `201` Created (`GameCenterLeaderboardReleaseResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing leaderboard releases
- [List Releases for a Leaderboard](./get-v1-gamecenterleaderboards-_id_-releases.md)
  Read the state of releases for a leaderboard and related information.
- [List release IDs for a Game Center leaderboard](./get-v1-gamecenterleaderboards-_id_-relationships-releases.md)
- [Read Leaderboard Release Information](./get-v1-gamecenterleaderboardreleases-_id_.md)
  Read the state of a specific leaderboard release.
- [Delete a Leaderboard Release](./delete-v1-gamecenterleaderboardreleases-_id_.md)
  Delete a new leaderboard release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenterleaderboardreleases)*