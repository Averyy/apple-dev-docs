# CVOpenGLTextureIsFlipped(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Determines whether an OpenGL texture is flipped vertically.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLTextureIsFlipped(_ image: CVOpenGLTexture) -> Bool
```

```c
extern Boolean CVOpenGLTextureIsFlipped(CVOpenGLTextureRef image);
```

#### Return Value

Returns `true` if (0,0) in the texture is in the upper-left corner, and `false` if (0,0) is in the lower-left corner.

#### Discussion

Quartz assumes a lower-left origin.

## Parameters

- `image`: The Core Video OpenGL texture whose vertical orientation you want to determine.

## See Also

### Inspecting Textures
- [func CVOpenGLTextureGetName(CVOpenGLTexture) -> GLuint](./cvopengltexturegetname%28_%29.md)
  Returns the texture target name of a CoreVideo OpenGL texture.
- [func CVOpenGLTextureGetTarget(CVOpenGLTexture) -> GLenum](./cvopengltexturegettarget%28_%29.md)
  Returns the texture target (for example, `GL_TEXTURE_2D`) of an OpenGL texture.
- [func CVOpenGLTextureGetCleanTexCoords(CVOpenGLTexture, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>)](./cvopengltexturegetcleantexcoords%28_,_,_,_,_%29.md)
  Returns the texture coordinates for the part of the image that should be displayed.
- [func CVOpenGLTextureGetTypeID() -> CFTypeID](./cvopengltexturegettypeid%28%29.md)
  Obtains the Core Foundation ID for the Core Video OpenGL texture type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltextureisflipped(_:))*