# Create a Game Center Leaderboard Set Version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a Game Center leaderboard set version.

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

`POST https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboardSetVersions`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterLeaderboardSetVersionV2CreateRequest`

## Responses

- `201` Created (`GameCenterLeaderboardSetVersionV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and creating leaderboard set versions
- [Read Game Center Leaderboard Set Version Information](./get-v2-gamecenterleaderboardsetversions-_id_.md)
  Get information about a specific Game Center leaderboard set version.
- [List All Localizations for a Game Center Leaderboard Set Version](./get-v2-gamecenterleaderboardsetversions-_id_-localizations.md)
  Get a list of localizations for a specific Game Center leaderboard set version.
- [Get All Localization IDs for a Game Center Leaderboard Set Version](./get-v2-gamecenterleaderboardsetversions-_id_-relationships-localizations.md)
  Get a list of localization resource IDs for a specific Game Center leaderboard set version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v2-gamecenterleaderboardsetversions)*