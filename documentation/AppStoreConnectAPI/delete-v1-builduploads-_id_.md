# Remove a Build Upload

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Remove a specific build upload for an app.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/buildUploads/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing build uploads
- [List All Build Uploads for an App](./get-v1-apps-_id_-builduploads.md)
  Get a list of all build uploads for a specific app.
- [List all build uploads ids for an app](./get-v1-apps-_id_-relationships-builduploads.md)
  Get a list of all build upload Ids for a specific app.
- [Read Build Upload Information](./get-v1-builduploads-_id_.md)
  Get details about a specific build upload file for an app.
- [Create a Build Upload](./post-v1-builduploads.md)
  Add a new build upload to an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-builduploads-_id_)*