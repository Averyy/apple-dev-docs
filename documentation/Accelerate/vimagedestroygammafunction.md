# vImageDestroyGammaFunction(_:)

**Framework**: Accelerate  
**Kind**: func

Destroys a gamma function object.

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
func vImageDestroyGammaFunction(_ f: GammaFunction!)
```

## Parameters

- `f`: The gamma function object.

## See Also

- [func vImageCreateGammaFunction(Float, Int32, vImage_Flags) -> GammaFunction!](vimagecreategammafunction(_:_:_:).md)
  Returns a gamma function object.
- [Gamma function types](1584480-gamma-function-types.md)
  Types of full- or half-precision gamma functions.
- [func vImageGamma_Planar8toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, GammaFunction!, vImage_Flags) -> vImage_Error](vimagegamma_planar8toplanarf(_:_:_:_:).md)
  Applies a gamma function to an 8-bit planar image to produce a 32-bit planar image.
- [func vImageGamma_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, GammaFunction!, vImage_Flags) -> vImage_Error](vimagegamma_planarftoplanar8(_:_:_:_:).md)
  Applies a gamma function to a 32-bit planar image to produce an 8-bit planar image.
- [func vImageGamma_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, GammaFunction!, vImage_Flags) -> vImage_Error](vimagegamma_planarf(_:_:_:_:).md)
  Applies a gamma function to a PlanarF image.
- [Adjusting saturation and applying tone mapping](adjusting-saturation-and-applying-tone-mapping.md)
  Convert an RGB image to discrete luminance and chrominance channels, and apply color and contrast treatments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagedestroygammafunction(_:))*