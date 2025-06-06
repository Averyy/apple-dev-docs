# kCVMetalTextureCacheMaximumTextureAgeKey

**Framework**: Core Video  
**Kind**: var

The length of time, in seconds, before the cache is automatically evicted.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let kCVMetalTextureCacheMaximumTextureAgeKey: CFString
```

#### Discussion

The default value is `1`. To disable the age-out mechanism completely, set a maximum texture age of `0`. The cache can be manually evicted with [`CVMetalTextureCacheFlush(_:_:)`](cvmetaltexturecacheflush(_:_:).md).

## See Also

- [let kCVMetalTextureUsage: CFString](kcvmetaltextureusage.md)
  The set of options that define how you can use a texture on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvmetaltexturecachemaximumtextureagekey)*