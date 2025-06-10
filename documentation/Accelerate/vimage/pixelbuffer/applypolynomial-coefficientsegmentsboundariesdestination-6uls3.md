# applyPolynomial(coefficientSegments:boundaries:destination:)

**Framework**: Accelerate  
**Kind**: method

Applies a set of piecewise polynomials to a 2-channel, 32-bit interleaved buffer and writes the result to a 2-channel, 8-bit interleaved buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.Interleaved8x2>)
```

#### Discussion

The following code shows an example of applying three polynomials to a [`vImage.InterleavedFx2`](vimage/interleavedfx2.md) buffer:

```swift
let src = vImage.PixelBuffer<vImage.InterleavedFx2>(
    pixelValues: [0.25, 0.5, 0.75, 1.0],
    size: vImage.Size(width: 2, height: 1))

let dest = vImage.PixelBuffer<vImage.Interleaved8x2>(
    size: src.size)

let factor = Float(255)
src.applyPolynomial(coefficientSegments: [ [1 * factor, 0, 0],
                                           [0, 1 * factor, 0],
                                           [0, 0, 1 * factor] ],
                    boundaries: [0, 1/3, 2/3, 1] as [Float],
                    destination: dest)

// Prints:
//  255     ≅ factor * 0.25⁰

//  127     ≅ factor * 0.5¹

//  143     ≅ factor * 0.75²
//  255     ≅ factor * 1.0²
print(dest.array)
```

## Parameters

- `coefficientSegments`: An array that contains the polynomial coefficient array. Each polynomial must be of the same order.
- `boundaries`: An array of boundary values, in increasing order, that separates adjacent ranges of pixel values.   must contain   elements.
- `destination`: The destination pixel buffer.

## See Also

- [Applying tone curve adjustments to images](applying-tone-curve-adjustments-to-images.md)
  Use the vImage library’s polynomial transform to apply tone curve adjustments to images.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-3b0d0.md)
  Applies a set of piecewise polynomials to a 32-bit planar buffer and writes the result to an 8-bit planar buffer.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.Interleaved8x3>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-4r6nf.md)
  Applies a set of piecewise polynomials to a 3-channel, 32-bit interleaved buffer and writes the result to a 3-channel, 8-bit interleaved buffer.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-1b2nu.md)
  Applies a set of piecewise polynomials to a 4-channel, 32-bit interleaved buffer and writes the result to a 4-channel, 8-bit interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-6uls3)*