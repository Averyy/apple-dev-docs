# clearDrawable()

**Framework**: AppKit  
**Kind**: method

Disassociates the OpenGL context from its viewport.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func clearDrawable()
```

#### Discussion

This method disassociates the receiver from any associated `NSView` object. If the receiver is in full-screen or offscreen mode, it exits that mode.

## See Also

- [var view: NSView?](nsopenglcontext/view.md)
  Returns the OpenGL context’s view.
- [func update()](nsopenglcontext/update.md)
  Updates the OpenGL context’s drawable object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/cleardrawable())*