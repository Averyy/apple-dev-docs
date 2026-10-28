# draggedColumn

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The index of the column that the user is dragging.

**Availability**:
- macOS

## Declaration

```swift
var draggedColumn: Int { get }
```

```objc
@property (readonly) NSInteger draggedColumn;
```

## Discussion

If the user is dragging a column, this property contains the index of that column; otherwise, it contains `-1`.

## See Also

### Checking altered columns
- [var draggedDistance: CGFloat](./draggeddistance.md)
  The horizontal distance that the user has dragged a column.
- [var resizedColumn: Int](./resizedcolumn.md)
  The index of the column that the user is resizing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheaderview/draggedcolumn)*