# NIMotionActivityState

**Framework**: Nearby Interaction  
**Kind**: enum

Motion states for a nearby accessory.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum NIMotionActivityState
```

#### Overview

Ranging accuracy improves when the framework knows whether the accessory is moving. Track your accessory’s motion using a method you choose and then use this enumeration to describe the motion among the available states. When the accessory’s motion state changes, inform the session by calling [`updateMotionState(_:forObjectWithToken:)`](nisession/updatemotionstate(_:forobjectwithtoken:).md)).

## Topics

### Specifying the motion state
- [NIMotionActivityState.stationary](nimotionactivitystate/stationary.md)
  A value that indicates the accessory isn’t moving.
- [NIMotionActivityState.moving](nimotionactivitystate/moving.md)
  A value that indicates the accessory is moving.
- [NIMotionActivityState.unknown](nimotionactivitystate/unknown.md)
  A value that indicates the accessory’s motion state is unknown.
### Creating a motion state
- [init?(rawValue: Int)](nimotionactivitystate/init(rawvalue:).md)
  Creates a motion state with the specified underlying value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Implementing spatial interactions with third-party accessories](implementing-spatial-interactions-with-third-party-accessories.md)
  Establish a connection with a nearby accessory to receive periodic measurements of its distance from the user.
- [class NINearbyAccessoryConfiguration](ninearbyaccessoryconfiguration.md)
  A configuration that enables interaction between iPhone and third-party accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nimotionactivitystate)*