# List all promotional offer resource ids for an auto-renewable subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of promotional offers for a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/promotionalOffers`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[subscriptionPromotionalOfferPrices]` ([string]): **Allowed Values**: `territory`, `subscriptionPricePoint`
- `fields[subscriptionPromotionalOffers]` ([string]): **Allowed Values**: `duration`, `name`, `numberOfPeriods`, `offerCode`, `offerMode`, `targetSubscriptionPlanType`, `subscription`, `prices`
- `fields[subscriptions]` ([string]): **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`
- `filter[territory]` ([string])
- `include` ([string]): **Allowed Values**: `subscription`, `prices`
- `limit` (integer): **Maximum**: `200`
- `limit[prices]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`SubscriptionPromotionalOffersResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting promotional offers
- [List promotional offer IDs for an auto-renewable subscription](./get-v1-subscriptions-_id_-relationships-promotionaloffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-promotionaloffers)*