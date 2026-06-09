# Delete a promotional offer from a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a specific promotional offer from an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/subscriptionPromotionalOffers/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create a promotional offer](post-v1-subscriptionpromotionaloffers.md)
  Create a promotional offer for an auto-renewable subscription.
- [List all promotional offer prices for a subscription](get-v1-subscriptionpromotionaloffers-_id_-prices.md)
  Get a list of prices of a promotional offer for an auto-renewable subscription, for a specified territory.
- [List price IDs for a subscription promotional offer](get-v1-subscriptionpromotionaloffers-_id_-relationships-prices.md)
- [Read promotional offer information](get-v1-subscriptionpromotionaloffers-_id_.md)
  Get details about a specific promotional offer for an auto-renewable subscription.
- [Modify a promotional offer](patch-v1-subscriptionpromotionaloffers-_id_.md)
  Update the prices for a specific promotional offer for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-subscriptionpromotionaloffers-_id_)*