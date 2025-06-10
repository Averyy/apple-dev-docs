# NSAccessibilityList

**Framework**: AppKit  
**Kind**: protocol

A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a list view.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSAccessibilityList : NSAccessibilityTable
```

#### Overview

Use this protocol when you want a user interface element to behave like a list—a view that displays a set of related records in a single-column table—in the accessibility hierarchy.

You can further enhance the adopting element by implementing any of the information properties or action methods that the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol declares.

> **Note**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

Although the [`NSAccessibilityList`](nsaccessibilitylist.md) protocol doesn’t declare any methods, it does conform to the [`NSAccessibilityTable`](nsaccessibilitytable.md) protocol. You may need to explicitly implement methods from any of the protocols that [`NSAccessibilityList`](nsaccessibilitylist.md) conforms to.

## Relationships

### Inherits From
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityGroup](nsaccessibilitygroup.md)
- [NSAccessibilityTable](nsaccessibilitytable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSAccessibilityTable](nsaccessibilitytable.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a table view.
- [protocol NSAccessibilityOutline](nsaccessibilityoutline.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as an outline view.
- [protocol NSAccessibilityRow](nsaccessibilityrow.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a row for a table, list, or outline view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitylist)*