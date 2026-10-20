# PKPaymentPassActivationState.requiresActivation

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

Not active but may be activated by the issuer.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: Use [`PKSecureElementPass.PassActivationState.requiresActivation`](../pksecureelementpass/passactivationstate-swift.enum/requiresactivation.md) instead.

## Declaration

```swift
case requiresActivation
```

```c
PKPaymentPassActivationStateRequiresActivation
```

## See Also

### Activation states
- [PKPaymentPassActivationState.activated](./activated.md)
  Active and ready for payment use.
- [PKPaymentPassActivationState.activating](./activating.md)
  Not ready for use but activation is in progress.
- [PKPaymentPassActivationState.suspended](./suspended.md)
  Not active and can’t be activated.
- [PKPaymentPassActivationState.deactivated](./deactivated.md)
  Not active because the issuer disabled the account associated with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/requiresactivation)*