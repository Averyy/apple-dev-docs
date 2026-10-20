# glGetInternalformativ(_:_:_:_:_:)

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
func glGetInternalformativ(_ target: GLenum, _ internalformat: GLenum, _ pname: GLenum, _ bufSize: GLsizei, _ params: UnsafeMutablePointer<GLint>!)
```

```c
extern void glGetInternalformativ(GLenum target, GLenum internalformat, GLenum pname, GLsizei bufSize, GLint *params);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glgetinternalformativ(_:_:_:_:_:))*