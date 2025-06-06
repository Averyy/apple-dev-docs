# setAccessibilitySelectedRows(_:)

**Framework**: AppKit  
**Kind**: method

Sets the table’s currently selected rows.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func setAccessibilitySelectedRows(_ selectedRows: [any NSAccessibilityRow])
```

#### Discussion

This method is the setter for the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s [`accessibilitySelectedRows`](nsaccessibility-c.protocol/accessibilityselectedrows.md) property. Implementing this method allows the user to change the selected row using an accessibility client. Additionally, your class needs to send a [`selectedRowsChanged`](nsaccessibility-swift.struct/notification/selectedrowschanged.md) notification whenever the table’s selected rows change.

## Parameters

- `selectedRows`: An array containing the row elements to be selected.

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
- [func accessibilityVisibleRows() -> [any NSAccessibilityRow]?](nsaccessibilitytable/accessibilityvisiblerows.md)
  Returns the visible rows for the table.
- [func accessibilityHeaderGroup() -> String?](nsaccessibilitytable/accessibilityheadergroup.md)
  Returns the header group for the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/setaccessibilityselectedrows(_:))*