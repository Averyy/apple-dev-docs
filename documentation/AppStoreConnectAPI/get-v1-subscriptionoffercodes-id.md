# Read subscription offer code information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get details about a specific subscription offer that has offer codes for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionOfferCodes/{id}`

## Parameters

- `fields[subscriptionOfferCodeCustomCodes]` ([string])
- `fields[subscriptionOfferCodeOneTimeUseCodes]` ([string])
- `fields[subscriptionOfferCodePrices]` ([string])
- `fields[subscriptionOfferCodes]` ([string])
- `include` ([string])
- `limit[customCodes]` (integer)
- `limit[oneTimeUseCodes]` (integer)
- `limit[prices]` (integer)
- `fields[subscriptions]` ([string])

## See Also

- [Create a subscription offer](post-v1-subscriptionoffercodes.md)
  Create a subscription offer that provides offer codes for an auto-renewable subscription.
- [Deactivate a subscription offer with offer codes](patch-v1-subscriptionoffercodes-_id_.md)
  Deactivate a subscription offer that has offer codes for an auto-renewable subscription.
- [List all subscription offer code prices](get-v1-subscriptionoffercodes-_id_-prices.md)
  Get a list of price tiers for a subscription offer code.
- [List price IDs for a subscription offer code](get-v1-subscriptionoffercodes-_id_-relationships-prices.md)
  Get a list of price resource IDs for a specific subscription offer code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionoffercodes-_id_)*