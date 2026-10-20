# UIAccessibilityVoiceOverStatusChanged

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

A notification that UIKit posts when VoiceOver starts or stops.

**Availability**:
- iOS 4.0+ - Deprecated in 11.0 (renamed: UIAccessibility.voiceOverStatusDidChangeNotification)
- iPadOS 4.0+ - Deprecated in 11.0 (renamed: UIAccessibility.voiceOverStatusDidChangeNotification)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: UIAccessibility.voiceOverStatusDidChangeNotification)
- tvOS 9.0+ - Deprecated in 11.0 (renamed: UIAccessibility.voiceOverStatusDidChangeNotification)

> **Deprecated**: Use [`voiceOverStatusDidChangeNotification`](./uiaccessibility/voiceoverstatusdidchangenotification.md) instead.

## Declaration

```swift
nonisolated
let UIAccessibilityVoiceOverStatusChanged: String
```

```c
extern NSString * const UIAccessibilityVoiceOverStatusChanged;
```

#### Discussion

This notification doesn’t include a parameter.

Use this notification to customize your application’s user interface (UI) for VoiceOver users. For example, if you display a UI element that briefly overlays other parts of your UI, you can make the display persistent for VoiceOver users, but allow it to disappear as designed for users who are not using VoiceOver. You can also use the [`isVoiceOverRunning`](./uiaccessibility/isvoiceoverrunning.md) function to determine whether VoiceOver is currently running.

Observe this notification using the default notification center.

## See Also

### VoiceOver
- [static let announcement: UIAccessibility.Notification](./uiaccessibility/notification/announcement.md)
  A notification that an app posts when it needs to convey an announcement to the assistive app.
- [static let voiceOverStatusDidChangeNotification: NSNotification.Name](./uiaccessibility/voiceoverstatusdidchangenotification.md)
  A notification that UIKit posts when VoiceOver starts or stops.
- [static let announcementDidFinishNotification: NSNotification.Name](./uiaccessibility/announcementdidfinishnotification.md)
  A notification that UIKit posts when the system finishes reading an announcement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityvoiceoverstatuschanged)*