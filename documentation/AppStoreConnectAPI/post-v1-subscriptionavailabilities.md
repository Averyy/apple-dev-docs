# Modify the territory availability of a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the territory availability of a specific subscription.

**Availability**:
- App Store Connect API 2.3+ - Deprecated in 4.4

> **Deprecated**: This endpoint is deprecated. Use [`Create a subscription plan availability`](./post-v1-subscriptionplanavailabilities.md) instead.

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities`

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionAvailabilityCreateRequest`

## Responses

- `201` Created (`SubscriptionAvailabilityResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read the availability of a subscription](./get-v1-subscriptionavailabilities-_id_.md)
  Get information about the territory availability for a subscription.
- [List the territory availability of a subscription](./get-v1-subscriptionavailabilities-_id_-availableterritories.md)
  List the territory availability and currency of a specific subscription.
- [List available territory IDs for a subscription availability](./get-v1-subscriptionavailabilities-_id_-relationships-availableterritories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptionavailabilities)*