# glGetBufferPointervOES(_:_:_:)

**Framework**: OpenGL ES  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 2.0+
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func glGetBufferPointervOES(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<UnsafeMutableRawPointer?>!)
```

```c
extern GLvoid glGetBufferPointervOES(GLenum target, GLenum pname, GLvoid **params);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glgetbufferpointervoes(_:_:_:))*