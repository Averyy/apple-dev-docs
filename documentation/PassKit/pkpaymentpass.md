# PKPaymentPass

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that represents a provisioned payment card for in-app payments.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class PKPaymentPass
```

#### Overview

Use [`PKSecureElementPass`](pksecureelementpass.md) in apps instead of this class to implement a payment pass in apps with these these system versions:

- iOS 13.4 or later
- macOS 11.0 or later
- watchOS 6.2 or later
- Mac Catalyst 13.4 or later

## Topics

### Determining activation state
- [var activationState: PKPaymentPassActivationState](pkpaymentpass/activationstate.md)
  The current activation state of the pass.
- [enum PKPaymentPassActivationState](pkpaymentpassactivationstate.md)
  Cases that indicate payment pass activation states.

## Relationships

### Inherits From
- [PKSecureElementPass](pksecureelementpass.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKAddPaymentPassViewController](pkaddpaymentpassviewcontroller.md)
  Displays an interface that lets users add cards to Apple Pay from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentpass)*