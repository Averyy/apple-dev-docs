# DockAccessory.BatteryChargeState

**Framework**: DockKit  
**Kind**: enum

The charging state of an accessory battery

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
enum BatteryChargeState
```

## Topics

### Operators
- [static func == (DockAccessory.BatteryChargeState, DockAccessory.BatteryChargeState) -> Bool](dockaccessory/batterychargestate/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [DockAccessory.BatteryChargeState.charging](dockaccessory/batterychargestate/charging.md)
  The battery is charging.
- [DockAccessory.BatteryChargeState.notChargeable](dockaccessory/batterychargestate/notchargeable.md)
  The battery is not a chargeable battery.
- [DockAccessory.BatteryChargeState.notCharging](dockaccessory/batterychargestate/notcharging.md)
  The battery is not charging.
### Instance Properties
- [var hashValue: Int](dockaccessory/batterychargestate/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](dockaccessory/batterychargestate/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](dockaccessory/batterychargestate/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/batterychargestate)*