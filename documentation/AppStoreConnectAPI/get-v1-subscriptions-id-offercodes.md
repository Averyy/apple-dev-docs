# List all offer codes for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of subscription offer codes for a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/offerCodes`

## Parameters

- `fields[subscriptionOfferCodeCustomCodes]` ([string])
- `fields[subscriptionOfferCodeOneTimeUseCodes]` ([string])
- `fields[subscriptionOfferCodePrices]` ([string])
- `fields[subscriptionOfferCodes]` ([string])
- `fields[subscriptions]` ([string])
- `filter[territory]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[customCodes]` (integer)
- `limit[oneTimeUseCodes]` (integer)
- `limit[prices]` (integer)

## See Also

- [List offer code IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-offercodes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-offercodes)*