# resizedColumn

**Framework**: AppKit  
**Kind**: property

The index of the column that the user is resizing.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var resizedColumn: Int { get }
```

#### Discussion

If the user is resizing a column, this property contains the index of that column; otherwise, it contains `-1`.

## See Also

- [var draggedColumn: Int](nstableheaderview/draggedcolumn.md)
  The index of the column that the user is dragging.
- [var draggedDistance: CGFloat](nstableheaderview/draggeddistance.md)
  The horizontal distance that the user has dragged a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheaderview/resizedcolumn)*