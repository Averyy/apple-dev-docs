# CVOpenGLESTextureGetTypeID()

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the Core Foundation type identifier for a Core Video texture-based image buffer.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLESTextureGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CVOpenGLESTextureGetTypeID();
```

## Return Value

The Core Foundation type identifier for the `CVOpenGLESTextureRef` type.

## See Also

### Inspecting Textures
- [func CVOpenGLESTextureGetTarget(CVOpenGLESTexture) -> GLenum](./cvopenglestexturegettarget%28_%29.md)
  Returns the texture target for a `CVOpenGLESTextureRef`.
- [func CVOpenGLESTextureGetName(CVOpenGLESTexture) -> GLuint](./cvopenglestexturegetname%28_%29.md)
  Returns the texture target name for a `CVOpenGLESTextureRef`.
- [func CVOpenGLESTextureGetCleanTexCoords(CVOpenGLESTexture, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>)](./cvopenglestexturegetcleantexcoords%28_,_,_,_,_%29.md)
  Returns convenient normalized texture coordinates for the part of the image that should be displayed.
- [func CVOpenGLESTextureIsFlipped(CVOpenGLESTexture) -> Bool](./cvopenglestextureisflipped%28_%29.md)
  Returns whether the image is flipped vertically or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestexturegettypeid())*