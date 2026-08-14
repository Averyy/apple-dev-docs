# Get Details of a Merchant Token Event

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: httpRequest

Get the details of a merchant token event after receiving a notification.

**Availability**:
- App Store Connect API 1.0.10+
- Apple Pay Merchant Token Management API 1.0.12+

## Mentions

- [Receiving and handling merchant token notifications](../applepaymerchanttokenmanagementapi/receiving-and-handling-merchant-token-notifications.md)

#### Discussion

For information about setting your server’s notification URL to receive life-cycle events, see [`tokenNotificationURL`](https://developer.apple.com/documentation/passkit/pkautomaticreloadpaymentrequest/tokennotificationurl) in [`PKAutomaticReloadPaymentRequest`](https://developer.apple.com/documentation/passkit/pkautomaticreloadpaymentrequest), [`tokenNotificationURL`](https://developer.apple.com/documentation/passkit/pkrecurringpaymentrequest/tokennotificationurl) in [`PKRecurringPaymentRequest`](https://developer.apple.com/documentation/passkit/pkrecurringpaymentrequest), [`tokenNotificationURL`](https://developer.apple.com/documentation/applepayontheweb/applepayautomaticreloadpaymentrequest/tokennotificationurl) in [`ApplePayAutomaticReloadPaymentRequest`](https://developer.apple.com/documentation/applepayontheweb/applepayautomaticreloadpaymentrequest), or [`tokenNotificationURL`](https://developer.apple.com/documentation/applepayontheweb/applepayrecurringpaymentrequest/tokennotificationurl) in [`ApplePayRecurringPaymentRequest`](https://developer.apple.com/documentation/applepayontheweb/applepayrecurringpaymentrequest).

## Endpoint

`GET https://apple-pay-gateway.apple.com/paymentservices/v1/merchantId/{merchantId}/merchantToken/event/{eventId}`

## Parameters

- `Accept` (string)
- `Content-Type` (string) *(required)*
- `x-request-id` (string) *(required)*

## See Also

- [object MerchantTokenEventResponse](merchanttokeneventresponse.md)
  A response body that contains information about a life-cycle event for a merchant token.
- [object MerchantTokenMetadata](merchanttokenmetadata.md)
  The card information related to a merchant token, including its card art and metadata.
- [object CardArt](cardart.md)
  Data for displaying art to represent a card.
- [object CardMetadata](cardmetadata.md)
  Data about the card, including its expiration date and suffix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/merchant-token-event-retrieval)*