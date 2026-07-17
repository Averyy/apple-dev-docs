# List plan availability IDs for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of plan availability resource IDs for a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 4.4+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/relationships/planAvailabilities`

## Parameters

- `limit` (integer): The maximum number of subscription plan availability resource identifiers to return.

## See Also

- [List plan availabilities for a subscription](get-v1-subscriptions-_id_-planavailabilities.md)
  List all plan availabilities for a specific auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-relationships-planavailabilities)*