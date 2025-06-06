# proximityStateDidChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification that posts when the state of the proximity sensor changes.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let proximityStateDidChangeNotification: NSNotification.Name
```

## Mentions

- [Processing queued notifications](processing-queued-notifications.md)

#### Discussion

You can obtain the proximity state by getting the value of the [`proximityState`](uidevice/proximitystate.md) property.

## See Also

- [class let batteryLevelDidChangeNotification: NSNotification.Name](uidevice/batteryleveldidchangenotification.md)
  A notification that posts when the battery level changes.
- [class let batteryStateDidChangeNotification: NSNotification.Name](uidevice/batterystatedidchangenotification.md)
  A notification that posts when battery state changes.
- [class let orientationDidChangeNotification: NSNotification.Name](uidevice/orientationdidchangenotification.md)
  A notification that posts when the orientation of the device changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/proximitystatedidchangenotification)*