# pixelBuffer

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the pixel-buffer object attached to the OpenGL context.

**Availability**:
- macOS 10.3+ - Deprecated in 10.7

> **Deprecated**: Use framebuffer objects instead.

## Declaration

```objc
- (NSOpenGLPixelBuffer *) pixelBuffer;
```

## Return Value

The pixel buffer object.

## See Also

### Working with Pixel Buffers
- [- setPixelBuffer:cubeMapFace:mipMapLevel:currentVirtualScreen:](./setpixelbuffer_cubemapface_mipmaplevel_currentvirtualscreen_.md)
  Attaches the specified pixel buffer to the OpenGL context.
- [- pixelBufferCubeMapFace](./pixelbuffercubemapface.md)
  Returns the cube map face of the pixel buffer attached to the OpenGL context.
- [- pixelBufferMipMapLevel](./pixelbuffermipmaplevel.md)
  Returns the mipmap level of the pixel buffer attached to the OpenGL context.
- [- setTextureImageToPixelBuffer:colorBuffer:](./settextureimagetopixelbuffer_colorbuffer_.md)
  Attaches the image data in the specified pixel buffer to the texture object currently bound by the OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/pixelbuffer)*