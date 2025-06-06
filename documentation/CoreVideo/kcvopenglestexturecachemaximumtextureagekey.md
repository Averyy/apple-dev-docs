# kCVOpenGLESTextureCacheMaximumTextureAgeKey

**Framework**: Core Video  
**Kind**: var

By default, textures will age out after one second. Setting a maximum texture age of zero will disable the age-out mechanism completely. The [`CVOpenGLESTextureCacheFlush(_:_:)`](cvopenglestexturecacheflush(_:_:).md) function can be used to force eviction in either case.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
let kCVOpenGLESTextureCacheMaximumTextureAgeKey: CFString
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvopenglestexturecachemaximumtextureagekey)*