# vImageCreateGammaFunction(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a gamma function object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageCreateGammaFunction(_ gamma: Float, _ gamma_type: Int32, _ flags: vImage_Flags) -> GammaFunction!
```

#### Return Value

A gamma function object that encapsulates a gamma value, a gamma function type, and option flags.

#### Discussion

Use this function to create a gamma function object that you pass to [`vImageGamma_Planar8toPlanarF(_:_:_:_:)`](vimagegamma_planar8toplanarf(_:_:_:_:).md), [`vImageGamma_PlanarFtoPlanar8(_:_:_:_:)`](vimagegamma_planarftoplanar8(_:_:_:_:).md), or [`vImageGamma_PlanarF(_:_:_:_:)`](vimagegamma_planarf(_:_:_:_:).md).

The vImage library provides a user-defined half-precision gamma type and constant half-precision gamma types, such as [`kvImageGamma_sRGB_forward_half_precision`](kvimagegamma_srgb_forward_half_precision.md). Use a half-precision gamma type when creating a gamma function for image data that’s intended for conversion to 8-bit. The half-precision gamma types work with floating-point values in the range `0...1` and provide a precision of ±1 / 4,096.

The gamma correction functions that use a [`GammaFunction`](gammafunction.md) object are symmetric around zero. That is, they treat negative values as if they’re positive, and restore the sign after applying the exponent.

## Parameters

- `gamma`: The gamma value when   is   or  .
- `gamma_type`: A constant that specifies the gamma type. See  .
- `flags`: Reserved for future use. Pass  .

## See Also

- [Gamma function types](1584480-gamma-function-types.md)
  Types of full- or half-precision gamma functions.
- [func vImageGamma_Planar8toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, GammaFunction!, vImage_Flags) -> vImage_Error](vimagegamma_planar8toplanarf(_:_:_:_:).md)
  Applies a gamma function to an 8-bit planar image to produce a 32-bit planar image.
- [func vImageGamma_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, GammaFunction!, vImage_Flags) -> vImage_Error](vimagegamma_planarftoplanar8(_:_:_:_:).md)
  Applies a gamma function to a 32-bit planar image to produce an 8-bit planar image.
- [func vImageGamma_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, GammaFunction!, vImage_Flags) -> vImage_Error](vimagegamma_planarf(_:_:_:_:).md)
  Applies a gamma function to a PlanarF image.
- [func vImageDestroyGammaFunction(GammaFunction!)](vimagedestroygammafunction(_:).md)
  Destroys a gamma function object.
- [Adjusting saturation and applying tone mapping](adjusting-saturation-and-applying-tone-mapping.md)
  Convert an RGB image to discrete luminance and chrominance channels, and apply color and contrast treatments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecreategammafunction(_:_:_:))*