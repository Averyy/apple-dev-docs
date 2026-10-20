# paymentNetwork

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The payment network for the card that funds this transaction.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 11.0+
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This property is deprecated. Use [`paymentMethod`](./paymentmethod.md) instead.

## Declaration

```swift
var paymentNetwork: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * paymentNetwork;
```

#### Discussion

The value of this property is one of the constants listed in [`PKPaymentRequest`](../pkpaymentrequest.md).

## See Also

### Deprecated
- [var paymentInstrumentName: String](./paymentinstrumentname.md)
  A description of the payment card that the user selected to fund the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenttoken/paymentnetwork)*