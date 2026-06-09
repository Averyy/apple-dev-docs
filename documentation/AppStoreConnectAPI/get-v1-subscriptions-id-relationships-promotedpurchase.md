# Get the promoted purchase ID for an auto-renewable subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/relationships/promotedPurchase`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create an auto-renewable subscription](post-v1-subscriptions.md)
  Create an auto-renewable subscription for your app.
- [Read subscription information](get-v1-subscriptions-_id_.md)
  Get information about a specific auto-renewable subscription.
- [Modify an auto-renewable subscription](patch-v1-subscriptions-_id_.md)
  Update a specific auto-renewable subscription.
- [Delete a subscription](delete-v1-subscriptions-_id_.md)
  Delete a specific auto-renewable subscription that you configured for an app.
- [List all localizations for an auto-renewable subscription](get-v1-subscriptions-_id_-subscriptionlocalizations.md)
  Get a list of the subscription localizations for a specific auto-renewable subscription.
- [List localization IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-subscriptionlocalizations.md)
- [List all introductory offers for a subscription](get-v1-subscriptions-_id_-introductoryoffers.md)
  Get a list of introductory offers for a specific auto-renewable subscription.
- [List all introductory offer resource ids for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-introductoryoffers.md)
  Get a list of resource IDs representing introductory offers for an auto-renewable subscription.
- [Delete an introductory offer from a subscription](delete-v1-subscriptions-_id_-relationships-introductoryoffers.md)
  Delete a specific introductory offer for an auto-renewable subscription.
- [Read promoted purchase information for a subscription](get-v1-subscriptions-_id_-promotedpurchase.md)
  Get details about the promoted purchase of an auto-renewable subscription.
- [List all offer codes for a subscription](get-v1-subscriptions-_id_-offercodes.md)
  Get a list of subscription offer codes for a specific auto-renewable subscription.
- [List offer code IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-offercodes.md)
- [List all promotional offer resource ids for an auto-renewable subscription](get-v1-subscriptions-_id_-promotionaloffers.md)
  Get a list of promotional offers for a specific auto-renewable subscription.
- [List promotional offer IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-promotionaloffers.md)
- [List all price points for a subscription](get-v1-subscriptions-_id_-pricepoints.md)
  Get a list of price points for an auto-renewable subscription by territory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-relationships-promotedpurchase)*