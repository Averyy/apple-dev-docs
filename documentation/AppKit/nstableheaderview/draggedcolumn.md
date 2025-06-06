# draggedColumn

**Framework**: AppKit  
**Kind**: property

The index of the column that the user is dragging.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var draggedColumn: Int { get }
```

#### Discussion

If the user is dragging a column, this property contains the index of that column; otherwise, it contains `-1`.

## See Also

- [var draggedDistance: CGFloat](nstableheaderview/draggeddistance.md)
  The horizontal distance that the user has dragged a column.
- [var resizedColumn: Int](nstableheaderview/resizedcolumn.md)
  The index of the column that the user is resizing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheaderview/draggedcolumn)*