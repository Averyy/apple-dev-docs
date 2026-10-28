# Modify an auto-renewable subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Configuring multi-seat subscriptions for organizations](./configuring-multi-seat-subscriptions-for-organizations.md)

## Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/subscriptions/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionUpdateRequest`

## Responses

- `200` OK (`SubscriptionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and managing subscriptions
- [Create an auto-renewable subscription](./post-v1-subscriptions.md)
  Create an auto-renewable subscription for your app.
- [Read subscription information](./get-v1-subscriptions-_id_.md)
  Get information about a specific auto-renewable subscription.
- [Delete a subscription](./delete-v1-subscriptions-_id_.md)
  Delete a specific auto-renewable subscription that you configured for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-subscriptions-_id_)*