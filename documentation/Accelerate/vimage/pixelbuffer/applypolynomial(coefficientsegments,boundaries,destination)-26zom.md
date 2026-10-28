# applyPolynomial(coefficientSegments:boundaries:destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Applies a set of piecewise polynomials to a 3-channel, 32-bit interleaved buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<Format>)
```

Available when `Format` is `vImage.InterleavedFx3`.

## Discussion

The following code shows an example of applying three polynomials to an [`vImage.InterleavedFx3`](../interleavedfx3.md) buffer:

```swift
let src = vImage.PixelBuffer<vImage.InterleavedFx3>(
    pixelValues: [0.25, 0.5, 0.75],
    size: vImage.Size(width: 1, height: 1))

let dest = vImage.PixelBuffer<vImage.InterleavedFx3>(
    size: src.size)

src.applyPolynomial(coefficientSegments: [ [1, 0, 0],
                                           [0, 1, 0],
                                           [0, 0, 1] ],
                    boundaries: [0, 1/3, 2/3, 1] as [Float],
                    destination: dest)

// Prints:
//  1.0     ≅ 1 * 0.25⁰

//  0.5     ≅ 1 * 0.5¹

//  0.5625  ≅ 1 * 0.75²
print(dest.array)
```

## Parameters

- `coefficientSegments`: An array that contains the polynomial coefficient array. Each polynomial must be of the same order.
- `boundaries`: An array of boundary values, in increasing order, that separates adjacent ranges of pixel values. `boundaries` must contain `coefficientSegments.count + 1` elements.
- `destination`: The destination pixel buffer.

## See Also

### Related Documentation
- [Applying tone curve adjustments to images](../../applying-tone-curve-adjustments-to-images.md)
  Use the vImage library’s polynomial transform to apply tone curve adjustments to images.
### Appying polynomial (32-bit)
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<Format>)](./applypolynomial%28coefficientsegments,boundaries,destination%29-3c46t.md)
  Applies a set of piecewise polynomials to a 32-bit planar buffer.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<Format>)](./applypolynomial%28coefficientsegments,boundaries,destination%29-8f5i9.md)
  Applies a set of piecewise polynomials to a 2-channel, 32-bit interleaved buffer.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<Format>)](./applypolynomial%28coefficientsegments,boundaries,destination%29-8uesn.md)
  Applies a set of piecewise polynomials to a 4-channel, 32-bit interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-26zom)*