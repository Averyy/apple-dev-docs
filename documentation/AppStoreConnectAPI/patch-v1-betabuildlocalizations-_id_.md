# Modify a beta build localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the localized What’s New text for a specific beta build and locale.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/betaBuildLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `BetaBuildLocalizationUpdateRequest`

## Responses

- `200` OK (`BetaBuildLocalizationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting Beta Build Localizations
- [Create a beta build localization](./post-v1-betabuildlocalizations.md)
  Create localized What’s New text for a build.
- [Delete a beta build localization](./delete-v1-betabuildlocalizations-_id_.md)
  Delete a specific beta build localization associated with a build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-betabuildlocalizations-_id_)*