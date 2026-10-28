# textureTarget

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The texture target of the OpenGL pixel buffer.

**Availability**:
- macOS 10.2+ - Deprecated in 10.7

## Declaration

```objc
@property (readonly) GLenum textureTarget;
```

## Return Value

The texture target, which can be one of the following values: `GL_TEXTURE_2D`, `GL_TEXTURE_CUBE_MAP`, or `GL_TEXTURE_RECTANGLE_EXT`.

## See Also

### Getting OpenGL Pixel Buffer Information
- [CGLPBufferObj](./cglpbufferobj.md)
  The underlying CGL pixel buffer object associated with the OpenGL pixel buffer object.
- [pixelsHigh](./pixelshigh.md)
  The height of the OpenGL pixel buffer’s texture (in pixels).
- [pixelsWide](./pixelswide.md)
  The width of the OpenGL pixel buffer’s texture, in pixels.
- [textureInternalFormat](./textureinternalformat.md)
  The internal format of the OpenGL pixel buffer’s texture.
- [textureMaxMipMapLevel](./texturemaxmipmaplevel.md)
  The maximum mipmap level of the OpenGL pixel buffer’s texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer/texturetarget)*