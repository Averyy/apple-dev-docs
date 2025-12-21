# outputTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The output texture into which this denoiser scaler writes its output.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var outputTexture: (any MTLTexture)? { get set }
```

#### Discussion

You are responsible for providing a texture with a private `storageMode` to this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase/outputtexture)*