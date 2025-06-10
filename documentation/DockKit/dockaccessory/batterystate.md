# DockAccessory.BatteryState

**Framework**: DockKit  
**Kind**: struct

A struct that represents an accessory battery state.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
struct BatteryState
```

#### Overview

This state is emitted when the battery level changes on accessory.

## Topics

### Operators
- [static func == (DockAccessory.BatteryState, DockAccessory.BatteryState) -> Bool](dockaccessory/batterystate/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [let batteryLevel: Double](dockaccessory/batterystate/batterylevel.md)
  Current charge percentage (0..1) of the battery
- [let chargeState: DockAccessory.BatteryChargeState](dockaccessory/batterystate/chargestate.md)
  An enumeration representing the charge state of the battery
- [var hashValue: Int](dockaccessory/batterystate/hashvalue.md)
  The hash value.
- [let lowBattery: Bool](dockaccessory/batterystate/lowbattery.md)
  True when accessory deems its charge to be too low to function properly
- [let name: String](dockaccessory/batterystate/name.md)
  The name of the battery that is sending this state from accessory
### Instance Methods
- [func hash(into: inout Hasher)](dockaccessory/batterystate/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](dockaccessory/batterystate/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/batterystate)*