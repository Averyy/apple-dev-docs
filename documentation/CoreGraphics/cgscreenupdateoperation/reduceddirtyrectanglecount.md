# reducedDirtyRectangleCount

**Framework**: Core Graphics  
**Kind**: property

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
static var reducedDirtyRectangleCount: CGScreenUpdateOperation { get }
```

#### Discussion

When presented as part of the requested operations to the function [`CGWaitForScreenUpdateRects(_:_:_:_:_:)`](cgwaitforscreenupdaterects(_:_:_:_:_:).md), specifies that the function should try to minimize the number of rectangles returned to represent the changed areas of the display.  The function may combine adjacent rectangles within a larger bounding rectangle, which may include unmodified areas of the display.

## See Also

- [static var refresh: CGScreenUpdateOperation](cgscreenupdateoperation/refresh.md)
  A screen-refresh operation.
- [static var move: CGScreenUpdateOperation](cgscreenupdateoperation/move.md)
  A screen-move operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgscreenupdateoperation/reduceddirtyrectanglecount)*