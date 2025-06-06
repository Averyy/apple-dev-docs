# CVOpenGLESTextureGetCleanTexCoords(_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Returns convenient normalized texture coordinates for the part of the image that should be displayed.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
func CVOpenGLESTextureGetCleanTexCoords(_ image: CVOpenGLESTexture, _ lowerLeft: UnsafeMutablePointer<GLfloat>, _ lowerRight: UnsafeMutablePointer<GLfloat>, _ upperRight: UnsafeMutablePointer<GLfloat>, _ upperLeft: UnsafeMutablePointer<GLfloat>)
```

#### Discussion

This function automatically takes into account whether or not the texture is flipped.

## Parameters

- `image`: The OpenGLES texture-based image buffer whose normalized texture coordinates are desired.
- `lowerLeft`: An array of two  s where the   and   normalized texture coordinates of the lower left corner of the image will be stored.
- `lowerRight`: An array of two  s where the   and   normalized texture coordinates of the lower right corner of the image will be stored.
- `upperRight`: An array of two  s where the   and   normalized texture coordinates of the upper right corner of the image will be stored.
- `upperLeft`: An array of two  s where the   and   normalized texture coordinates of the upper left corner of the image will be stored.

## See Also

- [func CVOpenGLESTextureGetTarget(CVOpenGLESTexture) -> GLenum](cvopenglestexturegettarget(_:).md)
  Returns the texture target for a `CVOpenGLESTextureRef`.
- [func CVOpenGLESTextureGetName(CVOpenGLESTexture) -> GLuint](cvopenglestexturegetname(_:).md)
  Returns the texture target name for a `CVOpenGLESTextureRef`.
- [func CVOpenGLESTextureIsFlipped(CVOpenGLESTexture) -> Bool](cvopenglestextureisflipped(_:).md)
  Returns whether the image is flipped vertically or not.
- [func CVOpenGLESTextureGetTypeID() -> CFTypeID](cvopenglestexturegettypeid().md)
  Returns the Core Foundation type identifier for a Core Video texture-based image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestexturegetcleantexcoords(_:_:_:_:_:))*