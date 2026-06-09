# Get All Version IDs for a Game Center Leaderboard

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of version resource IDs for a specific Game Center leaderboard.

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

`GET https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboards/{id}/relationships/versions`

## Parameters

- `limit` (integer)

## See Also

- [Read Game Center Leaderboard Information](get-v2-gamecenterleaderboards-_id_.md)
  Get information about a specific Game Center leaderboard.
- [List All Versions for a Game Center Leaderboard](get-v2-gamecenterleaderboards-_id_-versions.md)
  Get a list of versions for a specific Game Center leaderboard.
- [Read Leaderboard Information](get-v1-gamecenterleaderboards-_id_.md)
  Read information about a specific leaderboard.
- [Read Group Information for a Leaderboard](get-v1-gamecenterleaderboards-_id_-groupleaderboard.md)
  Read the group leadboard to which a leaderboard belongs.
- [List All Localizations for a Leaderboard](get-v1-gamecenterleaderboards-_id_-localizations.md)
  Get a list of localized metadata for a leaderboard.
- [List localization IDs for a Game Center leaderboard](get-v1-gamecenterleaderboards-_id_-relationships-localizations.md)
- [List all groups to which a leaderboard belongs](get-v1-gamecenterleaderboards-_id_-relationships-groupleaderboard.md)
  List associated group leaderboards for a specific leaderboard.
- [List Releases for a Leaderboard](get-v1-gamecenterleaderboards-_id_-releases.md)
  Read the state of releases for a leaderboard and related information.
- [List release IDs for a Game Center leaderboard](get-v1-gamecenterleaderboards-_id_-relationships-releases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterleaderboards-_id_-relationships-versions)*