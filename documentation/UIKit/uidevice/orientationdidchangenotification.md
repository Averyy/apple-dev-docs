# orientationDidChangeNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that posts when the orientation of the device changes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst

## Declaration

```swift
nonisolated
class let orientationDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIDeviceOrientationDidChangeNotification;
```

## Mentions

- [Processing queued notifications](../processing-queued-notifications.md)

#### Discussion

You can obtain the new orientation by getting the value of the [`orientation`](./orientation.md) property.

## See Also

### Managing notifications
- [class let batteryLevelDidChangeNotification: NSNotification.Name](./batteryleveldidchangenotification.md)
  A notification that posts when the battery level changes.
- [class let batteryStateDidChangeNotification: NSNotification.Name](./batterystatedidchangenotification.md)
  A notification that posts when battery state changes.
- [class let proximityStateDidChangeNotification: NSNotification.Name](./proximitystatedidchangenotification.md)
  A notification that posts when the state of the proximity sensor changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/orientationdidchangenotification)*