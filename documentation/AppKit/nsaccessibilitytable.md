# NSAccessibilityTable

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a table view.

**Availability**:
- macOS

## Declaration

```swift
protocol NSAccessibilityTable : NSAccessibilityGroup
```

```objc
@protocol NSAccessibilityTable <NSAccessibilityGroup>
```

#### Overview

Use this protocol when you want a user interface element to behave like a table—a view that uses a row-and-column format to display a set of related records and their attributes—in the accessibility hierarchy.

You can further enhance the adopting element by implementing any of the information properties or action methods that the [`NSAccessibilityProtocol`](./nsaccessibilityprotocol.md) protocol declares.

> **Explicit Implementation Required**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

## Topics

### Supporting Accessibility
- [func accessibilityColumnHeaderUIElements() -> [Any]?](./nsaccessibilitytable/accessibilitycolumnheaderuielements%28%29.md)
  Returns the column header accessibility elements for the table.
- [func accessibilityColumns() -> [Any]?](./nsaccessibilitytable/accessibilitycolumns%28%29.md)
  Returns the column accessibility elements for the table.
- [func accessibilityLabel() -> String?](./nsaccessibilitytable/accessibilitylabel%28%29.md)
  Returns a short description of the table.
- [func accessibilityRowHeaderUIElements() -> [Any]?](./nsaccessibilitytable/accessibilityrowheaderuielements%28%29.md)
  Returns the row header accessibility elements for the table.
- [func accessibilityRows() -> [any NSAccessibilityRow]?](./nsaccessibilitytable/accessibilityrows%28%29.md)
  Returns the row accessibility elements for the table.
- [func accessibilitySelectedCells() -> [Any]?](./nsaccessibilitytable/accessibilityselectedcells%28%29.md)
  The currently selected cells for the table.
- [func accessibilitySelectedColumns() -> [Any]?](./nsaccessibilitytable/accessibilityselectedcolumns%28%29.md)
  Returns the currently selected columns for the table.
- [func accessibilitySelectedRows() -> [any NSAccessibilityRow]?](./nsaccessibilitytable/accessibilityselectedrows%28%29.md)
  Returns the currently selected rows for the table.
- [func accessibilityVisibleCells() -> [Any]?](./nsaccessibilitytable/accessibilityvisiblecells%28%29.md)
  Returns the visible cells for the table.
- [func accessibilityVisibleColumns() -> [Any]?](./nsaccessibilitytable/accessibilityvisiblecolumns%28%29.md)
  Returns the visible columns for the table.
- [func accessibilityVisibleRows() -> [any NSAccessibilityRow]?](./nsaccessibilitytable/accessibilityvisiblerows%28%29.md)
  Returns the visible rows for the table.
- [func setAccessibilitySelectedRows([any NSAccessibilityRow])](./nsaccessibilitytable/setaccessibilityselectedrows%28_%29.md)
  Sets the table’s currently selected rows.
- [func accessibilityHeaderGroup() -> String?](./nsaccessibilitytable/accessibilityheadergroup%28%29.md)
  Returns the header group for the table.

## Relationships

### Inherits From
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityGroup](./nsaccessibilitygroup.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [NSAccessibilityList](./nsaccessibilitylist.md)
- [NSAccessibilityOutline](./nsaccessibilityoutline.md)
### Conforming Types
- [NSOutlineView](./nsoutlineview.md)
- [NSTableView](./nstableview.md)

## See Also

### Lists
- [protocol NSAccessibilityList](./nsaccessibilitylist.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a list view.
- [protocol NSAccessibilityOutline](./nsaccessibilityoutline.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as an outline view.
- [protocol NSAccessibilityRow](./nsaccessibilityrow.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a row for a table, list, or outline view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitytable)*