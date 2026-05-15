# Read Game Center Details

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read a specific Game Center detail and related information.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}`

## Parameters

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
- `fields[apps]` ([string])
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

- [Read the State of Game Center for an App](get-v1-apps-_id_-gamecenterdetail.md)
  Get Game Center detail information for an app.
- [Read App Versions for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterappversions.md)
  Get a list of app versions for a Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/gameCenterAppVersions](get-v1-gamecenterdetails-_id_-relationships-gamecenterappversions.md)
- [Read the Groups in a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecentergroup.md)
  Get a list of groups in a Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/gameCenterGroup](get-v1-gamecenterdetails-_id_-relationships-gamecentergroup.md)
- [Read the Challenges for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center detail.
- [Read Challenge IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterchallenges.md)
  List all the challenge IDs for a specific Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_)*