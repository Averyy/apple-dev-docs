# PKPaymentToken

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

Contains the user’s payment credentials.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class PKPaymentToken
```

#### Overview

You access the payment token for an authorized payment request using the [`token`](pkpayment/token.md) property of [`PKPayment`](pkpayment.md).

## Topics

### Working with payment tokens
- [var paymentData: Data](pkpaymenttoken/paymentdata.md)
  The payment data as a UTF-8 encoded serialization of a JSON dictionary.
- [var paymentMethod: PKPaymentMethod](pkpaymenttoken/paymentmethod.md)
  Information about the card used in the transaction.
- [class PKPaymentMethod](pkpaymentmethod.md)
  An object that contains information about payment methods.
- [var transactionIdentifier: String](pkpaymenttoken/transactionidentifier.md)
  A unique identifier for this payment.
### Deprecated
- [var paymentNetwork: String](pkpaymenttoken/paymentnetwork.md)
  The payment network for the card that funds this transaction.
- [var paymentInstrumentName: String](pkpaymenttoken/paymentinstrumentname.md)
  A description of the payment card that the user selected to fund the transaction.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var token: PKPaymentToken](pkpayment/token.md)
  The encrypted payment information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenttoken)*