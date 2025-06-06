# NSMatrix.Mode.trackModeMatrix

**Framework**: AppKit  
**Kind**: case

The [`NSCell`](nscell.md) objects are asked to track the mouse with [`trackMouse(with:in:of:untilMouseUp:)`](nscell/trackmouse(with:in:of:untilmouseup:).md) whenever the cursor is inside their bounds. No highlighting is performed.

**Availability**:
- macOS ?+

## Declaration

```swift
case trackModeMatrix
```

## See Also

- [NSMatrix.Mode.highlightModeMatrix](nsmatrix/mode-swift.enum/highlightmodematrix.md)
  An [`NSCell`](nscell.md) is highlighted before it’s asked to track the mouse, then unhighlighted when it’s done tracking.
- [NSMatrix.Mode.radioModeMatrix](nsmatrix/mode-swift.enum/radiomodematrix.md)
  Selects no more than one [`NSCell`](nscell.md) at a time.
- [NSMatrix.Mode.listModeMatrix](nsmatrix/mode-swift.enum/listmodematrix.md)
  [`NSCell`](nscell.md) objects are highlighted, but don’t track the mouse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/mode-swift.enum/trackmodematrix)*