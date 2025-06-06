# NSAccessibilityButton

**Framework**: AppKit  
**Kind**: protocol

A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a button.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSAccessibilityButton : NSAccessibilityElementProtocol
```

#### Overview

Use this protocol when you want a user interface element to behave like a button—a control that triggers an action when the user clicks it—in the accessibility hierarchy.

You can further enhance the adopting element by implementing any of the information properties or action methods that the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol declares.

> **Note**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

 Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

## Topics

### Supporting Accessibility
- [func accessibilityLabel() -> String?](nsaccessibilitybutton/accessibilitylabel.md)
  Returns a short description of the button.
- [func accessibilityPerformPress() -> Bool](nsaccessibilitybutton/accessibilityperformpress.md)
  Simulates clicking the button.

## Relationships

### Inherits From
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [NSAccessibilityCheckBox](nsaccessibilitycheckbox.md)
- [NSAccessibilityRadioButton](nsaccessibilityradiobutton.md)
- [NSAccessibilitySwitch](nsaccessibilityswitch.md)
### Conforming Types
- [NSButton](nsbutton.md)
- [NSPopUpButton](nspopupbutton.md)
- [NSStatusBarButton](nsstatusbarbutton.md)
- [NSSwitch](nsswitch.md)

## See Also

- [protocol NSAccessibilityRadioButton](nsaccessibilityradiobutton.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a radio button.
- [protocol NSAccessibilitySwitch](nsaccessibilityswitch.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a switch.
- [protocol NSAccessibilityCheckBox](nsaccessibilitycheckbox.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a checkbox.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitybutton)*