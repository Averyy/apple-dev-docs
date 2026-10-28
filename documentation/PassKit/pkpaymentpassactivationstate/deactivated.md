# PKPaymentPassActivationState.deactivated

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

Not active because the issuer disabled the account associated with the device.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: Use [`PKSecureElementPass.PassActivationState.deactivated`](../pksecureelementpass/passactivationstate-swift.enum/deactivated.md) instead.

## Declaration

```swift
case deactivated
```

```c
PKPaymentPassActivationStateDeactivated
```

## Discussion

To reactivate the account, reprovision the pass.

## See Also

### Activation states
- [PKPaymentPassActivationState.activated](./activated.md)
  Active and ready for payment use.
- [PKPaymentPassActivationState.requiresActivation](./requiresactivation.md)
  Not active but may be activated by the issuer.
- [PKPaymentPassActivationState.activating](./activating.md)
  Not ready for use but activation is in progress.
- [PKPaymentPassActivationState.suspended](./suspended.md)
  Not active and can’t be activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/deactivated)*