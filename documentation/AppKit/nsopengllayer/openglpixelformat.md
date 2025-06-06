# openGLPixelFormat

**Framework**: AppKit  
**Kind**: property

Provides access to the layer’s associated OpenGL pixel format.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var openGLPixelFormat: NSOpenGLPixelFormat? { get set }
```

#### Discussion

Subclasses shouldn’t invoke `setOpenGLPixelFormat:`, but can override it if desired to intercept assignment of the layer’s pixel format.

## See Also

- [func openGLPixelFormat(forDisplayMask: UInt32) -> NSOpenGLPixelFormat](nsopengllayer/openglpixelformat(fordisplaymask:).md)
  Returns the OpenGL pixel format suitable for the specified displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopengllayer/openglpixelformat)*