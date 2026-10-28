# List All Localizations for a Game Center Leaderboard Version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of localizations for a specific Game Center leaderboard version.

**Availability**:
- App Store Connect API 3.6+

## Overview

- id:
- fields[gameCenterLeaderboardImages]:
- fields[gameCenterLeaderboardLocalizations]:
- fields[gameCenterLeaderboardVersions]:
- include:
- limit:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboardVersions/{id}/localizations`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterLeaderboardImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `imageAsset`, `uploadOperations`, `assetDeliveryState`, `localization`
- `fields[gameCenterLeaderboardLocalizations]` ([string]): **Allowed Values**: `locale`, `name`, `formatterOverride`, `formatterSuffix`, `formatterSuffixSingular`, `description`, `version`, `image`
- `fields[gameCenterLeaderboardVersions]` ([string]): **Allowed Values**: `version`, `state`, `leaderboard`, `localizations`
- `include` ([string]): **Allowed Values**: `version`, `image`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`GameCenterLeaderboardLocalizationsV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and creating leaderboard versions
- [Read Game Center Leaderboard Version Information](./get-v2-gamecenterleaderboardversions-_id_.md)
  Get information about a specific Game Center leaderboard version.
- [Get All Localization IDs for a Game Center Leaderboard Version](./get-v2-gamecenterleaderboardversions-_id_-relationships-localizations.md)
  Get a list of localization resource IDs for a specific Game Center leaderboard version.
- [Create a Game Center Leaderboard Version](./post-v2-gamecenterleaderboardversions.md)
  Create a Game Center leaderboard version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterleaderboardversions-_id_-localizations)*