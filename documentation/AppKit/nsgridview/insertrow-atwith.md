# insertRow(at:with:)

**Framework**: AppKit  
**Kind**: method

Inserts the array of view objects into the grid view at the index.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
func insertRow(at index: Int, with views: [NSView]) -> NSGridRow
```

## See Also

- [func addRow(with: [NSView]) -> NSGridRow](nsgridview/addrow(with:).md)
  Adds an array of views to a new row.
- [func removeRow(at: Int)](nsgridview/removerow(at:).md)
  Removes the row from the grid view at the index.
- [func moveRow(at: Int, to: Int)](nsgridview/moverow(at:to:).md)
  Moves the specified row to the new row location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/insertrow(at:with:))*