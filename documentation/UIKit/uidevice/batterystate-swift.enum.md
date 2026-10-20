# UIDevice.BatteryState

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the battery power state of the device.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
enum BatteryState
```

```c
enum UIDeviceBatteryState : NSInteger;
```

#### Overview

These constants are used by the [`batteryState`](./batterystate-swift.property.md) property.

## Topics

### Constants
- [UIDevice.BatteryState.unknown](./batterystate-swift.enum/unknown.md)
  The battery state for the device can’t be determined.
- [UIDevice.BatteryState.unplugged](./batterystate-swift.enum/unplugged.md)
  The device isn’t plugged into power; the battery is discharging.
- [UIDevice.BatteryState.charging](./batterystate-swift.enum/charging.md)
  The device is plugged into power and the battery is less than 100% charged.
- [UIDevice.BatteryState.full](./batterystate-swift.enum/full.md)
  The device is plugged into power and the battery is 100% charged.
### Initializers
- [init?(rawValue: Int)](./batterystate-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the device battery state
- [var batteryLevel: Float](./batterylevel.md)
  The battery charge level for the device.
- [var isBatteryMonitoringEnabled: Bool](./isbatterymonitoringenabled.md)
  A Boolean value that indicates whether battery monitoring is enabled.
- [var batteryState: UIDevice.BatteryState](./batterystate-swift.property.md)
  The battery state for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/batterystate-swift.enum)*