# userNotificationCenter(_:shouldPresent:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate when the user notification center has decided not to present your notification.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
optional func userNotificationCenter(_ center: NSUserNotificationCenter, shouldPresent notification: NSUserNotification) -> Bool
```

```objc
- (BOOL) userNotificationCenter:(NSUserNotificationCenter *) center shouldPresentNotification:(NSUserNotification *) notification;
```

#### Return Value

[`true`](../../Swift/true.md) if the user notification should be displayed regardless; [`false`](../../Swift/false.md) otherwise.

## Parameters

- `center`: The user notification center.
- `notification`: The user notification object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate/usernotificationcenter(_:shouldpresent:))*