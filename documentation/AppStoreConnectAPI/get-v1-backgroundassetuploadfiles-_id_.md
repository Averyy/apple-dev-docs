# Read Information for an Uploaded Asset Pack

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get details about an uploaded asset pack for Apple hosted background asset.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/backgroundAssetUploadFiles/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `backgroundAssetVersions` resource ID from the [`Read Background Asset Upload File Information for a Background Asset Version`](./get-v1-backgroundassetversions-_id_-backgroundassetuploadfiles.md) response.

### Query Parameters

- `fields[backgroundAssetUploadFiles]` ([string]): **Allowed Values**: `assetDeliveryState`, `assetToken`, `assetType`, `fileName`, `fileSize`, `sourceFileChecksum`, `sourceFileChecksums`, `uploadOperations`

## Responses

- `200` OK (`BackgroundAssetUploadFileResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Uploading background asset files
- [Create a Reservation for an Asset Pack Upload](./post-v1-backgroundassetuploadfiles.md)
  Begin the process of uploading an asset pack for Apple-hosted background assets.
- [Commit an Uploaded Asset Pack to a Background Asset Version](./patch-v1-backgroundassetuploadfiles-_id_.md)
  Associate an uploaded asset pack with a background asset version to finish the upload process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-backgroundassetuploadfiles-_id_)*