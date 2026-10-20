# openGLContext()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the OpenGL context used by the view.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func openGLContext() -> NSOpenGLContext!
```

```objc
- (NSOpenGLContext *) openGLContext;
```

#### Return Value

An `NSOpenGLContext` object.

#### Discussion

This context as a read-only object . Do not attempt to change any of its settings. If you subclass `QCView` so that you can perform custom OpenGL drawing, you’ll need to use this method to retrieve the view’s OpenGL context.

## See Also

### Related Documentation
- [func render(atTime: TimeInterval, arguments: [AnyHashable : Any]!) -> Bool](./render%28attime,arguments%29.md)
  Overrides to perform  your custom operations prior to or after rendering a frame of a composition.
### Working With OpenGL
- [func openGLPixelFormat() -> NSOpenGLPixelFormat!](./openglpixelformat%28%29.md)
  Returns the OpenGL pixel format used by the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/openglcontext())*