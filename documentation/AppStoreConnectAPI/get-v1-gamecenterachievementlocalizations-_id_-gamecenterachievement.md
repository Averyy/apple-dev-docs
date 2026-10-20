# Read the Achievement Localization Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Read the achievement associated with specific localized information.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/{id}/gameCenterAchievement`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Apps resource. Obtain the app resource ID from the [`List All Localizations for an Achievement`](./get-v1-gamecenterachievements-_id_-localizations.md) response.

### Query Parameters

- `fields[gameCenterAchievementLocalizations]` ([string]): **Allowed Values**: `locale`, `name`, `beforeEarnedDescription`, `afterEarnedDescription`, `gameCenterAchievement`, `gameCenterAchievementImage`
- `fields[gameCenterAchievementReleases]` ([string]): **Allowed Values**: `live`, `gameCenterDetail`, `gameCenterAchievement`
- `fields[gameCenterAchievements]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `points`, `showBeforeEarned`, `repeatable`, `archived`, `activityProperties`, `gameCenterDetail`, `gameCenterGroup`, `groupAchievement`, `localizations`, `releases`, `activity`
- `fields[gameCenterDetails]` ([string]): **Allowed Values**: `arcadeEnabled`, `challengeEnabled`, `app`, `gameCenterAppVersions`, `gameCenterGroup`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`, `defaultLeaderboard`, `defaultLeaderboardV2`, `defaultGroupLeaderboard`, `defaultGroupLeaderboardV2`, `achievementReleases`, `activityReleases`, `challengeReleases`, `leaderboardReleases`, `leaderboardSetReleases`, `blockedPlayers`, `challengesMinimumPlatformVersions`
- `fields[gameCenterGroups]` ([string]): **Allowed Values**: `referenceName`, `gameCenterDetails`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`
- `include` ([string]): **Allowed Values**: `gameCenterDetail`, `gameCenterGroup`, `groupAchievement`, `localizations`, `releases`, `activity`
- `limit[localizations]` (integer) *(deprecated)*: **Maximum**: `50`
- `limit[releases]` (integer) *(deprecated)*: **Maximum**: `50`
- `fields[gameCenterActivities]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `playStyle`, `minimumPlayersCount`, `maximumPlayersCount`, `supportsPartyCode`, `archived`, `properties`, `gameCenterDetail`, `gameCenterGroup`, `achievements`, `achievementsV2`, `leaderboards`, `leaderboardsV2`, `versions`

## Responses

- `200` OK (`GameCenterAchievementResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading achievements localizations
- [Read Game Center Achievement Localization Information](./get-v2-gamecenterachievementlocalizations-_id_.md)
  Get information about a specific Game Center achievement localization.
- [List All Images for a Game Center Achievement Localization](./get-v2-gamecenterachievementlocalizations-_id_-image.md)
  Get a list of images for a specific Game Center achievement localization.
- [Get All Image IDs for a Game Center Achievement Localization](./get-v2-gamecenterachievementlocalizations-_id_-relationships-image.md)
  Get a list of image resource IDs for a specific Game Center achievement localization.
- [List All Localizations for an Achievement](./get-v1-gamecenterachievements-_id_-localizations.md)
  Read information about the release for specific achievement.
- [List localization IDs for a Game Center achievement](./get-v1-gamecenterachievements-_id_-relationships-localizations.md)
- [Read Achievement Localization Information](./get-v1-gamecenterachievementlocalizations-_id_.md)
  Read localized information for a specific locale for a specific achievement.
- [Read the achievement id for a  localization](./get-v1-gamecenterachievementlocalizations-_id_-relationships-gamecenterachievement.md)
  Read the achievement ID associated with specific localized information.
- [Read the Image for a Specific Achievement Localization](./get-v1-gamecenterachievementlocalizations-_id_-gamecenterachievementimage.md)
  Read the achievement image associated with specific localized information.
- [Get the achievement image ID for a Game Center achievement localization](./get-v1-gamecenterachievementlocalizations-_id_-relationships-gamecenterachievementimage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterachievementlocalizations-_id_-gamecenterachievement)*