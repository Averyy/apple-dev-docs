# uiElements

**Framework**: AppKit  
**Kind**: property

An array of elements for the notification.

**Availability**:
- macOS 10.9+

## Declaration

```swift
static let uiElements: NSAccessibility.NotificationUserInfoKey
```

#### Discussion

The value is an array of accessibility elements for the notification. For example, in the [`layoutChanged`](nsaccessibility-swift.struct/notification/layoutchanged.md) notification, use this key to include an array of elements that you add or change.

## See Also

- [static let announcement: NSAccessibility.NotificationUserInfoKey](nsaccessibility-swift.struct/notificationuserinfokey/announcement.md)
  The announcement as a localized string.
- [static let priority: NSAccessibility.NotificationUserInfoKey](nsaccessibility-swift.struct/notificationuserinfokey/priority.md)
  A priority level that can help an assistive app determine how to handle the corresponding notification.
- [enum NSAccessibilityPriorityLevel](nsaccessibilityprioritylevel.md)
  A data type for notification priority levels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/notificationuserinfokey/uielements)*