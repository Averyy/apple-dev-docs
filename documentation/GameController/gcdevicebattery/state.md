# GCDeviceBattery.State

**Framework**: Game Controller  
**Kind**: enum

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

## Topics

### States
- [GCDeviceBattery.State.unknown](gcdevicebattery/state/unknown.md)
  The state of the device’s battery is unknown.
- [GCDeviceBattery.State.discharging](gcdevicebattery/state/discharging.md)
  The device’s battery is discharging.
- [GCDeviceBattery.State.charging](gcdevicebattery/state/charging.md)
  The device’s battery has power and is charging, but isn’t fully charged.
- [GCDeviceBattery.State.full](gcdevicebattery/state/full.md)
  The device’s battery has power and is fully charged.
### Initializers
- [init?(rawValue: Int)](gcdevicebattery/state/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var batteryLevel: Float](gcdevicebattery/batterylevel.md)
  The charge level of a device’s battery.
- [var batteryState: GCDeviceBattery.State](gcdevicebattery/batterystate.md)
  The state of a device’s battery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicebattery/state)*