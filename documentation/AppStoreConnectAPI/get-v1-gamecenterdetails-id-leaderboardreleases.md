# Read Leaderboard Releases

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all leaderboard releases for a Game Center detail.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/leaderboardReleases`

## Parameters

- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterLeaderboardReleases]` ([string])
- `fields[gameCenterLeaderboards]` ([string])
- `filter[gameCenterLeaderboard]` ([string])
- `filter[live]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [List All Game Center Leaderboards for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterleaderboardsv2.md)
  Get a list of leaderboards for a specific Game Center detail.
- [Get All Leaderboard IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsv2.md)
  Get a list of leaderboard resource IDs for a specific Game Center detail.
- [List leaderboard release IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-leaderboardreleases.md)
- [Get leaderboards information](get-v1-gamecenterdetails-_id_-gamecenterleaderboards.md)
  Get all leaderboards and related information for a Game Center detail.
- [List Leaderboards](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboards.md)
  ​List all leaderboards for a Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-leaderboardreleases)*