# Modify Associated Achievements

**Framework**: App Store Connect API  
**Kind**: httpRequest

Modify the achievements for a Game Center detail.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/relationships/gameCenterAchievements`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the Game Center detail resource ID from the [`Read the state of game center for an app`](get-v1-apps-_id_-gamecenterdetail.md) response.

## See Also

- [List All Game Center Achievements for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterachievementsv2.md)
  Get a list of achievements for a specific Game Center detail.
- [Get All Achievement IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterachievementsv2.md)
  Get a list of achievement resource IDs for a specific Game Center detail.
- [List All Achievements](get-v1-gamecenterdetails-_id_-gamecenterachievements.md)
  List all achievement information for a Game Center detail.
- [List achievement releases](get-v1-gamecenterdetails-_id_-achievementreleases.md)
  Read information about the achievement releases for specific Game Center detail.
- [List achievement release IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-achievementreleases.md)
- [List Achievements](get-v1-gamecenterdetails-_id_-relationships-gamecenterachievements.md)
  List the achievements for a Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterdetails-_id_-relationships-gamecenterachievements)*