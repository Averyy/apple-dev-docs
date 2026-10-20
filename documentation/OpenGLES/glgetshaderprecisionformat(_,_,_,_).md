# glGetShaderPrecisionFormat(_:_:_:_:)

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
func glGetShaderPrecisionFormat(_ shadertype: GLenum, _ precisiontype: GLenum, _ range: UnsafeMutablePointer<GLint>!, _ precision: UnsafeMutablePointer<GLint>!)
```

```c
extern void glGetShaderPrecisionFormat(GLenum shadertype, GLenum precisiontype, GLint *range, GLint *precision);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glgetshaderprecisionformat(_:_:_:_:))*