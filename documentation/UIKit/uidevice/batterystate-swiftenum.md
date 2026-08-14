# UIDevice.BatteryState

**Framework**: UIKit  
**Kind**: enum

Constants that describe the battery power state of the device.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
enum BatteryState
```

#### Overview

These constants are used by the [`batteryState`](uidevice/batterystate-swift.property.md) property.

## Topics

### Constants
- [UIDevice.BatteryState.unknown](uidevice/batterystate-swift.enum/unknown.md)
  The battery state for the device can’t be determined.
- [UIDevice.BatteryState.unplugged](uidevice/batterystate-swift.enum/unplugged.md)
  The device isn’t plugged into power; the battery is discharging.
- [UIDevice.BatteryState.charging](uidevice/batterystate-swift.enum/charging.md)
  The device is plugged into power and the battery is less than 100% charged.
- [UIDevice.BatteryState.full](uidevice/batterystate-swift.enum/full.md)
  The device is plugged into power and the battery is 100% charged.
### Initializers
- [init?(rawValue: Int)](uidevice/batterystate-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var batteryLevel: Float](uidevice/batterylevel.md)
  The battery charge level for the device.
- [var isBatteryMonitoringEnabled: Bool](uidevice/isbatterymonitoringenabled.md)
  A Boolean value that indicates whether battery monitoring is enabled.
- [var batteryState: UIDevice.BatteryState](uidevice/batterystate-swift.property.md)
  The battery state for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/batterystate-swift.enum)*