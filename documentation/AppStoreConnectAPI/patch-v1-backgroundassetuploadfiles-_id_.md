# Commit an Uploaded Asset Pack to a Background Asset Version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Associate an uploaded asset pack with a background asset version to finish the upload process.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Understanding webhook events](./webhook-events.md)
- [App Store Connect API 4.1 release notes](./app-store-connect-api-4-1-release-notes.md)
- [Uploading and versioning Apple hosted background assets](./managing-apple-hosted-background-assets.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/backgroundAssetUploadFiles/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `backgroundAssetUploadFiles` resource ID from the [`Read Background Asset Upload File Information for a Background Asset Version`](./get-v1-backgroundassetversions-_id_-backgroundassetuploadfiles.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `BackgroundAssetUploadFileUpdateRequest`

## Responses

- `200` OK (`BackgroundAssetUploadFileResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Uploading background asset files
- [Read Information for an Uploaded Asset Pack](./get-v1-backgroundassetuploadfiles-_id_.md)
  Get details about an uploaded asset pack for Apple hosted background asset.
- [Create a Reservation for an Asset Pack Upload](./post-v1-backgroundassetuploadfiles.md)
  Begin the process of uploading an asset pack for Apple-hosted background assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-backgroundassetuploadfiles-_id_)*