# init(workingColorSpace:targetColorSpace:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a color match from a working color space and a target display color space.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(workingColorSpace: CGColorSpace, targetColorSpace: CGColorSpace) throws(LowLevelRendererError)
```

## Discussion

> **Throws**: [`LowLevelRendererError`](../../lowlevelrenderererror.md) if either color space is not a supported linear gamut.

## Parameters

- `workingColorSpace`: The color space in which the renderer performs shading calculations.
- `targetColorSpace`: The color space of the output display to convert to.

## See Also

### Creating a color match
- [init(colorGamutConversion: simd_half3x3, enableClampValues: Bool)](./init%28colorgamutconversion,enableclampvalues%29.md)
  Creates a color match using an explicit gamut conversion matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/colormatch-swift.struct/init(workingcolorspace:targetcolorspace:))*