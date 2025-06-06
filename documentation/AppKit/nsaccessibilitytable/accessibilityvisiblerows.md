# accessibilityVisibleRows()

**Framework**: AppKit  
**Kind**: method

Returns the visible rows for the table.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func accessibilityVisibleRows() -> [any NSAccessibilityRow]?
```

#### Return Value

An array containing the currently visible rows.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s [`accessibilityVisibleRows`](nsaccessibility-c.protocol/accessibilityvisiblerows.md) property.

## See Also

- [func accessibilityColumnHeaderUIElements() -> [Any]?](nsaccessibilitytable/accessibilitycolumnheaderuielements.md)
  Returns the column header accessibility elements for the table.
- [func accessibilityColumns() -> [Any]?](nsaccessibilitytable/accessibilitycolumns.md)
  Returns the column accessibility elements for the table.
- [func accessibilityLabel() -> String?](nsaccessibilitytable/accessibilitylabel.md)
  Returns a short description of the table.
- [func accessibilityRowHeaderUIElements() -> [Any]?](nsaccessibilitytable/accessibilityrowheaderuielements.md)
  Returns the row header accessibility elements for the table.
- [func accessibilityRows() -> [any NSAccessibilityRow]?](nsaccessibilitytable/accessibilityrows.md)
  Returns the row accessibility elements for the table.
- [func accessibilitySelectedCells() -> [Any]?](nsaccessibilitytable/accessibilityselectedcells.md)
  The currently selected cells for the table.
- [func accessibilitySelectedColumns() -> [Any]?](nsaccessibilitytable/accessibilityselectedcolumns.md)
  Returns the currently selected columns for the table.
- [func accessibilitySelectedRows() -> [any NSAccessibilityRow]?](nsaccessibilitytable/accessibilityselectedrows.md)
  Returns the currently selected rows for the table.
- [func accessibilityVisibleCells() -> [Any]?](nsaccessibilitytable/accessibilityvisiblecells.md)
  Returns the visible cells for the table.
- [func accessibilityVisibleColumns() -> [Any]?](nsaccessibilitytable/accessibilityvisiblecolumns.md)
  Returns the visible columns for the table.
- [func setAccessibilitySelectedRows([any NSAccessibilityRow])](nsaccessibilitytable/setaccessibilityselectedrows(_:).md)
  Sets the table’s currently selected rows.
- [func accessibilityHeaderGroup() -> String?](nsaccessibilitytable/accessibilityheadergroup.md)
  Returns the header group for the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/accessibilityvisiblerows())*