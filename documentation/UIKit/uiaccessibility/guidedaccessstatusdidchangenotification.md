# guidedAccessStatusDidChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification that indicates when a Guided Access session starts or ends.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
static let guidedAccessStatusDidChangeNotification: NSNotification.Name
```

#### Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

Use the [`isGuidedAccessEnabled`](uiaccessibility/isguidedaccessenabled.md) function to determine whether a Guided Access session is currently active.

## See Also

- [static let assistiveTouchStatusDidChangeNotification: NSNotification.Name](uiaccessibility/assistivetouchstatusdidchangenotification.md)
  A notification that indicates a change in the status of AssistiveTouch.
- [static let pauseAssistiveTechnology: UIAccessibility.Notification](uiaccessibility/notification/pauseassistivetechnology.md)
  A notification that pauses an assistive app’s operations temporarily.
- [static let resumeAssistiveTechnology: UIAccessibility.Notification](uiaccessibility/notification/resumeassistivetechnology.md)
  A notification that resumes an assistive app’s operations temporarily.
- [UIAccessibility.AssistiveTechnologyIdentifier](uiaccessibility/assistivetechnologyidentifier.md)
  Identifiers for assistive apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccessstatusdidchangenotification)*