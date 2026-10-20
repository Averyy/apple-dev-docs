# unlockFocus()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the focus from the image.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

> **Deprecated**: Use [`init(size:flipped:drawingHandler:)`](./init%28size,flipped,drawinghandler%29.md) instead.

## Declaration

```swift
func unlockFocus()
```

```objc
- (void) unlockFocus;
```

#### Discussion

This message must be sent after a successful [`lockFocus()`](./lockfocus%28%29.md) or [`lockFocusOnRepresentation:`](./lockfocusonrepresentation_.md) message and the completion of any intermediate drawing commands. This method restores the focus to the previous owner, if any.

Do not send this message if the preceding call to lock focus raised an `NSImageCacheException`.

## See Also

### Deprecated instance methods
- [func lockFocus()](./lockfocus%28%29.md)
  Prepares the image to receive drawing commands.
- [func lockFocusFlipped(Bool)](./lockfocusflipped%28_%29.md)
  Prepares the image to receive drawing commands using the specified flipped state.
- [convenience init(iconRef: IconRef)](./init%28iconref%29.md)
  Initializes the image object with a Carbon-style icon resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/unlockfocus())*