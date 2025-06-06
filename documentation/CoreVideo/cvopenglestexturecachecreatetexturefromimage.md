# CVOpenGLESTextureCacheCreateTextureFromImage(_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a [`CVOpenGLESTexture`](cvopenglestexture.md) object from an existing [`CVImageBuffer`](cvimagebuffer.md).

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
func CVOpenGLESTextureCacheCreateTextureFromImage(_ allocator: CFAllocator?, _ textureCache: CVOpenGLESTextureCache, _ sourceImage: CVImageBuffer, _ textureAttributes: CFDictionary?, _ target: GLenum, _ internalFormat: GLint, _ width: GLsizei, _ height: GLsizei, _ format: GLenum, _ type: GLenum, _ planeIndex: Int, _ textureOut: UnsafeMutablePointer<CVOpenGLESTexture?>) -> CVReturn
```

#### Return Value

Upon successful creation of the texture, this function returns [`kCVReturnSuccess`](kcvreturnsuccess.md).

#### Discussion

This function either creates a new or returns a cached [`CVOpenGLESTexture`](cvopenglestexture.md) texture object mapped to the [`CVImageBuffer`](cvimagebuffer.md) and associated parameters. This operation creates a live binding between the image buffer and the underlying texture object. The EAGLContext associated with the cache may be modified to create, delete, or bind textures. When used as a source texture or `GL_COLOR_ATTACHMENT`, the image buffer must be unlocked before rendering. The source or render buffer texture should not be re-used until the rendering has completed. This can be guaranteed by calling `glFlush()`.

Some example mappings can be seen in the following code snippet.

```objc
//Mapping a BGRA buffer as a source texture:
CVOpenGLESTextureCacheCreateTextureFromImage(kCFAllocatorDefault, textureCache, pixelBuffer, NULL, GL_TEXTURE_2D, GL_RGBA, width, height, GL_RGBA, GL_UNSIGNED_BYTE, 0, &outTexture);
//Mapping a BGRA buffer as a renderbuffer:
CVOpenGLESTextureCacheCreateTextureFromImage(kCFAllocatorDefault, textureCache, pixelBuffer, NULL, GL_RENDERBUFFER, GL_RGBA8_OES, width, height, GL_RGBA, GL_UNSIGNED_BYTE, 0, &outTexture);
//Mapping the luma plane of a 420v buffer as a source texture:
CVOpenGLESTextureCacheCreateTextureFromImage(kCFAllocatorDefault, textureCache, pixelBuffer, NULL, GL_TEXTURE_2D, GL_LUMINANCE, width, height, GL_LUMINANCE, GL_UNSIGNED_BYTE, 0, &outTexture);
//Mapping the chroma plane of a 420v buffer as a source texture:
CVOpenGLESTextureCacheCreateTextureFromImage(kCFAllocatorDefault, textureCache, pixelBuffer, NULL, GL_TEXTURE_2D, GL_LUMINANCE_ALPHA, width/2, height/2, GL_LUMINANCE_ALPHA, GL_UNSIGNED_BYTE, 1, &outTexture);
//Mapping a yuvs buffer as a source texture (note: yuvs/f and 2vuy are unpacked and resampled -- not colorspace converted)
CVOpenGLESTextureCacheCreateTextureFromImage(kCFAllocatorDefault, textureCache, pixelBuffer, NULL, GL_TEXTURE_2D, GL_RGB_422_APPLE, width, height, GL_RGB_422_APPLE, GL_UNSIGNED_SHORT_8_8_APPLE, 1, &outTexture);
```

## Parameters

- `allocator`: The   to use for allocating the texture object. This parameter can be  .
- `textureCache`: The texture cache object that will manage the texture.
- `sourceImage`: The   that you want to create a texture from.
- `textureAttributes`: A   containing the attributes to be used for creating the   objects. This parameter can be  .
- `target`: The target texture.   and   are the only targets currently supported.
- `internalFormat`: The number of color components in the texture. Examples are  ,  ,  ,  , and  .
- `width`: The width of the texture image.
- `height`: The height of the texture image.
- `format`: The format of the pixel data. Examples are   and  .
- `type`: The data type of the pixel data. One example is  .
- `planeIndex`: The plane of the   to map bind.  Ignored for non-planar  s.
- `textureOut`: A pointer to a   where the newly created texture object will be placed.

## See Also

- [func CVOpenGLESTextureCacheCreate(CFAllocator?, CFDictionary?, CVEAGLContext, CFDictionary?, UnsafeMutablePointer<CVOpenGLESTextureCache?>) -> CVReturn](cvopenglestexturecachecreate(_:_:_:_:_:).md)
  Creates a new Core Video texture cache.
- [func CVOpenGLESTextureCacheFlush(CVOpenGLESTextureCache, CVOptionFlags)](cvopenglestexturecacheflush(_:_:).md)
  Performs internal housekeeping/recycling operations on a texture cache.
- [func CVOpenGLESTextureCacheGetTypeID() -> CFTypeID](cvopenglestexturecachegettypeid().md)
  Returns the Core Foundation type identifier for a Core Video texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestexturecachecreatetexturefromimage(_:_:_:_:_:_:_:_:_:_:_:_:))*