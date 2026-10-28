# isBatteryMonitoringEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether battery monitoring is enabled.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var isBatteryMonitoringEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isBatteryMonitoringEnabled) BOOL batteryMonitoringEnabled;
```

## Discussion

Enable battery monitoring if your app needs to be notified of changes to the battery state, or if you want to check the battery charge level.

The default value of this property is [`false`](../../Swift/false.md), which:

- Disables the posting of battery-related notifications
- Disables the ability to read battery charge level and battery state

## See Also

### Related Documentation
- [class let batteryLevelDidChangeNotification: NSNotification.Name](./batteryleveldidchangenotification.md)
  A notification that posts when the battery level changes.
- [class let batteryStateDidChangeNotification: NSNotification.Name](./batterystatedidchangenotification.md)
  A notification that posts when battery state changes.
### Getting the device battery state
- [var batteryLevel: Float](./batterylevel.md)
  The battery charge level for the device.
- [var batteryState: UIDevice.BatteryState](./batterystate-swift.property.md)
  The battery state for the device.
- [UIDevice.BatteryState](./batterystate-swift.enum.md)
  Constants that describe the battery power state of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/isbatterymonitoringenabled)*