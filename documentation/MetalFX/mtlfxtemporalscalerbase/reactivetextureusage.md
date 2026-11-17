# reactiveTextureUsage

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The minimal texture-usage options that your app’s reactive-mask texture input needs to have for the temporal scaler.

**Availability**:
- iOS 17.4+ - Deprecated in 27.0
- iPadOS 17.4+ - Deprecated in 27.0
- Mac Catalyst 17.4+ - Deprecated in 27.0
- macOS 14.4+ - Deprecated in 27.0
- tvOS 17.4+ - Deprecated in 27.0
- visionOS 1.1+ - Deprecated in 27.0

## Declaration

```swift
var reactiveTextureUsage: MTLTextureUsage { get }
```

```objc
@property (nonatomic, readonly) MTLTextureUsage reactiveTextureUsage;
```

## Discussion

The input texture you set to the [`reactiveMaskTexture`](./reactivemasktexture.md) property needs to use the same set as, or a superset of, the [`MTLTextureUsage`](../../Metal/mtltextureusage.md) options of this property.

## See Also

### Configuring the reactive mask input
- [var reactiveMaskTexture: (any MTLTexture)?](./reactivemasktexture.md)
  A reactive-mask texture input you set for a temporal scaler that supports the correct usage options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase/reactivetextureusage)*