# NSAccessibilityOutline

**Framework**: AppKit  
**Kind**: protocol

A role-based protocol that declares the minimum interface necessary for an accessibility element to act as an outline view.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSAccessibilityOutline : NSAccessibilityTable
```

#### Overview

Use this protocol when you want a user interface element to behave like an outline—a view that uses a row-and-column format to display hierarchical data that can expand and collapse—in the accessibility hierarchy.

You can further enhance the adopting element by implementing any of the information properties or action methods that the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol declares.

> **Note**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

 Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

Although the [`NSAccessibilityOutline`](nsaccessibilityoutline.md) protocol doesn’t declare any methods, it does conform to the [`NSAccessibilityTable`](nsaccessibilitytable.md) protocol. You may need to explicitly implement methods from any of the protocols that [`NSAccessibilityOutline`](nsaccessibilityoutline.md) conforms to.

## Relationships

### Inherits From
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityGroup](nsaccessibilitygroup.md)
- [NSAccessibilityTable](nsaccessibilitytable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSOutlineView](nsoutlineview.md)

## See Also

- [protocol NSAccessibilityTable](nsaccessibilitytable.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a table view.
- [protocol NSAccessibilityList](nsaccessibilitylist.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a list view.
- [protocol NSAccessibilityRow](nsaccessibilityrow.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a row for a table, list, or outline view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityoutline)*