# CVOpenGLESTexture

**Framework**: Core Video  
**Role**: API Collection

A texture-based image buffer that supplies source image data to OpenGL ES.

## Overview

Core Video OpenGL ES textures are texture-based image buffers the system uses to supply source image data to OpenGL.

## Topics

### Inspecting Textures
- [func CVOpenGLESTextureGetTarget(CVOpenGLESTexture) -> GLenum](./cvopenglestexturegettarget%28_%29.md)
  Returns the texture target for a `CVOpenGLESTextureRef`.
- [func CVOpenGLESTextureGetName(CVOpenGLESTexture) -> GLuint](./cvopenglestexturegetname%28_%29.md)
  Returns the texture target name for a `CVOpenGLESTextureRef`.
- [func CVOpenGLESTextureGetCleanTexCoords(CVOpenGLESTexture, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>)](./cvopenglestexturegetcleantexcoords%28_,_,_,_,_%29.md)
  Returns convenient normalized texture coordinates for the part of the image that should be displayed.
- [func CVOpenGLESTextureIsFlipped(CVOpenGLESTexture) -> Bool](./cvopenglestextureisflipped%28_%29.md)
  Returns whether the image is flipped vertically or not.
- [func CVOpenGLESTextureGetTypeID() -> CFTypeID](./cvopenglestexturegettypeid%28%29.md)
  Returns the Core Foundation type identifier for a Core Video texture-based image buffer.
### Data Types
- [typealias CVOpenGLESTexture](./cvopenglestexture.md)
  A reference to a Core Video texture-based image buffer.

## See Also

### OpenGL ES
- [CVOpenGLESTextureCache](./cvopenglestexturecache-q2r.md)
  A cache used to create and manage OpenGL ES texture objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestexture-q2s)*