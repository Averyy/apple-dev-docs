# outputTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The output texture into which this denoiser scaler writes its output.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var outputTexture: (any MTLTexture)? { get set }
```

#### Discussion

You are responsible for providing a texture with a private `storageMode` to this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase/outputtexture)*