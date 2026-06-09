# Read the versions for a Game Center challenge

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get version information for a specific Game Center challenge.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterChallenges/{id}/relationships/versions`

## Parameters

- `limit` (integer)

## See Also

- [Create a Challenge Version](post-v1-gamecenterchallengeversions.md)
  Add a version for a specific Game Center challenge.
- [Read the Versions for a Challenge](get-v1-gamecenterchallenges-_id_-versions.md)
  Get a list of versions for a specific Game Center challenge.
- [Read Challenge Version Information](get-v1-gamecenterchallengeversions-_id_.md)
  Get information for a specific Game Center challenge localization.
- [Read Default Image Information for a Challenge Version](get-v1-gamecenterchallengeversions-_id_-defaultimage.md)
  Get details about the default image for a specific Game Center challenge version.
- [List All Localizations for a Challenge Version](get-v1-gamecenterchallengeversions-_id_-localizations.md)
  Get details about the default localization for a specific Game Center challenge version.
- [Get the default image id for a challenge version](get-v1-gamecenterchallengeversions-_id_-relationships-defaultimage.md)
  Get the default image ID for a specific Game Center challenge version.
- [Get the localization ids for a challenge version](get-v1-gamecenterchallengeversions-_id_-relationships-localizations.md)
  List all the localization IDs for a specific Game Center challenge version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterchallenges-_id_-relationships-versions)*