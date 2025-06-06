# paymentInstrumentName

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A description of the payment card that the user selected to fund the transaction.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var paymentInstrumentName: String { get }
```

#### Discussion

This string is suitable for display; it doesn’t contain the full payment information.

## See Also

- [var paymentNetwork: String](pkpaymenttoken/paymentnetwork.md)
  The payment network for the card that funds this transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenttoken/paymentinstrumentname)*