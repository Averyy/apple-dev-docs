# announcement

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that an app posts when it needs to convey an announcement to the assistive app.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
nonisolated
static let announcement: UIAccessibility.Notification
```

```c
extern const UIAccessibilityNotifications UIAccessibilityAnnouncementNotification;
```

#### Discussion

This notification includes a parameter that is an [`NSString`](../../../Foundation/nsstring.md) object that contains the announcement. An assistive app outputs the announcement string in the parameter.

Use this notification to provide accessibility information about events that don’t update the app’s UI, or that update the UI only briefly.

Post this notification using the [`post(notification:argument:)`](../post%28notification,argument%29.md) function.

## See Also

### VoiceOver
- [static let voiceOverStatusDidChangeNotification: NSNotification.Name](../voiceoverstatusdidchangenotification.md)
  A notification that UIKit posts when VoiceOver starts or stops.
- [static let announcementDidFinishNotification: NSNotification.Name](../announcementdidfinishnotification.md)
  A notification that UIKit posts when the system finishes reading an announcement.
- [let UIAccessibilityVoiceOverStatusChanged: String](../../uiaccessibilityvoiceoverstatuschanged.md)
  A notification that UIKit posts when VoiceOver starts or stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/notification/announcement)*