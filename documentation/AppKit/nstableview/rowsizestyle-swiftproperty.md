# rowSizeStyle

**Framework**: AppKit  
**Kind**: property

The row size style (small, medium, large, or custom) used by the table view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var rowSizeStyle: NSTableView.RowSizeStyle { get set }
```

#### Discussion

To set the row size style on a row by row basis, set the value of this property to [`NSTableView.RowSizeStyle.custom`](nstableview/rowsizestyle-swift.enum/custom.md) and implement the [`tableView(_:heightOfRow:)`](nstableviewdelegate/tableview(_:heightofrow:).md) method in your table view delegate object.

The default value of this property is [`NSTableView.RowSizeStyle.custom`](nstableview/rowsizestyle-swift.enum/custom.md), which tells the table to use the [`rowHeight`](nstableview/rowheight.md) of the table instead of any pre-determined system values. Generally, `rowSizeStyle` should always be [`NSTableView.RowSizeStyle.custom`](nstableview/rowsizestyle-swift.enum/custom.md) except for “source lists”.

## See Also

- [var effectiveRowSizeStyle: NSTableView.RowSizeStyle](nstableview/effectiverowsizestyle.md)
  The effective row size style for the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/rowsizestyle-swift.property)*