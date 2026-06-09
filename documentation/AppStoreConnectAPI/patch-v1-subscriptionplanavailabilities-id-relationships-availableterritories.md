# Replace the available territories for a subscription plan availability

**Framework**: App Store Connect API  
**Kind**: httpRequest

Replace the list of available territories for a specific subscription plan availability.

**Availability**:
- App Store Connect API 4.4+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/subscriptionPlanAvailabilities/{id}/relationships/availableTerritories`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `subscriptionPlanAvailability` resource ID from the [`List plan availabilities for a subscription`](get-v1-subscriptions-_id_-planavailabilities.md) response.

## See Also

- [List available territories for a subscription plan availability](get-v1-subscriptionplanavailabilities-_id_-availableterritories.md)
  List all territories where a specific subscription plan is available.
- [List available territory IDs for a subscription plan availability](get-v1-subscriptionplanavailabilities-_id_-relationships-availableterritories.md)
  Get a list of available territory resource IDs for a specific subscription plan availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-subscriptionplanavailabilities-_id_-relationships-availableterritories)*