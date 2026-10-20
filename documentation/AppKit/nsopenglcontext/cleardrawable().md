# clearDrawable()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Disassociates the OpenGL context from its viewport.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use Metal or MetalKit.

## Declaration

```swift
func clearDrawable()
```

```objc
- (void) clearDrawable;
```

#### Discussion

This method disassociates the receiver from any associated `NSView` object. If the receiver is in full-screen or offscreen mode, it exits that mode.

## See Also

### Managing the Drawable Object
- [var view: NSView?](./view.md)
  Returns the OpenGL context’s view.
- [func update()](./update%28%29.md)
  Updates the OpenGL context’s drawable object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/cleardrawable())*