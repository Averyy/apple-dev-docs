# assistiveTouchStatusDidChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification that indicates a change in the status of AssistiveTouch.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
static let assistiveTouchStatusDidChangeNotification: NSNotification.Name
```

#### Discussion

The user must enable Guided Access for this notification to post.

## See Also

- [static let guidedAccessStatusDidChangeNotification: NSNotification.Name](uiaccessibility/guidedaccessstatusdidchangenotification.md)
  A notification that indicates when a Guided Access session starts or ends.
- [static let pauseAssistiveTechnology: UIAccessibility.Notification](uiaccessibility/notification/pauseassistivetechnology.md)
  A notification that pauses an assistive app’s operations temporarily.
- [static let resumeAssistiveTechnology: UIAccessibility.Notification](uiaccessibility/notification/resumeassistivetechnology.md)
  A notification that resumes an assistive app’s operations temporarily.
- [UIAccessibility.AssistiveTechnologyIdentifier](uiaccessibility/assistivetechnologyidentifier.md)
  Identifiers for assistive apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/assistivetouchstatusdidchangenotification)*