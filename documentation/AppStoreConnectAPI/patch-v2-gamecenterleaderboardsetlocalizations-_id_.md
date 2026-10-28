# Modify a Game Center Leaderboard Set Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update a specific Game Center leaderboard set localization.

**Availability**:
- App Store Connect API 3.6+

## Overview

- id:
- 200:
- 400:
- 401:
- 403:
- 404:
- 409:
- 422:
- 429:

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboardSetLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterLeaderboardSetLocalizationV2UpdateRequest`

## Responses

- `200` OK (`GameCenterLeaderboardSetLocalizationV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing leaderboard set localizations
- [Read Game Center Leaderboard Set Localization Information](./get-v2-gamecenterleaderboardsetlocalizations-_id_.md)
  Get information about a specific Game Center leaderboard set localization.
- [List All Images for a Game Center Leaderboard Set Localization](./get-v2-gamecenterleaderboardsetlocalizations-_id_-image.md)
  Get a list of images for a specific Game Center leaderboard set localization.
- [Get All Image IDs for a Game Center Leaderboard Set Localization](./get-v2-gamecenterleaderboardsetlocalizations-_id_-relationships-image.md)
  Get a list of image resource IDs for a specific Game Center leaderboard set localization.
- [Create a Game Center Leaderboard Set Localization](./post-v2-gamecenterleaderboardsetlocalizations.md)
  Create a Game Center leaderboard set localization.
- [Delete a Game Center Leaderboard Set Localization](./delete-v2-gamecenterleaderboardsetlocalizations-_id_.md)
  Delete a specific Game Center leaderboard set localization.
- [Read Leaderboard Set Localization Information](./get-v1-gamecenterleaderboardsetlocalizations-_id_.md)
  Get information about a leaderboard set localization.
- [Read the Image Associated With a Leaderboard Set Localization](./get-v1-gamecenterleaderboardsetlocalizations-_id_-gamecenterleaderboardsetimage.md)
  Get information about a leaderboard set image associated with a leaderboard set localization.
- [Get the leaderboard set image ID for a Game Center leaderboard set localization](./get-v1-gamecenterleaderboardsetlocalizations-_id_-relationships-gamecenterleaderboardsetimage.md)
- [Create a Leaderboard Set Localization](./post-v1-gamecenterleaderboardsetlocalizations.md)
  Add a new leaderboard set localization.
- [Modify a Leaderboard Set Localization](./patch-v1-gamecenterleaderboardsetlocalizations-_id_.md)
  Edit a leaderboard set localization.
- [Delete a Leaderboard Set Localization](./delete-v1-gamecenterleaderboardsetlocalizations-_id_.md)
  Delete a localization that’s associated with a leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v2-gamecenterleaderboardsetlocalizations-_id_)*