# pageScrolled

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that an app posts when a scroll action completes.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
nonisolated
static let pageScrolled: UIAccessibility.Notification
```

```c
extern const UIAccessibilityNotifications UIAccessibilityPageScrolledNotification;
```

#### Discussion

This notification includes a parameter that is an [`NSString`](../../../Foundation/nsstring.md) object that contains a description of the new scroll position. An assistive app outputs the description string in the parameter.

Use this notification to provide custom information about the contents of the screen after a user performs a VoiceOver scroll gesture. For example, a tab-based app might provide a string like `Tab 3 of 5`, or an app that displays information in pages might provide a string like `Page 19 of 27`.

When an assistive app repeatedly receives the same scroll position string, it indicates to users that scrolling can’t continue due to a border or boundary.

Post this notification after the [`accessibilityScroll(_:)`](../../../ObjectiveC/nsobject-swift.class/accessibilityscroll%28_%29.md) method using the [`post(notification:argument:)`](../post%28notification,argument%29.md) function.

## See Also

### UI changes
- [static let screenChanged: UIAccessibility.Notification](./screenchanged.md)
  A notification that an app posts when a new view appears that occupies a major portion of the screen.
- [static let layoutChanged: UIAccessibility.Notification](./layoutchanged.md)
  A notification that an app posts when the layout of a screen changes.
- [static let switchControlStatusDidChangeNotification: NSNotification.Name](../switchcontrolstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Switch Control setting changes.
- [static let elementFocusedNotification: NSNotification.Name](../elementfocusednotification.md)
  A notification that UIKit posts when an assistive app focuses on an accessibility element.
- [static let reduceTransparencyStatusDidChangeNotification: NSNotification.Name](../reducetransparencystatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Reduce Transparency setting changes.
- [static let buttonShapesEnabledStatusDidChangeNotification: NSNotification.Name](../buttonshapesenabledstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Button Shapes setting changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/notification/pagescrolled)*