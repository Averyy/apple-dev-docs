# glShaderBinary(_:_:_:_:_:)

**Framework**: OpenGL ES  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 3.0+ - Deprecated in 12.0
- iPadOS 3.0+ - Deprecated in 12.0
- Mac Catalyst 3.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func glShaderBinary(_ n: GLsizei, _ shaders: UnsafePointer<GLuint>!, _ binaryformat: GLenum, _ binary: UnsafeRawPointer!, _ length: GLsizei)
```

```c
extern void glShaderBinary(GLsizei n, const GLuint *shaders, GLenum binaryformat, const GLvoid *binary, GLsizei length);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glshaderbinary(_:_:_:_:_:))*