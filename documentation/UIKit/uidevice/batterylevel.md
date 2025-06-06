# batteryLevel

**Framework**: UIKit  
**Kind**: property

The battery charge level for the device.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var batteryLevel: Float { get }
```

#### Discussion

Battery level ranges from 0.0 (fully discharged) to 1.0 (100% charged). Before accessing this property, ensure that battery monitoring is enabled.

If battery monitoring is not enabled, battery state is [`UIDevice.BatteryState.unknown`](uidevice/batterystate-swift.enum/unknown.md) and the value of this property is –1.0.

## See Also

- [var isBatteryMonitoringEnabled: Bool](uidevice/isbatterymonitoringenabled.md)
  A Boolean value that indicates whether battery monitoring is enabled.
- [var batteryState: UIDevice.BatteryState](uidevice/batterystate-swift.property.md)
  The battery state for the device.
- [UIDevice.BatteryState](uidevice/batterystate-swift.enum.md)
  Constants that describe the battery power state of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/batterylevel)*