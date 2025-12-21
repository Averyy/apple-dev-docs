# motionVectorScaleY

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The vertical scale factor the denoiser scaler applies to the input motion texture.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var motionVectorScaleY: Float { get set }
```

#### Discussion

The scaler converts the horizontal component of each value in [`motionTexture`](mtlfxtemporaldenoisedscalerbase/motiontexture.md) into fragment (pixel) coordinates by multiplying it by this property’s value.

If you set this property’s value to `1.0`, this denoiser scaler expects that each pixel’s motion vector points to that pixel’s location in the [`colorTexture`](mtlfxtemporaldenoisedscalerbase/colortexture.md) at the time of the last call to encode this scaler’s work. For example, in Metal’s standard device coordinates, where `(0,0)` represents the upper-left corner of the framebuffer, the motion vectors for an object that moves down and to the right in the [`colorTexture`](mtlfxtemporaldenoisedscalerbase/colortexture.md) by `10` pixels would be `(-10,-10)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase/motionvectorscaley)*