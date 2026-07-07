# LowLevelRenderer.ColorMatch

**Framework**: RealityKit  
**Kind**: struct

A color gamut conversion applied during resolve.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ColorMatch
```

#### Overview

The `colorGamutConversion` matrix transforms from the renderer’s working color space to the output display’s color space. Use `LowLevelRenderer.ColorMatch.init(workingColorSpace:targetColorSpace:)` to compute the correct matrix from a `CGColorSpace` pair, rather than constructing it manually.

## Topics

### Creating a color match
- [init(workingColorSpace: CGColorSpace, targetColorSpace: CGColorSpace) throws(LowLevelRendererError)](lowlevelrenderer/colormatch-swift.struct/init(workingcolorspace:targetcolorspace:).md)
  Creates a color match from a working color space and a target display color space.
- [init(colorGamutConversion: simd_half3x3, enableClampValues: Bool)](lowlevelrenderer/colormatch-swift.struct/init(colorgamutconversion:enableclampvalues:).md)
  Creates a color match using an explicit gamut conversion matrix.
### Configuring color matching
- [var colorGamutConversion: simd_half3x3](lowlevelrenderer/colormatch-swift.struct/colorgamutconversion.md)
  A 3×3 half-precision matrix that converts RGB values from the renderer’s working color space to the output display’s color space.
- [var enableClampValues: Bool](lowlevelrenderer/colormatch-swift.struct/enableclampvalues.md)
  A Boolean value that indicates whether output values are clamped to `[0, 1]` after gamut conversion.

## See Also

- [var colorMatch: LowLevelRenderer.ColorMatch](lowlevelrenderer/colormatch-swift.property.md)
  The active color gamut conversion. The renderer applies this value only when `enableColorMatch` is `true` in `Configuration`.
- [func setColorMatch(targetingColorSpace: CGColorSpace) throws(LowLevelRendererError)](lowlevelrenderer/setcolormatch(targetingcolorspace:).md)
  Updates the color match by computing a gamut conversion matrix from the renderer’s working color space to the given target display color space.
- [var workingColorSpace: CGColorSpace](lowlevelrenderer/workingcolorspace.md)
  The color space in which the renderer performs all shading calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/colormatch-swift.struct)*