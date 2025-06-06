# prepareOpenGL()

**Framework**: AppKit  
**Kind**: method

Used by subclasses to initialize OpenGL state.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func prepareOpenGL()
```

#### Discussion

This method is called only once after the OpenGL context is made the current context. Subclasses that implement this method can use it to configure the Open GL state in preparation for drawing.

## See Also

- [func clearGLContext()](nsopenglview/clearglcontext.md)
  Releases the [`NSOpenGLContext`](nsopenglcontext.md) object associated with the view.
- [var openGLContext: NSOpenGLContext?](nsopenglview/openglcontext.md)
  The [`NSOpenGLContext`](nsopenglcontext.md) object associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/prepareopengl())*