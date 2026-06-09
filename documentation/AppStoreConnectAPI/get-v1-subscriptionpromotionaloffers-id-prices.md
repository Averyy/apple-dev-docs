# List all promotional offer prices for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of prices of a promotional offer for an auto-renewable subscription, for a specified territory.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionPromotionalOffers/{id}/prices`

## Parameters

- `fields[subscriptionPricePoints]` ([string])
- `fields[subscriptionPromotionalOfferPrices]` ([string])
- `fields[territories]` ([string])
- `include` ([string])
- `limit` (integer)
- `filter[territory]` ([string])

## See Also

- [Create a promotional offer](post-v1-subscriptionpromotionaloffers.md)
  Create a promotional offer for an auto-renewable subscription.
- [List price IDs for a subscription promotional offer](get-v1-subscriptionpromotionaloffers-_id_-relationships-prices.md)
- [Read promotional offer information](get-v1-subscriptionpromotionaloffers-_id_.md)
  Get details about a specific promotional offer for an auto-renewable subscription.
- [Modify a promotional offer](patch-v1-subscriptionpromotionaloffers-_id_.md)
  Update the prices for a specific promotional offer for an auto-renewable subscription.
- [Delete a promotional offer from a subscription](delete-v1-subscriptionpromotionaloffers-_id_.md)
  Delete a specific promotional offer from an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionpromotionaloffers-_id_-prices)*