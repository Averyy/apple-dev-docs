# initWithTextureTarget:textureInternalFormat:textureMaxMipMapLevel:pixelsWide:pixelsHigh:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an `NSOpenGLPixelBuffer` object initialized with the specified parameters.

**Availability**:
- macOS 10.2+ - Deprecated in 10.7

## Declaration

```objc
- (instancetype) initWithTextureTarget:(GLenum) target textureInternalFormat:(GLenum) format textureMaxMipMapLevel:(GLint) maxLevel pixelsWide:(GLsizei) pixelsWide pixelsHigh:(GLsizei) pixelsHigh;
```

## Return Value

An initialized `NSOpenGLPixelBuffer` object or `nil` if the initialization failed. Initialization can fail if there is inconsistency among the parameter values. See the OpenGL documentation for `glTexImage2D` for more information.

## Discussion

The value you pass to the `target` parameter defines several other constraints that are then applied to the remaining parameters. The list below gives the values you can pass to `target` and the additional constraints.

- `GL_TEXTURE_2D`
- `GL_TEXTURE_CUBE_MAP` - the values in `pixelsWide` and `pixelsHigh` must be equal.
- `GL_TEXTURE_RECTANGLE_EXT` - `maxLevel` must be zero.

Normally, when using the `GL_TEXTURE_2D` and `GL_TEXTURE_CUBE_MAP` targets, you must specify width and height values that are powers of two. When the `ARB_texture_non_power_of_two` extension is present, however, some types of hardware can support values that are not powers of two. You should check for the presence of this extension before specifying non power-of-two values.

If the texture map cannot be created, you can use the `glGetError` function to get the error code.

## Parameters

- `target`: The texture object. This value should be one of the following:  `GL_TEXTURE_2D`,`GL_TEXTURE_CUBE_MAP`, or `GL_TEXTURE_RECTANGLE_EXT`.
- `format`: The base internal format of the texture. This value should be `GL_RGB`, `GL_RGBA`, or `GL_DEPTH_COMPONENT`.
- `maxLevel`: The desired maximum mipmap level of the structure, starting with zero.
- `pixelsWide`: The width of the texture (in pixels) in the pixel buffer.
- `pixelsHigh`: The height of the texture (in pixels) in the pixel buffer.

## See Also

### Initializing an OpenGL Pixel Buffer
- [- initWithCGLPBufferObj:](./initwithcglpbufferobj_.md)
  Initializes and returns an OpenGL pixel buffer object that encapsulates an existing CGL pixel buffer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer/initwithtexturetarget:textureinternalformat:texturemaxmipmaplevel:pixelswide:pixelshigh:)*