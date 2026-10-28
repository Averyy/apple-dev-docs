# List All Localizations for a Game Center Achievement Version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of localizations for a specific Game Center achievement version.

**Availability**:
- App Store Connect API 3.6+

## Overview

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

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterAchievementImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `imageAsset`, `uploadOperations`, `assetDeliveryState`, `localization`
- `fields[gameCenterAchievementLocalizations]` ([string]): **Allowed Values**: `locale`, `name`, `beforeEarnedDescription`, `afterEarnedDescription`, `version`, `image`
- `fields[gameCenterAchievementVersions]` ([string]): **Allowed Values**: `version`, `state`, `achievement`, `localizations`
- `include` ([string]): **Allowed Values**: `version`, `image`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`GameCenterAchievementLocalizationsV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and creating achievement versions
- [Read Game Center Achievement Version Information](./get-v2-gamecenterachievementversions-_id_.md)
  Get information about a specific Game Center achievement version.
- [Get All Localization IDs for a Game Center Achievement Version](./get-v2-gamecenterachievementversions-_id_-relationships-localizations.md)
  Get a list of localization resource IDs for a specific Game Center achievement version.
- [Create a Game Center Achievement Version](./post-v2-gamecenterachievementversions.md)
  Create a Game Center achievement version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterachievementversions-_id_-localizations)*