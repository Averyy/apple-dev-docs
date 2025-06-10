# exposureTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The exposure texture this scaler uses.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var exposureTexture: (any MTLTexture)? { get set }
```

#### Discussion

Create and assign a 1x1  `MTLPixelFormatR16Float`  texture to assign to this property. MetalFX reads the R channel of the texel at position `(0,0)` and uses it as the exposure value. It then uses this value to multiply the input color.

For best performance, use the GPU to generate the exposure value and store it into this texture.

> **Note**: The temporal scaler ignores this property if you create it with a descriptor that has its [`isAutoExposureEnabled`](mtlfxtemporalscalerdescriptor/isautoexposureenabled.md) property set to [`true`](https://developer.apple.com/documentation/swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase/exposuretexture)*