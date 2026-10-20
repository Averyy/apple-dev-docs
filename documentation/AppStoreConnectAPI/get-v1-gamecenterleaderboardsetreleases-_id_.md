# Read Leaderboard Set Release Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a leaderboard set release.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardSetReleases/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterLeaderboardSetReleases]` ([string]): **Allowed Values**: `live`, `gameCenterDetail`, `gameCenterLeaderboardSet`
- `include` ([string]): **Allowed Values**: `gameCenterDetail`, `gameCenterLeaderboardSet`
- `fields[gameCenterDetails]` ([string]): **Allowed Values**: `arcadeEnabled`, `challengeEnabled`, `app`, `gameCenterAppVersions`, `gameCenterGroup`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`, `defaultLeaderboard`, `defaultLeaderboardV2`, `defaultGroupLeaderboard`, `defaultGroupLeaderboardV2`, `achievementReleases`, `activityReleases`, `challengeReleases`, `leaderboardReleases`, `leaderboardSetReleases`, `blockedPlayers`, `challengesMinimumPlatformVersions`
- `fields[gameCenterLeaderboardSets]` ([string]) *(deprecated)*: **Allowed Values**: `referenceName`, `vendorIdentifier`, `gameCenterDetail`, `gameCenterGroup`, `groupLeaderboardSet`, `localizations`, `gameCenterLeaderboards`, `releases`

## Responses

- `200` OK (`GameCenterLeaderboardSetReleaseResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing leaderboard set releases
- [Create a Leaderboard Set Release](./post-v1-gamecenterleaderboardsetreleases.md)
  Add a new leaderboard set release.
- [Delete a Leaderboard Set Release](./delete-v1-gamecenterleaderboardsetreleases-_id_.md)
  Delete a new leaderboard set release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterleaderboardsetreleases-_id_)*