# Read promoted purchase information for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get details about the promoted purchase of an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/promotedPurchase`

## Parameters

- `fields[inAppPurchases]` ([string])
- `fields[promotedPurchases]` ([string])
- `fields[subscriptions]` ([string])
- `include` ([string])

## See Also

- [Get the promoted purchase ID for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-promotedpurchase.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-promotedpurchase)*