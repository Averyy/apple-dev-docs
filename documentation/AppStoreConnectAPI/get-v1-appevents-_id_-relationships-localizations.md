# List localization IDs for an app event

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appEvents/{id}/relationships/localizations`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`AppEventLocalizationsLinkagesResponse`, `application/json`)
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
- [List all in-app events for an app](./get-v1-apps-_id_-appevents.md)
  Get a list of in-app events for a specific app.
- [Modify an in-app event](./patch-v1-appevents-_id_.md)
  Update the metadata for a specific in-app event.
- [Create an in-app event](./post-v1-appevents.md)
  Create a new in-app event for your app.
- [Delete an app event](./delete-v1-appevents-_id_.md)
  Delete an in-app event and its related metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appevents-_id_-relationships-localizations)*