# Read Game Center Leaderboard Set Version Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific Game Center leaderboard set version.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- fields[gameCenterLeaderboardSetLocalizations]:
- fields[gameCenterLeaderboardSetVersions]:
- include:
- limit[localizations]:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboardSetVersions/{id}`

## Parameters

- `fields[gameCenterLeaderboardSetLocalizations]` ([string])
- `fields[gameCenterLeaderboardSetVersions]` ([string])
- `fields[gameCenterLeaderboardSets]` ([string])
- `include` ([string])
- `limit[localizations]` (integer)

## See Also

- [List All Localizations for a Game Center Leaderboard Set Version](get-v2-gamecenterleaderboardsetversions-_id_-localizations.md)
  Get a list of localizations for a specific Game Center leaderboard set version.
- [Get All Localization IDs for a Game Center Leaderboard Set Version](get-v2-gamecenterleaderboardsetversions-_id_-relationships-localizations.md)
  Get a list of localization resource IDs for a specific Game Center leaderboard set version.
- [Create a Game Center Leaderboard Set Version](post-v2-gamecenterleaderboardsetversions.md)
  Create a Game Center leaderboard set version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterleaderboardsetversions-_id_)*