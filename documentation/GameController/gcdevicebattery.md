# GCDeviceBattery

**Framework**: Game Controller  
**Kind**: class

The charge level and state of a device’s battery.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class GCDeviceBattery
```

#### Overview

Use this class to display the state of a device’s battery to a player.

## Topics

### Getting the battery level and state
- [var batteryLevel: Float](gcdevicebattery/batterylevel.md)
  The charge level of a device’s battery.
- [var batteryState: GCDeviceBattery.State](gcdevicebattery/batterystate.md)
  The state of a device’s battery.
- [GCDeviceBattery.State](gcdevicebattery/state.md)
  A state that indicates whether a device’s battery has power and is charging.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Input](input.md)
  Receive controller input in the way that best integrates with the flow of your game or game engine.
- [class GCMotion](gcmotion.md)
  A controller profile that supports orientation and motion.
- [class GCDeviceHaptics](gcdevicehaptics.md)
  The locations of haptic actuators on a game controller.
- [class GCDeviceLight](gcdevicelight.md)
  The colored light on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicebattery)*