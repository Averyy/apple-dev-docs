# List available territory IDs for a subscription availability

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 2.3+ - Deprecated in 4.4

> **Deprecated**: This endpoint is deprecated. Use [`List available territories for a subscription plan availability`](./get-v1-subscriptionplanavailabilities-_id_-availableterritories.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/{id}/relationships/availableTerritories`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`SubscriptionAvailabilityAvailableTerritoriesLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read the availability of a subscription](./get-v1-subscriptionavailabilities-_id_.md)
  Get information about the territory availability for a subscription.
- [List the territory availability of a subscription](./get-v1-subscriptionavailabilities-_id_-availableterritories.md)
  List the territory availability and currency of a specific subscription.
- [Modify the territory availability of a subscription](./post-v1-subscriptionavailabilities.md)
  Update the territory availability of a specific subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionavailabilities-_id_-relationships-availableterritories)*