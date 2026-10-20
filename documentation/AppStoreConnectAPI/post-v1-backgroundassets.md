# Create Asset Pack Record

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create an asset pack record for your Apple-hosted background assets.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Uploading and versioning Apple hosted background assets](./managing-apple-hosted-background-assets.md)
- [Understanding webhook events](./webhook-events.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/backgroundAssets`

## Request Body

**Content-Type**: `application/json`  
**Type**: `BackgroundAssetCreateRequest`

## Responses

- `201` Created (`BackgroundAssetResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Relating background assets to your app
- [Create Asset Pack Version Record](./post-v1-backgroundassetversions.md)
  Create an asset pack version record for your Apple-hosted background assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-backgroundassets)*