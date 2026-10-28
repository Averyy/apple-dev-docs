# setAccessibilitySelectedRows(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the table’s currently selected rows.

**Availability**:
- macOS

## Declaration

```swift
optional func setAccessibilitySelectedRows(_ selectedRows: [any NSAccessibilityRow])
```

```objc
- (void) setAccessibilitySelectedRows:(NSArray<id<NSAccessibilityRow>> *) selectedRows;
```

## Discussion

This method is the setter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilitySelectedRows`](../nsaccessibility-c.protocol/accessibilityselectedrows.md) property. Implementing this method allows the user to change the selected row using an accessibility client. Additionally, your class needs to send a [`selectedRowsChanged`](../nsaccessibility-swift.struct/notification/selectedrowschanged.md) notification whenever the table’s selected rows change.

## Parameters

- `selectedRows`: An array containing the row elements to be selected.

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
- [func accessibilitySelectedCells() -> [Any]?](./accessibilityselectedcells%28%29.md)
  The currently selected cells for the table.
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
- [func accessibilityHeaderGroup() -> String?](./accessibilityheadergroup%28%29.md)
  Returns the header group for the table.
### Related Documentation
- [accessibilitySelectedRows](../nsaccessibility-c.protocol/accessibilityselectedrows.md)
  The currently selected rows for the table or outline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/setaccessibilityselectedrows(_:))*