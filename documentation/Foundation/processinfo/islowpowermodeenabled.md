# isLowPowerModeEnabled

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates the current state of Low Power Mode.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isLowPowerModeEnabled: Bool { get }
```

#### Discussion

Users who wish to prolong their device’s battery life can enable Low Power Mode under Settings > Battery. In Low Power Mode, the system conserves battery life by enacting certain energy-saving measures, such as:

- Reducing CPU and GPU performance.
- Reducing screen brightness.
- Pausing discretionary and background activities.

Your app can query the [`isLowPowerModeEnabled`](processinfo/islowpowermodeenabled.md) property at any time to determine whether Low Power Mode is active.

Your app can also register to receive notifications when the Low Power Mode state of a device changes. To register for power state notifications, send the message [`addObserver(_:selector:name:object:)`](notificationcenter/addobserver(_:selector:name:object:).md) to the default notification center of your app (an instance of [`NotificationCenter`](notificationcenter.md)). Pass it a selector to call and a notification name of [`NSProcessInfoPowerStateDidChange`](nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange.md). When your app receives a notification of a power state change, query [`isLowPowerModeEnabled`](processinfo/islowpowermodeenabled.md) to determine the current power state. If Low Power Mode is active, take appropriate steps to reduce activity in your app. Otherwise, your app can resume normal operations.

For additional information, see [`React to Low Power Mode on iPhones`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/LowPowerMode.html#//apple_ref/doc/uid/TP40015243-CH31) in [`Energy Efficiency Guide for iOS Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/index.html#//apple_ref/doc/uid/TP40015243).

## See Also

- [static let NSProcessInfoPowerStateDidChange: NSNotification.Name](nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange.md)
  Posts when the power state of a device changes.
- [func addObserver(Any, selector: Selector, name: NSNotification.Name?, object: Any?)](notificationcenter/addobserver(_:selector:name:object:).md)
  Adds an entry to the notification center to call the provided selector with the notification.
- [class NotificationCenter](notificationcenter.md)
  A notification dispatch mechanism that enables the broadcast of information to registered observers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/islowpowermodeenabled)*