# List all introductory offers for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of introductory offers for a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/introductoryOffers`

## Parameters

- `fields[subscriptionIntroductoryOffers]` ([string])
- `fields[subscriptionPricePoints]` ([string])
- `fields[subscriptions]` ([string])
- `fields[territories]` ([string])
- `include` ([string])
- `limit` (integer)
- `filter[territory]` ([string])

## See Also

- [List all introductory offer resource ids for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-introductoryoffers.md)
  Get a list of resource IDs representing introductory offers for an auto-renewable subscription.
- [Delete an introductory offer from a subscription](delete-v1-subscriptions-_id_-relationships-introductoryoffers.md)
  Delete a specific introductory offer for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-introductoryoffers)*