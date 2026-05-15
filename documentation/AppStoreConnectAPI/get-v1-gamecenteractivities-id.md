# Read Activity Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information for a specific Game Center activity.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterActivities/{id}`

## Parameters

- `fields[gameCenterActivities]` ([string])
- `fields[gameCenterActivityVersions]` ([string])
- `include` ([string])
- `limit[achievements]` (integer)
- `limit[leaderboards]` (integer)
- `limit[versions]` (integer)
- `fields[gameCenterAchievements]` ([string])
- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterGroups]` ([string])
- `fields[gameCenterLeaderboards]` ([string])
- `limit[achievementsV2]` (integer)
- `limit[leaderboardsV2]` (integer)

## See Also

- [Create an Activity](post-v1-gamecenteractivities.md)
  Create an activity for your Game Center detail or Game Center group.
- [Add an Achievement to a Game Center Activity](post-v1-gamecenteractivities-_id_-relationships-achievementsv2.md)
  Add an achievement to a Game Center activity.
- [Add a Leaderboard to a Game Center Activity](post-v1-gamecenteractivities-_id_-relationships-leaderboardsv2.md)
  Add a leaderboard to a Game Center activity.
- [Modify the Achievements for a Game Center Activity](post-v1-gamecenteractivities-_id_-relationships-achievements.md)
  Update the relationship between achievements and a specific Game Center activity.
- [Modify the Leaderboards for a Game Center Activity](post-v1-gamecenteractivities-_id_-relationships-leaderboards.md)
  Update the relationship between a leaderboard and a specific Game Center activity.
- [Read the Versions for an Activity](get-v1-gamecenteractivities-_id_-versions.md)
  Get a list of versions for a specific Game Center activity.
- [GET /v1/gameCenterActivities/{id}/relationships/versions](get-v1-gamecenteractivities-_id_-relationships-versions.md)
- [List All Activities for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenteractivities.md)
  Get activity release information for a specific Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/gameCenterActivities](get-v1-gamecenterdetails-_id_-relationships-gamecenteractivities.md)
- [List All Activities for a Game Center Group](get-v1-gamecentergroups-_id_-gamecenteractivities.md)
  Get a list of all activities for a Game Center group.
- [GET /v1/gameCenterGroups/{id}/relationships/gameCenterActivities](get-v1-gamecentergroups-_id_-relationships-gamecenteractivities.md)
- [Modify an Activity](patch-v1-gamecenteractivities-_id_.md)
  Update details for a specific Game Center activity.
- [Delete an Activity](delete-v1-gamecenteractivities-_id_.md)
  Remove a specific Game Center activity.
- [Remove an Achievement](delete-v1-gamecenteractivities-_id_-relationships-achievementsv2.md)
  Remove an achievement from a Game Center activity.
- [Remove a Leaderboard](delete-v1-gamecenteractivities-_id_-relationships-leaderboardsv2.md)
  Remove a leaderboard from a Game Center activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenteractivities-_id_)*