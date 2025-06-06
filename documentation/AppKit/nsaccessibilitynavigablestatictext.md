# NSAccessibilityNavigableStaticText

**Framework**: AppKit  
**Kind**: protocol

A role-based protocol that declares the minimum interface necessary for an accessibility element to act as navigable static text.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSAccessibilityNavigableStaticText : NSAccessibilityStaticText
```

#### Overview

Use this protocol when you want to represent larger blocks of text. The protocol allows users to navigate through the text a line at a time or a word at a time using an assistive app. For shorter pieces of text (for example, labels or headers), use the [`NSAccessibilityStaticText`](nsaccessibilitystatictext.md) protocol instead.

You can further enhance the adopting element by implementing any of the information properties or action methods that the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol declares.

> **Note**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

 Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

## Topics

### Supporting Accessibility
- [func accessibilityFrame(for: NSRange) -> NSRect](nsaccessibilitynavigablestatictext/accessibilityframe(for:).md)
  Returns the rectangle that encloses the specified range of characters.
- [func accessibilityLine(for: Int) -> Int](nsaccessibilitynavigablestatictext/accessibilityline(for:).md)
  Returns the line number for the line that contains the specified character index.
- [func accessibilityRange(forLine: Int) -> NSRange](nsaccessibilitynavigablestatictext/accessibilityrange(forline:).md)
  Returns the range of characters in the specified line.
- [func accessibilityString(for: NSRange) -> String?](nsaccessibilitynavigablestatictext/accessibilitystring(for:).md)
  Returns the substring for the specified range.

## Relationships

### Inherits From
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityStaticText](nsaccessibilitystatictext.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSComboBox](nscombobox.md)
- [NSSearchField](nssearchfield.md)
- [NSSecureTextField](nssecuretextfield.md)
- [NSTextField](nstextfield.md)
- [NSTextView](nstextview.md)
- [NSTokenField](nstokenfield.md)

## See Also

- [protocol NSAccessibilityStaticText](nsaccessibilitystatictext.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as static text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitynavigablestatictext)*