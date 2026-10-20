# NSMatrix.Mode.highlightModeMatrix

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

An [`NSCell`](../../nscell.md) is highlighted before it’s asked to track the mouse, then unhighlighted when it’s done tracking.

**Availability**:
- macOS

## Declaration

```swift
case highlightModeMatrix
```

```c
NSHighlightModeMatrix
```

## See Also

### Constants
- [NSMatrix.Mode.trackModeMatrix](./trackmodematrix.md)
  The [`NSCell`](../../nscell.md) objects are asked to track the mouse with [`trackMouse(with:in:of:untilMouseUp:)`](../../nscell/trackmouse%28with,in,of,untilmouseup%29.md) whenever the cursor is inside their bounds. No highlighting is performed.
- [NSMatrix.Mode.radioModeMatrix](./radiomodematrix.md)
  Selects no more than one [`NSCell`](../../nscell.md) at a time.
- [NSMatrix.Mode.listModeMatrix](./listmodematrix.md)
  [`NSCell`](../../nscell.md) objects are highlighted, but don’t track the mouse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/mode-swift.enum/highlightmodematrix)*