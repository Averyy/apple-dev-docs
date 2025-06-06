# clearGLContext()

**Framework**: AppKit  
**Kind**: method

Releases the [`NSOpenGLContext`](nsopenglcontext.md) object associated with the view.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func clearGLContext()
```

#### Discussion

If necessary, this method calls the [`clearDrawable()`](nsopenglcontext/cleardrawable().md) method of the context object before releasing it.

## See Also

- [func prepareOpenGL()](nsopenglview/prepareopengl.md)
  Used by subclasses to initialize OpenGL state.
- [var openGLContext: NSOpenGLContext?](nsopenglview/openglcontext.md)
  The [`NSOpenGLContext`](nsopenglcontext.md) object associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/clearglcontext())*