# setColorMatch(targetingColorSpace:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Updates the color match by computing a gamut conversion matrix from the renderer’s working color space to the given target display color space.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func setColorMatch(targetingColorSpace targetColorSpace: CGColorSpace) throws(LowLevelRendererError)
```

#### Discussion

> **Throws**: [`LowLevelRendererError`](../lowlevelrenderererror.md) if the target color space is not a supported linear gamut.

## Parameters

- `targetColorSpace`: The target display color space to convert to.

## See Also

### Managing color matching
- [var colorMatch: LowLevelRenderer.ColorMatch](./colormatch-swift.property.md)
  The active color gamut conversion. The renderer applies this value only when `enableColorMatch` is `true` in `Configuration`.
- [LowLevelRenderer.ColorMatch](./colormatch-swift.struct.md)
  A color gamut conversion applied during resolve.
- [var workingColorSpace: CGColorSpace](./workingcolorspace.md)
  The color space in which the renderer performs all shading calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/setcolormatch(targetingcolorspace:))*