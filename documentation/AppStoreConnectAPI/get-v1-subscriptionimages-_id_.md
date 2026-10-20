# Read subscription image information (v1)

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Read details about a specific subscription image.

**Availability**:
- App Store Connect API 3.6+ - Deprecated in 4.4.1

> **Deprecated**: This endpoint is deprecated. Use [`Read subscription image information`](./get-v2-subscriptionimages-_id_.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionImages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `subscriptionImages` resource ID from the [`List Subscription Images`](./get-v1-subscriptions-_id_-images.md) response.

### Query Parameters

- `fields[subscriptionImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `assetToken`, `imageAsset`, `uploadOperations`, `state`, `subscription`
- `fields[subscriptions]` ([string]): **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`
- `include` ([string]): **Allowed Values**: `subscription`

## Responses

- `200` OK (`SubscriptionImageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create an image for a subscription (v1)](./post-v1-subscriptionimages.md)
  Reserve an image asset to appear in the App Store, representing a subscription.
- [List Subscription Images](./get-v1-subscriptions-_id_-images.md)
  List all images for a specific subscription.
- [List subscription image ids](./get-v1-subscriptions-_id_-relationships-images.md)
  List all images IDs for a specific subscription.
- [Commit a subscription image (v1)](./patch-v1-subscriptionimages-_id_.md)
  Commit an uploaded subscription image.
- [Delete a subscription image (v1)](./delete-v1-subscriptionimages-_id_.md)
  Delete the image asset that appears on the App Store listing that represents a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionimages-_id_)*