# List All Versions for a Game Center Leaderboard Set

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of versions for a specific Game Center leaderboard set.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- fields[gameCenterLeaderboardSetLocalizations]:
- fields[gameCenterLeaderboardSetVersions]:
- fields[gameCenterLeaderboardSets]:
- include:
- limit:
- limit[localizations]:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboardSets/{id}/versions`

## Parameters

- `fields[gameCenterLeaderboardSetLocalizations]` ([string])
- `fields[gameCenterLeaderboardSetVersions]` ([string])
- `fields[gameCenterLeaderboardSets]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[localizations]` (integer)

## See Also

- [Read Game Center Leaderboard Set Information](get-v2-gamecenterleaderboardsets-_id_.md)
  Get information about a specific Game Center leaderboard set.
- [List All Leaderboards for a Game Center Leaderboard Set](get-v2-gamecenterleaderboardsets-_id_-gamecenterleaderboards.md)
  Get a list of leaderboards for a specific Game Center leaderboard set.
- [Get All Leaderboard IDs for a Game Center Leaderboard Set](get-v2-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Get a list of leaderboard resource IDs for a specific Game Center leaderboard set.
- [Get All Version IDs for a Game Center Leaderboard Set](get-v2-gamecenterleaderboardsets-_id_-relationships-versions.md)
  Get a list of version resource IDs for a specific Game Center leaderboard set.
- [Read Leaderboard Set Information](get-v1-gamecenterleaderboardsets-_id_.md)
  Read information about a specific leaderboard set.
- [List Leaderboard Information for a Leaderboard Set](get-v1-gamecenterleaderboardsets-_id_-gamecenterleaderboards.md)
  Read the leadboards that belong to a learderboard set.
- [List Leaderboard Sets in a Group Leaderboard Set](get-v1-gamecenterleaderboardsets-_id_-groupleaderboardset.md)
  List information about leaderboards and leaderboard sets in a group leaderboard set.
- [List All Localizations for a Leaderboard Set](get-v1-gamecenterleaderboardsets-_id_-localizations.md)
  Get a list of localized metadata for a leaderboard set.
- [List localization IDs for a Game Center leaderboard set](get-v1-gamecenterleaderboardsets-_id_-relationships-localizations.md)
- [Read the Leaderboards in a Leaderboard Set](get-v1-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  List all leaderboards in a leaderboard set.
- [Read the Group Leaderboard Set in a Leaderboard Set](get-v1-gamecenterleaderboardsets-_id_-relationships-groupleaderboardset.md)
  List all the group leaderboard sets in a leaderboard set.
- [List Releases for a Leaderboard Set](get-v1-gamecenterleaderboardsets-_id_-releases.md)
  Read the state of releases for a leaderboard set and related information.
- [List release IDs for a Game Center leaderboard set](get-v1-gamecenterleaderboardsets-_id_-relationships-releases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterleaderboardsets-_id_-versions)*