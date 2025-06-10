# motionStates

**Framework**: DockKit  
**Kind**: property

Motion information from the dock accessory that includes current orientation and velocity of all axes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
final var motionStates: DockAccessory.MotionStates { get throws }
```

#### Return Value

Motion states with the current orientation and velocity. The dock accessory controls the rate at which the state changes.

#### Discussion

This value holds a [`DockAccessory.MotionStates`](dockaccessory/motionstates-swift.struct.md) object, an asynchronous iterator used to find the desired dock accessory.

> **Note**: [`DockKitError.notConnected`](dockkiterror/notconnected.md) if device is disconnected, or [`DockKitError.notSupportedByDevice`](dockkiterror/notsupportedbydevice.md) if device doesn’t support updates.

## See Also

- [var limits: DockAccessory.Limits](dockaccessory/limits-swift.property.md)
  Current limits for the axes of rotation and maximum angular velocity.
- [DockAccessory.MotionState](dockaccessory/motionstate.md)
  An event that indicates the state of a dock accessory’s current position and speed.
- [DockAccessory.MotionStates](dockaccessory/motionstates-swift.struct.md)
  An asynchronous sequence of orientation and velocity updates from the device.
- [DockAccessory.Limits](dockaccessory/limits-swift.struct.md)
  Soft limits on multiple axes of rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/motionstates-swift.property)*