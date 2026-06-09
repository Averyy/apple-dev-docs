# Modify a subscription plan availability

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update the plan availability configuration for a specific subscription.

**Availability**:
- App Store Connect API 4.4+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/subscriptionPlanAvailabilities/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `subscriptionPlanAvailability` resource ID from the [`List plan availabilities for a subscription`](get-v1-subscriptions-_id_-planavailabilities.md) response.

## See Also

- [Create a subscription plan availability](post-v1-subscriptionplanavailabilities.md)
  Create the plan availability configuration for an auto-renewable subscription.
- [Read subscription plan availability information](get-v1-subscriptionplanavailabilities-_id_.md)
  Get information about a specific subscription plan availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-subscriptionplanavailabilities-_id_)*