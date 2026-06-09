# Get All Achievement IDs for a Game Center Detail

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of achievement resource IDs for a specific Game Center detail.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- limit:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/relationships/gameCenterAchievementsV2`

## Parameters

- `limit` (integer)

## See Also

- [List All Game Center Achievements for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterachievementsv2.md)
  Get a list of achievements for a specific Game Center detail.
- [List All Achievements](get-v1-gamecenterdetails-_id_-gamecenterachievements.md)
  List all achievement information for a Game Center detail.
- [List achievement releases](get-v1-gamecenterdetails-_id_-achievementreleases.md)
  Read information about the achievement releases for specific Game Center detail.
- [List achievement release IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-achievementreleases.md)
- [List Achievements](get-v1-gamecenterdetails-_id_-relationships-gamecenterachievements.md)
  List the achievements for a Game Center detail.
- [Modify Associated Achievements](patch-v1-gamecenterdetails-_id_-relationships-gamecenterachievements.md)
  Modify the achievements for a Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-relationships-gamecenterachievementsv2)*