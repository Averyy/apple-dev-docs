# setTextureImageToPixelBuffer:colorBuffer:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Attaches the image data in the specified pixel buffer to the texture object currently bound by the OpenGL context.

**Availability**:
- macOS 10.3+ - Deprecated in 10.7

> **Deprecated**: Use framebuffer objects instead.

## Declaration

```objc
- (void) setTextureImageToPixelBuffer:(NSOpenGLPixelBuffer *) pixelBuffer colorBuffer:(GLenum) source;
```

## Discussion

This method corresponds to the Core OpenGL method `CGLTexImagePBuffer`.

## Parameters

- `pixelBuffer`: The pixel buffer to attach.
- `source`: An OpenGL constant indicating which of the pixel buffer’s color buffers to use. Potential values for this parameter include `GL_FRONT`, `GL_BACK`, and `GL_AUX0`.

## See Also

### Working with Pixel Buffers
- [- setPixelBuffer:cubeMapFace:mipMapLevel:currentVirtualScreen:](./setpixelbuffer_cubemapface_mipmaplevel_currentvirtualscreen_.md)
  Attaches the specified pixel buffer to the OpenGL context.
- [- pixelBuffer](./pixelbuffer.md)
  Returns the pixel-buffer object attached to the OpenGL context.
- [- pixelBufferCubeMapFace](./pixelbuffercubemapface.md)
  Returns the cube map face of the pixel buffer attached to the OpenGL context.
- [- pixelBufferMipMapLevel](./pixelbuffermipmaplevel.md)
  Returns the mipmap level of the pixel buffer attached to the OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/settextureimagetopixelbuffer:colorbuffer:)*