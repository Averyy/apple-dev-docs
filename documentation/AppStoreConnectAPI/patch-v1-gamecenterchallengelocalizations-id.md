# Modify a Challenge Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update localization information for a specific Game Center challenge.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterChallengeLocalizations/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Read Challenge Localization Information](get-v1-gamecenterchallengelocalizations-_id_.md)
  Get information for a specific Game Center challenge localization.
- [Read Image Information for a Challenge Localization](get-v1-gamecenterchallengelocalizations-_id_-image.md)
  Get details about the image for a specific Game Center challenge localization.
- [Get the image id for a challenge localization](get-v1-gamecenterchallengelocalizations-_id_-relationships-image.md)
  Get the image ID for a specific Game Center challenge localization.
- [List All Localizations for a Challenge Version](get-v1-gamecenterchallengeversions-_id_-localizations.md)
  Get details about the default localization for a specific Game Center challenge version.
- [Get the localization ids for a challenge version](get-v1-gamecenterchallengeversions-_id_-relationships-localizations.md)
  List all the localization IDs for a specific Game Center challenge version.
- [Add a Challenge Localization](post-v1-gamecenterchallengelocalizations.md)
  Add a localization for a specific Game Center challenge.
- [Delete a Challenge Localization](delete-v1-gamecenterchallengelocalizations-_id_.md)
  Remove a specific localization from a Game Center challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterchallengelocalizations-_id_)*