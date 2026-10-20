# GCDeviceBattery.State

**Framework**: Game Controller  
**Kind**: enum  
**Role**: Enumeration

A state that indicates whether a device’s battery has power and is charging.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum State
```

```c
enum GCDeviceBatteryState : NSInteger;
```

## Topics

### States
- [GCDeviceBattery.State.unknown](./state/unknown.md)
  The state of the device’s battery is unknown.
- [GCDeviceBattery.State.discharging](./state/discharging.md)
  The device’s battery is discharging.
- [GCDeviceBattery.State.charging](./state/charging.md)
  The device’s battery has power and is charging, but isn’t fully charged.
- [GCDeviceBattery.State.full](./state/full.md)
  The device’s battery has power and is fully charged.
### Initializers
- [init?(rawValue: Int)](./state/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the battery level and state
- [var batteryLevel: Float](./batterylevel.md)
  The charge level of a device’s battery.
- [var batteryState: GCDeviceBattery.State](./batterystate.md)
  The state of a device’s battery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicebattery/state)*