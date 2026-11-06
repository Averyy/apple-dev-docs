# List versions for a retention message

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of versions for a specific retention message.

**Availability**:
- App Store Connect API 4.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/retentionMessages/{id}/versions`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the retention message resource ID from the [`List retention messages for an app`](./get-v1-apps-_id_-retentionmessages.md) response.

### Query Parameters

- `fields[retentionMessageVersions]` ([string]): Additional fields to include for each retention message version resource returned by the response.

  **Allowed Values**: `state`, `retentionMessage`, `localizations`, `placement`
- `fields[retentionMessages]` ([string]): Additional fields to include for each retention message resource returned by the response.

  **Allowed Values**: `referenceName`, `versions`, `subscriptions`
- `fields[retentionMessageLocalizations]` ([string]): Additional fields to include for each retention message localization resource returned by the response.

  **Allowed Values**: `locale`, `header`, `body`, `retentionMessageVersion`
- `fields[appAssetLibraryPlacements]` ([string]): Additional fields to include for each app asset library placement resource returned by the response.

  **Allowed Values**: `mediaType`, `placementType`, `placementGroup`, `createdDate`, `lastModifiedDate`, `state`, `stateDetails`, `image`, `video`, `appEventLocalization`, `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `retentionMessageVersion`
- `limit` (integer): The maximum number of version resources to return.

  **Maximum**: `200`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `retentionMessage`, `localizations`, `placement`
- `limit[localizations]` (integer): The maximum number of related localization resources to return.

  **Maximum**: `50`

## Responses

- `200` OK (`RetentionMessageVersionsResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Getting retention messages
- [Read a retention message](./get-v1-retentionmessages-_id_.md)
  Read details about a specific retention message.
- [List version IDs for a retention message](./get-v1-retentionmessages-_id_-relationships-versions.md)
  Get a list of version IDs for a specific retention message.
- [List subscriptions for a retention message](./get-v1-retentionmessages-_id_-subscriptions.md)
  Get a list of the auto-renewable subscriptions that use a specific retention message.
- [List subscription IDs for a retention message](./get-v1-retentionmessages-_id_-relationships-subscriptions.md)
  Get a list of the subscription IDs that use a specific retention message.
- [List retention messages for an app](./get-v1-apps-_id_-retentionmessages.md)
  Get a list of retention messages for a specific app.
- [List retention message IDs for an app](./get-v1-apps-_id_-relationships-retentionmessages.md)
  Get a list of retention message IDs for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-retentionmessages-_id_-versions)*