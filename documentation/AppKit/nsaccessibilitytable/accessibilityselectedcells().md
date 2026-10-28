# accessibilitySelectedCells()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The currently selected cells for the table.

**Availability**:
- macOS

## Declaration

```swift
optional func accessibilitySelectedCells() -> [Any]?
```

```objc
- (NSArray *) accessibilitySelectedCells;
```

## Return Value

An array containing the currently selected cells for the table.

## Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilitySelectedCells`](../nsaccessibility-c.protocol/accessibilityselectedcells.md) property. Additionally, your class needs to send a [`selectedCellsChanged`](../nsaccessibility-swift.struct/notification/selectedcellschanged.md) notification whenever the table’s selected cells change.

## See Also

### Supporting Accessibility
- [func accessibilityColumnHeaderUIElements() -> [Any]?](./accessibilitycolumnheaderuielements%28%29.md)
  Returns the column header accessibility elements for the table.
- [func accessibilityColumns() -> [Any]?](./accessibilitycolumns%28%29.md)
  Returns the column accessibility elements for the table.
- [func accessibilityLabel() -> String?](./accessibilitylabel%28%29.md)
  Returns a short description of the table.
- [func accessibilityRowHeaderUIElements() -> [Any]?](./accessibilityrowheaderuielements%28%29.md)
  Returns the row header accessibility elements for the table.
- [func accessibilityRows() -> [any NSAccessibilityRow]?](./accessibilityrows%28%29.md)
  Returns the row accessibility elements for the table.
- [func accessibilitySelectedColumns() -> [Any]?](./accessibilityselectedcolumns%28%29.md)
  Returns the currently selected columns for the table.
- [func accessibilitySelectedRows() -> [any NSAccessibilityRow]?](./accessibilityselectedrows%28%29.md)
  Returns the currently selected rows for the table.
- [func accessibilityVisibleCells() -> [Any]?](./accessibilityvisiblecells%28%29.md)
  Returns the visible cells for the table.
- [func accessibilityVisibleColumns() -> [Any]?](./accessibilityvisiblecolumns%28%29.md)
  Returns the visible columns for the table.
- [func accessibilityVisibleRows() -> [any NSAccessibilityRow]?](./accessibilityvisiblerows%28%29.md)
  Returns the visible rows for the table.
- [func setAccessibilitySelectedRows([any NSAccessibilityRow])](./setaccessibilityselectedrows%28_%29.md)
  Sets the table’s currently selected rows.
- [func accessibilityHeaderGroup() -> String?](./accessibilityheadergroup%28%29.md)
  Returns the header group for the table.
### Related Documentation
- [accessibilitySelectedCells](../nsaccessibility-c.protocol/accessibilityselectedcells.md)
  The currently selected cells for the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/accessibilityselectedcells())*