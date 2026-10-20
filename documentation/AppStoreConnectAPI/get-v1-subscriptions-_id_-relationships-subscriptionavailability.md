# Get the subscription availability ID for an auto-renewable subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+ - Deprecated in 4.4

> **Deprecated**: This endpoint is deprecated.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/relationships/subscriptionAvailability`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`SubscriptionSubscriptionAvailabilityLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting subscription availability
- [Read information about the availability of a subscription](./get-v1-subscriptions-_id_-subscriptionavailability.md)
  Get information about the territory availability for a subscription.
- [List plan availabilities for a subscription](./get-v1-subscriptions-_id_-planavailabilities.md)
  List all plan availabilities for a specific auto-renewable subscription.
- [List plan availability IDs for a subscription](./get-v1-subscriptions-_id_-relationships-planavailabilities.md)
  Get a list of plan availability resource IDs for a specific auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-relationships-subscriptionavailability)*