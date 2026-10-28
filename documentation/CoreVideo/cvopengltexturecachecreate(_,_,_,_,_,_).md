# CVOpenGLTextureCacheCreate(_:_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Creates a new texture cache.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLTextureCacheCreate(_ allocator: CFAllocator?, _ cacheAttributes: CFDictionary?, _ cglContext: CGLContextObj, _ cglPixelFormat: CGLPixelFormatObj, _ textureAttributes: CFDictionary?, _ cacheOut: UnsafeMutablePointer<CVOpenGLTextureCache?>) -> CVReturn
```

```c
extern CVReturn CVOpenGLTextureCacheCreate(CFAllocatorRef allocator, CFDictionaryRef cacheAttributes, CGLContextObj cglContext, CGLPixelFormatObj cglPixelFormat, CFDictionaryRef textureAttributes, CVOpenGLTextureCacheRef*cacheOut);
```

## Return Value

Returns [`kCVReturnSuccess`](./kcvreturnsuccess.md) on success.

## Parameters

- `allocator`: The `CFAllocatorRef` to use for allocating the cache.  May be NULL.
- `cacheAttributes`: A dictionary specifying options for the cache’s behavior, or `NULL` to use default options. For applicable keys and values, see [Cache Attributes](./cvopengltexturecache-cache-attributes.md).
- `cglContext`: The OpenGL context into which the texture objects will be created.
- `cglPixelFormat`: The OpenGL pixel format object used to create the passed in OpenGL context.
- `textureAttributes`: A `CFDictionaryRef` containing the attributes to be used for creating the `CVOpenGLTexture` objects.  May be `NULL`.
- `cacheOut`: Upon return, contains the newly created texture cache.

## See Also

### Functions
- [func CVOpenGLTextureCacheCreateTextureFromImage(CFAllocator?, CVOpenGLTextureCache, CVImageBuffer, CFDictionary?, UnsafeMutablePointer<CVOpenGLTexture?>) -> CVReturn](./cvopengltexturecachecreatetexturefromimage%28_,_,_,_,_%29.md)
  Creates a CVOpenGLTexture object from an existing [CVImageBuffer](./cvimagebuffer-q40.md).
- [func CVOpenGLTextureCacheFlush(CVOpenGLTextureCache, CVOptionFlags)](./cvopengltexturecacheflush%28_,_%29.md)
  Performs internal housekeeping/recycling operations on the cache.
- [func CVOpenGLTextureCacheGetTypeID() -> CFTypeID](./cvopengltexturecachegettypeid%28%29.md)
  Returns the Core Foundation type identifier for a the texture cache.
- [CVOpenGLTextureCacheRetain](./cvopengltexturecacheretain.md)
  Retains a texture cache object.
- [CVOpenGLTextureCacheRelease](./cvopengltexturecacherelease.md)
  Releases a texture cache object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturecachecreate(_:_:_:_:_:_:))*