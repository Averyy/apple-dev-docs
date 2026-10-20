# Modify an In-App Purchase Offer Code Custom Code

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update a specific In-App Purchase offer code custom code.

**Availability**:
- App Store Connect API 4.2+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/inAppPurchaseOfferCodeCustomCodes/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `InAppPurchaseOfferCodeCustomCodeUpdateRequest`

## Responses

- `200` OK (`InAppPurchaseOfferCodeCustomCodeResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Custom Offer Codes
- [Create an In-App Purchase Offer Code Custom Code](./post-v1-inapppurchaseoffercodecustomcodes.md)
  Create a custom code for an In-App Purchase offer code.
- [List All Custom Codes for an In-App Purchase Offer Code](./get-v1-inapppurchaseoffercodes-_id_-customcodes.md)
  Get a list of custom codes for a specific In-App Purchase offer code.
- [Get All Custom Code IDs for an In-App Purchase Offer Code](./get-v1-inapppurchaseoffercodes-_id_-relationships-customcodes.md)
  Get a list of custom code resource IDs for a specific In-App Purchase offer code.
- [Read In-App Purchase Offer Code Custom Code Information](./get-v1-inapppurchaseoffercodecustomcodes-_id_.md)
  Get information about a specific In-App Purchase offer code custom code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-inapppurchaseoffercodecustomcodes-_id_)*