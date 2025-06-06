# CVOpenGLTextureGetTarget(_:)

**Framework**: Core Video  
**Kind**: func

Returns the texture target (for example, `GL_TEXTURE_2D`) of an OpenGL texture.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLTextureGetTarget(_ image: CVOpenGLTexture) -> GLenum
```

#### Return Value

The OpenGL texture target.

#### Discussion

See the [`OpenGL specification`](https://developer.apple.comhttp://www.opengl.org/documentation/) for more information about texture targets.

## Parameters

- `image`: The Core Video OpenGL texture whose target you want to obtain.

## See Also

- [func CVOpenGLTextureGetName(CVOpenGLTexture) -> GLuint](cvopengltexturegetname(_:).md)
  Returns the texture target name of a CoreVideo OpenGL texture.
- [func CVOpenGLTextureGetCleanTexCoords(CVOpenGLTexture, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>)](cvopengltexturegetcleantexcoords(_:_:_:_:_:).md)
  Returns the texture coordinates for the part of the image that should be displayed.
- [func CVOpenGLTextureIsFlipped(CVOpenGLTexture) -> Bool](cvopengltextureisflipped(_:).md)
  Determines whether an OpenGL texture is flipped vertically.
- [func CVOpenGLTextureGetTypeID() -> CFTypeID](cvopengltexturegettypeid().md)
  Obtains the Core Foundation ID for the Core Video OpenGL texture type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturegettarget(_:))*