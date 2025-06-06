# CVOpenGLTextureGetTypeID()

**Framework**: Core Video  
**Kind**: func

Obtains the Core Foundation ID for the Core Video OpenGL texture type.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLTextureGetTypeID() -> CFTypeID
```

#### Return Value

The Core Foundation ID for this type.

## See Also

- [func CVOpenGLTextureGetName(CVOpenGLTexture) -> GLuint](cvopengltexturegetname(_:).md)
  Returns the texture target name of a CoreVideo OpenGL texture.
- [func CVOpenGLTextureGetTarget(CVOpenGLTexture) -> GLenum](cvopengltexturegettarget(_:).md)
  Returns the texture target (for example, `GL_TEXTURE_2D`) of an OpenGL texture.
- [func CVOpenGLTextureGetCleanTexCoords(CVOpenGLTexture, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>)](cvopengltexturegetcleantexcoords(_:_:_:_:_:).md)
  Returns the texture coordinates for the part of the image that should be displayed.
- [func CVOpenGLTextureIsFlipped(CVOpenGLTexture) -> Bool](cvopengltextureisflipped(_:).md)
  Determines whether an OpenGL texture is flipped vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturegettypeid())*