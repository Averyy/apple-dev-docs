# getValues(_:forAttribute:forVirtualScreen:)

**Framework**: AppKit  
**Kind**: method

Gets the value for the specified pixel format attribute.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func getValues(_ vals: UnsafeMutablePointer<GLint>, forAttribute attrib: NSOpenGLPixelFormatAttribute, forVirtualScreen screen: GLint)
```

#### Discussion

Because the value for an attribute may be different on each virtual screen, the virtual screen must be specified along with the attribute.

## Parameters

- `vals`: On input, a pointer to a   variable. On output, the variable contains the value of the requested attribute.
- `attrib`: The requested attribute. For a list of attribute constants, see the table in Constants.
- `screen`: The screen from which you want to retrieve the attribute. This parameter must be a value between 0 and the number of virtual screens ( ) minus 1.

## See Also

- [convenience init?(attributes: UnsafePointer<NSOpenGLPixelFormatAttribute>)](nsopenglpixelformat/init(attributes:).md)
  Returns an OpenGL pixel format object initialized with specified pixel format attributes.
- [var cglPixelFormatObj: CGLPixelFormatObj?](nsopenglpixelformat/cglpixelformatobj.md)
  The low-level, platform-specific Core OpenGL (CGL) pixel format object represented by the receiver.
- [var numberOfVirtualScreens: GLint](nsopenglpixelformat/numberofvirtualscreens.md)
  The number of virtual screens associated with the OpenGL pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/getvalues(_:forattribute:forvirtualscreen:))*