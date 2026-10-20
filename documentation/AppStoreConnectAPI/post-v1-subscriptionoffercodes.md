# Create a subscription offer

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a subscription offer that provides offer codes for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptionOfferCodes`

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionOfferCodeCreateRequest`

## Responses

- `201` Created (`SubscriptionOfferCodeResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and Managing Subscription Offers
- [Read subscription offer code information](./get-v1-subscriptionoffercodes-_id_.md)
  Get details about a specific subscription offer that has offer codes for an auto-renewable subscription.
- [Deactivate a subscription offer with offer codes](./patch-v1-subscriptionoffercodes-_id_.md)
  Deactivate a subscription offer that has offer codes for an auto-renewable subscription.
- [List all subscription offer code prices](./get-v1-subscriptionoffercodes-_id_-prices.md)
  Get a list of price tiers for a subscription offer code.
- [List price IDs for a subscription offer code](./get-v1-subscriptionoffercodes-_id_-relationships-prices.md)
  Get a list of price resource IDs for a specific subscription offer code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptionoffercodes)*