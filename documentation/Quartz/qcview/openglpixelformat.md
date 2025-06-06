# openGLPixelFormat()

**Framework**: Quartz  
**Kind**: method

Returns the OpenGL pixel format used by the view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func openGLPixelFormat() -> NSOpenGLPixelFormat!
```

#### Return Value

An `NSOpenGLPixelFormat` object.

#### Discussion

This pixel format as a read-only object. Do not attempt to change any of its settings.

## See Also

- [func openGLContext() -> NSOpenGLContext!](qcview/openglcontext.md)
  Returns the OpenGL context used by the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/openglpixelformat())*