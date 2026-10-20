# NSMatrix.Mode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants determine how [`NSCell`](../nscell.md) objects behave when an [`NSMatrix`](../nsmatrix.md) object is tracking the mouse.

**Availability**:
- macOS

## Declaration

```swift
enum Mode
```

```c
enum NSMatrixMode : NSUInteger;
```

## Topics

### Constants
- [NSMatrix.Mode.trackModeMatrix](./mode-swift.enum/trackmodematrix.md)
  The [`NSCell`](../nscell.md) objects are asked to track the mouse with [`trackMouse(with:in:of:untilMouseUp:)`](../nscell/trackmouse%28with,in,of,untilmouseup%29.md) whenever the cursor is inside their bounds. No highlighting is performed.
- [NSMatrix.Mode.highlightModeMatrix](./mode-swift.enum/highlightmodematrix.md)
  An [`NSCell`](../nscell.md) is highlighted before it’s asked to track the mouse, then unhighlighted when it’s done tracking.
- [NSMatrix.Mode.radioModeMatrix](./mode-swift.enum/radiomodematrix.md)
  Selects no more than one [`NSCell`](../nscell.md) at a time.
- [NSMatrix.Mode.listModeMatrix](./mode-swift.enum/listmodematrix.md)
  [`NSCell`](../nscell.md) objects are highlighted, but don’t track the mouse.
### Initializers
- [init?(rawValue: UInt)](./mode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/mode-swift.enum)*