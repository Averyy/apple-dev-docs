# Get Details of a Merchant Token Event

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: httpRequest

Get the details of a merchant token event after receiving a notification.

**Availability**:
- App Store Connect API 1.0.10+

#### Discussion

For information about setting your server’s notification URL to receive life-cycle events, see [`tokenNotificationURL`](https://developer.apple.com/documentation/PassKit/PKAutomaticReloadPaymentRequest/tokenNotificationURL) in [`PKAutomaticReloadPaymentRequest`](https://developer.apple.com/documentation/PassKit/PKAutomaticReloadPaymentRequest), [`tokenNotificationURL`](https://developer.apple.com/documentation/PassKit/PKRecurringPaymentRequest/tokenNotificationURL) in [`PKRecurringPaymentRequest`](https://developer.apple.com/documentation/PassKit/PKRecurringPaymentRequest), [`tokenNotificationURL`](https://developer.apple.com/documentation/apple_pay_on_the_web/applepayautomaticreloadpaymentrequest/3955921-tokennotificationurl) in [`ApplePayAutomaticReloadPaymentRequest`](https://developer.apple.com/documentation/apple_pay_on_the_web/applepayautomaticreloadpaymentrequest), or [`tokenNotificationURL`](https://developer.apple.com/documentation/apple_pay_on_the_web/applepayrecurringpaymentrequest/3955958-tokennotificationurl) in [`ApplePayRecurringPaymentRequest`](https://developer.apple.com/documentation/apple_pay_on_the_web/applepayrecurringpaymentrequest).

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