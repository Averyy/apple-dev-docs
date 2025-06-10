# HMEventTriggerActivationState

**Framework**: HomeKit  
**Kind**: enum

The activation state of an event trigger.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum HMEventTriggerActivationState
```

## Topics

### Inspecting activation state
- [HMEventTriggerActivationState.disabled](hmeventtriggeractivationstate/disabled.md)
  Trigger is not activated.
- [HMEventTriggerActivationState.disabledNoCompatibleHomeHub](hmeventtriggeractivationstate/disablednocompatiblehomehub.md)
  Trigger is not active because there is no compatible home hub.
- [HMEventTriggerActivationState.disabledNoHomeHub](hmeventtriggeractivationstate/disablednohomehub.md)
  Trigger is not active because there is no home hub.
- [HMEventTriggerActivationState.disabledNoLocationServicesAuthorization](hmeventtriggeractivationstate/disablednolocationservicesauthorization.md)
  Trigger is not active because the user has not authorized use of location services.
- [HMEventTriggerActivationState.enabled](hmeventtriggeractivationstate/enabled.md)
  The trigger is currently active.
### Initializers
- [init?(rawValue: UInt)](hmeventtriggeractivationstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var triggerActivationState: HMEventTriggerActivationState](hmeventtrigger/triggeractivationstate.md)
  The current activation state of the trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtriggeractivationstate)*