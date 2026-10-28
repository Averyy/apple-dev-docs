# activationState

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The current activation state of the pass.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: Use [`passActivationState`](../pksecureelementpass/passactivationstate-swift.property.md) instead.

## Declaration

```swift
var activationState: PKPaymentPassActivationState { get }
```

```objc
@property (nonatomic, readonly) PKPaymentPassActivationState activationState;
```

## Discussion

You must activate a payment pass before you can use it.

For possible values and their meanings, see [`PKPaymentPass`](../pkpaymentpass.md).

## See Also

### Related Documentation
- [Wallet Developer Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/index.html#//apple_ref/doc/uid/TP40012195)
### Determining activation state
- [enum PKPaymentPassActivationState](../pkpaymentpassactivationstate.md)
  Cases that indicate payment pass activation states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentpass/activationstate)*