# Read promotional offer information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get details about a specific promotional offer for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionPromotionalOffers/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[subscriptionPromotionalOfferPrices]` ([string]): **Allowed Values**: `territory`, `subscriptionPricePoint`
- `fields[subscriptionPromotionalOffers]` ([string]): **Allowed Values**: `duration`, `name`, `numberOfPeriods`, `offerCode`, `offerMode`, `targetSubscriptionPlanType`, `subscription`, `prices`
- `include` ([string]): **Allowed Values**: `subscription`, `prices`
- `limit[prices]` (integer): **Maximum**: `50`
- `fields[subscriptions]` ([string]): **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`

## Responses

- `200` OK (`SubscriptionPromotionalOfferResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create a promotional offer](./post-v1-subscriptionpromotionaloffers.md)
  Create a promotional offer for an auto-renewable subscription.
- [List all promotional offer prices for a subscription](./get-v1-subscriptionpromotionaloffers-_id_-prices.md)
  Get a list of prices of a promotional offer for an auto-renewable subscription, for a specified territory.
- [List price IDs for a subscription promotional offer](./get-v1-subscriptionpromotionaloffers-_id_-relationships-prices.md)
- [Modify a promotional offer](./patch-v1-subscriptionpromotionaloffers-_id_.md)
  Update the prices for a specific promotional offer for an auto-renewable subscription.
- [Delete a promotional offer from a subscription](./delete-v1-subscriptionpromotionaloffers-_id_.md)
  Delete a specific promotional offer from an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionpromotionaloffers-_id_)*