# List available territories for a subscription plan availability

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all territories where a specific subscription plan is available.

**Availability**:
- App Store Connect API 4.4+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionPlanAvailabilities/{id}/availableTerritories`

## Parameters

- `fields[territories]` ([string]): Additional fields to include for each territory resource that the response returns.
- `limit` (integer): The maximum number of territory resources to return.

## See Also

- [List available territory IDs for a subscription plan availability](get-v1-subscriptionplanavailabilities-_id_-relationships-availableterritories.md)
  Get a list of available territory resource IDs for a specific subscription plan availability.
- [Replace the available territories for a subscription plan availability](patch-v1-subscriptionplanavailabilities-_id_-relationships-availableterritories.md)
  Replace the list of available territories for a specific subscription plan availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionplanavailabilities-_id_-availableterritories)*