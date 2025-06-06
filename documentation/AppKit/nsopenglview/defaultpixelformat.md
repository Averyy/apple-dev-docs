# defaultPixelFormat()

**Framework**: AppKit  
**Kind**: method

Returns a default [`NSOpenGLPixelFormat`](nsopenglpixelformat.md) object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
class func defaultPixelFormat() -> NSOpenGLPixelFormat
```

#### Return Value

A pixel format object with no attributes set.

#### Discussion

Typically used with the initializer [`init(frame:pixelFormat:)`](nsopenglview/init(frame:pixelformat:).md), this object has no attributes set.

## See Also

- [var pixelFormat: NSOpenGLPixelFormat?](nsopenglview/pixelformat.md)
  The [`NSOpenGLPixelFormat`](nsopenglpixelformat.md) object associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/defaultpixelformat())*