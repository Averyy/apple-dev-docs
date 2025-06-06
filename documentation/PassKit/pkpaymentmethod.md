# PKPaymentMethod

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that contains information about payment methods.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class PKPaymentMethod
```

## Topics

### Getting the pass
- [var secureElementPass: PKSecureElementPass?](pkpaymentmethod/secureelementpass.md)
  The accompanying Secure Element pass.
- [var paymentPass: PKPaymentPass?](pkpaymentmethod/paymentpass.md)
  The accompanying payment pass.
### Getting the payment method’s attributes
- [var type: PKPaymentMethodType](pkpaymentmethod/type.md)
  A value that represents the card’s type.
- [enum PKPaymentMethodType](pkpaymentmethodtype.md)
  The type of cards available in Apple Pay.
- [var displayName: String?](pkpaymentmethod/displayname.md)
  A string, suitable for display, that describes the card.
- [var network: PKPaymentNetwork?](pkpaymentmethod/network.md)
  A string, suitable for display, that describes the payment network for the card.
- [var billingAddress: CNContact?](pkpaymentmethod/billingaddress.md)
  The user’s billing address.

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

- [var paymentData: Data](pkpaymenttoken/paymentdata.md)
  The payment data as a UTF-8 encoded serialization of a JSON dictionary.
- [var paymentMethod: PKPaymentMethod](pkpaymenttoken/paymentmethod.md)
  Information about the card used in the transaction.
- [var transactionIdentifier: String](pkpaymenttoken/transactionidentifier.md)
  A unique identifier for this payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentmethod)*