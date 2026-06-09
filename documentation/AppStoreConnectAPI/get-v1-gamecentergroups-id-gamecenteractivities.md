# List all activities for a game center group

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of all activities for a Game Center group.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring Game center activities](configuring-game-center-activities.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterGroups/{id}/gameCenterActivities`

## Parameters

- `fields[gameCenterAchievements]` ([string])
- `fields[gameCenterActivities]` ([string])
- `fields[gameCenterActivityVersions]` ([string])
- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterGroups]` ([string])
- `fields[gameCenterLeaderboards]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[achievements]` (integer)
- `limit[leaderboards]` (integer)
- `limit[versions]` (integer)
- `limit[achievementsV2]` (integer)
- `limit[leaderboardsV2]` (integer)

## See Also

- [Create an Activity](post-v1-gamecenteractivities.md)
  Create an activity for your Game Center detail or Game Center group.
- [Add an Achievement to a Game Center Activity](post-v1-gamecenteractivities-_id_-relationships-achievementsv2.md)
  Add an achievement to a Game Center activity.
- [Add a Leaderboard to a Game Center Activity](post-v1-gamecenteractivities-_id_-relationships-leaderboardsv2.md)
  Add a leaderboard to a Game Center activity.
- [Modify the achievements for a game center activity](post-v1-gamecenteractivities-_id_-relationships-achievements.md)
  Update the relationship between achievements and a specific Game Center activity.
- [Modify the leaderboards for a game center activity](post-v1-gamecenteractivities-_id_-relationships-leaderboards.md)
  Update the relationship between a leaderboard and a specific Game Center activity.
- [Read Activity Information](get-v1-gamecenteractivities-_id_.md)
  Get information for a specific Game Center activity.
- [Read the Versions for an Activity](get-v1-gamecenteractivities-_id_-versions.md)
  Get a list of versions for a specific Game Center activity.
- [List version IDs for a Game Center activity](get-v1-gamecenteractivities-_id_-relationships-versions.md)
- [List all activities for a game center detail](get-v1-gamecenterdetails-_id_-gamecenteractivities.md)
  Get activity release information for a specific Game Center detail.
- [List Game Center activity IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-gamecenteractivities.md)
- [List activity IDs for a Game Center group](get-v1-gamecentergroups-_id_-relationships-gamecenteractivities.md)
  Get a list of activity IDs for a specific Game Center group.
- [Modify an Activity](patch-v1-gamecenteractivities-_id_.md)
  Update details for a specific Game Center activity.
- [Delete an Activity](delete-v1-gamecenteractivities-_id_.md)
  Remove a specific Game Center activity.
- [Remove an Achievement](delete-v1-gamecenteractivities-_id_-relationships-achievementsv2.md)
  Remove an achievement from a Game Center activity.
- [Remove a Leaderboard](delete-v1-gamecenteractivities-_id_-relationships-leaderboardsv2.md)
  Remove a leaderboard from a Game Center activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecentergroups-_id_-gamecenteractivities)*