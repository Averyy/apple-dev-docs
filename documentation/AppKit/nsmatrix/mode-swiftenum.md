# NSMatrix.Mode

**Framework**: AppKit  
**Kind**: enum

These constants determine how [`NSCell`](nscell.md) objects behave when an [`NSMatrix`](nsmatrix.md) object is tracking the mouse.

**Availability**:
- macOS ?+

## Declaration

```swift
enum Mode
```

## Topics

### Constants
- [NSMatrix.Mode.trackModeMatrix](nsmatrix/mode-swift.enum/trackmodematrix.md)
  The [`NSCell`](nscell.md) objects are asked to track the mouse with [`trackMouse(with:in:of:untilMouseUp:)`](nscell/trackmouse(with:in:of:untilmouseup:).md) whenever the cursor is inside their bounds. No highlighting is performed.
- [NSMatrix.Mode.highlightModeMatrix](nsmatrix/mode-swift.enum/highlightmodematrix.md)
  An [`NSCell`](nscell.md) is highlighted before it’s asked to track the mouse, then unhighlighted when it’s done tracking.
- [NSMatrix.Mode.radioModeMatrix](nsmatrix/mode-swift.enum/radiomodematrix.md)
  Selects no more than one [`NSCell`](nscell.md) at a time.
- [NSMatrix.Mode.listModeMatrix](nsmatrix/mode-swift.enum/listmodematrix.md)
  [`NSCell`](nscell.md) objects are highlighted, but don’t track the mouse.
### Initializers
- [init?(rawValue: UInt)](nsmatrix/mode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/mode-swift.enum)*