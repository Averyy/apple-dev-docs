# Read In-App Event Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific in-app event.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appEvents/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app event resource ID from the [`List all in-app events for an app`](./get-v1-apps-_id_-appevents.md) response.

### Query Parameters

- `fields[appEventLocalizations]` ([string]): Additional fields to include for each app event localization resource returned by the response.

  **Allowed Values**: `locale`, `name`, `shortDescription`, `longDescription`, `appEvent`, `appEventScreenshots`, `appEventVideoClips`, `placements`
- `fields[appEvents]` ([string]): Additional fields to include for each app event resource returned by the response.

  **Allowed Values**: `referenceName`, `badge`, `eventState`, `deepLink`, `purchaseRequirement`, `primaryLocale`, `priority`, `purpose`, `territorySchedules`, `archivedTerritorySchedules`, `localizations`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `localizations`
- `limit[localizations]` (integer): The maximum number of related localizations resources to return.

  **Maximum**: `50`

## Responses

- `200` OK (`AppEventResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [List all localizations for an in-app event](./get-v1-appevents-_id_-localizations.md)
  Get a list of all localizations for a specific in-app event.
- [List localization IDs for an app event](./get-v1-appevents-_id_-relationships-localizations.md)
- [List all in-app events for an app](./get-v1-apps-_id_-appevents.md)
  Get a list of in-app events for a specific app.
- [Modify an in-app event](./patch-v1-appevents-_id_.md)
  Update the metadata for a specific in-app event.
- [Create an in-app event](./post-v1-appevents.md)
  Create a new in-app event for your app.
- [Delete an app event](./delete-v1-appevents-_id_.md)
  Delete an in-app event and its related metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appevents-_id_)*