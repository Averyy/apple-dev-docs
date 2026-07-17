# List all promotional offer resource ids for an auto-renewable subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of promotional offers for a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/promotionalOffers`

## Parameters

- `fields[subscriptionPromotionalOfferPrices]` ([string])
- `fields[subscriptionPromotionalOffers]` ([string])
- `fields[subscriptions]` ([string])
- `filter[territory]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[prices]` (integer)

## See Also

- [List promotional offer IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-promotionaloffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-promotionaloffers)*