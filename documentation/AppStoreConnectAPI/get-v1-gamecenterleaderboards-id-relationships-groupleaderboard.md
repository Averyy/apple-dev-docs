# List All Groups to Which a Leaderboard Belongs

**Framework**: App Store Connect API  
**Kind**: httpRequest

List associated group leaderboards for a specific leaderboard.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/{id}/relationships/groupLeaderboard`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the leaderboard resource ID from the [`Read Leaderboard Information`](get-v1-gamecenterdetails-_id_-gamecenterleaderboards.md) response.

## See Also

- [Read Game Center Leaderboard Information](get-v2-gamecenterleaderboards-_id_.md)
  Get information about a specific Game Center leaderboard.
- [List All Versions for a Game Center Leaderboard](get-v2-gamecenterleaderboards-_id_-versions.md)
  Get a list of versions for a specific Game Center leaderboard.
- [Get All Version IDs for a Game Center Leaderboard](get-v2-gamecenterleaderboards-_id_-relationships-versions.md)
  Get a list of version resource IDs for a specific Game Center leaderboard.
- [Read Leaderboard Information](get-v1-gamecenterleaderboards-_id_.md)
  Read information about a specific leaderboard.
- [Read Group Information for a Leaderboard](get-v1-gamecenterleaderboards-_id_-groupleaderboard.md)
  Read the group leadboard to which a leaderboard belongs.
- [List All Localizations for a Leaderboard](get-v1-gamecenterleaderboards-_id_-localizations.md)
  Get a list of localized metadata for a leaderboard.
- [GET /v1/gameCenterLeaderboards/{id}/relationships/localizations](get-v1-gamecenterleaderboards-_id_-relationships-localizations.md)
- [List Releases for a Leaderboard](get-v1-gamecenterleaderboards-_id_-releases.md)
  Read the state of releases for a leaderboard and related information.
- [GET /v1/gameCenterLeaderboards/{id}/relationships/releases](get-v1-gamecenterleaderboards-_id_-relationships-releases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterleaderboards-_id_-relationships-groupleaderboard)*