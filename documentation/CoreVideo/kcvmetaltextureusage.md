# kCVMetalTextureUsage

**Framework**: Core Video  
**Kind**: var

The set of options that define how you can use a texture on the GPU.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
let kCVMetalTextureUsage: CFString
```

#### Discussion

The default value is [`unknown`](https://developer.apple.com/documentation/Metal/MTLTextureUsage/unknown). Use only values which are valid for [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage).

## See Also

- [let kCVMetalTextureCacheMaximumTextureAgeKey: CFString](kcvmetaltexturecachemaximumtextureagekey.md)
  The length of time, in seconds, before the cache is automatically evicted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvmetaltextureusage)*