# draggedDistance

**Framework**: AppKit  
**Kind**: property

The horizontal distance that the user has dragged a column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var draggedDistance: CGFloat { get }
```

#### Discussion

If the user is dragging a column, this property contains that column’s horizontal distance from its original position; otherwise, the property’s value is undefined.

## See Also

- [var draggedColumn: Int](nstableheaderview/draggedcolumn.md)
  The index of the column that the user is dragging.
- [var resizedColumn: Int](nstableheaderview/resizedcolumn.md)
  The index of the column that the user is resizing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheaderview/draggeddistance)*