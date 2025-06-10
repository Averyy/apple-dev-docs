# vImageSymmetricPiecewisePolynomial_PlanarF(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a set of symmetric piecewise polynomials to transform a 32-bit planar image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vImageSymmetricPiecewisePolynomial_PlanarF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ coefficients: UnsafeMutablePointer<UnsafePointer<Float>?>, _ boundaries: UnsafePointer<Float>, _ order: UInt32, _ log2segments: UInt32, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

You can approximate many different correction functions by carefully choosing the polynomials and the ranges of input values they operate on. For example, the sample code project [`Applying tone curve adjustments to images`](applying-tone-curve-adjustments-to-images.md) demonstrates how to apply tone curve adjustments to images using polynomial transforms.

The [`vImageSymmetricPiecewisePolynomial_PlanarF(_:_:_:_:_:_:_:)`](vimagesymmetricpiecewisepolynomial_planarf(_:_:_:_:_:_:_:).md) function differs from the [`vImagePiecewisePolynomial_PlanarF(_:_:_:_:_:_:_:)`](vimagepiecewisepolynomial_planarf(_:_:_:_:_:_:_:).md) function in that it uses the following modified polynomial that’s symmetric about zero:

```c
p'(x) = p(fabsf(x)) * copysignf( 1.0f, x)
```

This means that negative source pixel values return negative destination pixel values rather than zeros.

The following code defines two sets of polynomial coefficients, `coefficients0` as `[0.0, 0.5, 0.0]` and `coefficients1` as `[0.0, 0.0, 1.0].` The boundaries array, `[0, 0.5, 1]`, specifies that the [`vImageSymmetricPiecewisePolynomial_PlanarF(_:_:_:_:_:_:_:)`](vimagesymmetricpiecewisepolynomial_planarf(_:_:_:_:_:_:_:).md) function applies `coefficients0` to source pixels less than `0.5`, and applies `coefficients1` other pixels.

Note that the boundaries array contains three elements that define two ranges: `0..<0.5` and `0.5...1`. The `order` value equals the number of coefficients in each segment minus one.

```swift
let source = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [-0, -0.2, -0.4, -0.6, -0.8, -1],
    size: vImage.Size(width: 6, height: 1))

let destination = vImage.PixelBuffer<vImage.PlanarF>(
    size: source.size)

let coefficients0: [Float] = [0.0, 0.5, 0.0] // 0.0 * x⁰ + 0.5 * x¹ + 0.0 * x²
let coefficients1: [Float] = [0.0, 0.0, 1.0] // 0.0 * x⁰ + 0.0 * x¹ + 1.0 * x²

let boundaries: [Float] = [0, 0.5, 1]

let order = UInt32(2)

let log2segments = UInt32(1)

coefficients0.withUnsafeBufferPointer { coefficients0Ptr in
    coefficients1.withUnsafeBufferPointer { coefficients1Ptr in
        source.withUnsafePointerToVImageBuffer { src in
            destination.withUnsafePointerToVImageBuffer { dest in
                
                var coeffs = [ coefficients0Ptr.baseAddress,
                               coefficients1Ptr.baseAddress ]
                
                vImagePiecewisePolynomial_PlanarF(
                    src,
                    dest,
                    &coeffs,
                    boundaries,
                    order,
                    log2segments,
                    vImage_Flags(kvImageNoFlags))
            }
        }
    }
}
```

On return, the destination buffer contains the values `[0.0, -0.1, -0.2, -0.36, -0.64, -1.0]`. This is equivalent to the following scalar code:

```swift
let result = source.array.map { x in
    let coefficients = x < 0.5 ? coefficients0 : coefficients1
    return coefficients[0] * pow(x, 0) +
           coefficients[1] * pow(x, 1) +
           coefficients[2] * pow(x, 2)
}
```

For best performance, choose a single higher-order polynomial over many lower-order polynomials. However, this function uses single-precision arithmetic, and large high-order coefficients may cause rounding errors.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `coefficients`: Order the coefficients from the zeroth-order term to the highest order term. For example, the function evaluates the coefficients   as  .
- `boundaries`: A pointer to an array of boundary values, in increasing order, that separates adjacent ranges of pixel values. The first boundary value is the lowest in the range and the function clips input values lower than this to this value. The last boundary value is the highest in the range and the function clips input values higher than this to this value. The boundary values between the first and last separate the subranges from each other.
- `order`: The order of the polynomials.
- `log2segments`: The number of polynomials to represent as a base-2 logarithm. If you pass a noninteger power-of-two number of polynomials, round up to the next integer power of two, and repeat the last polynomial the appropriate number of times.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImagePiecewisePolynomial_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<Float>?>, UnsafePointer<Float>, UInt32, UInt32, vImage_Flags) -> vImage_Error](vimagepiecewisepolynomial_planarf(_:_:_:_:_:_:_:).md)
  Applies a set of piecewise polynomials to transform a 32-bit planar image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagesymmetricpiecewisepolynomial_planarf(_:_:_:_:_:_:_:))*