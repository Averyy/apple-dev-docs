# Read Leaderboard Set Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Read information about a specific leaderboard set.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated. Use [`Read Game Center Leaderboard Set Information`](./get-v2-gamecenterleaderboardsets-_id_.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardSets/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterLeaderboardSetLocalizations]` ([string]) *(deprecated)*: **Allowed Values**: `locale`, `name`, `gameCenterLeaderboardSet`, `gameCenterLeaderboardSetImage`
- `fields[gameCenterLeaderboardSetReleases]` ([string]) *(deprecated)*: **Allowed Values**: `live`, `gameCenterDetail`, `gameCenterLeaderboardSet`
- `fields[gameCenterLeaderboardSets]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `gameCenterDetail`, `gameCenterGroup`, `groupLeaderboardSet`, `localizations`, `gameCenterLeaderboards`, `releases`
- `fields[gameCenterLeaderboards]` ([string]) *(deprecated)*: **Allowed Values**: `defaultFormatter`, `referenceName`, `vendorIdentifier`, `submissionType`, `scoreSortType`, `scoreRangeStart`, `scoreRangeEnd`, `recurrenceStartDate`, `recurrenceDuration`, `recurrenceRule`, `archived`, `activityProperties`, `visibility`, `gameCenterDetail`, `gameCenterGroup`, `groupLeaderboard`, `gameCenterLeaderboardSets`, `localizations`, `releases`, `activity`, `challenge`
- `include` ([string]): **Allowed Values**: `gameCenterDetail`, `gameCenterGroup`, `groupLeaderboardSet`, `localizations`, `gameCenterLeaderboards`, `releases`
- `limit[gameCenterLeaderboards]` (integer) *(deprecated)*: **Maximum**: `50`
- `limit[localizations]` (integer) *(deprecated)*: **Maximum**: `50`
- `limit[releases]` (integer) *(deprecated)*: **Maximum**: `50`
- `fields[gameCenterDetails]` ([string]): **Allowed Values**: `arcadeEnabled`, `challengeEnabled`, `app`, `gameCenterAppVersions`, `gameCenterGroup`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`, `defaultLeaderboard`, `defaultLeaderboardV2`, `defaultGroupLeaderboard`, `defaultGroupLeaderboardV2`, `achievementReleases`, `activityReleases`, `challengeReleases`, `leaderboardReleases`, `leaderboardSetReleases`, `blockedPlayers`, `challengesMinimumPlatformVersions`
- `fields[gameCenterGroups]` ([string]): **Allowed Values**: `referenceName`, `gameCenterDetails`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`

## Responses

- `200` OK (`GameCenterLeaderboardSetResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading leaderboard sets
- [Read Game Center Leaderboard Set Information](./get-v2-gamecenterleaderboardsets-_id_.md)
  Get information about a specific Game Center leaderboard set.
- [List All Leaderboards for a Game Center Leaderboard Set](./get-v2-gamecenterleaderboardsets-_id_-gamecenterleaderboards.md)
  Get a list of leaderboards for a specific Game Center leaderboard set.
- [Get All Leaderboard IDs for a Game Center Leaderboard Set](./get-v2-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Get a list of leaderboard resource IDs for a specific Game Center leaderboard set.
- [List All Versions for a Game Center Leaderboard Set](./get-v2-gamecenterleaderboardsets-_id_-versions.md)
  Get a list of versions for a specific Game Center leaderboard set.
- [Get All Version IDs for a Game Center Leaderboard Set](./get-v2-gamecenterleaderboardsets-_id_-relationships-versions.md)
  Get a list of version resource IDs for a specific Game Center leaderboard set.
- [List Leaderboard Information for a Leaderboard Set](./get-v1-gamecenterleaderboardsets-_id_-gamecenterleaderboards.md)
  Read the leadboards that belong to a learderboard set.
- [List Leaderboard Sets in a Group Leaderboard Set](./get-v1-gamecenterleaderboardsets-_id_-groupleaderboardset.md)
  List information about leaderboards and leaderboard sets in a group leaderboard set.
- [List All Localizations for a Leaderboard Set](./get-v1-gamecenterleaderboardsets-_id_-localizations.md)
  Get a list of localized metadata for a leaderboard set.
- [List localization IDs for a Game Center leaderboard set](./get-v1-gamecenterleaderboardsets-_id_-relationships-localizations.md)
- [Read the Leaderboards in a Leaderboard Set](./get-v1-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  List all leaderboards in a leaderboard set.
- [Read the Group Leaderboard Set in a Leaderboard Set](./get-v1-gamecenterleaderboardsets-_id_-relationships-groupleaderboardset.md)
  List all the group leaderboard sets in a leaderboard set.
- [List Releases for a Leaderboard Set](./get-v1-gamecenterleaderboardsets-_id_-releases.md)
  Read the state of releases for a leaderboard set and related information.
- [List release IDs for a Game Center leaderboard set](./get-v1-gamecenterleaderboardsets-_id_-relationships-releases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterleaderboardsets-_id_)*