# Gamma function types

**Framework**: Accelerate  
**Role**: API Collection

Types of full- or half-precision gamma functions.

## Topics

### User-defined gamma values
- [var kvImageGamma_UseGammaValue: Int](./kvimagegamma_usegammavalue.md)
  A user-defined gamma value with full-precision calculation.
- [var kvImageGamma_UseGammaValue_half_precision: Int](./kvimagegamma_usegammavalue_half_precision.md)
  A user-defined gamma value with half-precision calculation.
### Constant gamma values
- [var kvImageGamma_BT709_forward_half_precision: Int](./kvimagegamma_bt709_forward_half_precision.md)
  The ITU-R BT.709 standard.
- [var kvImageGamma_BT709_reverse_half_precision: Int](./kvimagegamma_bt709_reverse_half_precision.md)
  The ITU-R BT.709 standard reverse.
- [var kvImageGamma_sRGB_forward_half_precision: Int](./kvimagegamma_srgb_forward_half_precision.md)
  A half-precision calculation using the sRGB standard gamma value of 2.2.
- [var kvImageGamma_sRGB_reverse_half_precision: Int](./kvimagegamma_srgb_reverse_half_precision.md)
  A half-precision calculation using the sRGB standard gamma value of 1/2.2.
- [var kvImageGamma_5_over_9_half_precision: Int](./kvimagegamma_5_over_9_half_precision.md)
  A half-precision calculation using a gamma value of 5/9 or 1/1.8.
- [var kvImageGamma_5_over_11_half_precision: Int](./kvimagegamma_5_over_11_half_precision.md)
  A half-precision calculation using a gamma value of 5/11 or 1/2.2.
- [var kvImageGamma_9_over_5_half_precision: Int](./kvimagegamma_9_over_5_half_precision.md)
  A half-precision calculation using a gamma value of 9/5 or 1.8.
- [var kvImageGamma_9_over_11_half_precision: Int](./kvimagegamma_9_over_11_half_precision.md)
  A half-precision calculation using a gamma value of 9/11 or (9/5)/(11/5).
- [var kvImageGamma_11_over_5_half_precision: Int](./kvimagegamma_11_over_5_half_precision.md)
  A half-precision calculation using a gamma value of 11/5 or 2.2.
- [var kvImageGamma_11_over_9_half_precision: Int](./kvimagegamma_11_over_9_half_precision.md)
  A half-precision calculation using a gamma value of 11/9 or (11/5)/(9/5).

## See Also

### Applying a gamma function
- [func vImageCreateGammaFunction(Float, Int32, vImage_Flags) -> GammaFunction!](./vimagecreategammafunction%28_,_,_%29.md)
  Returns a gamma function object.
- [func vImageGamma_Planar8toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, GammaFunction!, vImage_Flags) -> vImage_Error](./vimagegamma_planar8toplanarf%28_,_,_,_%29.md)
  Applies a gamma function to an 8-bit planar image to produce a 32-bit planar image.
- [func vImageGamma_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, GammaFunction!, vImage_Flags) -> vImage_Error](./vimagegamma_planarftoplanar8%28_,_,_,_%29.md)
  Applies a gamma function to a 32-bit planar image to produce an 8-bit planar image.
- [func vImageGamma_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, GammaFunction!, vImage_Flags) -> vImage_Error](./vimagegamma_planarf%28_,_,_,_%29.md)
  Applies a gamma function to a PlanarF image.
- [func vImageDestroyGammaFunction(GammaFunction!)](./vimagedestroygammafunction%28_%29.md)
  Destroys a gamma function object.
- [Adjusting saturation and applying tone mapping](./adjusting-saturation-and-applying-tone-mapping.md)
  Convert an RGB image to discrete luminance and chrominance channels, and apply color and contrast treatments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/1584480-gamma-function-types)*