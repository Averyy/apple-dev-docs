# PKSecureElementPass.PassActivationState.activating

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

The pass isn’t ready to use, but activation is in progress

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
case activating
```

```c
PKSecureElementPassActivationStateActivating
```

## See Also

### Activation states
- [PKSecureElementPass.PassActivationState.requiresActivation](./requiresactivation.md)
  The pass requires activation by the issuer.
- [PKSecureElementPass.PassActivationState.activated](./activated.md)
  The pass is active and ready to use.
- [PKSecureElementPass.PassActivationState.suspended](./suspended.md)
  The user or the issuer has suspended the pass and it isn’t available to use.
- [PKSecureElementPass.PassActivationState.deactivated](./deactivated.md)
  The issuer has deactivated the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksecureelementpass/passactivationstate-swift.enum/activating)*