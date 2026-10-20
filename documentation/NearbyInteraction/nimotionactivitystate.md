# NIMotionActivityState

**Framework**: Nearby Interaction  
**Kind**: enum  
**Role**: Enumeration

Motion states for a nearby accessory.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum NIMotionActivityState
```

```c
enum NIMotionActivityState : NSInteger;
```

#### Overview

Ranging accuracy improves when the framework knows whether the accessory is moving. Track your accessory’s motion using a method you choose and then use this enumeration to describe the motion among the available states. When the accessory’s motion state changes, inform the session by calling [`updateMotionState(_:forObjectWithToken:)`](./nisession/updatemotionstate%28_,forobjectwithtoken%29.md)).

## Topics

### Specifying the motion state
- [NIMotionActivityState.stationary](./nimotionactivitystate/stationary.md)
  A value that indicates the accessory isn’t moving.
- [NIMotionActivityState.moving](./nimotionactivitystate/moving.md)
  A value that indicates the accessory is moving.
- [NIMotionActivityState.unknown](./nimotionactivitystate/unknown.md)
  A value that indicates the accessory’s motion state is unknown.
### Creating a motion state
- [init?(rawValue: Int)](./nimotionactivitystate/init%28rawvalue%29.md)
  Creates a motion state with the specified underlying value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Providing accessory state information
- [func updateMotionState(NIMotionActivityState, forObjectWithToken: NIDiscoveryToken)](./nisession/updatemotionstate%28_,forobjectwithtoken%29.md)
  Notifies the session of an accessory’s motion state change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nimotionactivitystate)*