# pixelBufferCubeMapFace

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the cube map face of the pixel buffer attached to the OpenGL context.

**Availability**:
- macOS 10.3+ - Deprecated in 10.7

> **Deprecated**: Use framebuffer objects instead.

## Declaration

```objc
- (GLenum) pixelBufferCubeMapFace;
```

#### Return Value

For pixel buffers with a texture target of `GL_CUBE_MAP`, this value is zero or one of the following values:

#### Discussion

- `GL_TEXTURE_CUBE_MAP_POSITIVE_X`
- `GL_TEXTURE_CUBE_MAP_POSITIVE_Y`
- `GL_TEXTURE_CUBE_MAP_POSITIVE_Z`
- `GL_TEXTURE_CUBE_MAP_NEGATIVE_X`
- `GL_TEXTURE_CUBE_MAP_NEGATIVE_Y`
- `GL_TEXTURE_CUBE_MAP_NEGATIVE_Z`

## See Also

### Working with Pixel Buffers
- [- setPixelBuffer:cubeMapFace:mipMapLevel:currentVirtualScreen:](./setpixelbuffer_cubemapface_mipmaplevel_currentvirtualscreen_.md)
  Attaches the specified pixel buffer to the OpenGL context.
- [- pixelBuffer](./pixelbuffer.md)
  Returns the pixel-buffer object attached to the OpenGL context.
- [- pixelBufferMipMapLevel](./pixelbuffermipmaplevel.md)
  Returns the mipmap level of the pixel buffer attached to the OpenGL context.
- [- setTextureImageToPixelBuffer:colorBuffer:](./settextureimagetopixelbuffer_colorbuffer_.md)
  Attaches the image data in the specified pixel buffer to the texture object currently bound by the OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/pixelbuffercubemapface)*