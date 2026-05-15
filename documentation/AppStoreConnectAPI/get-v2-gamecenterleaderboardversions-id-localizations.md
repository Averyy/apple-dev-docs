# List All Localizations for a Game Center Leaderboard Version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of localizations for a specific Game Center leaderboard version.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- fields[gameCenterLeaderboardImages]:
- fields[gameCenterLeaderboardLocalizations]:
- fields[gameCenterLeaderboardVersions]:
- include:
- limit:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboardVersions/{id}/localizations`

## Parameters

- `fields[gameCenterLeaderboardImages]` ([string])
- `fields[gameCenterLeaderboardLocalizations]` ([string])
- `fields[gameCenterLeaderboardVersions]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [Read Game Center Leaderboard Version Information](get-v2-gamecenterleaderboardversions-_id_.md)
  Get information about a specific Game Center leaderboard version.
- [Get All Localization IDs for a Game Center Leaderboard Version](get-v2-gamecenterleaderboardversions-_id_-relationships-localizations.md)
  Get a list of localization resource IDs for a specific Game Center leaderboard version.
- [Create a Game Center Leaderboard Version](post-v2-gamecenterleaderboardversions.md)
  Create a Game Center leaderboard version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterleaderboardversions-_id_-localizations)*