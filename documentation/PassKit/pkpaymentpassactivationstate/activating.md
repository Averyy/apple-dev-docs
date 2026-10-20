# PKPaymentPassActivationState.activating

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

Not ready for use but activation is in progress.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: Use [`PKSecureElementPass.PassActivationState.activating`](../pksecureelementpass/passactivationstate-swift.enum/activating.md) instead.

## Declaration

```swift
case activating
```

```c
PKPaymentPassActivationStateActivating
```

## See Also

### Activation states
- [PKPaymentPassActivationState.activated](./activated.md)
  Active and ready for payment use.
- [PKPaymentPassActivationState.requiresActivation](./requiresactivation.md)
  Not active but may be activated by the issuer.
- [PKPaymentPassActivationState.suspended](./suspended.md)
  Not active and can’t be activated.
- [PKPaymentPassActivationState.deactivated](./deactivated.md)
  Not active because the issuer disabled the account associated with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/activating)*