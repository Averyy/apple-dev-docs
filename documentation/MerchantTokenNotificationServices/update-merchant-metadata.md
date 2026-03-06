# Update Merchant Metadata

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: httpRequest

Update the merchant token’s notification URL.

**Availability**:
- Apple Pay Merchant Token Management API 1.0.12+

#### Discussion

The merchant server calls this API to update the value of a merchant token’s `tokenNotificationURL`. This URL receives life-cycle and metadata update notifications from the Apple Pay servers about the Apple Pay merchant token.

## Endpoint

`POST https://apple-pay-gateway.apple.com/paymentservices/v1/merchantId/{merchantId}/merchantToken/updateMerchantMetadata`

## Parameters

- `Accept` (string): The response format the client expects, for example, `application/json` for JSON.
- `Content-Type` (string) *(required)*: The format of the data sent in the request body, for example, `application/json` for JSON payloads.
- `x-request-id` (string) *(required)*: The header used to uniquely identify the request.

## Request Body

The request body you use to specify the updated merchant metadata.

## See Also

- [Receiving and handling merchant token notifications](../applepaymerchanttokenmanagementapi/receiving-and-handling-merchant-token-notifications.md)
  Implement an endpoint to receive and handle merchant token life-cycle updates from Apple Pay.
- [Send Merchant Token Event](send-merchant-token-event.md)
  Receive and handle merchant token life-cycle updates from Apple Pay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/update-merchant-metadata)*