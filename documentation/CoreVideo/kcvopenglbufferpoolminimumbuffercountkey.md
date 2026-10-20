# kCVOpenGLBufferPoolMinimumBufferCountKey

**Framework**: Core Video  
**Kind**: var  
**Role**: Global Variable

The minimum number of buffers to be kept in the pool (type `CFNumber`).

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
let kCVOpenGLBufferPoolMinimumBufferCountKey: CFString
```

```c
extern CFStringRef const kCVOpenGLBufferPoolMinimumBufferCountKey;
```

## See Also

### Constants
- [let kCVOpenGLBufferPoolMaximumBufferAgeKey: CFString](./kcvopenglbufferpoolmaximumbufferagekey.md)
  The maximum time that unused buffers should be kept before they are deallocated (type `CFAbsoluteTime`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvopenglbufferpoolminimumbuffercountkey)*