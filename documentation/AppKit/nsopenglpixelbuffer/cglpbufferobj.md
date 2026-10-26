# CGLPBufferObj

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The underlying CGL pixel buffer object associated with the OpenGL pixel buffer object.

**Availability**:
- macOS 10.6+ - Deprecated in 10.7

## Declaration

```objc
@property (readonly, nullable) CGLPBufferObj CGLPBufferObj;
```

#### Return Value

The CGL pixel buffer object that encapsulates the actual pixel buffer.

## See Also

### Getting OpenGL Pixel Buffer Information
- [pixelsHigh](./pixelshigh.md)
  The height of the OpenGL pixel buffer’s texture (in pixels).
- [pixelsWide](./pixelswide.md)
  The width of the OpenGL pixel buffer’s texture, in pixels.
- [textureInternalFormat](./textureinternalformat.md)
  The internal format of the OpenGL pixel buffer’s texture.
- [textureMaxMipMapLevel](./texturemaxmipmaplevel.md)
  The maximum mipmap level of the OpenGL pixel buffer’s texture.
- [textureTarget](./texturetarget.md)
  The texture target of the OpenGL pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer/cglpbufferobj)*