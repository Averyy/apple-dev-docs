# Replace the available territories for a subscription plan availability

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Replace the list of available territories for a specific subscription plan availability.

**Availability**:
- App Store Connect API 4.4+

## Mentions

- [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/subscriptionPlanAvailabilities/{id}/relationships/availableTerritories`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `subscriptionPlanAvailability` resource ID from the [`List plan availabilities for a subscription`](./get-v1-subscriptions-_id_-planavailabilities.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionPlanAvailabilityAvailableTerritoriesLinkagesRequest`

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing available territories
- [List available territories for a subscription plan availability](./get-v1-subscriptionplanavailabilities-_id_-availableterritories.md)
  List all territories where a specific subscription plan is available.
- [List available territory IDs for a subscription plan availability](./get-v1-subscriptionplanavailabilities-_id_-relationships-availableterritories.md)
  Get a list of available territory resource IDs for a specific subscription plan availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-subscriptionplanavailabilities-_id_-relationships-availableterritories)*