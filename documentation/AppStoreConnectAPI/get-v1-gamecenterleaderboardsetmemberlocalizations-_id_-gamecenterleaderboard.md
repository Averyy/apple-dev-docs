# Read Leaderboard Information for a Leaderboard Set Member Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a leaderboard for a specific leaderboard set member localization.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardSetMemberLocalizations/{id}/gameCenterLeaderboard`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterDetails]` ([string]): **Allowed Values**: `arcadeEnabled`, `challengeEnabled`, `app`, `gameCenterAppVersions`, `gameCenterGroup`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`, `defaultLeaderboard`, `defaultLeaderboardV2`, `defaultGroupLeaderboard`, `defaultGroupLeaderboardV2`, `achievementReleases`, `activityReleases`, `challengeReleases`, `leaderboardReleases`, `leaderboardSetReleases`, `blockedPlayers`, `challengesMinimumPlatformVersions`
- `fields[gameCenterGroups]` ([string]): **Allowed Values**: `referenceName`, `gameCenterDetails`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`
- `fields[gameCenterLeaderboardLocalizations]` ([string]): **Allowed Values**: `locale`, `name`, `formatterOverride`, `formatterSuffix`, `formatterSuffixSingular`, `description`, `gameCenterLeaderboard`, `gameCenterLeaderboardImage`
- `fields[gameCenterLeaderboardReleases]` ([string]): **Allowed Values**: `live`, `gameCenterDetail`, `gameCenterLeaderboard`
- `fields[gameCenterLeaderboardSets]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `gameCenterDetail`, `gameCenterGroup`, `groupLeaderboardSet`, `localizations`, `gameCenterLeaderboards`, `releases`
- `fields[gameCenterLeaderboards]` ([string]): **Allowed Values**: `defaultFormatter`, `referenceName`, `vendorIdentifier`, `submissionType`, `scoreSortType`, `scoreRangeStart`, `scoreRangeEnd`, `recurrenceStartDate`, `recurrenceDuration`, `recurrenceRule`, `archived`, `activityProperties`, `visibility`, `gameCenterDetail`, `gameCenterGroup`, `groupLeaderboard`, `gameCenterLeaderboardSets`, `localizations`, `releases`, `activity`, `challenge`
- `include` ([string]): **Allowed Values**: `gameCenterDetail`, `gameCenterGroup`, `groupLeaderboard`, `gameCenterLeaderboardSets`, `localizations`, `releases`, `activity`, `challenge`
- `limit[gameCenterLeaderboardSets]` (integer) *(deprecated)*: **Maximum**: `50`
- `limit[localizations]` (integer) *(deprecated)*: **Maximum**: `50`
- `limit[releases]` (integer) *(deprecated)*: **Maximum**: `50`
- `fields[gameCenterActivities]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `playStyle`, `minimumPlayersCount`, `maximumPlayersCount`, `supportsPartyCode`, `archived`, `properties`, `gameCenterDetail`, `gameCenterGroup`, `achievements`, `achievementsV2`, `leaderboards`, `leaderboardsV2`, `versions`
- `fields[gameCenterChallenges]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `archived`, `challengeType`, `repeatable`, `gameCenterDetail`, `gameCenterGroup`, `versions`, `leaderboard`, `leaderboardV2`

## Responses

- `200` OK (`GameCenterLeaderboardResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing leaderboard set member localizations
- [Read Leaderboard Set Member Localization Information](./get-v1-gamecenterleaderboardsetmemberlocalizations.md)
  Get information about leaderboard member set localizations.
- [Read the leaderboard id for a leaderboard set member localization](./get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-relationships-gamecenterleaderboard.md)
  Get the leaderboard ID for a specific leaderboard set member localization.
- [Read Leaderboard Set Information for a Leaderboard Set Member Localization](./get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-gamecenterleaderboardset.md)
  Get information about a leaderboard set for a specific leaderboard set member localization.
- [Get the leaderboard set ID for a Game Center leaderboard set member localization](./get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-relationships-gamecenterleaderboardset.md)
- [Create a Leaderboard Set Member Localization](./post-v1-gamecenterleaderboardsetmemberlocalizations.md)
  Add a new leaderboard set localization.
- [Modify a Leaderboard Set Member Localization](./patch-v1-gamecenterleaderboardsetmemberlocalizations-_id_.md)
  Edit a leaderboard set member localization.
- [Delete a Leaderboard Set Member Localization](./delete-v1-gamecenterleaderboardsetmemberlocalizations-_id_.md)
  Delete a localization that’s associated with a leaderboard set member.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-gamecenterleaderboard)*