# Get leaderboard sets information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get all leaderboard sets and related information for a Game Center detail.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/gameCenterLeaderboardSets`

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

- [List All Game Center Leaderboard Sets for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterleaderboardsetsv2.md)
  Get a list of leaderboard sets for a specific Game Center detail.
- [Get All Leaderboard Set IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsetsv2.md)
  Get a list of leaderboard set resource IDs for a specific Game Center detail.
- [List Leaderboard Sets](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsets.md)
  List all leaderboards for a Game Center detail.
- [Get leaderboard set releases information](get-v1-gamecenterdetails-_id_-leaderboardsetreleases.md)
  List all leaderboard set releases for a Game Center detail.
- [List leaderboard set release IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-leaderboardsetreleases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-gamecenterleaderboardsets)*