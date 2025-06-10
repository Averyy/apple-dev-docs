# PaymentCardVerificationRequest

**Framework**: ProximityReader  
**Kind**: struct

A request to verify details for a contactless payment card.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
struct PaymentCardVerificationRequest
```

#### Overview

Create a `PaymentCardVerificationRequest` object to verify details of a person’s payment card before performing a transaction with that card. For example, you might use a verification request to make sure the person’s card supports a specific currency. After creating a request object, pass it to the [`readPaymentCard(_:)`](paymentcardreadersession/readpaymentcard(_:)-hr97.md) or [`readPaymentCard(_:vasRequest:stopOnVASResult:)`](paymentcardreadersession/readpaymentcard(_:vasrequest:stoponvasresult:).md) method of your session to read the card details.

## Topics

### Creating the verification request
- [init(currencyCode: String, for: PaymentCardVerificationRequest.Reason)](paymentcardverificationrequest/init(currencycode:for:).md)
  Creates a new verification request using the specified currency and reason information.
### Getting the request details
- [let currencyCode: String](paymentcardverificationrequest/currencycode.md)
  The ISO 4217 code that indicates the currency type.
- [let verificationReason: PaymentCardVerificationRequest.Reason](paymentcardverificationrequest/verificationreason.md)
  The reason you asked to verify someone’s card.
- [PaymentCardVerificationRequest.Reason](paymentcardverificationrequest/reason.md)
  The reason for the verification request.
### Setting the user interface language
- [var userInterfaceLanguage: Locale.Language?](paymentcardverificationrequest/userinterfacelanguage.md)
  The language to use when localizing the user interface.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PaymentCardTransactionRequest](paymentcardtransactionrequest.md)
  A request for a contactless purchase or refund that includes the purchase amount and currency information.
- [struct PaymentCardReadResult](paymentcardreadresult.md)
  The result of a payment card read operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardverificationrequest)*