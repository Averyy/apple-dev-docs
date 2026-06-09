# Read the state of game center for an app

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

- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.
- `fields[gameCenterAchievementReleases]` ([string]): Additional fields to include for each Game Center achievement release resource returned by the response.
- `fields[gameCenterAchievements]` ([string]): Additional fields to include for each Game Center achievement resource returned by the response.
- `fields[gameCenterAppVersions]` ([string]): Additional fields to include for each Game Center app version resource returned by the response.
- `fields[gameCenterDetails]` ([string]): Additional fields to include for each Game Center detail resource returned by the response.
- `fields[gameCenterGroups]` ([string]): Additional fields to include for each Game Center group resource returned by the response.
- `fields[gameCenterLeaderboardReleases]` ([string]): Additional fields to include for each Game Center leaderboard release resource returned by the response.
- `fields[gameCenterLeaderboardSetReleases]` ([string]): Additional fields to include for each Game Center leaderboard set release resource returned by the response.
- `fields[gameCenterLeaderboardSets]` ([string]): Additional fields to include for each Game Center leaderboard set resource returned by the response.
- `fields[gameCenterLeaderboards]` ([string]): Additional fields to include for each Game Center leaderboard resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[achievementReleases]` (integer): The maximum number of related achievement releases resources to return.
- `limit[gameCenterAchievements]` (integer): The maximum number of related Game Center achievements resources to return.
- `limit[gameCenterAppVersions]` (integer): The maximum number of related Game Center app versions resources to return.
- `limit[gameCenterLeaderboardSets]` (integer): The maximum number of related Game Center leaderboard sets resources to return.
- `limit[gameCenterLeaderboards]` (integer): The maximum number of related Game Center leaderboards resources to return.
- `limit[leaderboardReleases]` (integer): The maximum number of related leaderboard releases resources to return.
- `limit[leaderboardSetReleases]` (integer): The maximum number of related leaderboard set releases resources to return.
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

- [Get the Game Center detail ID for an app](get-v1-apps-_id_-relationships-gamecenterdetail.md)
- [List Game Center-enabled version IDs for an app](get-v1-apps-_id_-relationships-gamecenterenabledversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-gamecenterdetail)*