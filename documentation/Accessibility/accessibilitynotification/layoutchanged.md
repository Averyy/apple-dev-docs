# AccessibilityNotification.LayoutChanged

**Framework**: Accessibility  
**Kind**: struct

A notification that an app posts when the layout of a screen changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct LayoutChanged
```

#### Overview

Optionally, include a parameter that contains the accessibility element for VoiceOver to move to after processing the notification.

## Topics

### Creating a layout change notification
- [init(Any?)](accessibilitynotification/layoutchanged/init(_:).md)
  Creates a layout change notification.

## See Also

- [AccessibilityNotification.Announcement](accessibilitynotification/announcement.md)
  A notification that an app posts when it needs to convey an announcement to an assistive app.
- [AccessibilityNotification.ScreenChanged](accessibilitynotification/screenchanged.md)
  A notification that an app posts when a new view appears that occupies a major portion of the screen.
- [AccessibilityNotification.PageScrolled](accessibilitynotification/pagescrolled.md)
  A notification that an app posts when a scroll action completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitynotification/layoutchanged)*