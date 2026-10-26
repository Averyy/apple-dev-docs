# CVOpenGLTextureCache

**Framework**: Core Video  
**Role**: API Collection

A cache used to create and manage OpenGL texture objects.

## Topics

### Functions
- [func CVOpenGLTextureCacheCreate(CFAllocator?, CFDictionary?, CGLContextObj, CGLPixelFormatObj, CFDictionary?, UnsafeMutablePointer<CVOpenGLTextureCache?>) -> CVReturn](./cvopengltexturecachecreate%28_,_,_,_,_,_%29.md)
  Creates a new texture cache.
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
### Data Types
- [class CVOpenGLTextureCache](./cvopengltexturecache.md)
### Constants
- [Cache Attributes](./cvopengltexturecache-cache-attributes.md)
  Dictionary keys and values for use with the cacheAttributes parameter of [`CVOpenGLTextureCacheCreate(_:_:_:_:_:_:)`](./cvopengltexturecachecreate%28_,_,_,_,_,_%29.md)

## See Also

### OpenGL
- [CVOpenGLTexture](./cvopengltexture-782.md)
  A texture-based image buffer that supplies source image data to OpenGL.
- [CVOpenGLBuffer](./cvopenglbuffer-77s.md)
  An image buffer used to store image data in video memory.
- [CVOpenGLBufferPool](./cvopenglbufferpool-77j.md)
  A utility object for managing a set of recyclable OpenGL buffer objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturecache-780)*