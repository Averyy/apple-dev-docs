# Read the achievement id for a  localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read the achievement ID associated with specific localized information.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/{id}/relationships/gameCenterAchievement`

## Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Apps resource. Obtain the app resource ID from the [`List All Localizations for an Achievement`](get-v1-gamecenterachievements-_id_-localizations.md) response.

## See Also

- [Read Game Center Achievement Localization Information](get-v2-gamecenterachievementlocalizations-_id_.md)
  Get information about a specific Game Center achievement localization.
- [List All Images for a Game Center Achievement Localization](get-v2-gamecenterachievementlocalizations-_id_-image.md)
  Get a list of images for a specific Game Center achievement localization.
- [Get All Image IDs for a Game Center Achievement Localization](get-v2-gamecenterachievementlocalizations-_id_-relationships-image.md)
  Get a list of image resource IDs for a specific Game Center achievement localization.
- [List All Localizations for an Achievement](get-v1-gamecenterachievements-_id_-localizations.md)
  Read information about the release for specific achievement.
- [List localization IDs for a Game Center achievement](get-v1-gamecenterachievements-_id_-relationships-localizations.md)
- [Read Achievement Localization Information](get-v1-gamecenterachievementlocalizations-_id_.md)
  Read localized information for a specific locale for a specific achievement.
- [Read the Achievement Localization Information](get-v1-gamecenterachievementlocalizations-_id_-gamecenterachievement.md)
  Read the achievement associated with specific localized information.
- [Read the Image for a Specific Achievement Localization](get-v1-gamecenterachievementlocalizations-_id_-gamecenterachievementimage.md)
  Read the achievement image associated with specific localized information.
- [Get the achievement image ID for a Game Center achievement localization](get-v1-gamecenterachievementlocalizations-_id_-relationships-gamecenterachievementimage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterachievementlocalizations-_id_-relationships-gamecenterachievement)*