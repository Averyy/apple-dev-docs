# List All Images for a Game Center Achievement Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of images for a specific Game Center achievement localization.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- fields[gameCenterAchievementImages]:
- fields[gameCenterAchievementLocalizations]:
- include:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterAchievementLocalizations/{id}/image`

## Parameters

- `fields[gameCenterAchievementImages]` ([string])
- `fields[gameCenterAchievementLocalizations]` ([string])
- `include` ([string])

## See Also

- [Read Game Center Achievement Localization Information](get-v2-gamecenterachievementlocalizations-_id_.md)
  Get information about a specific Game Center achievement localization.
- [Get All Image IDs for a Game Center Achievement Localization](get-v2-gamecenterachievementlocalizations-_id_-relationships-image.md)
  Get a list of image resource IDs for a specific Game Center achievement localization.
- [List All Localizations for an Achievement](get-v1-gamecenterachievements-_id_-localizations.md)
  Read information about the release for specific achievement.
- [List localization IDs for a Game Center achievement](get-v1-gamecenterachievements-_id_-relationships-localizations.md)
- [Read Achievement Localization Information](get-v1-gamecenterachievementlocalizations-_id_.md)
  Read localized information for a specific locale for a specific achievement.
- [Read the Achievement Localization Information](get-v1-gamecenterachievementlocalizations-_id_-gamecenterachievement.md)
  Read the achievement associated with specific localized information.
- [Read the achievement id for a  localization](get-v1-gamecenterachievementlocalizations-_id_-relationships-gamecenterachievement.md)
  Read the achievement ID associated with specific localized information.
- [Read the Image for a Specific Achievement Localization](get-v1-gamecenterachievementlocalizations-_id_-gamecenterachievementimage.md)
  Read the achievement image associated with specific localized information.
- [Get the achievement image ID for a Game Center achievement localization](get-v1-gamecenterachievementlocalizations-_id_-relationships-gamecenterachievementimage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterachievementlocalizations-_id_-image)*