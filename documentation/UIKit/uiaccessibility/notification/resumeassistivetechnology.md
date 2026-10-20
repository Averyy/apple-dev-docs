# resumeAssistiveTechnology

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that resumes an assistive app’s operations temporarily.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
nonisolated
static let resumeAssistiveTechnology: UIAccessibility.Notification
```

```c
extern const UIAccessibilityNotifications UIAccessibilityResumeAssistiveTechnologyNotification;
```

#### Discussion

When posting the notification, specify the assistive app to resume as the parameter. You must post this notification to balance out the previous posting of a [`pauseAssistiveTechnology`](./pauseassistivetechnology.md) notification. Post this notification using the [`post(notification:argument:)`](../post%28notification,argument%29.md) function.

## See Also

### Assistive apps
- [static let assistiveTouchStatusDidChangeNotification: NSNotification.Name](../assistivetouchstatusdidchangenotification.md)
  A notification that indicates a change in the status of AssistiveTouch.
- [static let guidedAccessStatusDidChangeNotification: NSNotification.Name](../guidedaccessstatusdidchangenotification.md)
  A notification that indicates when a Guided Access session starts or ends.
- [static let pauseAssistiveTechnology: UIAccessibility.Notification](./pauseassistivetechnology.md)
  A notification that pauses an assistive app’s operations temporarily.
- [UIAccessibility.AssistiveTechnologyIdentifier](../assistivetechnologyidentifier.md)
  Identifiers for assistive apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/notification/resumeassistivetechnology)*