# paymentNetwork

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The payment network for the card that funds this transaction.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var paymentNetwork: String { get }
```

#### Discussion

The value of this property is one of the constants listed in [`PKPaymentRequest`](pkpaymentrequest.md).

## See Also

- [var paymentInstrumentName: String](pkpaymenttoken/paymentinstrumentname.md)
  A description of the payment card that the user selected to fund the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenttoken/paymentnetwork)*