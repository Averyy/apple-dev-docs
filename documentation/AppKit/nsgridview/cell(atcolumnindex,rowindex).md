# cell(atColumnIndex:rowIndex:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the grid cell object at the specified column and row index.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func cell(atColumnIndex columnIndex: Int, rowIndex: Int) -> NSGridCell
```

```objc
- (NSGridCell *) cellAtColumnIndex:(NSInteger) columnIndex rowIndex:(NSInteger) rowIndex;
```

## See Also

### Creating and Merging Cells
- [func cell(for: NSView) -> NSGridCell?](./cell%28for%29.md)
  Returns the grid cell object that contains the given view or one of its ancestors.
- [func mergeCells(inHorizontalRange: NSRange, verticalRange: NSRange)](./mergecells%28inhorizontalrange,verticalrange%29.md)
  Expands the cell at the top-leading corner of the horizontal and vertical range to cover the entire area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/cell(atcolumnindex:rowindex:))*