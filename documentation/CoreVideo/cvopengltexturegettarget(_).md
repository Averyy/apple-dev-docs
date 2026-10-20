# CVOpenGLTextureGetTarget(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the texture target (for example, `GL_TEXTURE_2D`) of an OpenGL texture.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLTextureGetTarget(_ image: CVOpenGLTexture) -> GLenum
```

```c
extern GLenum CVOpenGLTextureGetTarget(CVOpenGLTextureRef image);
```

#### Return Value

The OpenGL texture target.

#### Discussion

See the [OpenGL specification](http://www.opengl.org/documentation/) for more information about texture targets.

## Parameters

- `image`: The Core Video OpenGL texture whose target you want to obtain.

## See Also

### Inspecting Textures
- [func CVOpenGLTextureGetName(CVOpenGLTexture) -> GLuint](./cvopengltexturegetname%28_%29.md)
  Returns the texture target name of a CoreVideo OpenGL texture.
- [func CVOpenGLTextureGetCleanTexCoords(CVOpenGLTexture, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>)](./cvopengltexturegetcleantexcoords%28_,_,_,_,_%29.md)
  Returns the texture coordinates for the part of the image that should be displayed.
- [func CVOpenGLTextureIsFlipped(CVOpenGLTexture) -> Bool](./cvopengltextureisflipped%28_%29.md)
  Determines whether an OpenGL texture is flipped vertically.
- [func CVOpenGLTextureGetTypeID() -> CFTypeID](./cvopengltexturegettypeid%28%29.md)
  Obtains the Core Foundation ID for the Core Video OpenGL texture type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturegettarget(_:))*