# cell(for:)

**Framework**: AppKit  
**Kind**: method

Returns the grid cell object that contains the given view or one of its ancestors.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
func cell(for view: NSView) -> NSGridCell?
```

## See Also

- [func cell(atColumnIndex: Int, rowIndex: Int) -> NSGridCell](nsgridview/cell(atcolumnindex:rowindex:).md)
  Returns the grid cell object at the specified column and row index.
- [func mergeCells(inHorizontalRange: NSRange, verticalRange: NSRange)](nsgridview/mergecells(inhorizontalrange:verticalrange:).md)
  Expands the cell at the top-leading corner of the horizontal and vertical range to cover the entire area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/cell(for:))*