# CVOpenGLESTextureGetName(_:)

**Framework**: Core Video  
**Kind**: func

Returns the texture target name for a `CVOpenGLESTextureRef`.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
func CVOpenGLESTextureGetName(_ image: CVOpenGLESTexture) -> GLuint
```

#### Return Value

An OpenGLES texture target name associated with the texture referenced by the `image` parameter.

## Parameters

- `image`: The OpenGLES texture-based image buffer whose target name is desired.

## See Also

- [func CVOpenGLESTextureGetTarget(CVOpenGLESTexture) -> GLenum](cvopenglestexturegettarget(_:).md)
  Returns the texture target for a `CVOpenGLESTextureRef`.
- [func CVOpenGLESTextureGetCleanTexCoords(CVOpenGLESTexture, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>)](cvopenglestexturegetcleantexcoords(_:_:_:_:_:).md)
  Returns convenient normalized texture coordinates for the part of the image that should be displayed.
- [func CVOpenGLESTextureIsFlipped(CVOpenGLESTexture) -> Bool](cvopenglestextureisflipped(_:).md)
  Returns whether the image is flipped vertically or not.
- [func CVOpenGLESTextureGetTypeID() -> CFTypeID](cvopenglestexturegettypeid().md)
  Returns the Core Foundation type identifier for a Core Video texture-based image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestexturegetname(_:))*