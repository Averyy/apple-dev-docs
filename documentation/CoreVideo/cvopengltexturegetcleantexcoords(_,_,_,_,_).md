# CVOpenGLTextureGetCleanTexCoords(_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the texture coordinates for the part of the image that should be displayed.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLTextureGetCleanTexCoords(_ image: CVOpenGLTexture, _ lowerLeft: UnsafeMutablePointer<GLfloat>, _ lowerRight: UnsafeMutablePointer<GLfloat>, _ upperRight: UnsafeMutablePointer<GLfloat>, _ upperLeft: UnsafeMutablePointer<GLfloat>)
```

```c
extern void CVOpenGLTextureGetCleanTexCoords(CVOpenGLTextureRef image, GLfloat lowerLeft[2], GLfloat lowerRight[2], GLfloat upperRight[2], GLfloat upperLeft[2]);
```

#### Discussion

This function automatically takes into account whether or not the texture is flipped.

## Parameters

- `image`: The Core Video OpenGL texture whose clean tex coordinates you want to obtain.
- `lowerLeft`: On output, the `GLFloat` array holds the *s* and *t* texture coordinates of the lower-left corner of the image.
- `lowerRight`: On output, the `GLFloat` array holds the *s* and *t* texture coordinates of the lower-right corner of the image.
- `upperRight`: On output, the `GLFloat` array holds the *s* and *t* texture coordinates of the upper-right corner of the image.
- `upperLeft`: On output, the `GLFloat` array holds the *s* and *t* texture coordinates of the upper-left corner of the image.

## See Also

### Related Documentation
- [Core Video Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreVideo/CVProg_Intro/CVProg_Intro.html#//apple_ref/doc/uid/TP40001536)
### Inspecting Textures
- [func CVOpenGLTextureGetName(CVOpenGLTexture) -> GLuint](./cvopengltexturegetname%28_%29.md)
  Returns the texture target name of a CoreVideo OpenGL texture.
- [func CVOpenGLTextureGetTarget(CVOpenGLTexture) -> GLenum](./cvopengltexturegettarget%28_%29.md)
  Returns the texture target (for example, `GL_TEXTURE_2D`) of an OpenGL texture.
- [func CVOpenGLTextureIsFlipped(CVOpenGLTexture) -> Bool](./cvopengltextureisflipped%28_%29.md)
  Determines whether an OpenGL texture is flipped vertically.
- [func CVOpenGLTextureGetTypeID() -> CFTypeID](./cvopengltexturegettypeid%28%29.md)
  Obtains the Core Foundation ID for the Core Video OpenGL texture type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturegetcleantexcoords(_:_:_:_:_:))*