# List All Localizations for an Activity Version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get details about the default localization for a specific Game Center activity version.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterActivityVersions/{id}/localizations`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterActivityImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `imageAsset`, `uploadOperations`, `assetDeliveryState`
- `fields[gameCenterActivityLocalizations]` ([string]): **Allowed Values**: `locale`, `name`, `description`, `version`, `image`
- `fields[gameCenterActivityVersions]` ([string]): **Allowed Values**: `version`, `state`, `fallbackUrl`, `activity`, `localizations`, `defaultImage`, `releases`
- `include` ([string]): **Allowed Values**: `version`, `image`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`GameCenterActivityLocalizationsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Read, create, and update Game Center activity versions
- [Read the Versions for an Activity](./get-v1-gamecenteractivities-_id_-versions.md)
  Get a list of versions for a specific Game Center activity.
- [List version IDs for a Game Center activity](./get-v1-gamecenteractivities-_id_-relationships-versions.md)
- [Read Activity Version Information](./get-v1-gamecenteractivityversions-_id_.md)
  Get information for a specific Game Center activity version.
- [Read Default Image Information for an Activity Version](./get-v1-gamecenteractivityversions-_id_-defaultimage.md)
  Get details about the default image for a specific Game Center activity version.
- [Get the default image ID for a Game Center activity version](./get-v1-gamecenteractivityversions-_id_-relationships-defaultimage.md)
- [List localization IDs for a Game Center activity version](./get-v1-gamecenteractivityversions-_id_-relationships-localizations.md)
- [Add an Activity Version Release](./post-v1-gamecenteractivityversionreleases.md)
  Add a version release for a specific Game Center activity.
- [Create an Activity Version](./post-v1-gamecenteractivityversions.md)
  Add an activity to a Game Center detail, group, or leaderboard.
- [Modify an Activity Version](./patch-v1-gamecenteractivityversions-_id_.md)
  Update a specific activity version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenteractivityversions-_id_-localizations)*