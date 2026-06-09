# List available territory IDs for a subscription plan availability

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of available territory resource IDs for a specific subscription plan availability.

**Availability**:
- App Store Connect API 4.4+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionPlanAvailabilities/{id}/relationships/availableTerritories`

## Parameters

- `limit` (integer): The maximum number of territory resource identifiers to return.

## See Also

- [List available territories for a subscription plan availability](get-v1-subscriptionplanavailabilities-_id_-availableterritories.md)
  List all territories where a specific subscription plan is available.
- [Replace the available territories for a subscription plan availability](patch-v1-subscriptionplanavailabilities-_id_-relationships-availableterritories.md)
  Replace the list of available territories for a specific subscription plan availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionplanavailabilities-_id_-relationships-availableterritories)*