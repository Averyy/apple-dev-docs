# Add retention message offers to a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add retention offers to the retention message for a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 4.6+

## Mentions

- [Setting up retention messaging for auto-renewable subscriptions](./setting-up-retention-messaging.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/relationships/retentionMessageOffers`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the subscription resource ID from the [`List all subscriptions for a subscription group`](./get-v1-subscriptiongroups-_id_-subscriptions.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionRetentionMessageOffersLinkagesRequest`

The request body you use to add relationship to retention message offer.

## Responses

- `204` No Content: The request completed successfully with no response body.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`): The request data is not valid.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Choosing offers for a retention message
- [List retention message offers for a subscription](./get-v1-subscriptions-_id_-retentionmessageoffers.md)
  Get a list of the retention offers that appear with the retention message for a specific auto-renewable subscription.
- [List retention message offer IDs for a subscription](./get-v1-subscriptions-_id_-relationships-retentionmessageoffers.md)
  Get a list of the offer IDs that appear with the retention message for a specific auto-renewable subscription.
- [Remove retention message offers from a subscription](./delete-v1-subscriptions-_id_-relationships-retentionmessageoffers.md)
  Remove retention offers from the retention message for a specific auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptions-_id_-relationships-retentionmessageoffers)*