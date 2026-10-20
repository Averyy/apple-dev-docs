# cell(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the grid cell object that contains the given view or one of its ancestors.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func cell(for view: NSView) -> NSGridCell?
```

```objc
- (NSGridCell *) cellForView:(NSView *) view;
```

## See Also

### Creating and Merging Cells
- [func cell(atColumnIndex: Int, rowIndex: Int) -> NSGridCell](./cell%28atcolumnindex,rowindex%29.md)
  Returns the grid cell object at the specified column and row index.
- [func mergeCells(inHorizontalRange: NSRange, verticalRange: NSRange)](./mergecells%28inhorizontalrange,verticalrange%29.md)
  Expands the cell at the top-leading corner of the horizontal and vertical range to cover the entire area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/cell(for:))*