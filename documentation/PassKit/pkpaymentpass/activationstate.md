# activationState

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The current activation state of the pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var activationState: PKPaymentPassActivationState { get }
```

#### Discussion

You must activate a payment pass before you can use it.

For possible values and their meanings, see [`PKPaymentPass`](pkpaymentpass.md).

## See Also

- [Wallet Developer Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/index.html#//apple_ref/doc/uid/TP40012195)
- [enum PKPaymentPassActivationState](pkpaymentpassactivationstate.md)
  Cases that indicate payment pass activation states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentpass/activationstate)*