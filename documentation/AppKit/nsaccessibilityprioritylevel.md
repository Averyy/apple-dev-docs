# NSAccessibilityPriorityLevel

**Framework**: AppKit  
**Kind**: enum

A data type for notification priority levels.

**Availability**:
- macOS 10.9+

## Declaration

```swift
enum NSAccessibilityPriorityLevel
```

#### Overview

Use these priority levels as values for the [`priority`](nsaccessibility-swift.struct/notificationuserinfokey/priority.md) key.

## Topics

### Priority Levels
- [NSAccessibilityPriorityLevel.high](nsaccessibilityprioritylevel/high.md)
  The notification is a high priority.
- [NSAccessibilityPriorityLevel.medium](nsaccessibilityprioritylevel/medium.md)
  The notification is a medium priority.
- [NSAccessibilityPriorityLevel.low](nsaccessibilityprioritylevel/low.md)
  The notification is a low priority.
### Initializers
- [init?(rawValue: Int)](nsaccessibilityprioritylevel/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static let announcement: NSAccessibility.NotificationUserInfoKey](nsaccessibility-swift.struct/notificationuserinfokey/announcement.md)
  The announcement as a localized string.
- [static let uiElements: NSAccessibility.NotificationUserInfoKey](nsaccessibility-swift.struct/notificationuserinfokey/uielements.md)
  An array of elements for the notification.
- [static let priority: NSAccessibility.NotificationUserInfoKey](nsaccessibility-swift.struct/notificationuserinfokey/priority.md)
  A priority level that can help an assistive app determine how to handle the corresponding notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprioritylevel)*