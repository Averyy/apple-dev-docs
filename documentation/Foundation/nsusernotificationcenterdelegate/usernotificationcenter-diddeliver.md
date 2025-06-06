# userNotificationCenter(_:didDeliver:)

**Framework**: Foundation  
**Kind**: method

Sent to the delegate when a notification delivery date has arrived.

**Availability**:
- macOS 10.8+

## Declaration

```swift
optional func userNotificationCenter(_ center: NSUserNotificationCenter, didDeliver notification: NSUserNotification)
```

#### Discussion

This method is always called, regardless of your application state and even if you deliver the user notification yourself using [`deliver(_:)`](nsusernotificationcenter/deliver(_:).md).

This delegate method is invoked before the [`userNotificationCenter(_:shouldPresent:)`](nsusernotificationcenterdelegate/usernotificationcenter(_:shouldpresent:).md) delegate method.

## Parameters

- `center`: The user notification center.
- `notification`: The user notification object.

## See Also

- [func userNotificationCenter(NSUserNotificationCenter, didActivate: NSUserNotification)](nsusernotificationcenterdelegate/usernotificationcenter(_:didactivate:).md)
  Sent to the delegate when a user clicks on a user notification presented by the user notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate/usernotificationcenter(_:diddeliver:))*