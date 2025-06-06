# accessibilityCell(forColumn:row:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the cell at the specified column and row.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityCell(forColumn column: Int, row: Int) -> Any?
```

#### Return Value

The cell specified by the column and row indexes.

#### Discussion

This property is required for all elements that function as cell-based tables.

## Parameters

- `column`: The column index.
- `row`: The row index.

## See Also

- [func accessibilityColumnIndexRange() -> NSRange](nsaccessibilityprotocol/accessibilitycolumnindexrange.md)
  Returns the column index range of the cell.
- [func setAccessibilityColumnIndexRange(NSRange)](nsaccessibilityprotocol/setaccessibilitycolumnindexrange(_:).md)
  Sets the column index range of the cell.
- [func accessibilityRowIndexRange() -> NSRange](nsaccessibilityprotocol/accessibilityrowindexrange.md)
  Returns the row index range of the cell.
- [func setAccessibilityRowIndexRange(NSRange)](nsaccessibilityprotocol/setaccessibilityrowindexrange(_:).md)
  Sets the row index range of the cell.
- [func accessibilitySelectedCells() -> [Any]?](nsaccessibilityprotocol/accessibilityselectedcells.md)
  Returns the currently selected cells for the table.
- [func setAccessibilitySelectedCells([Any]?)](nsaccessibilityprotocol/setaccessibilityselectedcells(_:).md)
  Sets the currently selected cells for the table.
- [func accessibilityVisibleCells() -> [Any]?](nsaccessibilityprotocol/accessibilityvisiblecells.md)
  Returns the visible cells for the table.
- [func setAccessibilityVisibleCells([Any]?)](nsaccessibilityprotocol/setaccessibilityvisiblecells(_:).md)
  Sets the visible cells for the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilitycell(forcolumn:row:))*