# isBatteryMonitoringEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether battery monitoring is enabled.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isBatteryMonitoringEnabled: Bool { get set }
```

#### Discussion

Enable battery monitoring if your app needs to be notified of changes to the battery state, or if you want to check the battery charge level.

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false), which:

- Disables the posting of battery-related notifications
- Disables the ability to read battery charge level and battery state

## See Also

- [class let batteryLevelDidChangeNotification: NSNotification.Name](uidevice/batteryleveldidchangenotification.md)
  A notification that posts when the battery level changes.
- [class let batteryStateDidChangeNotification: NSNotification.Name](uidevice/batterystatedidchangenotification.md)
  A notification that posts when battery state changes.
- [var batteryLevel: Float](uidevice/batterylevel.md)
  The battery charge level for the device.
- [var batteryState: UIDevice.BatteryState](uidevice/batterystate-swift.property.md)
  The battery state for the device.
- [UIDevice.BatteryState](uidevice/batterystate-swift.enum.md)
  Constants that describe the battery power state of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/isbatterymonitoringenabled)*