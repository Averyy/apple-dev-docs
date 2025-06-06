# paymentMethod

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

Information about the card used in the transaction.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var paymentMethod: PKPaymentMethod { get }
```

## See Also

- [var paymentData: Data](pkpaymenttoken/paymentdata.md)
  The payment data as a UTF-8 encoded serialization of a JSON dictionary.
- [class PKPaymentMethod](pkpaymentmethod.md)
  An object that contains information about payment methods.
- [var transactionIdentifier: String](pkpaymenttoken/transactionidentifier.md)
  A unique identifier for this payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenttoken/paymentmethod)*