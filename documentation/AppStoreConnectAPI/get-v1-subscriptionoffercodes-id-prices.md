# List all subscription offer code prices

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of price tiers for a subscription offer code.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionOfferCodes/{id}/prices`

## Parameters

- `fields[subscriptionOfferCodePrices]` ([string])
- `fields[subscriptionPricePoints]` ([string])
- `fields[territories]` ([string])
- `include` ([string])
- `limit` (integer)
- `filter[territory]` ([string])

## See Also

- [Create a subscription offer](post-v1-subscriptionoffercodes.md)
  Create a subscription offer that provides offer codes for an auto-renewable subscription.
- [Read subscription offer code information](get-v1-subscriptionoffercodes-_id_.md)
  Get details about a specific subscription offer that has offer codes for an auto-renewable subscription.
- [Deactivate a subscription offer with offer codes](patch-v1-subscriptionoffercodes-_id_.md)
  Deactivate a subscription offer that has offer codes for an auto-renewable subscription.
- [List price IDs for a subscription offer code](get-v1-subscriptionoffercodes-_id_-relationships-prices.md)
  Get a list of price resource IDs for a specific subscription offer code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionoffercodes-_id_-prices)*