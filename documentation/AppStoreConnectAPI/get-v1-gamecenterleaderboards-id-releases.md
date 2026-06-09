# List Releases for a Leaderboard

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read the state of releases for a leaderboard and related information.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/{id}/releases`

## Parameters

- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterLeaderboardReleases]` ([string])
- `fields[gameCenterLeaderboards]` ([string])
- `filter[gameCenterDetail]` ([string])
- `filter[live]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [List release IDs for a Game Center leaderboard](get-v1-gamecenterleaderboards-_id_-relationships-releases.md)
- [Read Leaderboard Release Information](get-v1-gamecenterleaderboardreleases-_id_.md)
  Read the state of a specific leaderboard release.
- [Create a Leaderboard Release](post-v1-gamecenterleaderboardreleases.md)
  Add a new leaderboard release.
- [Delete a Leaderboard Release](delete-v1-gamecenterleaderboardreleases-_id_.md)
  Delete a new leaderboard release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterleaderboards-_id_-releases)*