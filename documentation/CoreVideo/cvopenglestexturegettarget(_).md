# CVOpenGLESTextureGetTarget(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the texture target for a `CVOpenGLESTextureRef`.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLESTextureGetTarget(_ image: CVOpenGLESTexture) -> GLenum
```

```c
extern GLenum CVOpenGLESTextureGetTarget(CVOpenGLESTextureRef image);
```

## Return Value

An OpenGLES texture target, such as `GL_TEXTURE_2D`.

## Parameters

- `image`: The OpenGLES texture-based image buffer whose target is desired.

## See Also

### Inspecting Textures
- [func CVOpenGLESTextureGetName(CVOpenGLESTexture) -> GLuint](./cvopenglestexturegetname%28_%29.md)
  Returns the texture target name for a `CVOpenGLESTextureRef`.
- [func CVOpenGLESTextureGetCleanTexCoords(CVOpenGLESTexture, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>)](./cvopenglestexturegetcleantexcoords%28_,_,_,_,_%29.md)
  Returns convenient normalized texture coordinates for the part of the image that should be displayed.
- [func CVOpenGLESTextureIsFlipped(CVOpenGLESTexture) -> Bool](./cvopenglestextureisflipped%28_%29.md)
  Returns whether the image is flipped vertically or not.
- [func CVOpenGLESTextureGetTypeID() -> CFTypeID](./cvopenglestexturegettypeid%28%29.md)
  Returns the Core Foundation type identifier for a Core Video texture-based image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestexturegettarget(_:))*