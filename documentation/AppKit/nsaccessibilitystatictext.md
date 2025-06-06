# NSAccessibilityStaticText

**Framework**: AppKit  
**Kind**: protocol

A role-based protocol that declares the minimum interface necessary for an accessibility element to act as static text.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSAccessibilityStaticText : NSAccessibilityElementProtocol
```

#### Overview

Use this protocol when you want to represent short pieces of text, such as headers or labels. For longer blocks of text, use the [`NSAccessibilityNavigableStaticText`](nsaccessibilitynavigablestatictext.md) protocol.

You can further enhance the adopting element by implementing any of the information properties or action methods that the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol declares.

> **Note**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

 Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

## Topics

### Supporting Accessibility
- [func accessibilityAttributedString(for: NSRange) -> NSAttributedString?](nsaccessibilitystatictext/accessibilityattributedstring(for:).md)
  Returns the attributed substring for the specified range of characters.
- [func accessibilityValue() -> String?](nsaccessibilitystatictext/accessibilityvalue.md)
  Returns the text that the accessibility element displays.
- [func accessibilityVisibleCharacterRange() -> NSRange](nsaccessibilitystatictext/accessibilityvisiblecharacterrange.md)
  Returns the range of visible characters in the document.

## Relationships

### Inherits From
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [NSAccessibilityNavigableStaticText](nsaccessibilitynavigablestatictext.md)
### Conforming Types
- [NSComboBox](nscombobox.md)
- [NSSearchField](nssearchfield.md)
- [NSSecureTextField](nssecuretextfield.md)
- [NSTextField](nstextfield.md)
- [NSTextView](nstextview.md)
- [NSTokenField](nstokenfield.md)

## See Also

- [protocol NSAccessibilityNavigableStaticText](nsaccessibilitynavigablestatictext.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as navigable static text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitystatictext)*