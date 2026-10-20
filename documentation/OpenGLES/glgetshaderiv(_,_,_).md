# glGetShaderiv(_:_:_:)

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
func glGetShaderiv(_ shader: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!)
```

```c
extern void glGetShaderiv(GLuint shader, GLenum pname, GLint *params);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glgetshaderiv(_:_:_:))*