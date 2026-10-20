# accessibilityCell(forColumn:row:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the cell at the specified column and row.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityCell(forColumn column: Int, row: Int) -> Any?
```

```objc
- (id) accessibilityCellForColumn:(NSInteger) column row:(NSInteger) row;
```

#### Return Value

The cell specified by the column and row indexes.

#### Discussion

This property is required for all elements that function as cell-based tables.

## Parameters

- `column`: The column index.
- `row`: The row index.

## See Also

### Configuring cell-based tables
- [func accessibilityColumnIndexRange() -> NSRange](./accessibilitycolumnindexrange%28%29.md)
  Returns the column index range of the cell.
- [func setAccessibilityColumnIndexRange(NSRange)](./setaccessibilitycolumnindexrange%28_%29.md)
  Sets the column index range of the cell.
- [func accessibilityRowIndexRange() -> NSRange](./accessibilityrowindexrange%28%29.md)
  Returns the row index range of the cell.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilitycell(forcolumn:row:))*