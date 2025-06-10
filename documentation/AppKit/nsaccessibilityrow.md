# NSAccessibilityRow

**Framework**: AppKit  
**Kind**: protocol

A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a row for a table, list, or outline view.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSAccessibilityRow : NSAccessibilityGroup
```

#### Overview

You can further enhance the adopting element by implementing any of the information properties or action methods that the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol declares.

> **Note**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

## Topics

### Supporting Accessibility
- [func accessibilityDisclosureLevel() -> Int](nsaccessibilityrow/accessibilitydisclosurelevel.md)
  Returns the indention level for the row.
- [func accessibilityIndex() -> Int](nsaccessibilityrow/accessibilityindex.md)
  Returns the index for the row.

## Relationships

### Inherits From
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityGroup](nsaccessibilitygroup.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSTableRowView](nstablerowview.md)

## See Also

- [protocol NSAccessibilityTable](nsaccessibilitytable.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a table view.
- [protocol NSAccessibilityList](nsaccessibilitylist.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a list view.
- [protocol NSAccessibilityOutline](nsaccessibilityoutline.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as an outline view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityrow)*