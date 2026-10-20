# Modify a subscription plan availability

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the plan availability configuration for a specific subscription.

**Availability**:
- App Store Connect API 4.4+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/subscriptionPlanAvailabilities/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `subscriptionPlanAvailability` resource ID from the [`List plan availabilities for a subscription`](./get-v1-subscriptions-_id_-planavailabilities.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionPlanAvailabilityUpdateRequest`

## Responses

- `200` OK (`SubscriptionPlanAvailabilityResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and modifying plan availability
- [Create a subscription plan availability](./post-v1-subscriptionplanavailabilities.md)
  Create the plan availability configuration for an auto-renewable subscription.
- [Read subscription plan availability information](./get-v1-subscriptionplanavailabilities-_id_.md)
  Get information about a specific subscription plan availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-subscriptionplanavailabilities-_id_)*