# setPixelBuffer:cubeMapFace:mipMapLevel:currentVirtualScreen:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Attaches the specified pixel buffer to the OpenGL context.

**Availability**:
- macOS 10.3+ - Deprecated in 10.7

> **Deprecated**: Use framebuffer objects instead.

## Declaration

```objc
- (void) setPixelBuffer:(NSOpenGLPixelBuffer *) pixelBuffer cubeMapFace:(GLenum) face mipMapLevel:(GLint) level currentVirtualScreen:(GLint) screen;
```

## Discussion

The `NSOpenGLPixelBuffer` object gives the receiver access to accelerated offscreen rendering in the pixel buffer, which is primarily used for textures.

## Parameters

- `pixelBuffer`: The pixel buffer to attach.
- `face`: For pixel buffers with a texture target of `GL_CUBE_MAP`, this parameter should be zero or one of the following values:

  - `GL_TEXTURE_CUBE_MAP_POSITIVE_X`
  - `GL_TEXTURE_CUBE_MAP_POSITIVE_Y`
  - `GL_TEXTURE_CUBE_MAP_POSITIVE_Z`
  - `GL_TEXTURE_CUBE_MAP_NEGATIVE_X`
  - `GL_TEXTURE_CUBE_MAP_NEGATIVE_Y`
  - `GL_TEXTURE_CUBE_MAP_NEGATIVE_Z`
- `level`: The desired mipmap level for rendering. This value must be less than or equal to the maximum texture mipmap level of `pixelBuffer` (accessible through an `NSOpenGLPixelBuffer` object’s [`textureMaxMipMapLevel`](../nsopenglpixelbuffer/texturemaxmipmaplevel.md) method).
- `screen`: The virtual screen of the receiver (if applicable) should be set to the same value as the current virtual screen you are using for rendering onscreen

## See Also

### Related Documentation
- [- initWithTextureTarget:textureInternalFormat:textureMaxMipMapLevel:pixelsWide:pixelsHigh:](../nsopenglpixelbuffer/initwithtexturetarget_textureinternalformat_texturemaxmipmaplevel_pixelswide_pixelshigh_.md)
  Returns an `NSOpenGLPixelBuffer` object initialized with the specified parameters.
- [var currentVirtualScreen: GLint](./currentvirtualscreen.md)
  Returns the current virtual screen for the OpenGL context.
### Working with Pixel Buffers
- [- pixelBuffer](./pixelbuffer.md)
  Returns the pixel-buffer object attached to the OpenGL context.
- [- pixelBufferCubeMapFace](./pixelbuffercubemapface.md)
  Returns the cube map face of the pixel buffer attached to the OpenGL context.
- [- pixelBufferMipMapLevel](./pixelbuffermipmaplevel.md)
  Returns the mipmap level of the pixel buffer attached to the OpenGL context.
- [- setTextureImageToPixelBuffer:colorBuffer:](./settextureimagetopixelbuffer_colorbuffer_.md)
  Attaches the image data in the specified pixel buffer to the texture object currently bound by the OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/setpixelbuffer:cubemapface:mipmaplevel:currentvirtualscreen:)*