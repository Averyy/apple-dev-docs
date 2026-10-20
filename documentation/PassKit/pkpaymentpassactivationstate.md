# PKPaymentPassActivationState

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

Cases that indicate payment pass activation states.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: Use [`PKSecureElementPass.PassActivationState`](./pksecureelementpass/passactivationstate-swift.enum.md) instead.

## Declaration

```swift
enum PKPaymentPassActivationState
```

```c
enum PKPaymentPassActivationState : NSUInteger;
```

## Topics

### Activation states
- [PKPaymentPassActivationState.activated](./pkpaymentpassactivationstate/activated.md)
  Active and ready for payment use.
- [PKPaymentPassActivationState.requiresActivation](./pkpaymentpassactivationstate/requiresactivation.md)
  Not active but may be activated by the issuer.
- [PKPaymentPassActivationState.activating](./pkpaymentpassactivationstate/activating.md)
  Not ready for use but activation is in progress.
- [PKPaymentPassActivationState.suspended](./pkpaymentpassactivationstate/suspended.md)
  Not active and can’t be activated.
- [PKPaymentPassActivationState.deactivated](./pkpaymentpassactivationstate/deactivated.md)
  Not active because the issuer disabled the account associated with the device.
### Initializers
- [init?(rawValue: UInt)](./pkpaymentpassactivationstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Determining activation state
- [var activationState: PKPaymentPassActivationState](./pkpaymentpass/activationstate.md)
  The current activation state of the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate)*