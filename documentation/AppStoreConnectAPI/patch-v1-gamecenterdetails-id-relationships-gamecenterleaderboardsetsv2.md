# Modify the Leaderboard Sets for a Game Center Detail

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update the leaderboard sets relationship for a specific Game Center detail.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- 204:
- 401:
- 403:
- 404:
- 409:
- 422:
- 429:

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/relationships/gameCenterLeaderboardSetsV2`

## Parameters

- `id` (string) *(required)*

## See Also

- [Enable Game Center for an App](post-v1-gamecenterdetails.md)
  Create a Game Center detail for an app.
- [Modify a Game Center Detail for an App](patch-v1-gamecenterdetails-_id_.md)
  Edit challenge state, default leaderboards, and groups.
- [Modify the Achievements for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterachievementsv2.md)
  Update the achievements relationship for a specific Game Center detail.
- [Modify the Leaderboards for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsv2.md)
  Update the leaderboards relationship for a specific Game Center detail.
- [Modify the Associated Leaderboard Sets for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsets.md)
  Edit the associated leaderboard sets for a Game Center detail.
- [Modify the Associated Leaderboards for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboards.md)
  Edit the associated leaderboards for a Game Center detail.
- [Modify the Challenges Minimum Platform Version for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-challengesminimumplatformversions.md)
  Update the relationship between a challenges minimum platform version and a specific Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsetsv2)*