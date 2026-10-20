# reducedDirtyRectangleCount

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
static var reducedDirtyRectangleCount: CGScreenUpdateOperation { get }
```

```c
kCGScreenUpdateOperationReducedDirtyRectangleCount
```

#### Discussion

When presented as part of the requested operations to the function [`CGWaitForScreenUpdateRects(_:_:_:_:_:)`](../cgwaitforscreenupdaterects%28_,_,_,_,_%29.md), specifies that the function should try to minimize the number of rectangles returned to represent the changed areas of the display.  The function may combine adjacent rectangles within a larger bounding rectangle, which may include unmodified areas of the display.

## See Also

### Constants
- [static var refresh: CGScreenUpdateOperation](./refresh.md)
  A screen-refresh operation.
- [static var move: CGScreenUpdateOperation](./move.md)
  A screen-move operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgscreenupdateoperation/reduceddirtyrectanglecount)*