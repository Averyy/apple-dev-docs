# glGetUniformIndices(_:_:_:_:)

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
func glGetUniformIndices(_ program: GLuint, _ uniformCount: GLsizei, _ uniformNames: UnsafePointer<UnsafePointer<GLchar>?>!, _ uniformIndices: UnsafeMutablePointer<GLuint>!)
```

```c
extern void glGetUniformIndices(GLuint program, GLsizei uniformCount, const GLchar * const*uniformNames, GLuint *uniformIndices);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glgetuniformindices(_:_:_:_:))*