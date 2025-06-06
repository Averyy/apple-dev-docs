# addRow(with:)

**Framework**: AppKit  
**Kind**: method

Adds an array of views to a new row.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
func addRow(with views: [NSView]) -> NSGridRow
```

#### Discussion

You can insert and remove rows and columns dynamically in a grid view. The grid is enlarged as needed to hold the specified views.

## See Also

- [func insertRow(at: Int, with: [NSView]) -> NSGridRow](nsgridview/insertrow(at:with:).md)
  Inserts the array of view objects into the grid view at the index.
- [func removeRow(at: Int)](nsgridview/removerow(at:).md)
  Removes the row from the grid view at the index.
- [func moveRow(at: Int, to: Int)](nsgridview/moverow(at:to:).md)
  Moves the specified row to the new row location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/addrow(with:))*