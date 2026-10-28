# Transforming with polynomials

**Framework**: Accelerate  
**Role**: API Collection

Use polynomials to apply color transformations to images.

## Overview

Polynomial functions apply one or more polynomials to the input image to generate the output image. You can use polynomial functions to apply tone curve adjustments to images.

## Topics

### Applying a polynomial
- [Applying tone curve adjustments to images](./applying-tone-curve-adjustments-to-images.md)
  Use the vImage library’s polynomial transform to apply tone curve adjustments to images.
- [func vImagePiecewisePolynomial_Planar8toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<Float>?>, UnsafePointer<Float>, UInt32, UInt32, vImage_Flags) -> vImage_Error](./vimagepiecewisepolynomial_planar8toplanarf%28_,_,_,_,_,_,_%29.md)
  Applies a set of piecewise polynomials to transform an 8-bit planar image to a 32-bit planar image.
- [func vImagePiecewisePolynomial_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<Float>?>, UnsafePointer<Float>, UInt32, UInt32, vImage_Flags) -> vImage_Error](./vimagepiecewisepolynomial_planarftoplanar8%28_,_,_,_,_,_,_%29.md)
  Applies a set of piecewise polynomials to transform a 32-bit planar image to an 8-bit planar image.
- [func vImagePiecewisePolynomial_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<Float>?>, UnsafePointer<Float>, UInt32, UInt32, vImage_Flags) -> vImage_Error](./vimagepiecewisepolynomial_planarf%28_,_,_,_,_,_,_%29.md)
  Applies a set of piecewise polynomials to transform a 32-bit planar image.
### Applying a symmetric polynomial
- [func vImageSymmetricPiecewisePolynomial_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<Float>?>, UnsafePointer<Float>, UInt32, UInt32, vImage_Flags) -> vImage_Error](./vimagesymmetricpiecewisepolynomial_planarf%28_,_,_,_,_,_,_%29.md)
  Applies a set of symmetric piecewise polynomials to transform a 32-bit planar image.
### Applying a rational expression
- [func vImagePiecewiseRational_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<Float>?>, UnsafeMutablePointer<UnsafePointer<Float>?>, UnsafePointer<Float>, UInt32, UInt32, UInt32, vImage_Flags) -> vImage_Error](./vimagepiecewiserational_planarf%28_,_,_,_,_,_,_,_,_%29.md)
  Applies a set of piecewise rational expressions to transform a 32-bit planar image.

## See Also

### Applying color transforms to images
- [Transforming with lookup tables](./transforming-with-lookup-tables.md)
  Use lookup tables to apply color transformations to images.
- [Transforming with matrix multiplication](./transforming-with-matrix-multiplication.md)
  Use matrix multiplication to apply color transformations to images.
- [Transforming with a gamma function](./transforming-with-a-gamma-function.md)
  Use gamma functions to apply color transformations to images.
- [Applying a flood fill to an image](./applying-a-flood-fill-to-an-image.md)
  Fill connected components of an image with a new color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/transforming-with-polynomials)*