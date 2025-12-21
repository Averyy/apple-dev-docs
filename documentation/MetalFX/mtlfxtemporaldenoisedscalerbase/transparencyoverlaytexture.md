# transparencyOverlayTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The transparency overlay texture that this scaler evaluates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var transparencyOverlayTexture: (any MTLTexture)? { get set }
```

#### Discussion

Use this RGBA texture to provide to the denoiser an overlay with your transparent pixels, such as the output of your particle systems. MetalFX interprets this to be a texture in linear color space, with the RGB channels ranging between `0` and infinity, and the alpha channel in the range `[0,1]`, representing the opacity of the pixel.

You are responsible for ensuring the usage and pixel format of the texture you assign to this property matches the texture usage [`transparencyOverlayTextureUsage`](mtlfxtemporaldenoisedscalerbase/transparencyoverlaytextureusage.md) requests and the pixel format that [`transparencyOverlayTextureFormat`](mtlfxtemporaldenoisedscalerdescriptor/transparencyoverlaytextureformat.md) requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase/transparencyoverlaytexture)*