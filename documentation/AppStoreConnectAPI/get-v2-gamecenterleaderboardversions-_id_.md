# Read Game Center Leaderboard Version Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific Game Center leaderboard version.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- fields[gameCenterLeaderboardLocalizations]:
- fields[gameCenterLeaderboardVersions]:
- include:
- limit[localizations]:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboardVersions/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterLeaderboardLocalizations]` ([string]): **Allowed Values**: `locale`, `name`, `formatterOverride`, `formatterSuffix`, `formatterSuffixSingular`, `description`, `version`, `image`
- `fields[gameCenterLeaderboardVersions]` ([string]): **Allowed Values**: `version`, `state`, `leaderboard`, `localizations`
- `fields[gameCenterLeaderboards]` ([string]): **Allowed Values**: `defaultFormatter`, `referenceName`, `vendorIdentifier`, `submissionType`, `scoreSortType`, `scoreRangeStart`, `scoreRangeEnd`, `recurrenceStartDate`, `recurrenceDuration`, `recurrenceRule`, `archived`, `activityProperties`, `visibility`, `gameCenterDetail`, `gameCenterGroup`, `gameCenterLeaderboardSets`, `gameCenterScoreModerations`, `activity`, `challenge`, `versions`
- `include` ([string]): **Allowed Values**: `leaderboard`, `localizations`
- `limit[localizations]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`GameCenterLeaderboardVersionV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and creating leaderboard versions
- [List All Localizations for a Game Center Leaderboard Version](./get-v2-gamecenterleaderboardversions-_id_-localizations.md)
  Get a list of localizations for a specific Game Center leaderboard version.
- [Get All Localization IDs for a Game Center Leaderboard Version](./get-v2-gamecenterleaderboardversions-_id_-relationships-localizations.md)
  Get a list of localization resource IDs for a specific Game Center leaderboard version.
- [Create a Game Center Leaderboard Version](./post-v2-gamecenterleaderboardversions.md)
  Create a Game Center leaderboard version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterleaderboardversions-_id_)*