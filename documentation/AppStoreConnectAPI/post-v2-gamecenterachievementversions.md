# Create a Game Center Achievement Version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a Game Center achievement version.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- 201:
- 400:
- 401:
- 403:
- 409:
- 422:
- 429:

## Endpoint

`POST https://api.appstoreconnect.apple.com/v2/gameCenterAchievementVersions`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterAchievementVersionV2CreateRequest`

## Responses

- `201` Created (`GameCenterAchievementVersionV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and creating achievement versions
- [Read Game Center Achievement Version Information](./get-v2-gamecenterachievementversions-_id_.md)
  Get information about a specific Game Center achievement version.
- [List All Localizations for a Game Center Achievement Version](./get-v2-gamecenterachievementversions-_id_-localizations.md)
  Get a list of localizations for a specific Game Center achievement version.
- [Get All Localization IDs for a Game Center Achievement Version](./get-v2-gamecenterachievementversions-_id_-relationships-localizations.md)
  Get a list of localization resource IDs for a specific Game Center achievement version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v2-gamecenterachievementversions)*