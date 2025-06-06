# reactiveTextureUsage

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The minimal texture-usage options that your app’s reactive-mask texture input needs to have for the temporal scaler.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+

## Declaration

```swift
var reactiveTextureUsage: MTLTextureUsage { get }
```

#### Discussion

The input texture you set to the [`reactiveMaskTexture`](mtlfxtemporalscaler/reactivemasktexture.md) property needs to use the same set as, or a superset of, the [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage) options of this property.

## See Also

- [var reactiveMaskTexture: (any MTLTexture)?](mtlfxtemporalscaler/reactivemasktexture.md)
  A reactive-mask texture input you set for a temporal scaler that supports the correct usage options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/reactivetextureusage)*