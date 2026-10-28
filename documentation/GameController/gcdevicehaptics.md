# GCDeviceHaptics

**Framework**: Game Controller  
**Kind**: class  
**Role**: Class

The locations of haptic actuators on a game controller.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class GCDeviceHaptics
```

```objc
@interface GCDeviceHaptics : NSObject
```

## Overview

Use this class to create a haptic engine with a specified locality. Any patterns you send to that engine play on the specified actuators.

> ❗ **Important**:  The [`supportsHaptics`](../CoreHaptics/chhapticdevicecapability/supportshaptics.md) property of the engine that returns from the [`createEngine(withLocality:)`](./gcdevicehaptics/createengine%28withlocality%29.md) method applies to the device, not the game controller. Use the [`supportedLocalities`](./gcdevicehaptics/supportedlocalities.md) method in this class to determine whether a game controller supports haptics.

## Topics

### Creating a haptics engine
- [func createEngine(withLocality: GCHapticsLocality) -> CHHapticEngine?](./gcdevicehaptics/createengine%28withlocality%29.md)
  Creates a haptics engine with the specified locality.
- [let GCHapticDurationInfinite: Float](./gchapticdurationinfinite.md)
  An infinite duration for a haptics event.
### Getting the localities
- [var supportedLocalities: Set<GCHapticsLocality>](./gcdevicehaptics/supportedlocalities.md)
  The locations of haptic actuators on the device.
- [struct GCHapticsLocality](./gchapticslocality.md)
  The location of one or more haptics actuators on a game controller.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Game controller profiles
- [Input](./input.md)
  Receive controller input in the way that best integrates with the flow of your game or game engine.
- [class GCMotion](./gcmotion.md)
  A controller profile that supports orientation and motion.
- [class GCDeviceBattery](./gcdevicebattery.md)
  The charge level and state of a device’s battery.
- [class GCDeviceLight](./gcdevicelight.md)
  The colored light on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicehaptics)*