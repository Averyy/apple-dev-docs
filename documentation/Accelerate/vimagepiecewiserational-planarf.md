# vImagePiecewiseRational_PlanarF(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a set of piecewise rational expressions to transform a 32-bit planar image.

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
func vImagePiecewiseRational_PlanarF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ topCoefficients: UnsafeMutablePointer<UnsafePointer<Float>?>, _ bottomCoefficients: UnsafeMutablePointer<UnsafePointer<Float>?>, _ boundaries: UnsafePointer<Float>, _ topOrder: UInt32, _ bottomOrder: UInt32, _ log2segments: UInt32, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

You can approximate many different correction functions by carefully choosing the polynomials and the ranges of input values they operate on. For example, the sample code project [`Applying tone curve adjustments to images`](applying-tone-curve-adjustments-to-images.md) demonstrates how to apply tone curve adjustments to images using polynomial transforms.

The [`vImagePiecewiseRational_PlanarF(_:_:_:_:_:_:_:_:_:)`](vimagepiecewiserational_planarf(_:_:_:_:_:_:_:_:_:).md) function evaluates polynomials similarly to [`vImagePiecewisePolynomial_PlanarF(_:_:_:_:_:_:_:)`](vimagepiecewisepolynomial_planarf(_:_:_:_:_:_:_:).md), but works with two sets of polynomials the `topCoefficients` and `bottomCoefficients` parameters specify. The function writes the result of evaluating the top polynomials divided by the result of evaluating the bottom polynomials to the destination pixel.

The following code defines two sets of polynomial coefficients, `topCoefficients` as `[0.0, 0.5, 0.0]` and `bottomCoefficients` as `[0.0, 0.0, 1.0, 0.2]`. The result of the expression for each pixel is (`0.0 * x⁰ + 0.5 * x¹ + 0.0 * x²) / (0.0 * x⁰ + 0.0 * x¹ + 1.0 * x² + 0.2 * x³)`.

Note that this function allows the top and bottom polynomials to be of different orders. This example defines the boundaries array as `[-.infinity, .infinity]` so that a single rational expression covers pixels of any value.

```swift
let source = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [0.2, 0.4, 0.6, 0.8, 1],
    size: vImage.Size(width: 5, height: 1))

let destination = vImage.PixelBuffer<vImage.PlanarF>(
    size: source.size)

// 0.0 * x⁰ + 0.5 * x¹ + 0.0 * x²
let topCoefficients: [Float] = [0.0, 0.5, 0.0]
let topOrder = UInt32(topCoefficients.count - 1)

// 0.0 * x⁰ + 0.0 * x¹ + 1.0 * x² + 0.2 * x³
let bottomCoefficients: [Float] = [0.0, 0.0, 1.0, 0.2]
let bottomOrder = UInt32(bottomCoefficients.count - 1)

let boundaries: [Float] = [-.infinity, .infinity]

let log2segments = UInt32(0)

topCoefficients.withUnsafeBufferPointer { topCoefficientsPtr in
    bottomCoefficients.withUnsafeBufferPointer { bottomCoefficientsPtr in
        source.withUnsafePointerToVImageBuffer { src in
            destination.withUnsafePointerToVImageBuffer { dest in
                
                var topCoeffs = [ topCoefficientsPtr.baseAddress ]
                var bottomCoeffs = [ bottomCoefficientsPtr.baseAddress ]
                
                vImagePiecewiseRational_PlanarF(
                    src,
                    dest,
                    &topCoeffs,
                    &bottomCoeffs,
                    boundaries,
                    topOrder,
                    bottomOrder,
                    log2segments,
                    vImage_Flags(kvImageNoFlags))
            }
        }
    }
}
```

On return, the destination buffer contains the values `[2.4038463, 1.1574074, 0.7440475, 0.53879315, 0.41666666]`. This is equivalent to the following scalar code:

```swift
let result = source.array.map { x in
    
    let numerator = topCoefficients[0] * pow(x, 0) +
                    topCoefficients[1] * pow(x, 1) +
                    topCoefficients[2] * pow(x, 2)
    
    let denominator = bottomCoefficients[0] * pow(x, 0) +
                      bottomCoefficients[1] * pow(x, 1) +
                      bottomCoefficients[2] * pow(x, 2) +
                      bottomCoefficients[3] * pow(x, 3)
    
    return numerator / denominator
}
```

This function doesn’t deliver IEEE-754 correct division and doesn’t round per the IEEE-754 current rounding mode. It incurs up to two units in the last place of error. This function returns undefined results for edge cases that include denormals, infinities, NaNs, and division by zero.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `topCoefficients`: Order the coefficients from the zeroth-order term to the highest order term. For example, the function evaluates the coefficients   as  .
- `bottomCoefficients`: Order the coefficients from the zeroth-order term to the highest order term. For example, the function evaluates the coefficients   as  .
- `boundaries`: A pointer to an array of boundary values, in increasing order, that separates adjacent ranges of pixel values. The first boundary value is the lowest in the range and the function clips input values lower than this to this value. The last boundary value is the highest in the range and the function clips input values higher than this to this value. The boundary values between the first and last separate the subranges from each other.
- `topOrder`: The order of the numerator polynomials.
- `bottomOrder`: The order of the denominator polynomials.
- `log2segments`: The number of rational expressions to represent as a base-2 logarithm. If you pass a noninteger power-of-two number of polynomials, round up to the next integer power of two, and repeat the last expression the appropriate number of times.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagepiecewiserational_planarf(_:_:_:_:_:_:_:_:_:))*