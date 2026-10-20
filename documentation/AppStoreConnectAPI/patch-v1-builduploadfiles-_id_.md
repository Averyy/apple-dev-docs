# Commit a Build Upload File

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Commit a build upload file to a specific build upload.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/buildUploadFiles/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `BuildUploadFileUpdateRequest`

## Responses

- `200` OK (`BuildUploadFileResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)

## See Also

### Reading and uploading build files
- [Read Build Upload File Information](./get-v1-builduploadfiles-_id_.md)
  Get details about a specific build upload file for a build upload.
- [Read build upload file information for a build upload](./get-v1-builduploads-_id_-builduploadfiles.md)
  Get build upload file information for a specific build upload.
- [Read the build upload file id for a build upload](./get-v1-builduploads-_id_-relationships-builduploadfiles.md)
  Get the build upload file ID for a specific build upload.
- [Create a Reservation for a Build Upload File](./post-v1-builduploadfiles.md)
  Reserve a build upload file for a specific build upload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-builduploadfiles-_id_)*