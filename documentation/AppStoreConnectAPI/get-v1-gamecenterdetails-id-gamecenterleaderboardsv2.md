# List All Game Center Leaderboards for a Game Center Detail

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of leaderboards for a specific Game Center detail.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- fields[gameCenterActivities]:
- fields[gameCenterChallenges]:
- fields[gameCenterDetails]:
- fields[gameCenterGroups]:
- fields[gameCenterLeaderboardSets]:
- fields[gameCenterLeaderboardVersions]:
- fields[gameCenterLeaderboards]:
- filter[archived]:
- filter[id]:
- filter[referenceName]:
- include:
- limit:
- limit[gameCenterLeaderboardSets]:
- limit[versions]:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/gameCenterLeaderboardsV2`

## Parameters

- `fields[gameCenterActivities]` ([string])
- `fields[gameCenterChallenges]` ([string])
- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterGroups]` ([string])
- `fields[gameCenterLeaderboardSets]` ([string])
- `fields[gameCenterLeaderboardVersions]` ([string])
- `fields[gameCenterLeaderboards]` ([string])
- `filter[archived]` ([string])
- `filter[id]` ([string])
- `filter[referenceName]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[gameCenterLeaderboardSets]` (integer)
- `limit[versions]` (integer)

## See Also

- [Get All Leaderboard IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsv2.md)
  Get a list of leaderboard resource IDs for a specific Game Center detail.
- [Read Leaderboard Releases](get-v1-gamecenterdetails-_id_-leaderboardreleases.md)
  List all leaderboard releases for a Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/leaderboardReleases](get-v1-gamecenterdetails-_id_-relationships-leaderboardreleases.md)
- [Read Leaderboard Information](get-v1-gamecenterdetails-_id_-gamecenterleaderboards.md)
  Get all leaderboards and related information for a Game Center detail.
- [List Leaderboards](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboards.md)
  ​List all leaderboards for a Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-gamecenterleaderboardsv2)*