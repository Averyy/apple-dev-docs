# Delete an app event

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete an in-app event and its related metadata.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appEvents/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app event resource ID from the [`List all in-app events for an app`](./get-v1-apps-_id_-appevents.md) response.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read In-App Event Information](./get-v1-appevents-_id_.md)
  Get information about a specific in-app event.
- [List all localizations for an in-app event](./get-v1-appevents-_id_-localizations.md)
  Get a list of all localizations for a specific in-app event.
- [List localization IDs for an app event](./get-v1-appevents-_id_-relationships-localizations.md)
- [List all in-app events for an app](./get-v1-apps-_id_-appevents.md)
  Get a list of in-app events for a specific app.
- [Modify an in-app event](./patch-v1-appevents-_id_.md)
  Update the metadata for a specific in-app event.
- [Create an in-app event](./post-v1-appevents.md)
  Create a new in-app event for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appevents-_id_)*