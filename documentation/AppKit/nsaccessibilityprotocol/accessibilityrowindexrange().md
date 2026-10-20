# accessibilityRowIndexRange()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the row index range of the cell.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityRowIndexRange() -> NSRange
```

## See Also

### Configuring cell-based tables
- [func accessibilityColumnIndexRange() -> NSRange](./accessibilitycolumnindexrange%28%29.md)
  Returns the column index range of the cell.
- [func setAccessibilityColumnIndexRange(NSRange)](./setaccessibilitycolumnindexrange%28_%29.md)
  Sets the column index range of the cell.
- [func setAccessibilityRowIndexRange(NSRange)](./setaccessibilityrowindexrange%28_%29.md)
  Sets the row index range of the cell.
- [func accessibilitySelectedCells() -> [Any]?](./accessibilityselectedcells%28%29.md)
  Returns the currently selected cells for the table.
- [func setAccessibilitySelectedCells([Any]?)](./setaccessibilityselectedcells%28_%29.md)
  Sets the currently selected cells for the table.
- [func accessibilityVisibleCells() -> [Any]?](./accessibilityvisiblecells%28%29.md)
  Returns the visible cells for the table.
- [func setAccessibilityVisibleCells([Any]?)](./setaccessibilityvisiblecells%28_%29.md)
  Sets the visible cells for the table.
- [func accessibilityCell(forColumn: Int, row: Int) -> Any?](./accessibilitycell%28forcolumn,row%29.md)
  Returns the cell at the specified column and row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityrowindexrange())*