# NSAccessibilityLayoutArea

**Framework**: Appkit  
**Kind**: protocol

A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a layout area.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSAccessibilityLayoutArea : NSAccessibilityGroup
```

#### Overview

Use this protocol when you want to create a canvas that contains layout items.

You can further enhance the adopting element by implementing any of the information properties or action methods that the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol declares.

> **Note**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

## Topics

### Supporting Accessibility
- [func accessibilityChildren() -> [Any]?](nsaccessibilitylayoutarea/accessibilitychildren.md)
  Returns the accessibility element’s children in the accessibility hierarchy.
- [var accessibilityFocusedUIElement: Any](nsaccessibilitylayoutarea/accessibilityfocuseduielement.md)
  The child accessibility element with the current focus.
- [func accessibilityLabel() -> String](nsaccessibilitylayoutarea/accessibilitylabel.md)
  Returns a short description of the layout area.
- [func accessibilitySelectedChildren() -> [Any]?](nsaccessibilitylayoutarea/accessibilityselectedchildren.md)
  Returns the layout area’s currently selected children.

## Relationships

### Inherits From
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityGroup](nsaccessibilitygroup.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSAccessibilityLayoutItem](nsaccessibilitylayoutitem.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a layout item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nsaccessibilitylayoutarea)*