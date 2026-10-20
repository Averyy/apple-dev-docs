# kCVOpenGLESTextureCacheMaximumTextureAgeKey

**Framework**: Core Video  
**Kind**: var  
**Role**: Global Variable

By default, textures will age out after one second. Setting a maximum texture age of zero will disable the age-out mechanism completely. The [`CVOpenGLESTextureCacheFlush(_:_:)`](./cvopenglestexturecacheflush%28_,_%29.md) function can be used to force eviction in either case.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
let kCVOpenGLESTextureCacheMaximumTextureAgeKey: CFString
```

```c
extern CFStringRef const kCVOpenGLESTextureCacheMaximumTextureAgeKey;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvopenglestexturecachemaximumtextureagekey)*