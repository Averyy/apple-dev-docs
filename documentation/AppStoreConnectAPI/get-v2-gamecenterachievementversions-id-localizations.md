# List All Localizations for a Game Center Achievement Version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of localizations for a specific Game Center achievement version.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- fields[gameCenterAchievementImages]:
- fields[gameCenterAchievementLocalizations]:
- fields[gameCenterAchievementVersions]:
- include:
- limit:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterAchievementVersions/{id}/localizations`

## Parameters

- `fields[gameCenterAchievementImages]` ([string])
- `fields[gameCenterAchievementLocalizations]` ([string])
- `fields[gameCenterAchievementVersions]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [Read Game Center Achievement Version Information](get-v2-gamecenterachievementversions-_id_.md)
  Get information about a specific Game Center achievement version.
- [Get All Localization IDs for a Game Center Achievement Version](get-v2-gamecenterachievementversions-_id_-relationships-localizations.md)
  Get a list of localization resource IDs for a specific Game Center achievement version.
- [Create a Game Center Achievement Version](post-v2-gamecenterachievementversions.md)
  Create a Game Center achievement version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterachievementversions-_id_-localizations)*