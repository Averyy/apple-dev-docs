# NSAccessibilityStepper

**Framework**: AppKit  
**Kind**: protocol

A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a stepper.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSAccessibilityStepper : NSAccessibilityElementProtocol
```

#### Overview

Use this protocol when you want a user interface element to behave like a stepper—a control with up and down arrow buttons for incrementing or decrementing a value—in the accessibility hierarchy.

You can further enhance the adopting element by implementing any of the information properties or action methods that the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol declares.

> **Note**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

## Topics

### Supporting Accessibility
- [func accessibilityLabel() -> String?](nsaccessibilitystepper/accessibilitylabel.md)
  Returns a short description of the stepper.
- [func accessibilityPerformDecrement() -> Bool](nsaccessibilitystepper/accessibilityperformdecrement.md)
  Decrements the stepper’s value.
- [func accessibilityPerformIncrement() -> Bool](nsaccessibilitystepper/accessibilityperformincrement.md)
  Increments the stepper’s value.
- [func accessibilityValue() -> Any?](nsaccessibilitystepper/accessibilityvalue.md)
  Returns the stepper’s value.

## Relationships

### Inherits From
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSStepper](nsstepper.md)

## See Also

- [protocol NSAccessibilitySlider](nsaccessibilityslider.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a slider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitystepper)*