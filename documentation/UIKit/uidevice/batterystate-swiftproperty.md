# batteryState

**Framework**: UIKit  
**Kind**: property

The battery state for the device.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var batteryState: UIDevice.BatteryState { get }
```

#### Discussion

The value for [`batteryState`](uidevice/batterystate-swift.property.md) is one of the constants in [`UIDevice.BatteryState`](uidevice/batterystate-swift.enum.md).

If battery monitoring is not enabled, the value of this property is [`UIDevice.BatteryState.unknown`](uidevice/batterystate-swift.enum/unknown.md).

## See Also

- [var batteryLevel: Float](uidevice/batterylevel.md)
  The battery charge level for the device.
- [var isBatteryMonitoringEnabled: Bool](uidevice/isbatterymonitoringenabled.md)
  A Boolean value that indicates whether battery monitoring is enabled.
- [UIDevice.BatteryState](uidevice/batterystate-swift.enum.md)
  Constants that describe the battery power state of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/batterystate-swift.property)*