# Get leaderboards information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get all leaderboards and related information for a Game Center detail.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/gameCenterLeaderboards`

## Parameters

- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterGroups]` ([string])
- `fields[gameCenterLeaderboardLocalizations]` ([string])
- `fields[gameCenterLeaderboardReleases]` ([string])
- `fields[gameCenterLeaderboardSets]` ([string])
- `fields[gameCenterLeaderboards]` ([string])
- `filter[archived]` ([string])
- `filter[id]` ([string])
- `filter[referenceName]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[gameCenterLeaderboardSets]` (integer)
- `limit[localizations]` (integer)
- `limit[releases]` (integer)
- `fields[gameCenterActivities]` ([string])
- `fields[gameCenterChallenges]` ([string])

## See Also

- [List All Game Center Leaderboards for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterleaderboardsv2.md)
  Get a list of leaderboards for a specific Game Center detail.
- [Get All Leaderboard IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsv2.md)
  Get a list of leaderboard resource IDs for a specific Game Center detail.
- [Read Leaderboard Releases](get-v1-gamecenterdetails-_id_-leaderboardreleases.md)
  List all leaderboard releases for a Game Center detail.
- [List leaderboard release IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-leaderboardreleases.md)
- [List Leaderboards](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboards.md)
  ​List all leaderboards for a Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-gamecenterleaderboards)*