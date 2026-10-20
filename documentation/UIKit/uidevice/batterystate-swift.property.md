# batteryState

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The battery state for the device.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var batteryState: UIDevice.BatteryState { get }
```

```objc
@property (nonatomic, readonly) UIDeviceBatteryState batteryState;
```

#### Discussion

The value for [`batteryState`](./batterystate-swift.property.md) is one of the constants in [`UIDevice.BatteryState`](./batterystate-swift.enum.md).

If battery monitoring is not enabled, the value of this property is [`UIDevice.BatteryState.unknown`](./batterystate-swift.enum/unknown.md).

## See Also

### Getting the device battery state
- [var batteryLevel: Float](./batterylevel.md)
  The battery charge level for the device.
- [var isBatteryMonitoringEnabled: Bool](./isbatterymonitoringenabled.md)
  A Boolean value that indicates whether battery monitoring is enabled.
- [UIDevice.BatteryState](./batterystate-swift.enum.md)
  Constants that describe the battery power state of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/batterystate-swift.property)*