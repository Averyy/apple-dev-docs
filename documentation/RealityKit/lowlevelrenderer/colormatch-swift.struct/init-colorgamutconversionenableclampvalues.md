# init(colorGamutConversion:enableClampValues:)

**Framework**: RealityKit  
**Kind**: init

Creates a color match using an explicit gamut conversion matrix.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(colorGamutConversion: simd_half3x3 = matrix_identity_half3x3, enableClampValues: Bool = false)
```

## Parameters

- `colorGamutConversion`: A 3×3 matrix that converts RGB values from the renderer’s working color space to the output display’s color space. Defaults to identity.
- `enableClampValues`: If `true`, output values are clamped to `[0, 1]` after gamut conversion. Defaults to `false`.

## See Also

- [init(workingColorSpace: CGColorSpace, targetColorSpace: CGColorSpace) throws(LowLevelRendererError)](lowlevelrenderer/colormatch-swift.struct/init(workingcolorspace:targetcolorspace:).md)
  Creates a color match from a working color space and a target display color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/colormatch-swift.struct/init(colorgamutconversion:enableclampvalues:))*