# enableClampValues

**Framework**: RealityKit  
**Kind**: property

A Boolean value that indicates whether output values are clamped to `[0, 1]` after gamut conversion.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var enableClampValues: Bool { get set }
```

#### Discussion

Set this to `true` when the output texture uses a non-extended pixel format.

## See Also

- [var colorGamutConversion: simd_half3x3](lowlevelrenderer/colormatch-swift.struct/colorgamutconversion.md)
  A 3×3 half-precision matrix that converts RGB values from the renderer’s working color space to the output display’s color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/colormatch-swift.struct/enableclampvalues)*