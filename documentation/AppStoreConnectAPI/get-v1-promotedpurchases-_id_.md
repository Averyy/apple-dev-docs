# Read promoted purchase information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get details about a specific promoted In-App Purchase.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/promotedPurchases/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[promotedPurchases]` ([string]): **Allowed Values**: `visibleForAllUsers`, `enabled`, `state`, `inAppPurchaseV2`, `subscription`
- `include` ([string]): **Allowed Values**: `inAppPurchaseV2`, `subscription`
- `fields[inAppPurchases]` ([string]): **Allowed Values**: `name`, `productId`, `inAppPurchaseType`, `state`, `reviewNote`, `familySharable`, `contentHosting`, `inAppPurchaseLocalizations`, `pricePoints`, `content`, `appStoreReviewScreenshot`, `promotedPurchase`, `iapPriceSchedule`, `inAppPurchaseAvailability`, `images`, `offerCodes`, `versions`
- `fields[subscriptions]` ([string]): **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`

## Responses

- `200` OK (`PromotedPurchaseResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Promote a purchase](./post-v1-promotedpurchases.md)
  Add an existing In-App Purchase or auto-renewable subscription to the promoted In-App Purchases on an app listing in the App Store.
- [List all promoted purchases for an app](./get-v1-apps-_id_-promotedpurchases.md)
  Get a list of promoted In-App Purchases, including promoted auto-renewable subscriptions, for an app.
- [List promoted purchase ids for an app](./get-v1-apps-_id_-relationships-promotedpurchases.md)
  Get a list of resource IDs representing promoted purchases for an auto-renewable subscription.
- [Modify a promoted In-App Purchase](./patch-v1-promotedpurchases-_id_.md)
  Update the visibility of a promoted In-App Purchase.
- [Modify the order of a promoted purchase for an app](./patch-v1-apps-_id_-relationships-promotedpurchases.md)
  Update the order of promoted purchases.
- [Remove a promoted purchase](./delete-v1-promotedpurchases-_id_.md)
  Remove a promotion for an In-App Purchase or auto-renewable subscription from the App Store listing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-promotedpurchases-_id_)*