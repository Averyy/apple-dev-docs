# orientationDidChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification that posts when the orientation of the device changes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+

## Declaration

```swift
nonisolated
class let orientationDidChangeNotification: NSNotification.Name
```

## Mentions

- [Processing queued notifications](processing-queued-notifications.md)

#### Discussion

You can obtain the new orientation by getting the value of the [`orientation`](uidevice/orientation.md) property.

## See Also

- [class let batteryLevelDidChangeNotification: NSNotification.Name](uidevice/batteryleveldidchangenotification.md)
  A notification that posts when the battery level changes.
- [class let batteryStateDidChangeNotification: NSNotification.Name](uidevice/batterystatedidchangenotification.md)
  A notification that posts when battery state changes.
- [class let proximityStateDidChangeNotification: NSNotification.Name](uidevice/proximitystatedidchangenotification.md)
  A notification that posts when the state of the proximity sensor changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/orientationdidchangenotification)*