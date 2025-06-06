# transactionIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A unique identifier for this payment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var transactionIdentifier: String { get }
```

#### Discussion

This identifier is suitable for use in a receipt.

## See Also

- [var paymentData: Data](pkpaymenttoken/paymentdata.md)
  The payment data as a UTF-8 encoded serialization of a JSON dictionary.
- [var paymentMethod: PKPaymentMethod](pkpaymenttoken/paymentmethod.md)
  Information about the card used in the transaction.
- [class PKPaymentMethod](pkpaymentmethod.md)
  An object that contains information about payment methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenttoken/transactionidentifier)*