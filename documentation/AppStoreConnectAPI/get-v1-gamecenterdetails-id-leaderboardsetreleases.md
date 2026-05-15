# Read Leaderboard Set Release Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all leaderboard set releases for a Game Center detail.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/leaderboardSetReleases`

## Parameters

- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterLeaderboardSetReleases]` ([string])
- `fields[gameCenterLeaderboardSets]` ([string])
- `filter[gameCenterLeaderboardSet]` ([string])
- `filter[live]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [List All Game Center Leaderboard Sets for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterleaderboardsetsv2.md)
  Get a list of leaderboard sets for a specific Game Center detail.
- [Get All Leaderboard Set IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsetsv2.md)
  Get a list of leaderboard set resource IDs for a specific Game Center detail.
- [Read Leaderboard Set Information](get-v1-gamecenterdetails-_id_-gamecenterleaderboardsets.md)
  Get all leaderboard sets and related information for a Game Center detail.
- [List Leaderboard Sets](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsets.md)
  List all leaderboards for a Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/leaderboardSetReleases](get-v1-gamecenterdetails-_id_-relationships-leaderboardsetreleases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-leaderboardsetreleases)*