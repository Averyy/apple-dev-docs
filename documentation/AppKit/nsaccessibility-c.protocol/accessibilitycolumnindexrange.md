# accessibilityColumnIndexRange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The column index range of the cell.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property NSRange accessibilityColumnIndexRange;
```

#### Discussion

This property contains the column’s starting index and index span in the table. Use this property in the elements representing a table’s cell.

## See Also

### Configuring cell-based tables
- [func accessibilityCell(forColumn: Int, row: Int) -> Any?](../nsaccessibilityprotocol/accessibilitycell%28forcolumn,row%29.md)
  Returns the cell at the specified column and row.
- [accessibilityRowIndexRange](./accessibilityrowindexrange.md)
  The row index range of the cell.
- [accessibilitySelectedCells](./accessibilityselectedcells.md)
  The currently selected cells for the table.
- [accessibilityVisibleCells](./accessibilityvisiblecells.md)
  The visible cells for the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilitycolumnindexrange)*