# post(element:notification:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Sends a notification to any observing assistive apps.

**Availability**:
- macOS

## Declaration

```swift
static func post(element: Any, notification: NSAccessibility.Notification)
```

```c
extern void NSAccessibilityPostNotification(id element, NSAccessibilityNotificationName notification);
```

## Discussion

Sends `notification` to any assistive applications that register to receive the notification from the user interface object `element` in your app. Accessibility notifications require special handling, so they can’t post using [`NotificationCenter`](../../Foundation/notificationcenter.md).

## See Also

### Posting Notifications
- [static func post(element: Any, notification: NSAccessibility.Notification, userInfo: [NSAccessibility.NotificationUserInfoKey : Any]?)](./post%28element,notification,userinfo%29.md)
  Sends a notification and an optional user info dictionary to any observing assistive apps.
- [static func raiseBadArgumentException(Any!, NSAccessibility.Attribute!, Any!)](./raisebadargumentexception%28_,_,_%29.md)
  Raises an error if the parameter is the wrong type or has an illegal value


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:))*