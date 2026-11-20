# Create a subscription price change preview

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Preview how proposed subscription prices, including volume pricing tiers, change what existing subscribers pay.

**Availability**:
- App Store Connect API 4.6.1+

## Mentions

- [App Store Connect API 4.6.1 release notes](./app-store-connect-api-4-6-1-release-notes.md)
- [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md)
- [Unpreserving prices after volume pricing takes effect](./removing-price-preservation-after-volume-pricing-takes-effect.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptionPriceChangePreviews`

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionPriceChangePreviewCreateRequest`

The request body you use to create a subscription price change preview.

## Responses

- `201` Created (`SubscriptionPriceChangePreviewResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`): The request data is not valid.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptionpricechangepreviews)*