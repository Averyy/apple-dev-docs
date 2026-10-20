# CVOpenGLTexture

**Framework**: Core Video  
**Role**: API Collection

A texture-based image buffer that supplies source image data to OpenGL.

#### Overview

Core Video OpenGL textures are texture-based image buffers used for supplying source image data to OpenGL.

## Topics

### Inspecting Textures
- [func CVOpenGLTextureGetName(CVOpenGLTexture) -> GLuint](./cvopengltexturegetname%28_%29.md)
  Returns the texture target name of a CoreVideo OpenGL texture.
- [func CVOpenGLTextureGetTarget(CVOpenGLTexture) -> GLenum](./cvopengltexturegettarget%28_%29.md)
  Returns the texture target (for example, `GL_TEXTURE_2D`) of an OpenGL texture.
- [func CVOpenGLTextureGetCleanTexCoords(CVOpenGLTexture, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>)](./cvopengltexturegetcleantexcoords%28_,_,_,_,_%29.md)
  Returns the texture coordinates for the part of the image that should be displayed.
- [func CVOpenGLTextureIsFlipped(CVOpenGLTexture) -> Bool](./cvopengltextureisflipped%28_%29.md)
  Determines whether an OpenGL texture is flipped vertically.
- [func CVOpenGLTextureGetTypeID() -> CFTypeID](./cvopengltexturegettypeid%28%29.md)
  Obtains the Core Foundation ID for the Core Video OpenGL texture type.
### Data Types
- [typealias CVOpenGLTexture](./cvopengltexture.md)
  A reference to an OpenGL texture-based image buffer object.

## See Also

### OpenGL
- [CVOpenGLTextureCache](./cvopengltexturecache-780.md)
  A cache used to create and manage OpenGL texture objects.
- [CVOpenGLBuffer](./cvopenglbuffer-77s.md)
  An image buffer used to store image data in video memory.
- [CVOpenGLBufferPool](./cvopenglbufferpool-77j.md)
  A utility object for managing a set of recyclable OpenGL buffer objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexture-782)*