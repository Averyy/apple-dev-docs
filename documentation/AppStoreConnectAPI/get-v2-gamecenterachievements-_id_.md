# Read Game Center Achievement Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific Game Center achievement.

**Availability**:
- App Store Connect API 3.6+

## Overview

- id:
- fields[gameCenterAchievementVersions]:
- fields[gameCenterAchievements]:
- include:
- limit[versions]:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterAchievements/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterAchievementVersions]` ([string]): **Allowed Values**: `version`, `state`, `achievement`, `localizations`
- `fields[gameCenterAchievements]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `points`, `showBeforeEarned`, `repeatable`, `archived`, `activityProperties`, `gameCenterDetail`, `gameCenterGroup`, `activity`, `versions`
- `fields[gameCenterActivities]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `playStyle`, `minimumPlayersCount`, `maximumPlayersCount`, `supportsPartyCode`, `archived`, `properties`, `gameCenterDetail`, `gameCenterGroup`, `achievements`, `achievementsV2`, `leaderboards`, `leaderboardsV2`, `versions`
- `fields[gameCenterDetails]` ([string]): **Allowed Values**: `arcadeEnabled`, `challengeEnabled`, `app`, `gameCenterAppVersions`, `gameCenterGroup`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`, `defaultLeaderboard`, `defaultLeaderboardV2`, `defaultGroupLeaderboard`, `defaultGroupLeaderboardV2`, `achievementReleases`, `activityReleases`, `challengeReleases`, `leaderboardReleases`, `leaderboardSetReleases`, `blockedPlayers`, `challengesMinimumPlatformVersions`
- `fields[gameCenterGroups]` ([string]): **Allowed Values**: `referenceName`, `gameCenterDetails`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`
- `include` ([string]): **Allowed Values**: `gameCenterDetail`, `gameCenterGroup`, `activity`, `versions`
- `limit[versions]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`GameCenterAchievementV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading achievements
- [List All Versions for a Game Center Achievement](./get-v2-gamecenterachievements-_id_-versions.md)
  Get a list of versions for a specific Game Center achievement.
- [Get All Version IDs for a Game Center Achievement](./get-v2-gamecenterachievements-_id_-relationships-versions.md)
  Get a list of version resource IDs for a specific Game Center achievement.
- [List All Achievements](./get-v1-gamecenterdetails-_id_-gamecenterachievements.md)
  List all achievement information for a Game Center detail.
- [Read Achievement Information](./get-v1-gamecenterachievements-_id_.md)
  Read information about a specific Game Center achievement.
- [List All Localizations for an Achievement](./get-v1-gamecenterachievements-_id_-localizations.md)
  Read information about the release for specific achievement.
- [Read Release Information for an Achievement](./get-v1-gamecenterachievements-_id_-releases.md)
  Read the state of an achievement release and related information.
- [List release IDs for a Game Center achievement](./get-v1-gamecenterachievements-_id_-relationships-releases.md)
- [List Associated Group Achievement Information for an Achievement](./get-v1-gamecenterachievements-_id_-groupachievement.md)
  Read information about the group for specific achievement.
- [List Group Achievements for an Achievement](./get-v1-gamecenterachievements-_id_-relationships-groupachievement.md)
  List associated group achievements for a specific achievement.
- [List achievement releases](./get-v1-gamecenterdetails-_id_-achievementreleases.md)
  Read information about the achievement releases for specific Game Center detail.
- [List achievement release IDs for a Game Center detail](./get-v1-gamecenterdetails-_id_-relationships-achievementreleases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterachievements-_id_)*