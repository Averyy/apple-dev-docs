# pixelFormat

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The [`NSOpenGLPixelFormat`](../nsopenglpixelformat.md) object associated with the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use MTKView instead.

## Declaration

```swift
var pixelFormat: NSOpenGLPixelFormat? { get set }
```

```objc
@property (strong, nullable) NSOpenGLPixelFormat * pixelFormat;
```

## See Also

### Related Documentation
- [init?(frame: NSRect, pixelFormat: NSOpenGLPixelFormat?)](./init%28frame,pixelformat%29.md)
  Returns an `NSOpenGLView` object initialized with the specified frame rectangle and pixel format.
### Managing the NSOpenGLPixelFormat
- [class func defaultPixelFormat() -> NSOpenGLPixelFormat](./defaultpixelformat%28%29.md)
  Returns a default [`NSOpenGLPixelFormat`](../nsopenglpixelformat.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/pixelformat)*