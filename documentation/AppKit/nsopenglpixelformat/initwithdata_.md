# initWithData:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an OpenGL pixel format object initialized with specified pixel format attribute data.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use [`init(attributes:)`](./init%28attributes%29.md) instead.

## Declaration

```objc
- (id) initWithData:(NSData *) attribs;
```

## See Also

### Creating an OpenGL Pixel Format
- [init?(cglPixelFormatObj: CGLPixelFormatObj)](./init%28cglpixelformatobj%29-2zqw4.md)
  Returns an OpenGL pixel format object initialized with using an existing CGL pixel format object.
- [convenience init?(attributes: UnsafePointer<NSOpenGLPixelFormatAttribute>)](./init%28attributes%29.md)
  Returns an OpenGL pixel format object initialized with specified pixel format attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/initwithdata:)*