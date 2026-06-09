# List plan availabilities for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the subscription plan availabilities related to a subscription.

**Availability**:
- App Store Connect API 3.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/planAvailabilities`

## Parameters

- `fields[subscriptionPlanAvailabilities]` ([string]): Additional fields to include for each subscriptionPlanAvailabilities resource that the response returns.
- `fields[territories]` ([string]): Additional fields to include for each territories resource that the response returns.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of subscriptionPlanAvailabilities resources to return.
- `limit[availableTerritories]` (integer): The maximum number of related availableTerritories resources to return.

## See Also

- [List plan availability IDs for a subscription](get-v1-subscriptions-_id_-relationships-planavailabilities.md)
  List the resource IDs of related subscription plan availabilities for a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-planavailabilities)*