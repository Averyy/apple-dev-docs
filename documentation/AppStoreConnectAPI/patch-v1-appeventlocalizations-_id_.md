# Modify an app event localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the localized metadata for a specific in-app event.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appEventLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app event localization resource ID from the [`List all localizations for an in-app event`](./get-v1-appevents-_id_-localizations.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppEventLocalizationUpdateRequest`

## Responses

- `200` OK (`AppEventLocalizationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read app event localization information](./get-v1-appeventlocalizations-_id_.md)
  Get information about a specific app event localization.
- [List all video clips for an app event localization](./get-v1-appeventlocalizations-_id_-appeventvideoclips.md)
  Get a list of video clips for a specific app event localization.
- [List app event video clip IDs for an app event localization](./get-v1-appeventlocalizations-_id_-relationships-appeventvideoclips.md)
- [List all screenshots for an app event localization](./get-v1-appeventlocalizations-_id_-appeventscreenshots.md)
  Get a list of screenshots for a specific app event localization.
- [List app event screenshot IDs for an app event localization](./get-v1-appeventlocalizations-_id_-relationships-appeventscreenshots.md)
- [Create an app event localization](./post-v1-appeventlocalizations.md)
  Add a new localization for an in-app event.
- [Delete an app event localization](./delete-v1-appeventlocalizations-_id_.md)
  Delete localized metadata that you configured for an in-app event.
- [List related placements](./get-v1-appeventlocalizations-_id_-placements.md)
  List the placements for an in-app event localization.
- [List the placement IDs for an in-app event localization](./get-v1-appeventlocalizations-_id_-relationships-placements.md)
  Get a list of placement resource IDs for a specific in-app event localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appeventlocalizations-_id_)*