# exposureTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

An exposure texture that this denoiser scaler evaluates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var exposureTexture: (any MTLTexture)? { get set }
```

#### Discussion

Create and assign a 1x1  `MTLPixelFormatR16Float`  texture to assign to this property. MetalFX reads the R channel of the texel at position `(0,0)` and uses it as the exposure value. It then uses this value to multiply the input color.

For best performance, use the GPU to generate the exposure value and store it into this texture.

> **Note**: The temporal scaler ignores this property if you create it with a descriptor that has its [`isAutoExposureEnabled`](mtlfxtemporalscalerdescriptor/isautoexposureenabled.md) property set to [`true`](https://developer.apple.com/documentation/Swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase/exposuretexture)*