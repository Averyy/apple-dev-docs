# CVOpenGLBuffer

**Framework**: Core Video

An image buffer used to store image data in video memory.

## Topics

### Functions
- [func CVOpenGLBufferCreate(CFAllocator?, Int, Int, CFDictionary?, UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn](cvopenglbuffercreate(_:_:_:_:_:).md)
  Creates a new Core Video OpenGL buffer that can be used for OpenGL rendering purposes
- [func CVOpenGLBufferAttach(CVOpenGLBuffer, CGLContextObj, GLenum, GLint, GLint) -> CVReturn](cvopenglbufferattach(_:_:_:_:_:).md)
  Attaches an OpenGL context to a Core Video OpenGL buffer.
- [func CVOpenGLBufferGetAttributes(CVOpenGLBuffer) -> Unmanaged<CFDictionary>?](cvopenglbuffergetattributes(_:).md)
  Obtains the attributes of a Core Video OpenGL buffer.
- [func CVOpenGLBufferGetTypeID() -> CFTypeID](cvopenglbuffergettypeid().md)
  Obtains the Core Foundation type ID for the OpenGL buffer type.
### Data Types
- [typealias CVOpenGLBuffer](cvopenglbuffer.md)
  A reference to a Core Video OpenGL buffer object.
### Constants
- [let kCVOpenGLBufferHeight: CFString](kcvopenglbufferheight.md)
  The height of the buffer.
- [let kCVOpenGLBufferInternalFormat: CFString](kcvopenglbufferinternalformat.md)
  The OpenGL internal format of this buffer.
- [let kCVOpenGLBufferMaximumMipmapLevel: CFString](kcvopenglbuffermaximummipmaplevel.md)
  The maximum mipmap level for this buffer.
- [let kCVOpenGLBufferTarget: CFString](kcvopenglbuffertarget.md)
  The OpenGL target for this buffer.
- [let kCVOpenGLBufferWidth: CFString](kcvopenglbufferwidth.md)
  The width of the buffer.

## See Also

- [CVOpenGLTextureCache](cvopengltexturecache-780.md)
  A cache used to create and manage OpenGL texture objects.
- [CVOpenGLTexture](cvopengltexture-782.md)
  A texture-based image buffer that supplies source image data to OpenGL.
- [CVOpenGLBufferPool](cvopenglbufferpool-77j.md)
  A utility object for managing a set of recyclable OpenGL buffer objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbuffer-77s)*