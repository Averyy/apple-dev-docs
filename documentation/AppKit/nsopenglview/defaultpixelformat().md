# defaultPixelFormat()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a default [`NSOpenGLPixelFormat`](../nsopenglpixelformat.md) object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use MTKView instead.

## Declaration

```swift
class func defaultPixelFormat() -> NSOpenGLPixelFormat
```

```objc
+ (NSOpenGLPixelFormat *) defaultPixelFormat;
```

## Return Value

A pixel format object with no attributes set.

## Discussion

Typically used with the initializer [`init(frame:pixelFormat:)`](./init%28frame,pixelformat%29.md), this object has no attributes set.

## See Also

### Managing the NSOpenGLPixelFormat
- [var pixelFormat: NSOpenGLPixelFormat?](./pixelformat.md)
  The [`NSOpenGLPixelFormat`](../nsopenglpixelformat.md) object associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/defaultpixelformat())*