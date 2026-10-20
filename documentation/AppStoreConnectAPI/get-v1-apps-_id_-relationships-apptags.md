# List app tags IDs

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all app tag IDs for a specific app.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/relationships/appTags`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `limit` (integer): The maximum number of app tag resource identifiers to return.

  **Maximum**: `200`

## Responses

- `200` OK (`AppAppTagsLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading app tag information
- [List App Tags](./get-v1-apps-_id_-apptags.md)
  List all app tags for a specific app.
- [List territory IDs for an app tag](./get-v1-apptags-_id_-relationships-territories.md)
  List territory IDs for an app tag.
- [List Territories for an App Tag](./get-v1-apptags-_id_-territories.md)
  List territory availability for a specific app tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-relationships-apptags)*