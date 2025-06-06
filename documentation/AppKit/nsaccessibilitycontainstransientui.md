# NSAccessibilityContainsTransientUI

**Framework**: AppKit  
**Kind**: protocol

A role-based protocol that declares the minimum interface necessary for an accessibility element to support dynamic UI changes.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSAccessibilityContainsTransientUI : NSAccessibilityElementProtocol
```

#### Overview

Use this protocol to support accessibility in a UI that changes dynamically—usually in response to mouse-hover events.

Use this protocol in addition to another role-based protocol. See [`Custom Controls`](custom-controls.md).

> **Note**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

 Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

## Topics

### Supporting Accessibility
- [func accessibilityPerformShowAlternateUI() -> Bool](nsaccessibilitycontainstransientui/accessibilityperformshowalternateui.md)
  Displays the accessibility element’s alternative UI.
- [func accessibilityPerformShowDefaultUI() -> Bool](nsaccessibilitycontainstransientui/accessibilityperformshowdefaultui.md)
  Returns to the accessibility element’s original UI.
- [func isAccessibilityAlternateUIVisible() -> Bool](nsaccessibilitycontainstransientui/isaccessibilityalternateuivisible.md)
  Returns a Boolean value that determines whether the accessibility element’s alternative UI is currently visible.

## Relationships

### Inherits From
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycontainstransientui)*