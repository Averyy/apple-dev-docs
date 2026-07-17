# Delete prices from a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a scheduled subscription price change for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/relationships/prices`

## Parameters

- `id` (string) *(required)*

## See Also

- [List all price points for a subscription](get-v1-subscriptions-_id_-pricepoints.md)
  Get a list of price points for an auto-renewable subscription by territory.
- [List price point IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-pricepoints.md)
- [List all prices for a subscription](get-v1-subscriptions-_id_-prices.md)
  Get a list of prices for an auto-renewable subscription, by territory.
- [List all subscription price ids for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-prices.md)
  Get a list of resource IDs representing subscription prices for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-subscriptions-_id_-relationships-prices)*