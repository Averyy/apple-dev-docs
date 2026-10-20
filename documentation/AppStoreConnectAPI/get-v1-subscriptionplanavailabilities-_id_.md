# Read subscription plan availability information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific subscription plan availability.

**Availability**:
- App Store Connect API 4.4+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionPlanAvailabilities/{id}`

## Parameters

- `fields[subscriptionPlanAvailabilities]` ([string]): Additional fields to include for each subscription plan availability resource that the response returns.
- `fields[territories]` ([string]): Additional fields to include for each territory resource that the response returns.
- `include` ([string]): The relationship data to include in the response.
- `limit[availableTerritories]` (integer): The maximum number of available territory resources to return.

## See Also

- [Create a subscription plan availability](post-v1-subscriptionplanavailabilities.md)
  Create the plan availability configuration for an auto-renewable subscription.
- [Modify a subscription plan availability](patch-v1-subscriptionplanavailabilities-_id_.md)
  Update the plan availability configuration for a specific subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionplanavailabilities-_id_)*