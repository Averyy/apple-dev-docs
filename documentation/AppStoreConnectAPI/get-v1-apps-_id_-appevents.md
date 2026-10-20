# List all in-app events for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of in-app events for a specific app.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appEvents`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[appEventLocalizations]` ([string]): Additional fields to include for each app event localization resource returned by the response.

  **Allowed Values**: `locale`, `name`, `shortDescription`, `longDescription`, `appEvent`, `appEventScreenshots`, `appEventVideoClips`, `placements`
- `fields[appEvents]` ([string]): Additional fields to include for each app event resource returned by the response.

  **Allowed Values**: `referenceName`, `badge`, `eventState`, `deepLink`, `purchaseRequirement`, `primaryLocale`, `priority`, `purpose`, `territorySchedules`, `archivedTerritorySchedules`, `localizations`
- `filter[eventState]` ([string]): Filter the returned app events by event state.

  **Allowed Values**: `DRAFT`, `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `REJECTED`, `ACCEPTED`, `APPROVED`, `PUBLISHED`, `PAST`, `ARCHIVED`
- `filter[id]` ([string]): Filter the returned app events by ID.
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `localizations`
- `limit` (integer): The maximum number of app event resources to return.

  **Maximum**: `200`
- `limit[localizations]` (integer): The maximum number of related localizations resources to return.

  **Maximum**: `50`

## Responses

- `200` OK (`AppEventsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting app event information
- [List app event IDs for an app](./get-v1-apps-_id_-relationships-appevents.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-appevents)*