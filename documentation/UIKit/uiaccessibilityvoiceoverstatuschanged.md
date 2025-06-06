# UIAccessibilityVoiceOverStatusChanged

**Framework**: UIKit  
**Kind**: var

A notification that UIKit posts when VoiceOver starts or stops.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
nonisolated
let UIAccessibilityVoiceOverStatusChanged: String
```

#### Discussion

This notification doesn’t include a parameter.

Use this notification to customize your application’s user interface (UI) for VoiceOver users. For example, if you display a UI element that briefly overlays other parts of your UI, you can make the display persistent for VoiceOver users, but allow it to disappear as designed for users who are not using VoiceOver. You can also use the [`isVoiceOverRunning`](uiaccessibility/isvoiceoverrunning.md) function to determine whether VoiceOver is currently running.

Observe this notification using the default notification center.

## See Also

- [static let announcement: UIAccessibility.Notification](uiaccessibility/notification/announcement.md)
  A notification that an app posts when it needs to convey an announcement to the assistive app.
- [static let voiceOverStatusDidChangeNotification: NSNotification.Name](uiaccessibility/voiceoverstatusdidchangenotification.md)
  A notification that UIKit posts when VoiceOver starts or stops.
- [static let announcementDidFinishNotification: NSNotification.Name](uiaccessibility/announcementdidfinishnotification.md)
  A notification that UIKit posts when the system finishes reading an announcement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityvoiceoverstatuschanged)*