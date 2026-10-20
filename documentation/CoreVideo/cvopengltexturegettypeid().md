# CVOpenGLTextureGetTypeID()

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Obtains the Core Foundation ID for the Core Video OpenGL texture type.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLTextureGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CVOpenGLTextureGetTypeID();
```

#### Return Value

The Core Foundation ID for this type.

## See Also

### Inspecting Textures
- [func CVOpenGLTextureGetName(CVOpenGLTexture) -> GLuint](./cvopengltexturegetname%28_%29.md)
  Returns the texture target name of a CoreVideo OpenGL texture.
- [func CVOpenGLTextureGetTarget(CVOpenGLTexture) -> GLenum](./cvopengltexturegettarget%28_%29.md)
  Returns the texture target (for example, `GL_TEXTURE_2D`) of an OpenGL texture.
- [func CVOpenGLTextureGetCleanTexCoords(CVOpenGLTexture, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>)](./cvopengltexturegetcleantexcoords%28_,_,_,_,_%29.md)
  Returns the texture coordinates for the part of the image that should be displayed.
- [func CVOpenGLTextureIsFlipped(CVOpenGLTexture) -> Bool](./cvopengltextureisflipped%28_%29.md)
  Determines whether an OpenGL texture is flipped vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturegettypeid())*