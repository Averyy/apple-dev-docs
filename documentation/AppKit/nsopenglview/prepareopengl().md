# prepareOpenGL()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Used by subclasses to initialize OpenGL state.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use MTKView instead.

## Declaration

```swift
func prepareOpenGL()
```

```objc
- (void) prepareOpenGL;
```

## Discussion

This method is called only once after the OpenGL context is made the current context. Subclasses that implement this method can use it to configure the Open GL state in preparation for drawing.

## See Also

### Managing the NSOpenGLContext
- [func clearGLContext()](./clearglcontext%28%29.md)
  Releases the [`NSOpenGLContext`](../nsopenglcontext.md) object associated with the view.
- [var openGLContext: NSOpenGLContext?](./openglcontext.md)
  The [`NSOpenGLContext`](../nsopenglcontext.md) object associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/prepareopengl())*