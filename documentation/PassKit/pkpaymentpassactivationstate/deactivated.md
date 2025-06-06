# PKPaymentPassActivationState.deactivated

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

Not active because the issuer disabled the account associated with the device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case deactivated
```

#### Discussion

To reactivate the account, reprovision the pass.

## See Also

- [PKPaymentPassActivationState.activated](pkpaymentpassactivationstate/activated.md)
  Active and ready for payment use.
- [PKPaymentPassActivationState.requiresActivation](pkpaymentpassactivationstate/requiresactivation.md)
  Not active but may be activated by the issuer.
- [PKPaymentPassActivationState.activating](pkpaymentpassactivationstate/activating.md)
  Not ready for use but activation is in progress.
- [PKPaymentPassActivationState.suspended](pkpaymentpassactivationstate/suspended.md)
  Not active and can’t be activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/deactivated)*