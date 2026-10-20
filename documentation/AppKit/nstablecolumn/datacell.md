# dataCell

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The cell prototype used by the table column to draw individual cells.

**Availability**:
- macOS

> **Deprecated**: Cell-based table views are deprecated; use view-based table views instead. See [`tableView(_:viewFor:row:)`](../nstableviewdelegate/tableview%28_,viewfor,row%29.md) and [`view(atColumn:row:makeIfNecessary:)`](../nstableview/view%28atcolumn,row,makeifnecessary%29.md).

## Declaration

```swift
var dataCell: Any { get set }
```

```objc
@property (strong) id dataCell;
```

#### Discussion

You can use this property to control the font, alignment, and other text attributes for the table column contents.

You can also assign a cell that displays things other than text—for example, you can display images by setting the cell to [`NSImageCell`](../nsimagecell.md).

> **Note**:  This property is only valid for cell-based table views.

## See Also

### Deprecated methods
- [func dataCell(forRow: Int) -> Any](./datacell%28forrow%29.md)
  Returns the cell object used to display values in the specified row of the table column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/datacell)*