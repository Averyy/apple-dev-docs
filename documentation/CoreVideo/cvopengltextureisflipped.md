# CVOpenGLTextureIsFlipped(_:)

**Framework**: Core Video  
**Kind**: func

Determines whether an OpenGL texture is flipped vertically.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLTextureIsFlipped(_ image: CVOpenGLTexture) -> Bool
```

#### Return Value

Returns `true` if (0,0) in the texture is in the upper-left corner, and `false` if (0,0) is in the lower-left corner.

#### Discussion

Quartz assumes a lower-left origin.

## Parameters

- `image`: The Core Video OpenGL texture whose vertical orientation you want to determine.

## See Also

- [func CVOpenGLTextureGetName(CVOpenGLTexture) -> GLuint](cvopengltexturegetname(_:).md)
  Returns the texture target name of a CoreVideo OpenGL texture.
- [func CVOpenGLTextureGetTarget(CVOpenGLTexture) -> GLenum](cvopengltexturegettarget(_:).md)
  Returns the texture target (for example, `GL_TEXTURE_2D`) of an OpenGL texture.
- [func CVOpenGLTextureGetCleanTexCoords(CVOpenGLTexture, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>)](cvopengltexturegetcleantexcoords(_:_:_:_:_:).md)
  Returns the texture coordinates for the part of the image that should be displayed.
- [func CVOpenGLTextureGetTypeID() -> CFTypeID](cvopengltexturegettypeid().md)
  Obtains the Core Foundation ID for the Core Video OpenGL texture type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltextureisflipped(_:))*