# announcement

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The announcement as a localized string.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static let announcement: NSAccessibility.NotificationUserInfoKey
```

```c
extern NSAccessibilityNotificationUserInfoKey const NSAccessibilityAnnouncementKey;
```

#### Discussion

This key is required for [`NSAccessibilityProtocol`](../../nsaccessibilityprotocol.md) and should be used in conjunction with [`priority`](./priority.md) to help assistive apps determine the importance of the announcement.

## See Also

### Constants
- [static let uiElements: NSAccessibility.NotificationUserInfoKey](./uielements.md)
  An array of elements for the notification.
- [static let priority: NSAccessibility.NotificationUserInfoKey](./priority.md)
  A priority level that can help an assistive app determine how to handle the corresponding notification.
- [enum NSAccessibilityPriorityLevel](../../nsaccessibilityprioritylevel.md)
  A data type for notification priority levels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/notificationuserinfokey/announcement)*