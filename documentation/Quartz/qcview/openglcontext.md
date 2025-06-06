# openGLContext()

**Framework**: Quartz  
**Kind**: method

Returns the OpenGL context used by the view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func openGLContext() -> NSOpenGLContext!
```

#### Return Value

An `NSOpenGLContext` object.

#### Discussion

This context as a read-only object . Do not attempt to change any of its settings. If you subclass `QCView` so that you can perform custom OpenGL drawing, you’ll need to use this method to retrieve the view’s OpenGL context.

## See Also

- [func render(atTime: TimeInterval, arguments: [AnyHashable : Any]!) -> Bool](qcview/render(attime:arguments:).md)
  Overrides to perform  your custom operations prior to or after rendering a frame of a composition.
- [func openGLPixelFormat() -> NSOpenGLPixelFormat!](qcview/openglpixelformat.md)
  Returns the OpenGL pixel format used by the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/openglcontext())*