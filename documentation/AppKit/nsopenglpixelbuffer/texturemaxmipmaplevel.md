# textureMaxMipMapLevel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The maximum mipmap level of the OpenGL pixel buffer’s texture.

**Availability**:
- macOS 10.2+ - Deprecated in 10.7

## Declaration

```objc
@property (readonly) GLint textureMaxMipMapLevel;
```

## Return Value

The maximum mipmap level.

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
- [textureTarget](./texturetarget.md)
  The texture target of the OpenGL pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer/texturemaxmipmaplevel)*