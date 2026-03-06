# Read the state of Game Center for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get Game Center detail information for an app.

**Availability**:
- App Store Connect API 3.0+

## Mentions

- [Configuring Game center activities](configuring-game-center-activities.md)
- [Configuring Game Center challenges](configuring-game-center-challenges.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/gameCenterDetail`

## Parameters

- `fields[apps]` ([string])
- `fields[gameCenterAchievementReleases]` ([string])
- `fields[gameCenterAchievements]` ([string])
- `fields[gameCenterAppVersions]` ([string])
- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterGroups]` ([string])
- `fields[gameCenterLeaderboardReleases]` ([string])
- `fields[gameCenterLeaderboardSetReleases]` ([string])
- `fields[gameCenterLeaderboardSets]` ([string])
- `fields[gameCenterLeaderboards]` ([string])
- `include` ([string])
- `limit[achievementReleases]` (integer)
- `limit[gameCenterAchievements]` (integer)
- `limit[gameCenterAppVersions]` (integer)
- `limit[gameCenterLeaderboardSets]` (integer)
- `limit[gameCenterLeaderboards]` (integer)
- `limit[leaderboardReleases]` (integer)
- `limit[leaderboardSetReleases]` (integer)
- `fields[appStoreVersions]` ([string])
- `fields[gameCenterActivities]` ([string])
- `fields[gameCenterActivityVersionReleases]` ([string])
- `fields[gameCenterChallengeVersionReleases]` ([string])
- `fields[gameCenterChallenges]` ([string])
- `limit[activityReleases]` (integer)
- `limit[challengeReleases]` (integer)
- `limit[challengesMinimumPlatformVersions]` (integer)
- `limit[gameCenterAchievementsV2]` (integer)
- `limit[gameCenterActivities]` (integer)
- `limit[gameCenterChallenges]` (integer)
- `limit[gameCenterLeaderboardSetsV2]` (integer)
- `limit[gameCenterLeaderboardsV2]` (integer)

## See Also

- [GET /v1/apps/{id}/relationships/gameCenterDetail](get-v1-apps-_id_-relationships-gamecenterdetail.md)
- [GET /v1/apps/{id}/relationships/gameCenterEnabledVersions](get-v1-apps-_id_-relationships-gamecenterenabledversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-gamecenterdetail)*