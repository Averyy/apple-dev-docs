# glGetSyncivAPPLE(_:_:_:_:_:)

**Framework**: OpenGL ES  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 6.0+ - Deprecated in 12.0
- iPadOS 6.0+ - Deprecated in 12.0
- Mac Catalyst 6.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func glGetSyncivAPPLE(_ sync: GLsync!, _ pname: GLenum, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ values: UnsafeMutablePointer<GLint>!)
```

```c
extern void glGetSyncivAPPLE(GLsync sync, GLenum pname, GLsizei bufSize, GLsizei *length, GLint *values);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glgetsyncivapple(_:_:_:_:_:))*