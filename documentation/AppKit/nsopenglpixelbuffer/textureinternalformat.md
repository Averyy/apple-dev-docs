# textureInternalFormat

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The internal format of the OpenGL pixel buffer’s texture.

**Availability**:
- macOS 10.2+ - Deprecated in 10.7

## Declaration

```objc
@property (readonly) GLenum textureInternalFormat;
```

## Return Value

The texture format, which can be one of the following values: `GL_RGB`, `GL_RGBA`, or `GL_DEPTH_COMPONENT`.

## See Also

### Getting OpenGL Pixel Buffer Information
- [CGLPBufferObj](./cglpbufferobj.md)
  The underlying CGL pixel buffer object associated with the OpenGL pixel buffer object.
- [pixelsHigh](./pixelshigh.md)
  The height of the OpenGL pixel buffer’s texture (in pixels).
- [pixelsWide](./pixelswide.md)
  The width of the OpenGL pixel buffer’s texture, in pixels.
- [textureMaxMipMapLevel](./texturemaxmipmaplevel.md)
  The maximum mipmap level of the OpenGL pixel buffer’s texture.
- [textureTarget](./texturetarget.md)
  The texture target of the OpenGL pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer/textureinternalformat)*