# accessibilityVisibleRows()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the visible rows for the table.

**Availability**:
- macOS

## Declaration

```swift
optional func accessibilityVisibleRows() -> [any NSAccessibilityRow]?
```

```objc
- (NSArray<id<NSAccessibilityRow>> *) accessibilityVisibleRows;
```

#### Return Value

An array containing the currently visible rows.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilityVisibleRows`](../nsaccessibility-c.protocol/accessibilityvisiblerows.md) property.

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
- [func setAccessibilitySelectedRows([any NSAccessibilityRow])](./setaccessibilityselectedrows%28_%29.md)
  Sets the table’s currently selected rows.
- [func accessibilityHeaderGroup() -> String?](./accessibilityheadergroup%28%29.md)
  Returns the header group for the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/accessibilityvisiblerows())*