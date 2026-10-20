# Read Challenge Version Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information for a specific Game Center challenge localization.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterChallengeVersions/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterChallengeImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `imageAsset`, `uploadOperations`, `assetDeliveryState`
- `fields[gameCenterChallengeLocalizations]` ([string]): **Allowed Values**: `locale`, `name`, `description`, `version`, `image`
- `fields[gameCenterChallengeVersions]` ([string]): **Allowed Values**: `version`, `state`, `challenge`, `localizations`, `releases`, `defaultImage`
- `include` ([string]): **Allowed Values**: `challenge`, `localizations`, `releases`, `defaultImage`
- `limit[localizations]` (integer): **Maximum**: `50`
- `limit[releases]` (integer) *(deprecated)*: **Maximum**: `50`
- `fields[gameCenterChallengeVersionReleases]` ([string]) *(deprecated)*: **Allowed Values**: `version`
- `fields[gameCenterChallenges]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `archived`, `challengeType`, `repeatable`, `gameCenterDetail`, `gameCenterGroup`, `versions`, `leaderboard`, `leaderboardV2`

## Responses

- `200` OK (`GameCenterChallengeVersionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and listing versions
- [Create a Challenge Version](./post-v1-gamecenterchallengeversions.md)
  Add a version for a specific Game Center challenge.
- [Read the versions for a Game Center challenge](./get-v1-gamecenterchallenges-_id_-relationships-versions.md)
  Get version information for a specific Game Center challenge.
- [Read the Versions for a Challenge](./get-v1-gamecenterchallenges-_id_-versions.md)
  Get a list of versions for a specific Game Center challenge.
- [Read Default Image Information for a Challenge Version](./get-v1-gamecenterchallengeversions-_id_-defaultimage.md)
  Get details about the default image for a specific Game Center challenge version.
- [List All Localizations for a Challenge Version](./get-v1-gamecenterchallengeversions-_id_-localizations.md)
  Get details about the default localization for a specific Game Center challenge version.
- [Get the default image id for a challenge version](./get-v1-gamecenterchallengeversions-_id_-relationships-defaultimage.md)
  Get the default image ID for a specific Game Center challenge version.
- [Get the localization ids for a challenge version](./get-v1-gamecenterchallengeversions-_id_-relationships-localizations.md)
  List all the localization IDs for a specific Game Center challenge version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterchallengeversions-_id_)*