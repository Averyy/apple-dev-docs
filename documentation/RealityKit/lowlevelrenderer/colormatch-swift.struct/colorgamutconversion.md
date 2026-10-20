# colorGamutConversion

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A 3×3 half-precision matrix that converts RGB values from the renderer’s working color space to the output display’s color space.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var colorGamutConversion: simd_half3x3 { get set }
```

## See Also

### Configuring color matching
- [var enableClampValues: Bool](./enableclampvalues.md)
  A Boolean value that indicates whether output values are clamped to `[0, 1]` after gamut conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/colormatch-swift.struct/colorgamutconversion)*