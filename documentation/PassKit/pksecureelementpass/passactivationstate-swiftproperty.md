# passActivationState

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The activation state of the pass.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var passActivationState: PKSecureElementPass.PassActivationState { get }
```

#### Discussion

You must activate a secure pass before it can be used.

For possible values and their meanings, see [`PKSecureElementPass.PassActivationState`](pksecureelementpass/passactivationstate-swift.enum.md).

## See Also

- [PKSecureElementPass.PassActivationState](pksecureelementpass/passactivationstate-swift.enum.md)
  The activation states of a Secure Element pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksecureelementpass/passactivationstate-swift.property)*