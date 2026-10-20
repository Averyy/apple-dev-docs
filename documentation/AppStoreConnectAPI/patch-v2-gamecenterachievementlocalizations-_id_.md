# Modify a Game Center Achievement Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update a specific Game Center achievement localization.

**Availability**:
- App Store Connect API 3.6+

#### Overview

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

`PATCH https://api.appstoreconnect.apple.com/v2/gameCenterAchievementLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterAchievementLocalizationV2UpdateRequest`

## Responses

- `200` OK (`GameCenterAchievementLocalizationV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, modifying, and deleting achievements localizations
- [Create a Game Center Achievement Localization](./post-v2-gamecenterachievementlocalizations.md)
  Create a Game Center achievement localization.
- [Delete a Game Center Achievement Localization](./delete-v2-gamecenterachievementlocalizations-_id_.md)
  Delete a specific Game Center achievement localization.
- [Create an Achievement Localization](./post-v1-gamecenterachievementlocalizations.md)
  Add Game Center achievement localized information for a new locale.
- [Edit an Achievement Localization](./patch-v1-gamecenterachievementlocalizations-_id_.md)
  Modify localized Game Center achievement information for a particular language.
- [Delete an Achievement Localization](./delete-v1-gamecenterachievementlocalizations-_id_.md)
  Delete localization metadata that’s associated with an achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v2-gamecenterachievementlocalizations-_id_)*