# CVOpenGLTextureCacheCreateTextureFromImage(_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Creates a CVOpenGLTexture object from an existing [CVImageBuffer](./cvimagebuffer-q40.md).

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLTextureCacheCreateTextureFromImage(_ allocator: CFAllocator?, _ textureCache: CVOpenGLTextureCache, _ sourceImage: CVImageBuffer, _ attributes: CFDictionary?, _ textureOut: UnsafeMutablePointer<CVOpenGLTexture?>) -> CVReturn
```

```c
extern CVReturn CVOpenGLTextureCacheCreateTextureFromImage(CFAllocatorRef allocator, CVOpenGLTextureCacheRef textureCache, CVImageBufferRef sourceImage, CFDictionaryRef attributes, CVOpenGLTextureRef*textureOut);
```

## Return Value

Returns [`kCVReturnSuccess`](./kcvreturnsuccess.md) on success.

## Parameters

- `allocator`: The `CFAllocatorRef` to use for allocating the `CVOpenGLTexture` object.  May be `NULL`.
- `textureCache`: The texture cache object that will manage the texture.
- `sourceImage`: The source `CVImageBuffer` for which to create an `CVOpenGLTexture`.
- `attributes`: *This parameter is not currently supported and is for future use only.*

  The desired buffer attributes for the `CVOpenGLTexture`.
- `textureOut`: Upon return, contains the newly created texture.

## See Also

### Functions
- [func CVOpenGLTextureCacheCreate(CFAllocator?, CFDictionary?, CGLContextObj, CGLPixelFormatObj, CFDictionary?, UnsafeMutablePointer<CVOpenGLTextureCache?>) -> CVReturn](./cvopengltexturecachecreate%28_,_,_,_,_,_%29.md)
  Creates a new texture cache.
- [func CVOpenGLTextureCacheFlush(CVOpenGLTextureCache, CVOptionFlags)](./cvopengltexturecacheflush%28_,_%29.md)
  Performs internal housekeeping/recycling operations on the cache.
- [func CVOpenGLTextureCacheGetTypeID() -> CFTypeID](./cvopengltexturecachegettypeid%28%29.md)
  Returns the Core Foundation type identifier for a the texture cache.
- [CVOpenGLTextureCacheRetain](./cvopengltexturecacheretain.md)
  Retains a texture cache object.
- [CVOpenGLTextureCacheRelease](./cvopengltexturecacherelease.md)
  Releases a texture cache object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturecachecreatetexturefromimage(_:_:_:_:_:))*