# Create an auto-renewable subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create an auto-renewable subscription for your app.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Managing auto-renewable subscriptions](./managing-auto-renewable-subscriptions.md)

## Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptions`

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionCreateRequest`

## Responses

- `201` Created (`SubscriptionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and managing subscriptions
- [Read subscription information](./get-v1-subscriptions-_id_.md)
  Get information about a specific auto-renewable subscription.
- [Modify an auto-renewable subscription](./patch-v1-subscriptions-_id_.md)
  Update a specific auto-renewable subscription.
- [Delete a subscription](./delete-v1-subscriptions-_id_.md)
  Delete a specific auto-renewable subscription that you configured for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptions)*