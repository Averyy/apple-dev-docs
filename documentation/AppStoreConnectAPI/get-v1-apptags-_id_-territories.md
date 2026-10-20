# List Territories for an App Tag

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List territory availability for a specific app tag.

**Availability**:
- App Store Connect API 4.1+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated.

## Mentions

- [App Store Connect API 4.5 release notes](./app-store-connect-api-4-5-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appTags/{id}/territories`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app tag resource ID from the [`List App Tags`](./get-v1-apps-_id_-apptags.md) response.

### Query Parameters

- `fields[territories]` ([string]): Additional fields to include for each territory resource returned by the response.

  **Allowed Values**: `currency`
- `limit` (integer): The maximum number of territory resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`TerritoriesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading app tag information
- [List App Tags](./get-v1-apps-_id_-apptags.md)
  List all app tags for a specific app.
- [List app tags IDs](./get-v1-apps-_id_-relationships-apptags.md)
  List all app tag IDs for a specific app.
- [List territory IDs for an app tag](./get-v1-apptags-_id_-relationships-territories.md)
  List territory IDs for an app tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apptags-_id_-territories)*