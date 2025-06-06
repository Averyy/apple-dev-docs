# cell(atColumnIndex:rowIndex:)

**Framework**: AppKit  
**Kind**: method

Returns the grid cell object at the specified column and row index.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
func cell(atColumnIndex columnIndex: Int, rowIndex: Int) -> NSGridCell
```

## See Also

- [func cell(for: NSView) -> NSGridCell?](nsgridview/cell(for:).md)
  Returns the grid cell object that contains the given view or one of its ancestors.
- [func mergeCells(inHorizontalRange: NSRange, verticalRange: NSRange)](nsgridview/mergecells(inhorizontalrange:verticalrange:).md)
  Expands the cell at the top-leading corner of the horizontal and vertical range to cover the entire area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/cell(atcolumnindex:rowindex:))*