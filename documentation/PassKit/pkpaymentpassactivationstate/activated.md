# PKPaymentPassActivationState.activated

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

Active and ready for payment use.

**Availability**:
- iOS 8.0+ - Deprecated in 27.3
- iPadOS 8.0+ - Deprecated in 27.3
- Mac Catalyst 13.1+ - Deprecated in 27.3
- macOS 11.0+ - Deprecated in 27.3
- visionOS 1.0+ - Deprecated in 27.3
- watchOS 3.0+ - Deprecated in 27.3

> **Deprecated**: Use [`PKSecureElementPass.PassActivationState.activated`](../pksecureelementpass/passactivationstate-swift.enum/activated.md) instead.

## Declaration

```swift
case activated
```

```c
PKPaymentPassActivationStateActivated
```

## See Also

### Activation states
- [PKPaymentPassActivationState.requiresActivation](./requiresactivation.md)
  Not active but may be activated by the issuer.
- [PKPaymentPassActivationState.activating](./activating.md)
  Not ready for use but activation is in progress.
- [PKPaymentPassActivationState.suspended](./suspended.md)
  Not active and can’t be activated.
- [PKPaymentPassActivationState.deactivated](./deactivated.md)
  Not active because the issuer disabled the account associated with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/activated)*