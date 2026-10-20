# Modify an app info localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Modify localized app-level information for a particular language.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appInfoLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app info localization resource ID from the [`List all app info localizations for an app info`](./get-v1-appinfos-_id_-appinfolocalizations.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppInfoLocalizationUpdateRequest`

## Responses

- `200` OK (`AppInfoLocalizationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting Localized App Information
- [Create an app info localization](./post-v1-appinfolocalizations.md)
  Add app-level localized information for a new locale.
- [Delete an app info localization](./delete-v1-appinfolocalizations-_id_.md)
  Delete an app information localization that is associated with an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appinfolocalizations-_id_)*