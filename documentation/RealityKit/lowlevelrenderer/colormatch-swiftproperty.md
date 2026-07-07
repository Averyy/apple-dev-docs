# colorMatch

**Framework**: RealityKit  
**Kind**: property

The active color gamut conversion. The renderer applies this value only when `enableColorMatch` is `true` in `Configuration`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var colorMatch: LowLevelRenderer.ColorMatch { get set }
```

## See Also

- [LowLevelRenderer.ColorMatch](lowlevelrenderer/colormatch-swift.struct.md)
  A color gamut conversion applied during resolve.
- [func setColorMatch(targetingColorSpace: CGColorSpace) throws(LowLevelRendererError)](lowlevelrenderer/setcolormatch(targetingcolorspace:).md)
  Updates the color match by computing a gamut conversion matrix from the renderer’s working color space to the given target display color space.
- [var workingColorSpace: CGColorSpace](lowlevelrenderer/workingcolorspace.md)
  The color space in which the renderer performs all shading calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/colormatch-swift.property)*