# Read In-App Purchase image information (v1)

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Read details about a specific In-App Purchase image.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This endpoint is deprecated. Use [`Read In-App Purchase image information`](./get-v2-inapppurchaseimages-_id_.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseImages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `inAppPurchaseImages` resource ID from the [`List In-App Purchase images`](./get-v2-inapppurchases-_id_-images.md) response.

### Query Parameters

- `fields[inAppPurchaseImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `assetToken`, `imageAsset`, `uploadOperations`, `state`, `inAppPurchase`
- `fields[inAppPurchases]` ([string]): **Allowed Values**: `name`, `productId`, `inAppPurchaseType`, `state`, `reviewNote`, `familySharable`, `contentHosting`, `inAppPurchaseLocalizations`, `pricePoints`, `content`, `appStoreReviewScreenshot`, `promotedPurchase`, `iapPriceSchedule`, `inAppPurchaseAvailability`, `images`, `offerCodes`, `versions`
- `include` ([string]): **Allowed Values**: `inAppPurchase`

## Responses

- `200` OK (`InAppPurchaseImageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create an image for an In-App Purchase (v1)](./post-v1-inapppurchaseimages.md)
  Reserve an image asset to appear in the App Store, representing an In-App Purchase.
- [List In-App Purchase images](./get-v2-inapppurchases-_id_-images.md)
  List all images for a specific In-App Purchase.
- [Commit an image for an In-App Purchase (v1)](./patch-v1-inapppurchaseimages-_id_.md)
  Commit an uploaded image asset for an In-App Purchase.
- [Delete an In-App Purchase image (v1)](./delete-v1-inapppurchaseimages-_id_.md)
  Delete the image asset that appears on the App Store listing that represents an In-App Purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaseimages-_id_)*