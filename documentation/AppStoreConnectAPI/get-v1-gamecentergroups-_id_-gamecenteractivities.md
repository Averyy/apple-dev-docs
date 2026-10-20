# List all activities for a game center group

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of all activities for a Game Center group.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring Game center activities](./configuring-game-center-activities.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterGroups/{id}/gameCenterActivities`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterAchievements]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `points`, `showBeforeEarned`, `repeatable`, `archived`, `activityProperties`, `gameCenterDetail`, `gameCenterGroup`, `groupAchievement`, `localizations`, `releases`, `activity`, `versions`
- `fields[gameCenterActivities]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `playStyle`, `minimumPlayersCount`, `maximumPlayersCount`, `supportsPartyCode`, `archived`, `properties`, `gameCenterDetail`, `gameCenterGroup`, `achievements`, `achievementsV2`, `leaderboards`, `leaderboardsV2`, `versions`
- `fields[gameCenterActivityVersions]` ([string]): **Allowed Values**: `version`, `state`, `fallbackUrl`, `activity`, `localizations`, `defaultImage`, `releases`
- `fields[gameCenterDetails]` ([string]): **Allowed Values**: `arcadeEnabled`, `challengeEnabled`, `app`, `gameCenterAppVersions`, `gameCenterGroup`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`, `defaultLeaderboard`, `defaultLeaderboardV2`, `defaultGroupLeaderboard`, `defaultGroupLeaderboardV2`, `achievementReleases`, `activityReleases`, `challengeReleases`, `leaderboardReleases`, `leaderboardSetReleases`, `blockedPlayers`, `challengesMinimumPlatformVersions`
- `fields[gameCenterGroups]` ([string]): **Allowed Values**: `referenceName`, `gameCenterDetails`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`
- `fields[gameCenterLeaderboards]` ([string]): **Allowed Values**: `defaultFormatter`, `referenceName`, `vendorIdentifier`, `submissionType`, `scoreSortType`, `scoreRangeStart`, `scoreRangeEnd`, `recurrenceStartDate`, `recurrenceDuration`, `recurrenceRule`, `archived`, `activityProperties`, `visibility`, `gameCenterDetail`, `gameCenterGroup`, `groupLeaderboard`, `gameCenterLeaderboardSets`, `localizations`, `releases`, `activity`, `challenge`, `gameCenterScoreModerations`, `versions`
- `include` ([string]): **Allowed Values**: `gameCenterDetail`, `gameCenterGroup`, `achievements`, `achievementsV2`, `leaderboards`, `leaderboardsV2`, `versions`
- `limit` (integer): **Maximum**: `200`
- `limit[achievements]` (integer) *(deprecated)*: **Maximum**: `50`
- `limit[leaderboards]` (integer) *(deprecated)*: **Maximum**: `50`
- `limit[versions]` (integer): **Maximum**: `50`
- `limit[achievementsV2]` (integer): **Maximum**: `50`
- `limit[leaderboardsV2]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`GameCenterActivitiesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Game Center activities
- [Create an Activity](./post-v1-gamecenteractivities.md)
  Create an activity for your Game Center detail or Game Center group.
- [Add an Achievement to a Game Center Activity](./post-v1-gamecenteractivities-_id_-relationships-achievementsv2.md)
  Add an achievement to a Game Center activity.
- [Add a Leaderboard to a Game Center Activity](./post-v1-gamecenteractivities-_id_-relationships-leaderboardsv2.md)
  Add a leaderboard to a Game Center activity.
- [Modify the achievements for a game center activity](./post-v1-gamecenteractivities-_id_-relationships-achievements.md)
  Update the relationship between achievements and a specific Game Center activity.
- [Modify the leaderboards for a game center activity](./post-v1-gamecenteractivities-_id_-relationships-leaderboards.md)
  Update the relationship between a leaderboard and a specific Game Center activity.
- [Read Activity Information](./get-v1-gamecenteractivities-_id_.md)
  Get information for a specific Game Center activity.
- [Read the Versions for an Activity](./get-v1-gamecenteractivities-_id_-versions.md)
  Get a list of versions for a specific Game Center activity.
- [List version IDs for a Game Center activity](./get-v1-gamecenteractivities-_id_-relationships-versions.md)
- [List all activities for a game center detail](./get-v1-gamecenterdetails-_id_-gamecenteractivities.md)
  Get activity release information for a specific Game Center detail.
- [List Game Center activity IDs for a Game Center detail](./get-v1-gamecenterdetails-_id_-relationships-gamecenteractivities.md)
- [List activity IDs for a Game Center group](./get-v1-gamecentergroups-_id_-relationships-gamecenteractivities.md)
  Get a list of activity IDs for a specific Game Center group.
- [Modify an Activity](./patch-v1-gamecenteractivities-_id_.md)
  Update details for a specific Game Center activity.
- [Delete an Activity](./delete-v1-gamecenteractivities-_id_.md)
  Remove a specific Game Center activity.
- [Remove an Achievement](./delete-v1-gamecenteractivities-_id_-relationships-achievementsv2.md)
  Remove an achievement from a Game Center activity.
- [Remove a Leaderboard](./delete-v1-gamecenteractivities-_id_-relationships-leaderboardsv2.md)
  Remove a leaderboard from a Game Center activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecentergroups-_id_-gamecenteractivities)*