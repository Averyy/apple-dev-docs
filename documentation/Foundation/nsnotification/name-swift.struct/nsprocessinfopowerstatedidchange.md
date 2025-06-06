# NSProcessInfoPowerStateDidChange

**Framework**: Foundation  
**Kind**: property

Posts when the power state of a device changes.

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
static let NSProcessInfoPowerStateDidChange: NSNotification.Name
```

#### Discussion

After your observer receives this notification, query the [`isLowPowerModeEnabled`](processinfo/islowpowermodeenabled.md) property to determine the current power state of the device. If Low Power Mode is active, take appropriate steps to reduce activity in your app. Otherwise, your app can resume normal operations.

The notification object is a [`ProcessInfo`](processinfo.md) instance.

## See Also

- [func addObserver(Any, selector: Selector, name: NSNotification.Name?, object: Any?)](notificationcenter/addobserver(_:selector:name:object:).md)
  Adds an entry to the notification center to call the provided selector with the notification.
- [var isLowPowerModeEnabled: Bool](processinfo/islowpowermodeenabled.md)
  A Boolean value that indicates the current state of Low Power Mode.
- [class NotificationCenter](notificationcenter.md)
  A notification dispatch mechanism that enables the broadcast of information to registered observers.
- [class let thermalStateDidChangeNotification: NSNotification.Name](processinfo/thermalstatedidchangenotification.md)
  Posts when the thermal state of the system changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange)*