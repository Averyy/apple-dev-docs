# List plan availability IDs for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of plan availability resource IDs for a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 4.4+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/relationships/planAvailabilities`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `subscription` resource ID from the [`List all subscriptions for a subscription group`](./get-v1-subscriptiongroups-_id_-subscriptions.md) response.

### Query Parameters

- `limit` (integer): The maximum number of subscription plan availability resource identifiers to return.

  **Maximum**: `200`

## Responses

- `200` OK (`SubscriptionPlanAvailabilitiesLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading plan availability from a subscription
- [List plan availabilities for a subscription](./get-v1-subscriptions-_id_-planavailabilities.md)
  List all plan availabilities for a specific auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-relationships-planavailabilities)*