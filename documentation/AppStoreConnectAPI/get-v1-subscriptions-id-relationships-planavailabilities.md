# List plan availability IDs for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the resource IDs of related subscription plan availabilities for a subscription.

**Availability**:
- App Store Connect API 3.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/relationships/planAvailabilities`

## Parameters

- `limit` (integer): The maximum number of subscriptionPlanAvailabilities resource identifiers to return.

## See Also

- [List plan availabilities for a subscription](get-v1-subscriptions-_id_-planavailabilities.md)
  List the subscription plan availabilities related to a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-relationships-planavailabilities)*