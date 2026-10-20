# Create a Reservation for an Asset Pack Upload

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Begin the process of uploading an asset pack for Apple-hosted background assets.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Uploading and versioning Apple hosted background assets](./managing-apple-hosted-background-assets.md)
- [Understanding webhook events](./webhook-events.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/backgroundAssetUploadFiles`

## Request Body

**Content-Type**: `application/json`  
**Type**: `BackgroundAssetUploadFileCreateRequest`

## Responses

- `201` Created (`BackgroundAssetUploadFileResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Uploading background asset files
- [Read Information for an Uploaded Asset Pack](./get-v1-backgroundassetuploadfiles-_id_.md)
  Get details about an uploaded asset pack for Apple hosted background asset.
- [Commit an Uploaded Asset Pack to a Background Asset Version](./patch-v1-backgroundassetuploadfiles-_id_.md)
  Associate an uploaded asset pack with a background asset version to finish the upload process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-backgroundassetuploadfiles)*