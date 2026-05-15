# Read Leaderboard Release Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read the state of a specific leaderboard release.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardReleases/{id}`

## Parameters

- `fields[gameCenterLeaderboardReleases]` ([string])
- `include` ([string])
- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterLeaderboards]` ([string])

## See Also

- [List Releases for a Leaderboard](get-v1-gamecenterleaderboards-_id_-releases.md)
  Read the state of releases for a leaderboard and related information.
- [GET /v1/gameCenterLeaderboards/{id}/relationships/releases](get-v1-gamecenterleaderboards-_id_-relationships-releases.md)
- [Create a Leaderboard Release](post-v1-gamecenterleaderboardreleases.md)
  Add a new leaderboard release.
- [Delete a Leaderboard Release](delete-v1-gamecenterleaderboardreleases-_id_.md)
  Delete a new leaderboard release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterleaderboardreleases-_id_)*