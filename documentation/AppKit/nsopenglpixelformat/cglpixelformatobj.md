# cglPixelFormatObj

**Framework**: AppKit  
**Kind**: property

The low-level, platform-specific Core OpenGL (CGL) pixel format object represented by the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var cglPixelFormatObj: CGLPixelFormatObj? { get }
```

#### Return Value

A pointer to the underlying `CGLPixelFormatObj` object.

## See Also

- [func getValues(UnsafeMutablePointer<GLint>, forAttribute: NSOpenGLPixelFormatAttribute, forVirtualScreen: GLint)](nsopenglpixelformat/getvalues(_:forattribute:forvirtualscreen:).md)
  Gets the value for the specified pixel format attribute.
- [var numberOfVirtualScreens: GLint](nsopenglpixelformat/numberofvirtualscreens.md)
  The number of virtual screens associated with the OpenGL pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/cglpixelformatobj)*