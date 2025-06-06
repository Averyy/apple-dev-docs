# post(element:notification:userInfo:)

**Framework**: AppKit  
**Kind**: method

Sends a notification and an optional user info dictionary to any observing assistive apps.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static func post(element: Any, notification: NSAccessibility.Notification, userInfo: [NSAccessibility.NotificationUserInfoKey : Any]?)
```

#### Discussion

Sends `notification` and `userInfo` to any assistive apps that register to receive the notification from the UI object `element` in your app. The system restricts the `userInfo` dictionary values to the same values as it restricts the accessibility attributes. The `userInfo` dictionary can also be `nil` (most accessibility notifications don’t require it).

## See Also

- [static func post(element: Any, notification: NSAccessibility.Notification)](nsaccessibility-swift.struct/post(element:notification:).md)
  Sends a notification to any observing assistive apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/post(element:notification:userinfo:))*