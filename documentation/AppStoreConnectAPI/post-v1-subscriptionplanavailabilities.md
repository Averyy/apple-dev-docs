# Create a subscription plan availability

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create the plan availability configuration for an auto-renewable subscription.

**Availability**:
- App Store Connect API 4.4+

## Mentions

- [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptionPlanAvailabilities`

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionPlanAvailabilityCreateRequest`

## Responses

- `201` Created (`SubscriptionPlanAvailabilityResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and modifying plan availability
- [Read subscription plan availability information](./get-v1-subscriptionplanavailabilities-_id_.md)
  Get information about a specific subscription plan availability.
- [Modify a subscription plan availability](./patch-v1-subscriptionplanavailabilities-_id_.md)
  Update the plan availability configuration for a specific subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptionplanavailabilities)*