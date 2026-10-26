# accessibilityVisibleCells

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The visible cells for the table.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (copy, nullable) NSArray * accessibilityVisibleCells;
```

#### Discussion

This property is required for all elements that act like cell-based tables.

## See Also

### Configuring cell-based tables
- [func accessibilityCell(forColumn: Int, row: Int) -> Any?](../nsaccessibilityprotocol/accessibilitycell%28forcolumn,row%29.md)
  Returns the cell at the specified column and row.
- [accessibilityColumnIndexRange](./accessibilitycolumnindexrange.md)
  The column index range of the cell.
- [accessibilityRowIndexRange](./accessibilityrowindexrange.md)
  The row index range of the cell.
- [accessibilitySelectedCells](./accessibilityselectedcells.md)
  The currently selected cells for the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilityvisiblecells)*