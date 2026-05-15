# List All Game Center Leaderboard Sets for a Game Center Detail

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of leaderboard sets for a specific Game Center detail.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- fields[gameCenterDetails]:
- fields[gameCenterGroups]:
- fields[gameCenterLeaderboardSetVersions]:
- fields[gameCenterLeaderboardSets]:
- fields[gameCenterLeaderboards]:
- filter[id]:
- filter[referenceName]:
- include:
- limit:
- limit[gameCenterLeaderboards]:
- limit[versions]:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/gameCenterLeaderboardSetsV2`

## Parameters

- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterGroups]` ([string])
- `fields[gameCenterLeaderboardSetVersions]` ([string])
- `fields[gameCenterLeaderboardSets]` ([string])
- `fields[gameCenterLeaderboards]` ([string])
- `filter[id]` ([string])
- `filter[referenceName]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[gameCenterLeaderboards]` (integer)
- `limit[versions]` (integer)

## See Also

- [Get All Leaderboard Set IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsetsv2.md)
  Get a list of leaderboard set resource IDs for a specific Game Center detail.
- [Read Leaderboard Set Information](get-v1-gamecenterdetails-_id_-gamecenterleaderboardsets.md)
  Get all leaderboard sets and related information for a Game Center detail.
- [List Leaderboard Sets](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsets.md)
  List all leaderboards for a Game Center detail.
- [Read Leaderboard Set Release Information](get-v1-gamecenterdetails-_id_-leaderboardsetreleases.md)
  List all leaderboard set releases for a Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/leaderboardSetReleases](get-v1-gamecenterdetails-_id_-relationships-leaderboardsetreleases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-gamecenterleaderboardsetsv2)*