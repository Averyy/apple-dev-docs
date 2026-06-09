# Deactivate a subscription offer with offer codes

**Framework**: App Store Connect API  
**Kind**: httpRequest

Deactivate a subscription offer that has offer codes for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/subscriptionOfferCodes/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create a subscription offer](post-v1-subscriptionoffercodes.md)
  Create a subscription offer that provides offer codes for an auto-renewable subscription.
- [Read subscription offer code information](get-v1-subscriptionoffercodes-_id_.md)
  Get details about a specific subscription offer that has offer codes for an auto-renewable subscription.
- [List all subscription offer code prices](get-v1-subscriptionoffercodes-_id_-prices.md)
  Get a list of price tiers for a subscription offer code.
- [List price IDs for a subscription offer code](get-v1-subscriptionoffercodes-_id_-relationships-prices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-subscriptionoffercodes-_id_)*