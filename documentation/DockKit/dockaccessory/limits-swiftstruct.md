# DockAccessory.Limits

**Framework**: DockKit  
**Kind**: struct

Soft limits on multiple axes of rotation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct Limits
```

## Topics

### Creating limits
- [init(yaw: DockAccessory.Limits.Limit?, pitch: DockAccessory.Limits.Limit?, roll: DockAccessory.Limits.Limit?)](dockaccessory/limits-swift.struct/init(yaw:pitch:roll:).md)
  Creates the limit object.
### Specifying limits
- [DockAccessory.Limits.Limit](dockaccessory/limits-swift.struct/limit.md)
  A description of a limit placed on an axis of rotation.
### Getting properties
- [let pitch: DockAccessory.Limits.Limit?](dockaccessory/limits-swift.struct/pitch.md)
  The up and down limit.
- [let roll: DockAccessory.Limits.Limit?](dockaccessory/limits-swift.struct/roll.md)
  The side to side limit.
- [let yaw: DockAccessory.Limits.Limit?](dockaccessory/limits-swift.struct/yaw.md)
  The left and right limit.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [var motionStates: DockAccessory.MotionStates](dockaccessory/motionstates-swift.property.md)
  Motion information from the dock accessory that includes current orientation and velocity of all axes.
- [var limits: DockAccessory.Limits](dockaccessory/limits-swift.property.md)
  Current limits for the axes of rotation and maximum angular velocity.
- [DockAccessory.MotionState](dockaccessory/motionstate.md)
  An event that indicates the state of a dock accessory’s current position and speed.
- [DockAccessory.MotionStates](dockaccessory/motionstates-swift.struct.md)
  An asynchronous sequence of orientation and velocity updates from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/limits-swift.struct)*