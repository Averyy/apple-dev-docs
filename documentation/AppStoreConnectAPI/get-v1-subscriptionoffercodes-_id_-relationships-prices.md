# List price IDs for a subscription offer code

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of price resource IDs for a specific subscription offer code.

**Availability**:
- App Store Connect API 4.4+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionOfferCodes/{id}/relationships/prices`

## Parameters

- `limit` (integer)

## See Also

- [Create a subscription offer](post-v1-subscriptionoffercodes.md)
  Create a subscription offer that provides offer codes for an auto-renewable subscription.
- [Read subscription offer code information](get-v1-subscriptionoffercodes-_id_.md)
  Get details about a specific subscription offer that has offer codes for an auto-renewable subscription.
- [Deactivate a subscription offer with offer codes](patch-v1-subscriptionoffercodes-_id_.md)
  Deactivate a subscription offer that has offer codes for an auto-renewable subscription.
- [List all subscription offer code prices](get-v1-subscriptionoffercodes-_id_-prices.md)
  Get a list of price tiers for a subscription offer code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionoffercodes-_id_-relationships-prices)*