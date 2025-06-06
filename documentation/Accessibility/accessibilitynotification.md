# AccessibilityNotification

**Framework**: Accessibility  
**Kind**: enum

Types of accessibility notifications that an app can post.

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
enum AccessibilityNotification
```

#### Overview

Accessibility notifications provide a unified, multiplatform way for your app to convey information to someone using an assistive app. Your app can post these types of notifications:

-  to convey an announcement to an assistive app
-  to indicate when the layout of a screen changes
-  to indicate when a new view appears that occupies a major portion of the screen
-  to indicate when a scroll action completes

For announcement notifications, you can set a priority to specify the announcement’s importance relative to other announcements that are in the queue for an assistive app to speak. For more information, see [`AccessibilityNotification.Announcement`](accessibilitynotification/announcement.md).

## Topics

### Notifications
- [AccessibilityNotification.Announcement](accessibilitynotification/announcement.md)
  A notification that an app posts when it needs to convey an announcement to an assistive app.
- [AccessibilityNotification.LayoutChanged](accessibilitynotification/layoutchanged.md)
  A notification that an app posts when the layout of a screen changes.
- [AccessibilityNotification.ScreenChanged](accessibilitynotification/screenchanged.md)
  A notification that an app posts when a new view appears that occupies a major portion of the screen.
- [AccessibilityNotification.PageScrolled](accessibilitynotification/pagescrolled.md)
  A notification that an app posts when a scroll action completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitynotification)*