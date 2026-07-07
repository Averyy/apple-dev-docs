# CVOpenGLESTextureIsFlipped(_:)

**Framework**: Core Video  
**Kind**: func

Returns whether the image is flipped vertically or not.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
func CVOpenGLESTextureIsFlipped(_ image: CVOpenGLESTexture) -> Bool
```

#### Return Value

`True` if `{0,0}` represents the upper left of the texture; otherwise `False` if `{0,0}` represents the lower left of the texture.

## Parameters

- `image`: The OpenGLES texture-based image buffer whose orientation is desired.

## See Also

- [func CVOpenGLESTextureGetTarget(CVOpenGLESTexture) -> GLenum](cvopenglestexturegettarget(_:).md)
  Returns the texture target for a `CVOpenGLESTextureRef`.
- [func CVOpenGLESTextureGetName(CVOpenGLESTexture) -> GLuint](cvopenglestexturegetname(_:).md)
  Returns the texture target name for a `CVOpenGLESTextureRef`.
- [func CVOpenGLESTextureGetCleanTexCoords(CVOpenGLESTexture, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>)](cvopenglestexturegetcleantexcoords(_:_:_:_:_:).md)
  Returns convenient normalized texture coordinates for the part of the image that should be displayed.
- [func CVOpenGLESTextureGetTypeID() -> CFTypeID](cvopenglestexturegettypeid().md)
  Returns the Core Foundation type identifier for a Core Video texture-based image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestextureisflipped(_:))*