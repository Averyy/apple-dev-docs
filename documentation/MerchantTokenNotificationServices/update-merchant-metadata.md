# Update Merchant Metadata

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the merchant token’s notification URL.

**Availability**:
- Apple Pay Merchant Token Management API 1.0.12+

## Discussion

The merchant server calls this API to update the value of a merchant token’s `tokenNotificationURL`. This URL receives life-cycle and metadata update notifications from the Apple Pay servers about the Apple Pay merchant token.

## Endpoint

`POST https://apple-pay-gateway.apple.com/paymentservices/v1/merchantId/{merchantId}/merchantToken/updateMerchantMetadata`

## Parameters

### Path Parameters

- `merchantId` (string) *(required)*: The merchant identifier issued by Apple.

  **Maximum Length**: `64`

### Header Parameters

- `Accept` (string): The response format the client expects, for example, `application/json` for JSON.
- `Content-Type` (string) *(required)*: The format of the data sent in the request body, for example, `application/json` for JSON payloads.
- `x-request-id` (string) *(required)*: The header used to uniquely identify the request.

## Request Body

**Content-Type**: `application/json`  
**Type**: `UpdateMerchantMetadataRequest`

The request body you use to specify the updated merchant metadata.

## Responses

- `200` OK: Successful response.
- `400` Bad Request (`ErrorResponse`, `application/json`): Bad request.
- `403` Forbidden (`ErrorResponse`, `application/json`): Authorization failed.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `500` Internal Server Error (`ErrorResponse`, `application/json`): Internal server error.

## See Also

### Merchant token notification handling
- [Receiving and handling merchant token notifications](../ApplePayMerchantTokenManagementAPI/receiving-and-handling-merchant-token-notifications.md)
  Implement an endpoint to receive and handle merchant token life-cycle updates from Apple Pay.
- [Send Merchant Token Event](./send-merchant-token-event.md)
  Receive and handle merchant token life-cycle updates from Apple Pay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/update-merchant-metadata)*