# Read Game Center Achievement Version Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific Game Center achievement version.

**Availability**:
- App Store Connect API 3.6+

## Overview

- id:
- fields[gameCenterAchievementLocalizations]:
- fields[gameCenterAchievementVersions]:
- include:
- limit[localizations]:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterAchievementVersions/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterAchievementLocalizations]` ([string]): **Allowed Values**: `locale`, `name`, `beforeEarnedDescription`, `afterEarnedDescription`, `version`, `image`
- `fields[gameCenterAchievementVersions]` ([string]): **Allowed Values**: `version`, `state`, `achievement`, `localizations`
- `fields[gameCenterAchievements]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `points`, `showBeforeEarned`, `repeatable`, `archived`, `activityProperties`, `gameCenterDetail`, `gameCenterGroup`, `activity`, `versions`
- `include` ([string]): **Allowed Values**: `achievement`, `localizations`
- `limit[localizations]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`GameCenterAchievementVersionV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and creating achievement versions
- [List All Localizations for a Game Center Achievement Version](./get-v2-gamecenterachievementversions-_id_-localizations.md)
  Get a list of localizations for a specific Game Center achievement version.
- [Get All Localization IDs for a Game Center Achievement Version](./get-v2-gamecenterachievementversions-_id_-relationships-localizations.md)
  Get a list of localization resource IDs for a specific Game Center achievement version.
- [Create a Game Center Achievement Version](./post-v2-gamecenterachievementversions.md)
  Create a Game Center achievement version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterachievementversions-_id_)*