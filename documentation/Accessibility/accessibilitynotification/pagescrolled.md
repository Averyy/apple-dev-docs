# AccessibilityNotification.PageScrolled

**Framework**: Accessibility  
**Kind**: struct

A notification that an app posts when a scroll action completes.

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
struct PageScrolled
```

#### Overview

Include an announcement value, such as [`String`](https://developer.apple.com/documentation/Swift/String) or [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString), for an assistive app to announce. When an assistive app repeatedly receives the same scroll position value, it indicates to the user that scrolling can’t continue due to a border or boundary.

## Topics

### Creating a page scroll notification
- [init(String)](accessibilitynotification/pagescrolled/init(_:)-28520.md)
  Creates a page scroll notification with a string.
- [init(AttributedString)](accessibilitynotification/pagescrolled/init(_:)-39fee.md)
  Creates a page scroll notification with an attributed string value.
- [init(NSAttributedString)](accessibilitynotification/pagescrolled/init(_:)-2lkx.md)
  Creates a page scroll notification with an attributed string object.

## See Also

- [AccessibilityNotification.Announcement](accessibilitynotification/announcement.md)
  A notification that an app posts when it needs to convey an announcement to an assistive app.
- [AccessibilityNotification.LayoutChanged](accessibilitynotification/layoutchanged.md)
  A notification that an app posts when the layout of a screen changes.
- [AccessibilityNotification.ScreenChanged](accessibilitynotification/screenchanged.md)
  A notification that an app posts when a new view appears that occupies a major portion of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitynotification/pagescrolled)*