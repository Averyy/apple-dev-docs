# announcementDidFinishNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that UIKit posts when the system finishes reading an announcement.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
nonisolated
static let announcementDidFinishNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIAccessibilityAnnouncementDidFinishNotification;
```

## Discussion

The parameter is a dictionary with two keys, [`announcementStringValueUserInfoKey`](./announcementstringvalueuserinfokey.md) and [`announcementWasSuccessfulUserInfoKey`](./announcementwassuccessfuluserinfokey.md). Observe this notification using the default notification center.

## See Also

### VoiceOver
- [static let announcement: UIAccessibility.Notification](./notification/announcement.md)
  A notification that an app posts when it needs to convey an announcement to the assistive app.
- [static let voiceOverStatusDidChangeNotification: NSNotification.Name](./voiceoverstatusdidchangenotification.md)
  A notification that UIKit posts when VoiceOver starts or stops.
- [let UIAccessibilityVoiceOverStatusChanged: String](../uiaccessibilityvoiceoverstatuschanged.md)
  A notification that UIKit posts when VoiceOver starts or stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/announcementdidfinishnotification)*