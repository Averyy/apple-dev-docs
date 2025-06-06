# PKPaymentPassActivationState.activating

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

Not ready for use but activation is in progress.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case activating
```

## See Also

- [PKPaymentPassActivationState.activated](pkpaymentpassactivationstate/activated.md)
  Active and ready for payment use.
- [PKPaymentPassActivationState.requiresActivation](pkpaymentpassactivationstate/requiresactivation.md)
  Not active but may be activated by the issuer.
- [PKPaymentPassActivationState.suspended](pkpaymentpassactivationstate/suspended.md)
  Not active and can’t be activated.
- [PKPaymentPassActivationState.deactivated](pkpaymentpassactivationstate/deactivated.md)
  Not active because the issuer disabled the account associated with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/activating)*