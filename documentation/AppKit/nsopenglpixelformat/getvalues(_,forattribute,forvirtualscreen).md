# getValues(_:forAttribute:forVirtualScreen:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Gets the value for the specified pixel format attribute.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use Metal or MetalKit.

## Declaration

```swift
func getValues(_ vals: UnsafeMutablePointer<GLint>, forAttribute attrib: NSOpenGLPixelFormatAttribute, forVirtualScreen screen: GLint)
```

```objc
- (void) getValues:(GLint *) vals forAttribute:(NSOpenGLPixelFormatAttribute) attrib forVirtualScreen:(GLint) screen;
```

#### Discussion

Because the value for an attribute may be different on each virtual screen, the virtual screen must be specified along with the attribute.

## Parameters

- `vals`: On input, a pointer to a `long` variable. On output, the variable contains the value of the requested attribute.
- `attrib`: The requested attribute. For a list of attribute constants, see the table in Constants.
- `screen`: The screen from which you want to retrieve the attribute. This parameter must be a value between 0 and the number of virtual screens ([`numberOfVirtualScreens`](./numberofvirtualscreens.md)) minus 1.

## See Also

### Related Documentation
- [convenience init?(attributes: UnsafePointer<NSOpenGLPixelFormatAttribute>)](./init%28attributes%29.md)
  Returns an OpenGL pixel format object initialized with specified pixel format attributes.
### Managing the Pixel Format
- [var cglPixelFormatObj: CGLPixelFormatObj?](./cglpixelformatobj.md)
  The low-level, platform-specific Core OpenGL (CGL) pixel format object represented by the receiver.
- [var numberOfVirtualScreens: GLint](./numberofvirtualscreens.md)
  The number of virtual screens associated with the OpenGL pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/getvalues(_:forattribute:forvirtualscreen:))*