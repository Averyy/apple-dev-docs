# userNotificationCenter(_:shouldPresent:)

**Framework**: Foundation  
**Kind**: method

Sent to the delegate when the user notification center has decided not to present your notification.

**Availability**:
- macOS 10.8+

## Declaration

```swift
optional func userNotificationCenter(_ center: NSUserNotificationCenter, shouldPresent notification: NSUserNotification) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the user notification should be displayed regardless; [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## Parameters

- `center`: The user notification center.
- `notification`: The user notification object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate/usernotificationcenter(_:shouldpresent:))*