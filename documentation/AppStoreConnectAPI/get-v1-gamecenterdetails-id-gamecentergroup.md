# Read the Groups in a Game Center Detail

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of groups in a Game Center detail.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/gameCenterGroup`

## Parameters

- `fields[gameCenterAchievements]` ([string])
- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterGroups]` ([string])
- `fields[gameCenterLeaderboardSets]` ([string])
- `fields[gameCenterLeaderboards]` ([string])
- `include` ([string])
- `limit[gameCenterAchievements]` (integer)
- `limit[gameCenterDetails]` (integer)
- `limit[gameCenterLeaderboardSets]` (integer)
- `limit[gameCenterLeaderboards]` (integer)
- `fields[gameCenterActivities]` ([string])
- `fields[gameCenterChallenges]` ([string])
- `limit[gameCenterAchievementsV2]` (integer)
- `limit[gameCenterActivities]` (integer)
- `limit[gameCenterChallenges]` (integer)
- `limit[gameCenterLeaderboardSetsV2]` (integer)
- `limit[gameCenterLeaderboardsV2]` (integer)

## See Also

- [Read the State of Game Center for an App](get-v1-apps-_id_-gamecenterdetail.md)
  Get Game Center detail information for an app.
- [Read Game Center Details](get-v1-gamecenterdetails-_id_.md)
  Read a specific Game Center detail and related information.
- [Read App Versions for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterappversions.md)
  Get a list of app versions for a Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/gameCenterAppVersions](get-v1-gamecenterdetails-_id_-relationships-gamecenterappversions.md)
- [GET /v1/gameCenterDetails/{id}/relationships/gameCenterGroup](get-v1-gamecenterdetails-_id_-relationships-gamecentergroup.md)
- [Read the Challenges for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center detail.
- [Read Challenge IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterchallenges.md)
  List all the challenge IDs for a specific Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-gamecentergroup)*