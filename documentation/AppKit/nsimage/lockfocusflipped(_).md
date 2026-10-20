# lockFocusFlipped(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Prepares the image to receive drawing commands using the specified flipped state.

**Availability**:
- macOS 10.6+ - Deprecated in 27.0

> **Deprecated**: Use [`init(size:flipped:drawingHandler:)`](./init%28size,flipped,drawinghandler%29.md) instead.

## Declaration

```swift
func lockFocusFlipped(_ flipped: Bool)
```

```objc
- (void) lockFocusFlipped:(BOOL) flipped;
```

## Parameters

- `flipped`: [`true`](../../Swift/true.md) if the drawing context should be flipped, otherwise [`false`](../../Swift/false.md).

## See Also

### Deprecated instance methods
- [func lockFocus()](./lockfocus%28%29.md)
  Prepares the image to receive drawing commands.
- [func unlockFocus()](./unlockfocus%28%29.md)
  Removes the focus from the image.
- [convenience init(iconRef: IconRef)](./init%28iconref%29.md)
  Initializes the image object with a Carbon-style icon resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/lockfocusflipped(_:))*