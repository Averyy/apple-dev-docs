# mergeCells(inHorizontalRange:verticalRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Expands the cell at the top-leading corner of the horizontal and vertical range to cover the entire area.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func mergeCells(inHorizontalRange hRange: NSRange, verticalRange vRange: NSRange)
```

```objc
- (void) mergeCellsInHorizontalRange:(NSRange) hRange verticalRange:(NSRange) vRange;
```

#### Discussion

This function invalidates other cells in the range, and they no longer maintain their layout, constraints, or content views.  Cell merging has no effect on the base cell coordinate system of the grid view, and cell references within a merged region refer to the single merged cell.

Use this method to configure the grid geometry before installing views. If the cells being merged contain content views, only the top-leading views are kept.

## See Also

### Creating and Merging Cells
- [func cell(atColumnIndex: Int, rowIndex: Int) -> NSGridCell](./cell%28atcolumnindex,rowindex%29.md)
  Returns the grid cell object at the specified column and row index.
- [func cell(for: NSView) -> NSGridCell?](./cell%28for%29.md)
  Returns the grid cell object that contains the given view or one of its ancestors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/mergecells(inhorizontalrange:verticalrange:))*