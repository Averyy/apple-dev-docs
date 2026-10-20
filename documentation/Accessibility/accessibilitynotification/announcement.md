# AccessibilityNotification.Announcement

**Framework**: Accessibility  
**Kind**: struct  
**Role**: Structure

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

Include an announcement value, such as [`String`](../../Swift/string.md) or [`AttributedString`](../../Foundation/attributedstring.md), for an assistive app to announce.

Optionally, you can apply accessibility speech attributes to the announcement. For example, you can set a priority to specify the announcement’s importance relative to other announcements that are in the queue for an assistive app to speak. Announcement priorities give you more control over which announcements people need to hear, and which ones are acceptable to ignore or interrupt.

You specify an announcement priority using the [`accessibilitySpeechAnnouncementPriority`](../../Foundation/attributescopes/accessibilityattributes/accessibilityspeechannouncementpriority.md) property. The following code shows an example of how to post an announcement notification with a high priority, which interrupts other speech and isn’t interruptible after it starts:

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
- [init(String)](./announcement/init%28_%29-621va.md)
  Creates an announcement notification with a string.
- [init(NSAttributedString)](./announcement/init%28_%29-46byj.md)
  Creates an announcement notification with an attributed string value.
- [init(AttributedString)](./announcement/init%28_%29-btpf.md)
  Creates an announcement notification with an attributed string object.

## See Also

### Notifications
- [AccessibilityNotification.LayoutChanged](./layoutchanged.md)
  A notification that an app posts when the layout of a screen changes.
- [AccessibilityNotification.ScreenChanged](./screenchanged.md)
  A notification that an app posts when a new view appears that occupies a major portion of the screen.
- [AccessibilityNotification.PageScrolled](./pagescrolled.md)
  A notification that an app posts when a scroll action completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitynotification/announcement)*