# PKPaymentPassActivationState

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

Cases that indicate payment pass activation states.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum PKPaymentPassActivationState
```

## Topics

### Activation states
- [PKPaymentPassActivationState.activated](pkpaymentpassactivationstate/activated.md)
  Active and ready for payment use.
- [PKPaymentPassActivationState.requiresActivation](pkpaymentpassactivationstate/requiresactivation.md)
  Not active but may be activated by the issuer.
- [PKPaymentPassActivationState.activating](pkpaymentpassactivationstate/activating.md)
  Not ready for use but activation is in progress.
- [PKPaymentPassActivationState.suspended](pkpaymentpassactivationstate/suspended.md)
  Not active and can’t be activated.
- [PKPaymentPassActivationState.deactivated](pkpaymentpassactivationstate/deactivated.md)
  Not active because the issuer disabled the account associated with the device.
### Initializers
- [init?(rawValue: UInt)](pkpaymentpassactivationstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var activationState: PKPaymentPassActivationState](pkpaymentpass/activationstate.md)
  The current activation state of the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate)*