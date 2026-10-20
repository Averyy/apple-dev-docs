# Read subscription plan availability information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific subscription plan availability.

**Availability**:
- App Store Connect API 4.4+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionPlanAvailabilities/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `subscriptionPlanAvailability` resource ID from the [`List plan availabilities for a subscription`](./get-v1-subscriptions-_id_-planavailabilities.md) response.

### Query Parameters

- `fields[subscriptionPlanAvailabilities]` ([string]): Additional fields to include for each subscription plan availability resource that the response returns.

  **Allowed Values**: `availableInNewTerritories`, `planType`, `availableTerritories`
- `fields[territories]` ([string]): Additional fields to include for each territory resource that the response returns.

  **Allowed Values**: `currency`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `availableTerritories`
- `limit[availableTerritories]` (integer): The maximum number of available territory resources to return.

  **Maximum**: `50`

## Responses

- `200` OK (`SubscriptionPlanAvailabilityResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and modifying plan availability
- [Create a subscription plan availability](./post-v1-subscriptionplanavailabilities.md)
  Create the plan availability configuration for an auto-renewable subscription.
- [Modify a subscription plan availability](./patch-v1-subscriptionplanavailabilities-_id_.md)
  Update the plan availability configuration for a specific subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionplanavailabilities-_id_)*