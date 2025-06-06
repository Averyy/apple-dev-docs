# PKSecureElementPass.PassActivationState.suspended

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

The user or the issuer has suspended the pass and it isn’t available to use.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
case suspended
```

## See Also

- [PKSecureElementPass.PassActivationState.requiresActivation](pksecureelementpass/passactivationstate-swift.enum/requiresactivation.md)
  The pass requires activation by the issuer.
- [PKSecureElementPass.PassActivationState.activating](pksecureelementpass/passactivationstate-swift.enum/activating.md)
  The pass isn’t ready to use, but activation is in progress
- [PKSecureElementPass.PassActivationState.activated](pksecureelementpass/passactivationstate-swift.enum/activated.md)
  The pass is active and ready to use.
- [PKSecureElementPass.PassActivationState.deactivated](pksecureelementpass/passactivationstate-swift.enum/deactivated.md)
  The issuer has deactivated the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksecureelementpass/passactivationstate-swift.enum/suspended)*