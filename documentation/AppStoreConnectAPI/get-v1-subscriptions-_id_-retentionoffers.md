# List retention offers for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of all retention offers for a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 4.6+

## Mentions

- [Setting up retention messaging for auto-renewable subscriptions](./setting-up-retention-messaging.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/retentionOffers`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the subscription resource ID from the [`List all subscriptions for a subscription group`](./get-v1-subscriptiongroups-_id_-subscriptions.md) response.

### Query Parameters

- `fields[retentionOffers]` ([string]): Additional fields to include for each retention offer resource returned by the response.

  **Allowed Values**: `referenceName`, `offerId`, `duration`, `offerMode`, `periodCount`, `customerEligibilityPaidSubscriptionDurationInMonths`, `customerEligibilityWaitBetweenOffersInMonths`, `targetSubscriptionPlanType`, `subscription`, `prices`
- `fields[subscriptions]` ([string]): Additional fields to include for each subscription resource returned by the response.

  **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`, `retentionOffers`, `retentionMessage`, `retentionMessageOffers`
- `fields[retentionOfferPrices]` ([string]): Additional fields to include for each retention offer price resource returned by the response.

  **Allowed Values**: `territory`, `subscriptionPricePoint`
- `limit` (integer): The maximum number of retention offer resources to return.

  **Maximum**: `200`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `subscription`, `prices`
- `limit[prices]` (integer): The maximum number of related price resources to return.

  **Maximum**: `50`

## Responses

- `200` OK (`RetentionOffersResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Getting retention offers
- [Read a retention offer](./get-v1-retentionoffers-_id_.md)
  Read details about a specific retention offer.
- [List prices for a retention offer](./get-v1-retentionoffers-_id_-prices.md)
  Get a list of territory-specific prices for a specific retention offer.
- [List price IDs for a retention offer](./get-v1-retentionoffers-_id_-relationships-prices.md)
  Get a list of price IDs for a specific retention offer.
- [List retention offer IDs for a subscription](./get-v1-subscriptions-_id_-relationships-retentionoffers.md)
  Get a list of retention offer IDs for a specific auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-retentionoffers)*