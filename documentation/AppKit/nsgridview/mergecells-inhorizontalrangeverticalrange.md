# mergeCells(inHorizontalRange:verticalRange:)

**Framework**: AppKit  
**Kind**: method

Expands the cell at the top-leading corner of the horizontal and vertical range to cover the entire area.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
func mergeCells(inHorizontalRange hRange: NSRange, verticalRange vRange: NSRange)
```

#### Discussion

This function invalidates other cells in the range, and they no longer maintain their layout, constraints, or content views.  Cell merging has no effect on the base cell coordinate system of the grid view, and cell references within a merged region refer to the single merged cell.

Use this method to configure the grid geometry before installing views. If the cells being merged contain content views, only the top-leading views are kept.

## See Also

- [func cell(atColumnIndex: Int, rowIndex: Int) -> NSGridCell](nsgridview/cell(atcolumnindex:rowindex:).md)
  Returns the grid cell object at the specified column and row index.
- [func cell(for: NSView) -> NSGridCell?](nsgridview/cell(for:).md)
  Returns the grid cell object that contains the given view or one of its ancestors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/mergecells(inhorizontalrange:verticalrange:))*