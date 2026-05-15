# Read Challenge Version Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information for a specific Game Center challenge localization.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterChallengeVersions/{id}`

## Parameters

- `fields[gameCenterChallengeImages]` ([string])
- `fields[gameCenterChallengeLocalizations]` ([string])
- `fields[gameCenterChallengeVersions]` ([string])
- `include` ([string])
- `limit[localizations]` (integer)
- `limit[releases]` (integer)
- `fields[gameCenterChallengeVersionReleases]` ([string])
- `fields[gameCenterChallenges]` ([string])

## See Also

- [Create a Challenge Version](post-v1-gamecenterchallengeversions.md)
  Add a version for a specific Game Center challenge.
- [Read the Challenges for a Game Center Group](get-v1-gamecenterchallenges-_id_-relationships-versions.md)
  Get challenge information for a specific Game Center group.
- [Read the Versions for a Challenge](get-v1-gamecenterchallenges-_id_-versions.md)
  Get a list of versions for a specific Game Center challenge.
- [Read Default Image Information for a Challenge Version](get-v1-gamecenterchallengeversions-_id_-defaultimage.md)
  Get details about the default image for a specific Game Center challenge version.
- [List All Localizations for a Challenge Version](get-v1-gamecenterchallengeversions-_id_-localizations.md)
  Get details about the default localization for a specific Game Center challenge version.
- [Get the Default Image ID for a Challenge Version](get-v1-gamecenterchallengeversions-_id_-relationships-defaultimage.md)
  Get the default image ID for a specific Game Center challenge version.
- [Get the Localization IDs for a Challenge Version](get-v1-gamecenterchallengeversions-_id_-relationships-localizations.md)
  List all the localization IDs for a specific Game Center challenge version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterchallengeversions-_id_)*