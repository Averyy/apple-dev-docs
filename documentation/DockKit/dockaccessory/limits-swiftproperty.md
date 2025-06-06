# limits

**Framework**: Dockkit  
**Kind**: property

Current limits for the axes of rotation and maximum angular velocity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
final var limits: DockAccessory.Limits { get throws }
```

#### Return Value

The pitch, yaw, and roll limit. Each value can be `nil` if it’s unsupported. See [`DockAccessory.Limits`](dockaccessory/limits-swift.struct.md) for more information.

#### Discussion

> **Note**: [`DockKitError.notConnected`](dockkiterror/notconnected.md) if the device has disconnected.

## See Also

- [var motionStates: DockAccessory.MotionStates](dockaccessory/motionstates-swift.property.md)
  Motion information from the dock accessory that includes current orientation and velocity of all axes.
- [DockAccessory.MotionState](dockaccessory/motionstate.md)
  An event that indicates the state of a dock accessory’s current position and speed.
- [DockAccessory.MotionStates](dockaccessory/motionstates-swift.struct.md)
  An asynchronous sequence of orientation and velocity updates from the device.
- [DockAccessory.Limits](dockaccessory/limits-swift.struct.md)
  Soft limits on multiple axes of rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/limits-swift.property)*