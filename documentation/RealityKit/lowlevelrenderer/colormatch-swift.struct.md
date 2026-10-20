# LowLevelRenderer.ColorMatch

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A color gamut conversion applied during resolve.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ColorMatch
```

#### Overview

The `colorGamutConversion` matrix transforms from the renderer’s working color space to the output display’s color space. Use `LowLevelRenderer.ColorMatch.init(workingColorSpace:targetColorSpace:)` to compute the correct matrix from a `CGColorSpace` pair, rather than constructing it manually.

## Topics

### Creating a color match
- [init(workingColorSpace: CGColorSpace, targetColorSpace: CGColorSpace) throws(LowLevelRendererError)](./colormatch-swift.struct/init%28workingcolorspace,targetcolorspace%29.md)
  Creates a color match from a working color space and a target display color space.
- [init(colorGamutConversion: simd_half3x3, enableClampValues: Bool)](./colormatch-swift.struct/init%28colorgamutconversion,enableclampvalues%29.md)
  Creates a color match using an explicit gamut conversion matrix.
### Configuring color matching
- [var colorGamutConversion: simd_half3x3](./colormatch-swift.struct/colorgamutconversion.md)
  A 3×3 half-precision matrix that converts RGB values from the renderer’s working color space to the output display’s color space.
- [var enableClampValues: Bool](./colormatch-swift.struct/enableclampvalues.md)
  A Boolean value that indicates whether output values are clamped to `[0, 1]` after gamut conversion.

## See Also

### Managing color matching
- [var colorMatch: LowLevelRenderer.ColorMatch](./colormatch-swift.property.md)
  The active color gamut conversion. The renderer applies this value only when `enableColorMatch` is `true` in `Configuration`.
- [func setColorMatch(targetingColorSpace: CGColorSpace) throws(LowLevelRendererError)](./setcolormatch%28targetingcolorspace%29.md)
  Updates the color match by computing a gamut conversion matrix from the renderer’s working color space to the given target display color space.
- [var workingColorSpace: CGColorSpace](./workingcolorspace.md)
  The color space in which the renderer performs all shading calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/colormatch-swift.struct)*