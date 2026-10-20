# Modify an In-App Purchase Offer Code One-Time Use Code

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update a specific In-App Purchase offer code one-time use code.

**Availability**:
- App Store Connect API 4.2+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/inAppPurchaseOfferCodeOneTimeUseCodes/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `InAppPurchaseOfferCodeOneTimeUseCodeUpdateRequest`

## Responses

- `200` OK (`InAppPurchaseOfferCodeOneTimeUseCodeResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing One-Time Use Offer Codes
- [Create an In-App Purchase Offer Code One-Time Use Code](./post-v1-inapppurchaseoffercodeonetimeusecodes.md)
  Create a one-time use code for an In-App Purchase offer code.
- [Read In-App Purchase Offer Code One-Time Use Code Information](./get-v1-inapppurchaseoffercodeonetimeusecodes-_id_.md)
  Get information about a specific In-App Purchase offer code one-time use code.
- [List All One-Time Use Codes for an In-App Purchase Offer Code](./get-v1-inapppurchaseoffercodes-_id_-onetimeusecodes.md)
  Get a list of one-time use codes for a specific In-App Purchase offer code.
- [List All Values for an In-App Purchase Offer Code One-Time Use Code](./get-v1-inapppurchaseoffercodeonetimeusecodes-_id_-values.md)
  Get a list of values for a specific In-App Purchase offer code one-time use code.
- [Get All One-Time Use Code IDs for an In-App Purchase Offer Code](./get-v1-inapppurchaseoffercodes-_id_-relationships-onetimeusecodes.md)
  Get a list of one-time use code resource IDs for a specific In-App Purchase offer code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-inapppurchaseoffercodeonetimeusecodes-_id_)*