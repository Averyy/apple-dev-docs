# addColumn(with:)

**Framework**: AppKit  
**Kind**: method

Adds a new column containing the array of views.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
func addColumn(with views: [NSView]) -> NSGridColumn
```

#### Return Value

The newly created grid column.

## See Also

- [func insertColumn(at: Int, with: [NSView]) -> NSGridColumn](nsgridview/insertcolumn(at:with:).md)
  Inserts the array of view objects at the specified index.
- [func removeColumn(at: Int)](nsgridview/removecolumn(at:).md)
  Removes the column from the grid view at the specified index.
- [func moveColumn(at: Int, to: Int)](nsgridview/movecolumn(at:to:).md)
  Moves the specified column to a new column location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/addcolumn(with:))*