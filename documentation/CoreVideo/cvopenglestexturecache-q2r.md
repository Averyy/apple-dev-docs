# CVOpenGLESTextureCache

**Framework**: Core Video

A cache used to create and manage OpenGL ES texture objects.

#### Overview

Core Video uses OpenGL ES texture caches to cache and manage [`CVOpenGLESTexture`](cvopenglestexture.md) textures. These texture caches provide you with a way to directly read and write buffers with various pixel formats, such as 420v or BGRA, from GL ES.

## Topics

### Functions
- [func CVOpenGLESTextureCacheCreate(CFAllocator?, CFDictionary?, CVEAGLContext, CFDictionary?, UnsafeMutablePointer<CVOpenGLESTextureCache?>) -> CVReturn](cvopenglestexturecachecreate(_:_:_:_:_:).md)
  Creates a new Core Video texture cache.
- [func CVOpenGLESTextureCacheCreateTextureFromImage(CFAllocator?, CVOpenGLESTextureCache, CVImageBuffer, CFDictionary?, GLenum, GLint, GLsizei, GLsizei, GLenum, GLenum, Int, UnsafeMutablePointer<CVOpenGLESTexture?>) -> CVReturn](cvopenglestexturecachecreatetexturefromimage(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Creates a [`CVOpenGLESTexture`](cvopenglestexture.md) object from an existing [`CVImageBuffer`](cvimagebuffer.md).
- [func CVOpenGLESTextureCacheFlush(CVOpenGLESTextureCache, CVOptionFlags)](cvopenglestexturecacheflush(_:_:).md)
  Performs internal housekeeping/recycling operations on a texture cache.
- [func CVOpenGLESTextureCacheGetTypeID() -> CFTypeID](cvopenglestexturecachegettypeid().md)
  Returns the Core Foundation type identifier for a Core Video texture cache.
### Data Types
- [class CVOpenGLESTextureCache](cvopenglestexturecache.md)
- [typealias CVEAGLContext](cveaglcontext.md)
  A type that resolves to an [`EAGLContext`](https://developer.apple.com/documentation/OpenGLES/EAGLContext) pointer when appropriate.
### Constants
- [Cache Attributes](cvopenglestexturecache-cache-attributes.md)
  Attributes for the texture cache.

## See Also

- [CVOpenGLESTexture](cvopenglestexture-q2s.md)
  A texture-based image buffer that supplies source image data to OpenGL ES.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestexturecache-q2r)*