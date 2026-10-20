# List All Game Center Leaderboard Sets for a Game Center Group

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of leaderboard sets for a specific Game Center group.

**Availability**:
- App Store Connect API 3.6+

#### Overview

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

`GET https://api.appstoreconnect.apple.com/v1/gameCenterGroups/{id}/gameCenterLeaderboardSetsV2`

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

### Managing groups
- [Read Group Information](./get-v1-gamecentergroups.md)
  List information for all groups.
- [Read information for a specific group](./get-v1-gamecentergroups-_id_.md)
  Read information for a specific Game Center group.
- [Create a Group](./post-v1-gamecentergroups.md)
  Add a new group.
- [Modify a Group](./patch-v1-gamecentergroups-_id_.md)
  Edit the reference name for a group.
- [Delete a Group](./delete-v1-gamecentergroups-_id_.md)
  Remove a group.
- [List All Game Center Achievements for a Game Center Group](./get-v1-gamecentergroups-_id_-gamecenterachievementsv2.md)
  Get a list of achievements for a specific Game Center group.
- [List All Game Center Leaderboards for a Game Center Group](./get-v1-gamecentergroups-_id_-gamecenterleaderboardsv2.md)
  Get a list of leaderboards for a specific Game Center group.
- [List the Achievements in a Group](./get-v1-gamecentergroups-_id_-gamecenterachievements.md)
  List achievements information for a specific group.
- [List game center details for a group](./get-v1-gamecentergroups-_id_-gamecenterdetails.md)
  Read Game Center detail information for a specific group.
- [List Game Center detail IDs for a Game Center group](./get-v1-gamecentergroups-_id_-relationships-gamecenterdetails.md)
- [List Game Center detail IDs for a Game Center group](./get-v1-gamecentergroups-_id_-relationships-gamecenterdetails.md)
- [List game center leaderboard sets in a group](./get-v1-gamecentergroups-_id_-gamecenterleaderboardsets.md)
  Read Game Center leaderboard sets information for a specific group.
- [List game center leaderboards for a group](./get-v1-gamecentergroups-_id_-gamecenterleaderboards.md)
  Read Game Center leaderboard information for a specific group.
- [List all activities for a game center group](./get-v1-gamecentergroups-_id_-gamecenteractivities.md)
  Get a list of all activities for a Game Center group.
- [List activity IDs for a Game Center group](./get-v1-gamecentergroups-_id_-relationships-gamecenteractivities.md)
  Get a list of activity IDs for a specific Game Center group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecentergroups-_id_-gamecenterleaderboardsetsv2)*