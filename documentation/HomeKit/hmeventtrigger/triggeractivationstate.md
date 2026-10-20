# triggerActivationState

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The current activation state of the trigger.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var triggerActivationState: HMEventTriggerActivationState { get }
```

```objc
@property (nonatomic, assign, readonly) HMEventTriggerActivationState triggerActivationState;
```

#### Discussion

Specifies whether the trigger is currently active, or describes the problem.

## See Also

### Querying trigger activation state
- [enum HMEventTriggerActivationState](../hmeventtriggeractivationstate.md)
  The activation state of an event trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/triggeractivationstate)*