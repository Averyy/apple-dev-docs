# openGLPixelFormat

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Provides access to the layer’s associated OpenGL pixel format.

**Availability**:
- macOS 10.6+ - Deprecated in 10.14

> **Deprecated**: Please use CAMetalLayer instead.

## Declaration

```swift
var openGLPixelFormat: NSOpenGLPixelFormat? { get set }
```

```objc
@property (strong, nullable) NSOpenGLPixelFormat * openGLPixelFormat;
```

## Discussion

Subclasses shouldn’t invoke `setOpenGLPixelFormat:`, but can override it if desired to intercept assignment of the layer’s pixel format.

## See Also

### Managing the Pixel Format
- [func openGLPixelFormat(forDisplayMask: UInt32) -> NSOpenGLPixelFormat](./openglpixelformat%28fordisplaymask%29.md)
  Returns the OpenGL pixel format suitable for the specified displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopengllayer/openglpixelformat)*