# motionVectorScaleY

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The vertical scale factor the frame interpolator applies to the input motion texture.

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

The frame interpolator converts the horizontal component of each value in [`motionTexture`](mtlfxframeinterpolatorbase/motiontexture.md) into fragment (pixel) coordinates by multiplying it by this property’s value.

If you set this property’s value to `1.0`, this interpolator expects that each pixel’s motion vector points to the location where that pixel is in the [`prevColorTexture`](mtlfxframeinterpolatorbase/prevcolortexture.md). For example, in Metal’s standard device coordinates where `(0,0)` represents the upper-left corner of the framebuffer, the motion vectors for an object that moves down and to the right in the [`colorTexture`](mtlfxframeinterpolatorbase/colortexture.md) by `10` pixels would be `(-10,-10)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/motionvectorscaley)*