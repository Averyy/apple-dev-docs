# PaymentCardReadResult

**Framework**: ProximityReader  
**Kind**: struct

The result of a payment card read operation.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
struct PaymentCardReadResult
```

## Mentions

- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)
- [Accepting loyalty passes from Wallet](accepting-loyalty-passes-from-wallet.md)

#### Overview

The system returns a `PaymentCardReadResult` in response to your requests to read a person’s payment card. Use this information to facilitate payments with your payment service provider.

For information about how to read a payment card, see [`PaymentCardReaderSession`](paymentcardreadersession.md).

## Topics

### Getting the result data
- [let generalCardData: String?](paymentcardreadresult/generalcarddata.md)
  A Base64-encoded string that contains general cardholder and terminal data in tag-length-value (TLV) format.
- [let paymentCardData: String?](paymentcardreadresult/paymentcarddata.md)
  A Base64-encoded string that contains the encrypted payment information to send to your payment provider.
### Checking the read outcome
- [let outcome: PaymentCardReadResult.ReadOutcome](paymentcardreadresult/outcome.md)
  The outcome of the transaction.
- [PaymentCardReadResult.ReadOutcome](paymentcardreadresult/readoutcome.md)
  Values that describe the outcome of a read request.
### Getting the result ID
- [let id: String](paymentcardreadresult/id-swift.property.md)
  The unique identifier for the transaction.
### Getting the PIN status
- [let isPINFallback: Bool](paymentcardreadresult/ispinfallback.md)
  A Boolean value that indicates whether the PIN Fallback occurred.
- [let pinBypassed: Bool](paymentcardreadresult/pinbypassed.md)
  A Boolean value that indicates whether the consumer bypassed the PIN entry.
### Getting the kernel type
- [let applicationTypeIdentifier: String?](paymentcardreadresult/applicationtypeidentifier.md)
  A string identifier that represents the payment application type (kernel) used to read the card.
### Instance Properties
- [let cardEffectiveState: PaymentCardReadResult.CardEffectiveState?](paymentcardreadresult/cardeffectivestate-swift.property.md)
  The effective state of the card that the system read.
- [let cardExpirationState: PaymentCardReadResult.CardExpirationState?](paymentcardreadresult/cardexpirationstate-swift.property.md)
  The expiration state of the card that the system read.
### Type Aliases
- [PaymentCardReadResult.ID](paymentcardreadresult/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Enumerations
- [PaymentCardReadResult.CardEffectiveState](paymentcardreadresult/cardeffectivestate-swift.enum.md)
  Values that describe the effective state of the card that was read.
- [PaymentCardReadResult.CardExpirationState](paymentcardreadresult/cardexpirationstate-swift.enum.md)
  Values that describe the expiration state of the card that the system read.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PaymentCardTransactionRequest](paymentcardtransactionrequest.md)
  A request for a contactless purchase or refund that includes the purchase amount and currency information.
- [struct PaymentCardVerificationRequest](paymentcardverificationrequest.md)
  A request to verify details for a contactless payment card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadresult)*