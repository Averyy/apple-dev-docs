# openGLPixelFormat(forDisplayMask:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the OpenGL pixel format suitable for the specified displays.

**Availability**:
- macOS 10.6+ - Deprecated in 10.14

> **Deprecated**: Please use CAMetalLayer instead.

## Declaration

```swift
func openGLPixelFormat(forDisplayMask mask: UInt32) -> NSOpenGLPixelFormat
```

```objc
- (NSOpenGLPixelFormat *) openGLPixelFormatForDisplayMask:(uint32_t) mask;
```

#### Return Value

An autoreleased [`NSOpenGLPixelFormat`](../nsopenglpixelformat.md) object suitable for the displays.

#### Discussion

You must include an NSOpenGLPFAScreenMask specification in the pixel format attribute list that’s used to instantiate the NSOpenGLPixelFormat.

## Parameters

- `mask`: A mask specifying the displays the returned [`NSOpenGLPixelFormat`](../nsopenglpixelformat.md) must be suitable for.

## See Also

### Managing the Pixel Format
- [var openGLPixelFormat: NSOpenGLPixelFormat?](./openglpixelformat.md)
  Provides access to the layer’s associated OpenGL pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopengllayer/openglpixelformat(fordisplaymask:))*