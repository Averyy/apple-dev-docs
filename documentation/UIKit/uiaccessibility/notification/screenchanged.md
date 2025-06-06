# screenChanged

**Framework**: UIKit  
**Kind**: property

A notification that an app posts when a new view appears that occupies a major portion of the screen.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
nonisolated
static let screenChanged: UIAccessibility.Notification
```

#### Discussion

Post this notification using the [`post(notification:argument:)`](uiaccessibility/post(notification:argument:).md) function. Optionally, include a parameter that contains the accessibility element for VoiceOver to move to after processing the notification.

## See Also

- [static let layoutChanged: UIAccessibility.Notification](uiaccessibility/notification/layoutchanged.md)
  A notification that an app posts when the layout of a screen changes.
- [static let pageScrolled: UIAccessibility.Notification](uiaccessibility/notification/pagescrolled.md)
  A notification that an app posts when a scroll action completes.
- [static let switchControlStatusDidChangeNotification: NSNotification.Name](uiaccessibility/switchcontrolstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Switch Control setting changes.
- [static let elementFocusedNotification: NSNotification.Name](uiaccessibility/elementfocusednotification.md)
  A notification that UIKit posts when an assistive app focuses on an accessibility element.
- [static let reduceTransparencyStatusDidChangeNotification: NSNotification.Name](uiaccessibility/reducetransparencystatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Reduce Transparency setting changes.
- [static let buttonShapesEnabledStatusDidChangeNotification: NSNotification.Name](uiaccessibility/buttonshapesenabledstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Button Shapes setting changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/notification/screenchanged)*