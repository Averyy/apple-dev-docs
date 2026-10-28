# Get Details of a Merchant Token Event

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the details of a merchant token event after receiving a notification.

**Availability**:
- App Store Connect API 1.0.10+
- Apple Pay Merchant Token Management API 1.0.12+

## Mentions

- [Receiving and handling merchant token notifications](../ApplePayMerchantTokenManagementAPI/receiving-and-handling-merchant-token-notifications.md)

## Discussion

For information about setting your server’s notification URL to receive life-cycle events, see [`tokenNotificationURL`](../PassKit/pkautomaticreloadpaymentrequest/tokennotificationurl.md) in [`PKAutomaticReloadPaymentRequest`](../PassKit/pkautomaticreloadpaymentrequest.md), [`tokenNotificationURL`](../PassKit/pkrecurringpaymentrequest/tokennotificationurl.md) in [`PKRecurringPaymentRequest`](../PassKit/pkrecurringpaymentrequest.md), [`tokenNotificationURL`](../ApplePayontheWeb/applepayautomaticreloadpaymentrequest/tokennotificationurl.md) in [`ApplePayAutomaticReloadPaymentRequest`](../ApplePayontheWeb/applepayautomaticreloadpaymentrequest.md), or [`tokenNotificationURL`](../ApplePayontheWeb/applepayrecurringpaymentrequest/tokennotificationurl.md) in [`ApplePayRecurringPaymentRequest`](../ApplePayontheWeb/applepayrecurringpaymentrequest.md).

## Endpoint

`GET https://apple-pay-gateway.apple.com/paymentservices/v1/merchantId/{merchantId}/merchantToken/event/{eventId}`

## Parameters

### Path Parameters

- `eventId` (string) *(required)*: A unique event identifier that you receive in a notification from the Apple Pay server.
- `merchantId` (string) *(required)*: Your merchant identifier.

### Header Parameters

- `Accept` (string)
- `Content-Type` (string) *(required)*
- `x-request-id` (string) *(required)*

## Responses

- `200` OK (`MerchantTokenEventResponse`, `application/json`): Successful response.
- `400` Bad Request (`ErrorResponse`, `application/json`): Bad request.
- `500` Internal Server Error (`ErrorResponse`, `application/json`): Internal server error.

## See Also

### Merchant token event retrieval
- [object MerchantTokenEventResponse](./merchanttokeneventresponse.md)
  A response body that contains information about a life-cycle event for a merchant token.
- [object MerchantTokenMetadata](./merchanttokenmetadata.md)
  The card information related to a merchant token, including its card art and metadata.
- [object CardArt](./cardart.md)
  Data for displaying art to represent a card.
- [object CardMetadata](./cardmetadata.md)
  Data about the card, including its expiration date and suffix.
- [object EncryptedTokenMetadata](./encryptedtokenmetadata.md)
  Encrypted data about the merchant token, including its Merchant Payment Account Number (MPAN) and expiration date.
- [object TokenMetadata](./tokenmetadata.md)
  Unencrypted metadata about a merchant token, including its Merchant Payment Account Number (MPAN) and expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/merchant-token-event-retrieval)*