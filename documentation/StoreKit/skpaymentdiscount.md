# SKPaymentDiscount

**Framework**: StoreKit  
**Kind**: class

The signed discount to apply to a payment.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
class SKPaymentDiscount
```

## Mentions

- [Implementing promotional offers in your app](implementing-promotional-offers-in-your-app.md)
- [Generating a signature for promotional offers](generating-a-signature-for-promotional-offers.md)

#### Overview

The [`SKPaymentDiscount`](skpaymentdiscount.md) contains the details of a promotional offer discount that you want to apply to a [`SKMutablePayment`](skmutablepayment.md).

Include the signature that you generated in this object. For guidance, see [`Generating a signature for promotional offers`](generating-a-signature-for-promotional-offers.md). The App Store uses this signature and the parameters to validate the promotional offer. Keep in mind that the signature must correspond to the parameters in the payment for a transaction to be successful.

## Topics

### Initializing a Payment Discount
- [init(identifier: String, keyIdentifier: String, nonce: UUID, signature: String, timestamp: NSNumber)](skpaymentdiscount/init(identifier:keyidentifier:nonce:signature:timestamp:).md)
  Initializes the payment discount with a signature and the parameters used by the signature.
### Identifying the Discount
- [var identifier: String](skpaymentdiscount/identifier.md)
  A string used to uniquely identify a discount offer for a product.
- [var keyIdentifier: String](skpaymentdiscount/keyidentifier.md)
  A string that identifies the key used to generate the signature.
### Validating the Discount
- [var nonce: UUID](skpaymentdiscount/nonce.md)
  A universally unique ID (UUID) value that you define.
- [var signature: String](skpaymentdiscount/signature.md)
  A string representing the properties of a specific promotional offer, cryptographically signed.
- [var timestamp: NSNumber](skpaymentdiscount/timestamp.md)
  The date and time of the signature’s creation in milliseconds, formatted in Unix epoch time.

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
- [Sendable](../Swift/Sendable.md)

## See Also

- [var paymentDiscount: SKPaymentDiscount?](skpayment/paymentdiscount.md)
  The details of the discount offer to apply to the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentdiscount)*