# clearGLContext()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Releases the [`NSOpenGLContext`](../nsopenglcontext.md) object associated with the view.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use MTKView instead.

## Declaration

```swift
func clearGLContext()
```

```objc
- (void) clearGLContext;
```

## Discussion

If necessary, this method calls the [`clearDrawable()`](../nsopenglcontext/cleardrawable%28%29.md) method of the context object before releasing it.

## See Also

### Managing the NSOpenGLContext
- [func prepareOpenGL()](./prepareopengl%28%29.md)
  Used by subclasses to initialize OpenGL state.
- [var openGLContext: NSOpenGLContext?](./openglcontext.md)
  The [`NSOpenGLContext`](../nsopenglcontext.md) object associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/clearglcontext())*