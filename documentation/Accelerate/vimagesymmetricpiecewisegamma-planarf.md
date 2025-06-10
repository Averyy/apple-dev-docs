# vImageSymmetricPiecewiseGamma_PlanarF(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a symmetric piecewise gamma function to transform a 32-bit planar image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func vImageSymmetricPiecewiseGamma_PlanarF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ exponentialCoeffs: UnsafePointer<Float>, _ gamma: Float, _ linearCoeffs: UnsafePointer<Float>, _ boundary: Float, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The piecewise gamma calculation combines a linear and an exponential (gamma) curve on two regions of the input interval, separated by a specified boundary value. When the input is greater than or equal to the boundary value, the function uses the gamma curve to generate the output; otherwise, the function uses the linear curve. This function differs from [`vImagePiecewiseGamma_PlanarF(_:_:_:_:_:_:_:)`](vimagepiecewisegamma_planarf(_:_:_:_:_:_:_:).md) in that it’s symmetric about zero.

The following describes the operation with `x` representing the input pixel value:

```c
y = fabsf(x)

if y < boundary:    
    scale = linearCoeffs[0]
    bias = linearCoeffs[1]

    r = scale * y + bias
else:    
    scale = exponentialCoeffs[0]
    prebias = exponentialCoeffs[1]
    postbias = exponentialCoeffs[2]

    t = scale * y + prebias
    r = pow(t, gamma) + postbias
output pixel value = r * copysignf(1.0f, x)
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `exponentialCoeffs`: An array of three floating-point coefficients that specify the scale, prebias, and postbias for the gamma curve.
- `gamma`: The power function exponent for calculating gamma correction for the gamma curve.
- `linearCoeffs`: An array of two floating-point coefficients that specify the scale and bias for the linear curve.
- `boundary`: A value that defines the boundary between the linear curve and the gamma curve.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageSymmetricPiecewiseGamma_Planar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Float, UnsafePointer<Float>, Pixel_16S, vImage_Flags) -> vImage_Error](vimagesymmetricpiecewisegamma_planar16q12(_:_:_:_:_:_:_:).md)
  Applies a symmetric piecewise gamma function to transform a 16Q12 planar image to an 8-bit planar image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagesymmetricpiecewisegamma_planarf(_:_:_:_:_:_:_:))*