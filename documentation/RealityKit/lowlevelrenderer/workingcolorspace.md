# workingColorSpace

**Framework**: RealityKit  
**Kind**: property

The color space in which the renderer performs all shading calculations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var workingColorSpace: CGColorSpace { get }
```

#### Discussion

Do not assume a fixed working color space. Query this property and pass its value as `workingColorSpace:` to `ColorMatch.init(workingColorSpace:targetColorSpace:)` to compute a correct gamut conversion matrix.

## See Also

- [var colorMatch: LowLevelRenderer.ColorMatch](lowlevelrenderer/colormatch-swift.property.md)
  The active color gamut conversion. The renderer applies this value only when `enableColorMatch` is `true` in `Configuration`.
- [LowLevelRenderer.ColorMatch](lowlevelrenderer/colormatch-swift.struct.md)
  A color gamut conversion applied during resolve.
- [func setColorMatch(targetingColorSpace: CGColorSpace) throws(LowLevelRendererError)](lowlevelrenderer/setcolormatch(targetingcolorspace:).md)
  Updates the color match by computing a gamut conversion matrix from the renderer’s working color space to the given target display color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/workingcolorspace)*