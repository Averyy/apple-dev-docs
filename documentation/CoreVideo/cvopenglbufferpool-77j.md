# CVOpenGLBufferPool

**Framework**: Core Video  
**Role**: API Collection

A utility object for managing a set of recyclable OpenGL buffer objects.

## Topics

### Functions
- [func CVOpenGLBufferPoolCreate(CFAllocator?, CFDictionary?, CFDictionary?, UnsafeMutablePointer<CVOpenGLBufferPool?>) -> CVReturn](./cvopenglbufferpoolcreate%28_,_,_,_%29.md)
  Creates a new OpenGL buffer pool.
- [func CVOpenGLBufferPoolCreateOpenGLBuffer(CFAllocator?, CVOpenGLBufferPool, UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn](./cvopenglbufferpoolcreateopenglbuffer%28_,_,_%29.md)
  Creates a new OpenGL buffer from an OpenGL buffer pool.
- [func CVOpenGLBufferPoolGetAttributes(CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?](./cvopenglbufferpoolgetattributes%28_%29.md)
  Returns the pool attributes dictionary for an Open GL buffer pool.
- [func CVOpenGLBufferPoolGetOpenGLBufferAttributes(CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?](./cvopenglbufferpoolgetopenglbufferattributes%28_%29.md)
  Returns the attributes of OpenGL buffers that will be created from a buffer pool.
- [func CVOpenGLBufferPoolGetTypeID() -> CFTypeID](./cvopenglbufferpoolgettypeid%28%29.md)
  Obtains the Core Foundation ID for the OpenGL buffer pool type.
### Data Types
- [class CVOpenGLBufferPool](./cvopenglbufferpool.md)
  A reference to an OpenGL buffer pool object.
### Constants
- [let kCVOpenGLBufferPoolMaximumBufferAgeKey: CFString](./kcvopenglbufferpoolmaximumbufferagekey.md)
  The maximum time that unused buffers should be kept before they are deallocated (type `CFAbsoluteTime`).
- [let kCVOpenGLBufferPoolMinimumBufferCountKey: CFString](./kcvopenglbufferpoolminimumbuffercountkey.md)
  The minimum number of buffers to be kept in the pool (type `CFNumber`).

## See Also

### Related Documentation
- [Core Video Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreVideo/CVProg_Intro/CVProg_Intro.html#//apple_ref/doc/uid/TP40001536)
### OpenGL
- [CVOpenGLTextureCache](./cvopengltexturecache-780.md)
  A cache used to create and manage OpenGL texture objects.
- [CVOpenGLTexture](./cvopengltexture-782.md)
  A texture-based image buffer that supplies source image data to OpenGL.
- [CVOpenGLBuffer](./cvopenglbuffer-77s.md)
  An image buffer used to store image data in video memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbufferpool-77j)*