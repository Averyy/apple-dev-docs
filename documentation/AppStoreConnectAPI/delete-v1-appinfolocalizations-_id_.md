# Delete an app info localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete an app information localization that is associated with an app.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appInfoLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app info localization resource ID from the [`List all app info localizations for an app info`](./get-v1-appinfos-_id_-appinfolocalizations.md) response.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting Localized App Information
- [Create an app info localization](./post-v1-appinfolocalizations.md)
  Add app-level localized information for a new locale.
- [Modify an app info localization](./patch-v1-appinfolocalizations-_id_.md)
  Modify localized app-level information for a particular language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appinfolocalizations-_id_)*