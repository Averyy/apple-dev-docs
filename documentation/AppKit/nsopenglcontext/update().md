# update()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Updates the OpenGL context’s drawable object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use Metal or MetalKit.

## Declaration

```swift
@MainActor
func update()
```

```objc
- (void) update;
```

## Discussion

Call this method whenever the receiver’s drawable object changes size or location. A multithreaded application must synchronize all threads that access the same drawable object and call [`update()`](./update%28%29.md) for each thread’s context serially.

## See Also

### Managing the Drawable Object
- [var view: NSView?](./view.md)
  Returns the OpenGL context’s view.
- [func clearDrawable()](./cleardrawable%28%29.md)
  Disassociates the OpenGL context from its viewport.
- [- setFullScreen](./setfullscreen.md)
  Sets the OpenGL context to full-screen mode.
- [- setOffScreen:width:height:rowbytes:](./setoffscreen_width_height_rowbytes_.md)
  Instructs the OpenGL context to render into an offscreen buffer with the specified attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/update())*