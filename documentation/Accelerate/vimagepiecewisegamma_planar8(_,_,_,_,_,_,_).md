# vImagePiecewiseGamma_Planar8(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Applies a piecewise gamma function to transform an 8-bit planar image.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImagePiecewiseGamma_Planar8(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ exponentialCoeffs: UnsafePointer<Float>, _ gamma: Float, _ linearCoeffs: UnsafePointer<Float>, _ boundary: Pixel_8, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImagePiecewiseGamma_Planar8(const vImage_Buffer *src, const vImage_Buffer *dest, const float exponentialCoeffs[3], const float gamma, const float linearCoeffs[2], const Pixel_8 boundary, vImage_Flags flags);
```

#### Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

#### Discussion

The piecewise gamma calculation combines a linear and an exponential (gamma) curve on two regions of the input interval, separated by a specified boundary value. When the input is greater than or equal to the boundary value, the function uses the gamma curve to generate the output; otherwise, the function uses the linear curve.

The following describes the operation with `x` representing the input pixel value:

```c
if x < boundary:    
    scale = linearCoeffs[0]
    bias = linearCoeffs[1]

    r = scale * x + bias
else:    
    scale = exponentialCoeffs[0]
    prebias = exponentialCoeffs[1]
    postbias = exponentialCoeffs[2]

    t = scale * x + prebias
    r = pow(t, gamma) + postbias
output pixel value = r
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the `height`, `width`, and `rowBytes` fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `exponentialCoeffs`: An array of three floating-point coefficients that specify the scale, prebias, and postbias for the gamma curve.
- `gamma`: The power function exponent for calculating gamma correction for the gamma curve.
- `linearCoeffs`: An array of two floating-point coefficients that specify the scale and bias for the linear curve.
- `boundary`: A value that defines the boundary between the linear curve and the gamma curve.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

## See Also

### Applying a piecewise gamma function
- [Adjusting the brightness and contrast of an image](./adjusting-the-brightness-and-contrast-of-an-image.md)
  Use a gamma function to apply a linear or exponential curve.
- [func vImagePiecewiseGamma_Planar8toPlanar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Float, UnsafePointer<Float>, Pixel_8, vImage_Flags) -> vImage_Error](./vimagepiecewisegamma_planar8toplanar16q12%28_,_,_,_,_,_,_%29.md)
  Applies a piecewise gamma function to transform an 8-bit planar image to a 16Q12 planar image.
- [func vImagePiecewiseGamma_Planar8toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Float, UnsafePointer<Float>, Pixel_8, vImage_Flags) -> vImage_Error](./vimagepiecewisegamma_planar8toplanarf%28_,_,_,_,_,_,_%29.md)
  Applies a piecewise gamma function to transform an 8-bit planar image to a 32-bit planar image.
- [func vImagePiecewiseGamma_Planar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Float, UnsafePointer<Float>, Pixel_16S, vImage_Flags) -> vImage_Error](./vimagepiecewisegamma_planar16q12%28_,_,_,_,_,_,_%29.md)
  Applies a piecewise gamma function to transform a 16Q12 planar image.
- [func vImagePiecewiseGamma_Planar16Q12toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Float, UnsafePointer<Float>, Pixel_16S, vImage_Flags) -> vImage_Error](./vimagepiecewisegamma_planar16q12toplanar8%28_,_,_,_,_,_,_%29.md)
  Applies a piecewise gamma function to transform a 16Q12 planar image to an 8-bit planar image.
- [func vImagePiecewiseGamma_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Float, UnsafePointer<Float>, Float, vImage_Flags) -> vImage_Error](./vimagepiecewisegamma_planarf%28_,_,_,_,_,_,_%29.md)
  Applies a piecewise gamma function to transform a 32-bit planar image.
- [func vImagePiecewiseGamma_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Float, UnsafePointer<Float>, Float, vImage_Flags) -> vImage_Error](./vimagepiecewisegamma_planarftoplanar8%28_,_,_,_,_,_,_%29.md)
  Applies a piecewise gamma function to transform a 32-bit planar image to an 8-bit planar image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagepiecewisegamma_planar8(_:_:_:_:_:_:_:))*