# CVOpenGLTextureGetCleanTexCoords(_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Returns the texture coordinates for the part of the image that should be displayed.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLTextureGetCleanTexCoords(_ image: CVOpenGLTexture, _ lowerLeft: UnsafeMutablePointer<GLfloat>, _ lowerRight: UnsafeMutablePointer<GLfloat>, _ upperRight: UnsafeMutablePointer<GLfloat>, _ upperLeft: UnsafeMutablePointer<GLfloat>)
```

#### Discussion

This function automatically takes into account whether or not the texture is flipped.

## Parameters

- `image`: The Core Video OpenGL texture whose clean tex coordinates you want to obtain.
- `lowerLeft`: On output, the   array holds the   and   texture coordinates of the lower-left corner of the image.
- `lowerRight`: On output, the   array holds the   and   texture coordinates of the lower-right corner of the image.
- `upperRight`: On output, the   array holds the   and   texture coordinates of the upper-right corner of the image.
- `upperLeft`: On output, the   array holds the   and   texture coordinates of the upper-left corner of the image.

## See Also

- [Core Video Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreVideo/CVProg_Intro/CVProg_Intro.html#//apple_ref/doc/uid/TP40001536)
- [func CVOpenGLTextureGetName(CVOpenGLTexture) -> GLuint](cvopengltexturegetname(_:).md)
  Returns the texture target name of a CoreVideo OpenGL texture.
- [func CVOpenGLTextureGetTarget(CVOpenGLTexture) -> GLenum](cvopengltexturegettarget(_:).md)
  Returns the texture target (for example, `GL_TEXTURE_2D`) of an OpenGL texture.
- [func CVOpenGLTextureIsFlipped(CVOpenGLTexture) -> Bool](cvopengltextureisflipped(_:).md)
  Determines whether an OpenGL texture is flipped vertically.
- [func CVOpenGLTextureGetTypeID() -> CFTypeID](cvopengltexturegettypeid().md)
  Obtains the Core Foundation ID for the Core Video OpenGL texture type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturegetcleantexcoords(_:_:_:_:_:))*