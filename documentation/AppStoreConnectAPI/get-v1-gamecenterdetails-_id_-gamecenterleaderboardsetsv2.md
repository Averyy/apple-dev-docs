# List All Game Center Leaderboard Sets for a Game Center Detail

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of leaderboard sets for a specific Game Center detail.

**Availability**:
- App Store Connect API 3.6+

## Overview

- id:
- fields[gameCenterDetails]:
- fields[gameCenterGroups]:
- fields[gameCenterLeaderboardSetVersions]:
- fields[gameCenterLeaderboardSets]:
- fields[gameCenterLeaderboards]:
- filter[id]:
- filter[referenceName]:
- include:
- limit:
- limit[gameCenterLeaderboards]:
- limit[versions]:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/gameCenterLeaderboardSetsV2`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterDetails]` ([string]): **Allowed Values**: `arcadeEnabled`, `challengeEnabled`, `app`, `gameCenterAppVersions`, `gameCenterGroup`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`, `defaultLeaderboard`, `defaultLeaderboardV2`, `defaultGroupLeaderboard`, `defaultGroupLeaderboardV2`, `achievementReleases`, `activityReleases`, `challengeReleases`, `leaderboardReleases`, `leaderboardSetReleases`, `blockedPlayers`, `challengesMinimumPlatformVersions`
- `fields[gameCenterGroups]` ([string]): **Allowed Values**: `referenceName`, `gameCenterDetails`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`
- `fields[gameCenterLeaderboardSetVersions]` ([string]): **Allowed Values**: `version`, `state`, `leaderboardSet`, `localizations`
- `fields[gameCenterLeaderboardSets]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `gameCenterDetail`, `gameCenterGroup`, `gameCenterLeaderboards`, `versions`
- `fields[gameCenterLeaderboards]` ([string]): **Allowed Values**: `defaultFormatter`, `referenceName`, `vendorIdentifier`, `submissionType`, `scoreSortType`, `scoreRangeStart`, `scoreRangeEnd`, `recurrenceStartDate`, `recurrenceDuration`, `recurrenceRule`, `archived`, `activityProperties`, `visibility`, `gameCenterDetail`, `gameCenterGroup`, `gameCenterLeaderboardSets`, `gameCenterScoreModerations`, `activity`, `challenge`, `versions`
- `filter[id]` ([string])
- `filter[referenceName]` ([string])
- `include` ([string]): **Allowed Values**: `gameCenterDetail`, `gameCenterGroup`, `gameCenterLeaderboards`, `versions`
- `limit` (integer): **Maximum**: `200`
- `limit[gameCenterLeaderboards]` (integer): **Maximum**: `50`
- `limit[versions]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`GameCenterLeaderboardSetsV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and editing leaderboard sets in a Game Center detail
- [Get All Leaderboard Set IDs for a Game Center Detail](./get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsetsv2.md)
  Get a list of leaderboard set resource IDs for a specific Game Center detail.
- [Get leaderboard sets information](./get-v1-gamecenterdetails-_id_-gamecenterleaderboardsets.md)
  Get all leaderboard sets and related information for a Game Center detail.
- [List Leaderboard Sets](./get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsets.md)
  List all leaderboards for a Game Center detail.
- [Get leaderboard set releases information](./get-v1-gamecenterdetails-_id_-leaderboardsetreleases.md)
  List all leaderboard set releases for a Game Center detail.
- [List leaderboard set release IDs for a Game Center detail](./get-v1-gamecenterdetails-_id_-relationships-leaderboardsetreleases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-gamecenterleaderboardsetsv2)*