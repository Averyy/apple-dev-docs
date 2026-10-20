# CVOpenGLESTextureGetCleanTexCoords(_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns convenient normalized texture coordinates for the part of the image that should be displayed.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLESTextureGetCleanTexCoords(_ image: CVOpenGLESTexture, _ lowerLeft: UnsafeMutablePointer<GLfloat>, _ lowerRight: UnsafeMutablePointer<GLfloat>, _ upperRight: UnsafeMutablePointer<GLfloat>, _ upperLeft: UnsafeMutablePointer<GLfloat>)
```

```c
extern void CVOpenGLESTextureGetCleanTexCoords(CVOpenGLESTextureRef image, GLfloat lowerLeft[2], GLfloat lowerRight[2], GLfloat upperRight[2], GLfloat upperLeft[2]);
```

#### Discussion

This function automatically takes into account whether or not the texture is flipped.

## Parameters

- `image`: The OpenGLES texture-based image buffer whose normalized texture coordinates are desired.
- `lowerLeft`: An array of two `GLfloat`s where the `s` and `t` normalized texture coordinates of the lower left corner of the image will be stored.
- `lowerRight`: An array of two `GLfloat`s where the `s` and `t` normalized texture coordinates of the lower right corner of the image will be stored.
- `upperRight`: An array of two `GLfloat`s where the `s` and `t` normalized texture coordinates of the upper right corner of the image will be stored.
- `upperLeft`: An array of two `GLfloat`s where the `s` and `t` normalized texture coordinates of the upper left corner of the image will be stored.

## See Also

### Inspecting Textures
- [func CVOpenGLESTextureGetTarget(CVOpenGLESTexture) -> GLenum](./cvopenglestexturegettarget%28_%29.md)
  Returns the texture target for a `CVOpenGLESTextureRef`.
- [func CVOpenGLESTextureGetName(CVOpenGLESTexture) -> GLuint](./cvopenglestexturegetname%28_%29.md)
  Returns the texture target name for a `CVOpenGLESTextureRef`.
- [func CVOpenGLESTextureIsFlipped(CVOpenGLESTexture) -> Bool](./cvopenglestextureisflipped%28_%29.md)
  Returns whether the image is flipped vertically or not.
- [func CVOpenGLESTextureGetTypeID() -> CFTypeID](./cvopenglestexturegettypeid%28%29.md)
  Returns the Core Foundation type identifier for a Core Video texture-based image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestexturegetcleantexcoords(_:_:_:_:_:))*