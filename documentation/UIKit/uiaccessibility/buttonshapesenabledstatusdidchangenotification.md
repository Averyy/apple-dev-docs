# buttonShapesEnabledStatusDidChangeNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that UIKit posts when the system’s Button Shapes setting changes.

**Availability**:
- iOS 14.0+ - Deprecated in 26.1 (renamed: AccessibilitySettings.showBordersEnabledStatusDidChangeNotification)
- iPadOS 14.0+ - Deprecated in 26.1 (renamed: AccessibilitySettings.showBordersEnabledStatusDidChangeNotification)
- Mac Catalyst 14.0+ - Deprecated in 26.1 (renamed: AccessibilitySettings.showBordersEnabledStatusDidChangeNotification)
- tvOS 14.0+ - Deprecated in 26.1 (renamed: AccessibilitySettings.showBordersEnabledStatusDidChangeNotification)
- visionOS 1.0+ - Deprecated in 26.0 (renamed: AccessibilitySettings.showBordersEnabledStatusDidChangeNotification)

## Declaration

```swift
nonisolated
static let buttonShapesEnabledStatusDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIAccessibilityButtonShapesEnabledStatusDidChangeNotification;
```

#### Discussion

> **Related Sessions from WWDC20**:  Session 10020: [Make Your App Visually Accessible](https://developer.apple.com/wwdc20/10020)

## See Also

### UI changes
- [static let screenChanged: UIAccessibility.Notification](./notification/screenchanged.md)
  A notification that an app posts when a new view appears that occupies a major portion of the screen.
- [static let layoutChanged: UIAccessibility.Notification](./notification/layoutchanged.md)
  A notification that an app posts when the layout of a screen changes.
- [static let pageScrolled: UIAccessibility.Notification](./notification/pagescrolled.md)
  A notification that an app posts when a scroll action completes.
- [static let switchControlStatusDidChangeNotification: NSNotification.Name](./switchcontrolstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Switch Control setting changes.
- [static let elementFocusedNotification: NSNotification.Name](./elementfocusednotification.md)
  A notification that UIKit posts when an assistive app focuses on an accessibility element.
- [static let reduceTransparencyStatusDidChangeNotification: NSNotification.Name](./reducetransparencystatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Reduce Transparency setting changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/buttonshapesenabledstatusdidchangenotification)*