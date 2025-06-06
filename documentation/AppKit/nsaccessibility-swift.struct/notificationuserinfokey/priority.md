# priority

**Framework**: AppKit  
**Kind**: property

A priority level that can help an assistive app determine how to handle the corresponding notification.

**Availability**:
- macOS 10.9+

## Declaration

```swift
static let priority: NSAccessibility.NotificationUserInfoKey
```

#### Discussion

An example of using this key is VoiceOver which decides whether to speak an announcement immediately or after the current speech has finished. For a list of possible values, see [`NSAccessibilityPriorityLevel`](nsaccessibilityprioritylevel.md).

## See Also

- [static let announcement: NSAccessibility.NotificationUserInfoKey](nsaccessibility-swift.struct/notificationuserinfokey/announcement.md)
  The announcement as a localized string.
- [static let uiElements: NSAccessibility.NotificationUserInfoKey](nsaccessibility-swift.struct/notificationuserinfokey/uielements.md)
  An array of elements for the notification.
- [enum NSAccessibilityPriorityLevel](nsaccessibilityprioritylevel.md)
  A data type for notification priority levels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/notificationuserinfokey/priority)*