# batteryLevelDidChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification that posts when the battery level changes.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let batteryLevelDidChangeNotification: NSNotification.Name
```

## Mentions

- [Processing queued notifications](processing-queued-notifications.md)

#### Discussion

For this notification to be sent, you must set the [`isBatteryMonitoringEnabled`](uidevice/isbatterymonitoringenabled.md) property to [`true`](https://developer.apple.com/documentation/Swift/true).

Notifications for battery level change are sent no more frequently than once per minute. Don’t attempt to calculate battery drainage rate or battery time remaining; drainage rate can change frequently depending on built-in applications as well as your application.

You can obtain the battery level by getting the value of the [`batteryLevel`](uidevice/batterylevel.md) property.

## See Also

- [class let batteryStateDidChangeNotification: NSNotification.Name](uidevice/batterystatedidchangenotification.md)
  A notification that posts when battery state changes.
- [class let orientationDidChangeNotification: NSNotification.Name](uidevice/orientationdidchangenotification.md)
  A notification that posts when the orientation of the device changes.
- [class let proximityStateDidChangeNotification: NSNotification.Name](uidevice/proximitystatedidchangenotification.md)
  A notification that posts when the state of the proximity sensor changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/batteryleveldidchangenotification)*