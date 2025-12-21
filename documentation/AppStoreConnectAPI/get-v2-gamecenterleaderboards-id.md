# Read Game Center leaderboard information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific Game Center leaderboard.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- fields[gameCenterLeaderboardVersions]:
- fields[gameCenterLeaderboards]:
- include:
- limit[gameCenterLeaderboardSets]:
- limit[versions]:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## See Also

- [List all versions for a Game Center leaderboard](get-v2-gamecenterleaderboards-_id_-versions.md)
  Get a list of versions for a specific Game Center leaderboard.
- [Get all version IDs for a Game Center leaderboard](get-v2-gamecenterleaderboards-_id_-relationships-versions.md)
  Get a list of version resource IDs for a specific Game Center leaderboard.
- [Read leaderboard information](get-v1-gamecenterleaderboards-_id_.md)
  Read information about a specific leaderboard.
- [Read group information for a leaderboard](get-v1-gamecenterleaderboards-_id_-groupleaderboard.md)
  Read the group leadboard to which a leaderboard belongs.
- [List all localizations for a leaderboard](get-v1-gamecenterleaderboards-_id_-localizations.md)
  Get a list of localized metadata for a leaderboard.
- [GET /v1/gameCenterLeaderboards/{id}/relationships/localizations](get-v1-gamecenterleaderboards-_id_-relationships-localizations.md)
- [List all groups to which a leaderboard belongs ](get-v1-gamecenterleaderboards-_id_-relationships-groupleaderboard.md)
  List associated group leaderboards for a specific leaderboard.
- [List releases for a leaderboard](get-v1-gamecenterleaderboards-_id_-releases.md)
  Read the state of releases for a leaderboard and related information.
- [GET /v1/gameCenterLeaderboards/{id}/relationships/releases](get-v1-gamecenterleaderboards-_id_-relationships-releases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterleaderboards-_id_)*