# Create a Game Center Leaderboard Version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a Game Center leaderboard version.

**Availability**:
- App Store Connect API 3.6+

## Overview

- 201:
- 400:
- 401:
- 403:
- 409:
- 422:
- 429:

## Endpoint

`POST https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboardVersions`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterLeaderboardVersionV2CreateRequest`

## Responses

- `201` Created (`GameCenterLeaderboardVersionV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and creating leaderboard versions
- [Read Game Center Leaderboard Version Information](./get-v2-gamecenterleaderboardversions-_id_.md)
  Get information about a specific Game Center leaderboard version.
- [List All Localizations for a Game Center Leaderboard Version](./get-v2-gamecenterleaderboardversions-_id_-localizations.md)
  Get a list of localizations for a specific Game Center leaderboard version.
- [Get All Localization IDs for a Game Center Leaderboard Version](./get-v2-gamecenterleaderboardversions-_id_-relationships-localizations.md)
  Get a list of localization resource IDs for a specific Game Center leaderboard version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v2-gamecenterleaderboardversions)*