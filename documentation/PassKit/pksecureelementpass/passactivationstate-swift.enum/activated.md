# PKSecureElementPass.PassActivationState.activated

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

The pass is active and ready to use.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
case activated
```

```c
PKSecureElementPassActivationStateActivated
```

## See Also

### Activation states
- [PKSecureElementPass.PassActivationState.requiresActivation](./requiresactivation.md)
  The pass requires activation by the issuer.
- [PKSecureElementPass.PassActivationState.activating](./activating.md)
  The pass isn’t ready to use, but activation is in progress
- [PKSecureElementPass.PassActivationState.suspended](./suspended.md)
  The user or the issuer has suspended the pass and it isn’t available to use.
- [PKSecureElementPass.PassActivationState.deactivated](./deactivated.md)
  The issuer has deactivated the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksecureelementpass/passactivationstate-swift.enum/activated)*