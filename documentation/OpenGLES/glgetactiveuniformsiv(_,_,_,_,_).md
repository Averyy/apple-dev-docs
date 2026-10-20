# glGetActiveUniformsiv(_:_:_:_:_:)

**Framework**: OpenGL ES  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 7.0+ - Deprecated in 12.0
- iPadOS 7.0+ - Deprecated in 12.0
- Mac Catalyst 7.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func glGetActiveUniformsiv(_ program: GLuint, _ uniformCount: GLsizei, _ uniformIndices: UnsafePointer<GLuint>!, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!)
```

```c
extern void glGetActiveUniformsiv(GLuint program, GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname, GLint *params);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glgetactiveuniformsiv(_:_:_:_:_:))*