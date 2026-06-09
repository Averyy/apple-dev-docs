# List game center leaderboard sets in a group

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read Game Center leaderboard sets information for a specific group.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterGroups/{id}/gameCenterLeaderboardSets`

## Parameters

- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterGroups]` ([string])
- `fields[gameCenterLeaderboardSetLocalizations]` ([string])
- `fields[gameCenterLeaderboardSetReleases]` ([string])
- `fields[gameCenterLeaderboardSets]` ([string])
- `fields[gameCenterLeaderboards]` ([string])
- `filter[id]` ([string])
- `filter[referenceName]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[gameCenterLeaderboards]` (integer)
- `limit[localizations]` (integer)
- `limit[releases]` (integer)

## See Also

- [Read Group Information](get-v1-gamecentergroups.md)
  List information for all groups.
- [Read information for a specific group](get-v1-gamecentergroups-_id_.md)
  Read information for a specific Game Center group.
- [Create a Group](post-v1-gamecentergroups.md)
  Add a new group.
- [Modify a Group](patch-v1-gamecentergroups-_id_.md)
  Edit the reference name for a group.
- [Delete a Group](delete-v1-gamecentergroups-_id_.md)
  Remove a group.
- [List All Game Center Achievements for a Game Center Group](get-v1-gamecentergroups-_id_-gamecenterachievementsv2.md)
  Get a list of achievements for a specific Game Center group.
- [List All Game Center Leaderboard Sets for a Game Center Group](get-v1-gamecentergroups-_id_-gamecenterleaderboardsetsv2.md)
  Get a list of leaderboard sets for a specific Game Center group.
- [List All Game Center Leaderboards for a Game Center Group](get-v1-gamecentergroups-_id_-gamecenterleaderboardsv2.md)
  Get a list of leaderboards for a specific Game Center group.
- [List the Achievements in a Group](get-v1-gamecentergroups-_id_-gamecenterachievements.md)
  List achievements information for a specific group.
- [List game center details for a group](get-v1-gamecentergroups-_id_-gamecenterdetails.md)
  Read Game Center detail information for a specific group.
- [List Game Center detail IDs for a Game Center group](get-v1-gamecentergroups-_id_-relationships-gamecenterdetails.md)
- [List Game Center detail IDs for a Game Center group](get-v1-gamecentergroups-_id_-relationships-gamecenterdetails.md)
- [List game center leaderboards for a group](get-v1-gamecentergroups-_id_-gamecenterleaderboards.md)
  Read Game Center leaderboard information for a specific group.
- [List all activities for a game center group](get-v1-gamecentergroups-_id_-gamecenteractivities.md)
  Get a list of all activities for a Game Center group.
- [List activity IDs for a Game Center group](get-v1-gamecentergroups-_id_-relationships-gamecenteractivities.md)
  Get a list of activity IDs for a specific Game Center group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecentergroups-_id_-gamecenterleaderboardsets)*