# denoiseStrengthMaskTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The denoise strength mask texture this scaler evaluates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var denoiseStrengthMaskTexture: (any MTLTexture)? { get set }
```

#### Discussion

Use this single-channel texture to mark, at a per-pixel level, areas that this denoiser ignores. To configure a pixel that the denoiser ignores, provide `1.0` as the value at that pixel’s corresponding location on this texture.

You are responsible for ensuring the usage and pixel format of the texture you assign to this property matches the texture usage [`denoiseStrengthMaskTextureUsage`](mtlfxtemporaldenoisedscalerbase/denoisestrengthmasktextureusage.md) requests and the pixel format that [`denoiseStrengthMaskTextureFormat`](mtlfxtemporaldenoisedscalerdescriptor/denoisestrengthmasktextureformat.md) requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase/denoisestrengthmasktexture)*