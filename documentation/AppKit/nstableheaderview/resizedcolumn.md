# resizedColumn

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The index of the column that the user is resizing.

**Availability**:
- macOS

## Declaration

```swift
var resizedColumn: Int { get }
```

```objc
@property (readonly) NSInteger resizedColumn;
```

#### Discussion

If the user is resizing a column, this property contains the index of that column; otherwise, it contains `-1`.

## See Also

### Checking altered columns
- [var draggedColumn: Int](./draggedcolumn.md)
  The index of the column that the user is dragging.
- [var draggedDistance: CGFloat](./draggeddistance.md)
  The horizontal distance that the user has dragged a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheaderview/resizedcolumn)*