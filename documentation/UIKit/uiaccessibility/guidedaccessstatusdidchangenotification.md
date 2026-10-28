# guidedAccessStatusDidChangeNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that indicates when a Guided Access session starts or ends.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
nonisolated
static let guidedAccessStatusDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIAccessibilityGuidedAccessStatusDidChangeNotification;
```

## Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

Use the [`isGuidedAccessEnabled`](./isguidedaccessenabled.md) property to determine whether the Guided Access setting is enabled.

## See Also

### Assistive apps
- [static let assistiveTouchStatusDidChangeNotification: NSNotification.Name](./assistivetouchstatusdidchangenotification.md)
  A notification that indicates a change in the status of AssistiveTouch.
- [static let pauseAssistiveTechnology: UIAccessibility.Notification](./notification/pauseassistivetechnology.md)
  A notification that pauses an assistive app’s operations temporarily.
- [static let resumeAssistiveTechnology: UIAccessibility.Notification](./notification/resumeassistivetechnology.md)
  A notification that resumes an assistive app’s operations temporarily.
- [UIAccessibility.AssistiveTechnologyIdentifier](./assistivetechnologyidentifier.md)
  Identifiers for assistive apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccessstatusdidchangenotification)*