# AccessibilityNotification.Announcement

**Framework**: Accessibility  
**Kind**: struct

A notification that an app posts when it needs to convey an announcement to an assistive app.

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
struct Announcement
```

#### Overview

Include an announcement value, such as [`String`](https://developer.apple.com/documentation/Swift/String) or [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString), for an assistive app to announce.

Optionally, you can apply accessibility speech attributes to the announcement. For example, you can set a priority to specify the announcement’s importance relative to other announcements that are in the queue for an assistive app to speak. Announcement priorities give you more control over which announcements people need to hear, and which ones are acceptable to ignore or interrupt.

You specify an announcement priority using the [`accessibilitySpeechAnnouncementPriority`](https://developer.apple.com/documentation/Foundation/AttributeScopes/AccessibilityAttributes/accessibilitySpeechAnnouncementPriority) property. The following code shows an example of how to post an announcement notification with a high priority, which interrupts other speech and isn’t interruptible after it starts:

```swift
import SwiftUI

var body: some View {
    Button(action: {
        // Load the camera.
        openCamera()

        // Post an announcement to indicate the camera is done loading.
        var highPriorityAnnouncement = AttributedString("Camera active")
        highPriorityAnnouncement.accessibilitySpeechAnnouncementPriority = .high
        AccessibilityNotification.Announcement(highPriorityAnnouncement).post()
    }) {
        Image("Camera")
    }
}
```

## Topics

### Creating an announcement notification
- [init(String)](accessibilitynotification/announcement/init(_:)-621va.md)
  Creates an announcement notification with a string.
- [init(NSAttributedString)](accessibilitynotification/announcement/init(_:)-46byj.md)
  Creates an announcement notification with an attributed string value.
- [init(AttributedString)](accessibilitynotification/announcement/init(_:)-btpf.md)
  Creates an announcement notification with an attributed string object.

## See Also

- [AccessibilityNotification.LayoutChanged](accessibilitynotification/layoutchanged.md)
  A notification that an app posts when the layout of a screen changes.
- [AccessibilityNotification.ScreenChanged](accessibilitynotification/screenchanged.md)
  A notification that an app posts when a new view appears that occupies a major portion of the screen.
- [AccessibilityNotification.PageScrolled](accessibilitynotification/pagescrolled.md)
  A notification that an app posts when a scroll action completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitynotification/announcement)*