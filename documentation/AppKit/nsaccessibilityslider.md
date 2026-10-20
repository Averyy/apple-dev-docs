# NSAccessibilitySlider

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a slider.

**Availability**:
- macOS

## Declaration

```swift
protocol NSAccessibilitySlider : NSAccessibilityElementProtocol
```

```objc
@protocol NSAccessibilitySlider <NSAccessibilityElement>
```

#### Overview

Use this protocol when you want a user interface element to behave like a slider—a control that represents a continuous range of numerical values with a knob that represents the currently selected value—in the accessibility hierarchy.

You can further enhance the adopting element by implementing any of the information properties or action methods that the [`NSAccessibilityProtocol`](./nsaccessibilityprotocol.md) protocol declares.

> **Explicit Implementation Required**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

## Topics

### Supporting Accessibility
- [func accessibilityLabel() -> String?](./nsaccessibilityslider/accessibilitylabel%28%29.md)
  Returns a short description of the slider.
- [func accessibilityPerformDecrement() -> Bool](./nsaccessibilityslider/accessibilityperformdecrement%28%29.md)
  Decrements the slider’s value.
- [func accessibilityPerformIncrement() -> Bool](./nsaccessibilityslider/accessibilityperformincrement%28%29.md)
  Increments the slider’s value.
- [func accessibilityValue() -> Any?](./nsaccessibilityslider/accessibilityvalue%28%29.md)
  Returns the slider’s value.

## Relationships

### Inherits From
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSSlider](./nsslider.md)

## See Also

### Value Controls
- [protocol NSAccessibilityStepper](./nsaccessibilitystepper.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a stepper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityslider)*