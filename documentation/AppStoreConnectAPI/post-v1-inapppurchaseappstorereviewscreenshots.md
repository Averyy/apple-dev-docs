# Create an In-App Purchase review screenshot

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Reserve a review screenshot for an In-App Purchase.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Managing In-App Purchases](./managing-in-app-purchases.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/inAppPurchaseAppStoreReviewScreenshots`

## Request Body

**Content-Type**: `application/json`  
**Type**: `InAppPurchaseAppStoreReviewScreenshotCreateRequest`

## Responses

- `201` Created (`InAppPurchaseAppStoreReviewScreenshotResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read In-App Purchase review screenshot information](./get-v1-inapppurchaseappstorereviewscreenshots-_id_.md)
  Get information about a specific review screenshot for an In-App Purchase.
- [Commit a review screenshot for an In-App Purchase](./patch-v1-inapppurchaseappstorereviewscreenshots-_id_.md)
  Commit an uploaded image asset as a review screenshot for an In-App Purchase.
- [Delete a review screenshot for an In-App Purchase](./delete-v1-inapppurchaseappstorereviewscreenshots-_id_.md)
  Delete an image that you uploaded for review of an In-App Purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-inapppurchaseappstorereviewscreenshots)*