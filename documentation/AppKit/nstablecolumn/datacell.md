# dataCell

**Framework**: AppKit  
**Kind**: property

The cell prototype used by the table column to draw individual cells.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var dataCell: Any { get set }
```

#### Discussion

You can use this property to control the font, alignment, and other text attributes for the table column contents.

You can also assign a cell that displays things other than text—for example, you can display images by setting the cell to [`NSImageCell`](nsimagecell.md).

> **Note**:  This property is only valid for cell-based table views.

 This property is only valid for cell-based table views.

## See Also

- [func dataCell(forRow: Int) -> Any](nstablecolumn/datacell(forrow:).md)
  Returns the cell object used to display values in the specified row of the table column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/datacell)*