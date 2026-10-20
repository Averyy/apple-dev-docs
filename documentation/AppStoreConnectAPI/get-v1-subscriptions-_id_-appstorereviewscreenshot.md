# Read review screenshot information for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about review screenshot for a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/appStoreReviewScreenshot`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[subscriptionAppStoreReviewScreenshots]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `imageAsset`, `assetToken`, `assetType`, `uploadOperations`, `assetDeliveryState`, `subscription`
- `fields[subscriptions]` ([string]): **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`
- `include` ([string]): **Allowed Values**: `subscription`

## Responses

- `200` OK (`SubscriptionAppStoreReviewScreenshotResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting the App Store review screenshot
- [Get the App Store review screenshot ID for an auto-renewable subscription](./get-v1-subscriptions-_id_-relationships-appstorereviewscreenshot.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-appstorereviewscreenshot)*