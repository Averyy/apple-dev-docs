# CVOpenGLESTextureCacheCreate(_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Creates a new Core Video texture cache.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLESTextureCacheCreate(_ allocator: CFAllocator?, _ cacheAttributes: CFDictionary?, _ eaglContext: CVEAGLContext, _ textureAttributes: CFDictionary?, _ cacheOut: UnsafeMutablePointer<CVOpenGLESTextureCache?>) -> CVReturn
```

```c
extern CVReturn CVOpenGLESTextureCacheCreate(CFAllocatorRef allocator, CFDictionaryRef cacheAttributes, CVEAGLContext eaglContext, CFDictionaryRef textureAttributes, CVOpenGLESTextureCacheRef*cacheOut);
```

#### Return Value

Upon successful creation of the texture cache, this function returns [`kCVReturnSuccess`](./kcvreturnsuccess.md).

## Parameters

- `allocator`: The [`CFAllocator`](../CoreFoundation/cfallocator.md) to use for allocating the texture cache. This parameter can be `NULL`.
- `cacheAttributes`: A [`CFDictionary`](../CoreFoundation/cfdictionary.md) containing the attributes of the texture cache itself. This parameter can be `NULL`.
- `eaglContext`: The OpenGLES 2.0 context into which the texture objects will be created. OpenGLES 1.x contexts are not supported.
- `textureAttributes`: A [`CFDictionary`](../CoreFoundation/cfdictionary.md) containing the attributes to be used for creating the [`CVOpenGLESTexture`](./cvopenglestexture.md) objects. This parameter can be `NULL`.
- `cacheOut`: A pointer to a `CVOpenGLESTextureCacheRef` where the newly created texture cache will be placed.

## See Also

### Functions
- [func CVOpenGLESTextureCacheCreateTextureFromImage(CFAllocator?, CVOpenGLESTextureCache, CVImageBuffer, CFDictionary?, GLenum, GLint, GLsizei, GLsizei, GLenum, GLenum, Int, UnsafeMutablePointer<CVOpenGLESTexture?>) -> CVReturn](./cvopenglestexturecachecreatetexturefromimage%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Creates a [`CVOpenGLESTexture`](./cvopenglestexture.md) object from an existing [`CVImageBuffer`](./cvimagebuffer.md).
- [func CVOpenGLESTextureCacheFlush(CVOpenGLESTextureCache, CVOptionFlags)](./cvopenglestexturecacheflush%28_,_%29.md)
  Performs internal housekeeping/recycling operations on a texture cache.
- [func CVOpenGLESTextureCacheGetTypeID() -> CFTypeID](./cvopenglestexturecachegettypeid%28%29.md)
  Returns the Core Foundation type identifier for a Core Video texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestexturecachecreate(_:_:_:_:_:))*