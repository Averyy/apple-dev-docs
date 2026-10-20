# colorMatch

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The active color gamut conversion. The renderer applies this value only when `enableColorMatch` is `true` in `Configuration`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final var colorMatch: LowLevelRenderer.ColorMatch { get set }
```

## See Also

### Managing color matching
- [LowLevelRenderer.ColorMatch](./colormatch-swift.struct.md)
  A color gamut conversion applied during resolve.
- [func setColorMatch(targetingColorSpace: CGColorSpace) throws(LowLevelRendererError)](./setcolormatch%28targetingcolorspace%29.md)
  Updates the color match by computing a gamut conversion matrix from the renderer’s working color space to the given target display color space.
- [var workingColorSpace: CGColorSpace](./workingcolorspace.md)
  The color space in which the renderer performs all shading calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/colormatch-swift.property)*