# Create custom offer codes

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create custom offer codes for an auto-renewable subscription offer.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptionOfferCodeCustomCodes`

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionOfferCodeCustomCodeCreateRequest`

## Responses

- `201` Created (`SubscriptionOfferCodeCustomCodeResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Custom Offer Codes
- [List all custom offer codes for an auto-renewable subscription](./get-v1-subscriptionoffercodes-_id_-customcodes.md)
  Get details about a custom code for a specific subscription offer for an auto-renewable subscription.
- [List custom code IDs for a subscription offer code](./get-v1-subscriptionoffercodes-_id_-relationships-customcodes.md)
- [Read custom offer code information](./get-v1-subscriptionoffercodecustomcodes-_id_.md)
  Get details about a specific offer code for an auto-renewable subscription.
- [Deactivate custom offer codes](./patch-v1-subscriptionoffercodecustomcodes-_id_.md)
  Deactivate a batch of custom offer codes for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptionoffercodecustomcodes)*