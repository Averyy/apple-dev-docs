# Create an In-App Purchase image

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Reserve a promotion image for an In-App Purchase configured with the v2 API and prepare its asset upload.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [App Store Connect API 4.4.1 release notes](./app-store-connect-api-4-4-1-release-notes.md)
- [Working with In-App Purchase versions](./working-with-in-app-purchase-versions.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v2/inAppPurchaseImages`

## Request Body

**Content-Type**: `application/json`  
**Type**: `InAppPurchaseImageV2CreateRequest`

## Responses

- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `201` Created (`InAppPurchaseImageV2Response`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read In-App Purchase image information](./get-v2-inapppurchaseimages-_id_.md)
  Get the metadata for an In-App Purchase image configured with the v2 API, including the asset upload state.
- [Modify an In-App Purchase image](./patch-v2-inapppurchaseimages-_id_.md)
  Commit the asset upload for an In-App Purchase image configured with the v2 API.
- [Delete an In-App Purchase image](./delete-v2-inapppurchaseimages-_id_.md)
  Delete an In-App Purchase image configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v2-inapppurchaseimages)*