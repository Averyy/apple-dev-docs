# batteryStateDidChangeNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that posts when battery state changes.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let batteryStateDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIDeviceBatteryStateDidChangeNotification;
```

## Mentions

- [Processing queued notifications](../processing-queued-notifications.md)

#### Discussion

For this notification to be sent, you must set the [`isBatteryMonitoringEnabled`](./isbatterymonitoringenabled.md) property to [`true`](../../Swift/true.md).

You can obtain the battery state by getting the value of the [`batteryState`](./batterystate-swift.property.md) property.

## See Also

### Managing notifications
- [class let batteryLevelDidChangeNotification: NSNotification.Name](./batteryleveldidchangenotification.md)
  A notification that posts when the battery level changes.
- [class let orientationDidChangeNotification: NSNotification.Name](./orientationdidchangenotification.md)
  A notification that posts when the orientation of the device changes.
- [class let proximityStateDidChangeNotification: NSNotification.Name](./proximitystatedidchangenotification.md)
  A notification that posts when the state of the proximity sensor changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/batterystatedidchangenotification)*