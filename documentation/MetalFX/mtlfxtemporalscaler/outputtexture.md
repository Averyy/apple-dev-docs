# outputTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

An output texture that supports the correct depth texture usage options.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
var outputTexture: (any MTLTexture)? { get set }
```

#### Discussion

The texture you set to this property must meet the following requirements:

- The texture’s [`storageMode`](https://developer.apple.com/documentation/Metal/MTLResource/storageMode) property is [`MTLStorageMode.private`](https://developer.apple.com/documentation/Metal/MTLStorageMode/private).
- The texture’s [`usage`](https://developer.apple.com/documentation/Metal/MTLTexture/usage) property uses the [`colorTextureUsage`](mtlfxtemporalscaler/colortextureusage.md) property’s [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage) options as a minimum, and can use additional options.
- The texture’s dimensions is equal to the [`outputWidth`](mtlfxtemporalscaler/outputwidth.md) and [`outputHeight`](mtlfxtemporalscaler/outputheight.md) properties.

## See Also

- [var outputTextureUsage: MTLTextureUsage](mtlfxtemporalscaler/outputtextureusage.md)
  The minimal texture usage options that your app’s output texture must set to apply the temporal scaler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/outputtexture)*