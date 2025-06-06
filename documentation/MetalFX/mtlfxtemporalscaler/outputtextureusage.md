# outputTextureUsage

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The minimal texture usage options that your app’s output texture must set to apply the temporal scaler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
var outputTextureUsage: MTLTextureUsage { get }
```

#### Discussion

The texture your app sets to the [`outputTexture`](mtlfxtemporalscaler/outputtexture.md) property must use the same set (or a superset) of the [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage) options in this property.

## See Also

- [var outputTexture: (any MTLTexture)?](mtlfxtemporalscaler/outputtexture.md)
  An output texture that supports the correct depth texture usage options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/outputtextureusage)*