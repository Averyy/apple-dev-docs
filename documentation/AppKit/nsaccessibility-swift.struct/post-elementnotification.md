# post(element:notification:)

**Framework**: AppKit  
**Kind**: method

Sends a notification to any observing assistive apps.

**Availability**:
- macOS ?+

## Declaration

```swift
static func post(element: Any, notification: NSAccessibility.Notification)
```

#### Discussion

Sends `notification` to any assistive applications that register to receive the notification from the user interface object `element` in your app. Accessibility notifications require special handling, so they can’t post using [`NotificationCenter`](https://developer.apple.com/documentation/foundation/notificationcenter).

## See Also

- [static func post(element: Any, notification: NSAccessibility.Notification, userInfo: [NSAccessibility.NotificationUserInfoKey : Any]?)](nsaccessibility-swift.struct/post(element:notification:userinfo:).md)
  Sends a notification and an optional user info dictionary to any observing assistive apps.
- [static func raiseBadArgumentException(Any!, NSAccessibility.Attribute!, Any!)](nsaccessibility-swift.struct/raisebadargumentexception(_:_:_:).md)
  Raises an error if the parameter is the wrong type or has an illegal value


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:))*