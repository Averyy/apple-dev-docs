# post(element:notification:userInfo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Sends a notification and an optional user info dictionary to any observing assistive apps.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static func post(element: Any, notification: NSAccessibility.Notification, userInfo: [NSAccessibility.NotificationUserInfoKey : Any]?)
```

```c
extern void NSAccessibilityPostNotificationWithUserInfo(id element, NSAccessibilityNotificationName notification, NSDictionary<NSString *,id> *userInfo);
```

## Discussion

Sends `notification` and `userInfo` to any assistive apps that register to receive the notification from the UI object `element` in your app. The system restricts the `userInfo` dictionary values to the same values as it restricts the accessibility attributes. The `userInfo` dictionary can also be `nil` (most accessibility notifications don’t require it).

## See Also

### Posting Notifications
- [static func post(element: Any, notification: NSAccessibility.Notification)](./post%28element,notification%29.md)
  Sends a notification to any observing assistive apps.
- [static func raiseBadArgumentException(Any!, NSAccessibility.Attribute!, Any!)](./raisebadargumentexception%28_,_,_%29.md)
  Raises an error if the parameter is the wrong type or has an illegal value


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:userinfo:))*