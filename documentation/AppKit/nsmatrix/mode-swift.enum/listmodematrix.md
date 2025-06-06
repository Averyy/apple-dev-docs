# NSMatrix.Mode.listModeMatrix

**Framework**: AppKit  
**Kind**: case

[`NSCell`](nscell.md) objects are highlighted, but don’t track the mouse.

**Availability**:
- macOS ?+

## Declaration

```swift
case listModeMatrix
```

## See Also

- [NSMatrix.Mode.trackModeMatrix](nsmatrix/mode-swift.enum/trackmodematrix.md)
  The [`NSCell`](nscell.md) objects are asked to track the mouse with [`trackMouse(with:in:of:untilMouseUp:)`](nscell/trackmouse(with:in:of:untilmouseup:).md) whenever the cursor is inside their bounds. No highlighting is performed.
- [NSMatrix.Mode.highlightModeMatrix](nsmatrix/mode-swift.enum/highlightmodematrix.md)
  An [`NSCell`](nscell.md) is highlighted before it’s asked to track the mouse, then unhighlighted when it’s done tracking.
- [NSMatrix.Mode.radioModeMatrix](nsmatrix/mode-swift.enum/radiomodematrix.md)
  Selects no more than one [`NSCell`](nscell.md) at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/mode-swift.enum/listmodematrix)*