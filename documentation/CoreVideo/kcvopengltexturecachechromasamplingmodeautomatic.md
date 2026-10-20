# kCVOpenGLTextureCacheChromaSamplingModeAutomatic

**Framework**: Core Video  
**Kind**: var  
**Role**: Global Variable

The default mode if not otherwise specified.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
let kCVOpenGLTextureCacheChromaSamplingModeAutomatic: CFString
```

```c
extern CFStringRef const kCVOpenGLTextureCacheChromaSamplingModeAutomatic;
```

## See Also

### Values
- [let kCVOpenGLTextureCacheChromaSamplingModeHighestQuality: CFString](./kcvopengltexturecachechromasamplingmodehighestquality.md)
  Forces the highest quality regardless of performance impact.
- [let kCVOpenGLTextureCacheChromaSamplingModeBestPerformance: CFString](./kcvopengltexturecachechromasamplingmodebestperformance.md)
  Set the chroma sample mode to use the most performant way possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvopengltexturecachechromasamplingmodeautomatic)*