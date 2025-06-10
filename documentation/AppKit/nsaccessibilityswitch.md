# NSAccessibilitySwitch

**Framework**: AppKit  
**Kind**: protocol

A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a switch.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSAccessibilitySwitch : NSAccessibilityButton
```

#### Overview

Use this protocol when you want a user interface element to behave like a switch—a control that toggles between an on state and an off state—in the accessibility hierarchy.

You can further enhance the adopting element by implementing any of the information properties or action methods that the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol declares.

> **Note**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

## Topics

### Supporting Accessibility
- [func accessibilityPerformDecrement() -> Bool](nsaccessibilityswitch/accessibilityperformdecrement.md)
  Decrements the switch’s value.
- [func accessibilityPerformIncrement() -> Bool](nsaccessibilityswitch/accessibilityperformincrement.md)
  Increments the switch’s value.
- [func accessibilityValue() -> String?](nsaccessibilityswitch/accessibilityvalue.md)
  Returns the switch’s value.

## Relationships

### Inherits From
- [NSAccessibilityButton](nsaccessibilitybutton.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSSwitch](nsswitch.md)

## See Also

- [protocol NSAccessibilityButton](nsaccessibilitybutton.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a button.
- [protocol NSAccessibilityRadioButton](nsaccessibilityradiobutton.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a radio button.
- [protocol NSAccessibilityCheckBox](nsaccessibilitycheckbox.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a checkbox.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityswitch)*