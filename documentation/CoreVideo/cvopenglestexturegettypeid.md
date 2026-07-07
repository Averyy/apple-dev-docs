# CVOpenGLESTextureGetTypeID()

**Framework**: Core Video  
**Kind**: func

Returns the Core Foundation type identifier for a Core Video texture-based image buffer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
func CVOpenGLESTextureGetTypeID() -> CFTypeID
```

#### Return Value

The Core Foundation type identifier for the `CVOpenGLESTextureRef` type.

## See Also

- [func CVOpenGLESTextureGetTarget(CVOpenGLESTexture) -> GLenum](cvopenglestexturegettarget(_:).md)
  Returns the texture target for a `CVOpenGLESTextureRef`.
- [func CVOpenGLESTextureGetName(CVOpenGLESTexture) -> GLuint](cvopenglestexturegetname(_:).md)
  Returns the texture target name for a `CVOpenGLESTextureRef`.
- [func CVOpenGLESTextureGetCleanTexCoords(CVOpenGLESTexture, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>)](cvopenglestexturegetcleantexcoords(_:_:_:_:_:).md)
  Returns convenient normalized texture coordinates for the part of the image that should be displayed.
- [func CVOpenGLESTextureIsFlipped(CVOpenGLESTexture) -> Bool](cvopenglestextureisflipped(_:).md)
  Returns whether the image is flipped vertically or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestexturegettypeid())*