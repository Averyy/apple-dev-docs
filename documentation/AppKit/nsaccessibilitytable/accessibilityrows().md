# accessibilityRows()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the row accessibility elements for the table.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityRows() -> [any NSAccessibilityRow]?
```

```objc
- (NSArray<id<NSAccessibilityRow>> *) accessibilityRows;
```

## Return Value

An array containing the table’s row elements.

## Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilityRows`](../nsaccessibility-c.protocol/accessibilityrows.md) property.

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
- [func setAccessibilitySelectedRows([any NSAccessibilityRow])](./setaccessibilityselectedrows%28_%29.md)
  Sets the table’s currently selected rows.
- [func accessibilityHeaderGroup() -> String?](./accessibilityheadergroup%28%29.md)
  Returns the header group for the table.
### Related Documentation
- [accessibilityRows](../nsaccessibility-c.protocol/accessibilityrows.md)
  The row accessibility elements for the table or outline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/accessibilityrows())*