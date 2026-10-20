# Read promoted purchase information for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get details about the promoted purchase of an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/promotedPurchase`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[inAppPurchases]` ([string]): **Allowed Values**: `name`, `productId`, `inAppPurchaseType`, `state`, `reviewNote`, `familySharable`, `contentHosting`, `inAppPurchaseLocalizations`, `pricePoints`, `content`, `appStoreReviewScreenshot`, `promotedPurchase`, `iapPriceSchedule`, `inAppPurchaseAvailability`, `images`, `offerCodes`, `versions`
- `fields[promotedPurchases]` ([string]): **Allowed Values**: `visibleForAllUsers`, `enabled`, `state`, `inAppPurchaseV2`, `subscription`
- `fields[subscriptions]` ([string]): **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`
- `include` ([string]): **Allowed Values**: `inAppPurchaseV2`, `subscription`

## Responses

- `200` OK (`PromotedPurchaseResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting the promoted purchase
- [Get the promoted purchase ID for an auto-renewable subscription](./get-v1-subscriptions-_id_-relationships-promotedpurchase.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-promotedpurchase)*