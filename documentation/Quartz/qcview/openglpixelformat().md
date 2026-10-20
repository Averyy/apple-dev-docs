# openGLPixelFormat()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the OpenGL pixel format used by the view.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func openGLPixelFormat() -> NSOpenGLPixelFormat!
```

```objc
- (NSOpenGLPixelFormat *) openGLPixelFormat;
```

#### Return Value

An `NSOpenGLPixelFormat` object.

#### Discussion

This pixel format as a read-only object. Do not attempt to change any of its settings.

## See Also

### Working With OpenGL
- [func openGLContext() -> NSOpenGLContext!](./openglcontext%28%29.md)
  Returns the OpenGL context used by the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/openglpixelformat())*