# List available territory IDs for a subscription plan availability

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of available territory resource IDs for a specific subscription plan availability.

**Availability**:
- App Store Connect API 4.4+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionPlanAvailabilities/{id}/relationships/availableTerritories`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `subscriptionPlanAvailability` resource ID from the [`List plan availabilities for a subscription`](./get-v1-subscriptions-_id_-planavailabilities.md) response.

### Query Parameters

- `limit` (integer): The maximum number of territory resource identifiers to return.

  **Maximum**: `200`

## Responses

- `200` OK (`SubscriptionPlanAvailabilityAvailableTerritoriesLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing available territories
- [List available territories for a subscription plan availability](./get-v1-subscriptionplanavailabilities-_id_-availableterritories.md)
  List all territories where a specific subscription plan is available.
- [Replace the available territories for a subscription plan availability](./patch-v1-subscriptionplanavailabilities-_id_-relationships-availableterritories.md)
  Replace the list of available territories for a specific subscription plan availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionplanavailabilities-_id_-relationships-availableterritories)*