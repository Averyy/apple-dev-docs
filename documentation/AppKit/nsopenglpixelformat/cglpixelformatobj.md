# cglPixelFormatObj

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The low-level, platform-specific Core OpenGL (CGL) pixel format object represented by the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use Metal or MetalKit.

## Declaration

```swift
var cglPixelFormatObj: CGLPixelFormatObj? { get }
```

```objc
@property (readonly, nullable) CGLPixelFormatObj CGLPixelFormatObj;
```

## Return Value

A pointer to the underlying `CGLPixelFormatObj` object.

## See Also

### Managing the Pixel Format
- [func getValues(UnsafeMutablePointer<GLint>, forAttribute: NSOpenGLPixelFormatAttribute, forVirtualScreen: GLint)](./getvalues%28_,forattribute,forvirtualscreen%29.md)
  Gets the value for the specified pixel format attribute.
- [var numberOfVirtualScreens: GLint](./numberofvirtualscreens.md)
  The number of virtual screens associated with the OpenGL pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/cglpixelformatobj)*