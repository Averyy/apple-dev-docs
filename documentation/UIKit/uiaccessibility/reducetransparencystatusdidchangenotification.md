# reduceTransparencyStatusDidChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification that UIKit posts when the system’s Reduce Transparency setting changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
static let reduceTransparencyStatusDidChangeNotification: NSNotification.Name
```

#### Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

## See Also

- [static let screenChanged: UIAccessibility.Notification](uiaccessibility/notification/screenchanged.md)
  A notification that an app posts when a new view appears that occupies a major portion of the screen.
- [static let layoutChanged: UIAccessibility.Notification](uiaccessibility/notification/layoutchanged.md)
  A notification that an app posts when the layout of a screen changes.
- [static let pageScrolled: UIAccessibility.Notification](uiaccessibility/notification/pagescrolled.md)
  A notification that an app posts when a scroll action completes.
- [static let switchControlStatusDidChangeNotification: NSNotification.Name](uiaccessibility/switchcontrolstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Switch Control setting changes.
- [static let elementFocusedNotification: NSNotification.Name](uiaccessibility/elementfocusednotification.md)
  A notification that UIKit posts when an assistive app focuses on an accessibility element.
- [static let buttonShapesEnabledStatusDidChangeNotification: NSNotification.Name](uiaccessibility/buttonshapesenabledstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Button Shapes setting changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/reducetransparencystatusdidchangenotification)*