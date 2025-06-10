# applyPolynomial(coefficientSegments:boundaries:destination:)

**Framework**: Accelerate  
**Kind**: method

Applies a set of piecewise polynomials to an 8-bit planar buffer and writes the result to a 32-bit planar buffer.

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
func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.PlanarF>)
```

#### Discussion

The following code shows an example of applying three polynomials to a [`vImage.Planar8`](vimage/planar8.md) buffer:

```swift
let src = vImage.PixelBuffer<vImage.Planar8>(
    pixelValues: [32, 64, 128, 192, 255],
    size: vImage.Size(width: 5, height: 1))

let dest = vImage.PixelBuffer<vImage.PlanarF>(
    size: src.size)

src.applyPolynomial(coefficientSegments: [ [1, 1, 0],
                                           [0, 1, 0],
                                           [0, 0, 1] ],
                    boundaries: [0, 1/3, 2/3, 1] as [Float],
                    destination: dest)

// Prints:
//  1.0         ≅ 1 * (32 / 255)⁰
//  1.0         ≅ 1 * (64 / 255)⁰

//  0.5019608   ≅ 1 * (128 / 255)¹

//  0.56692046  ≅ 1 * (192 / 255)²
//  1.0         ≅ 1 * (255 / 255)²
print(dest.array)
```

## Parameters

- `coefficientSegments`: An array that contains the polynomial coefficient array. Each polynomial must be of the same order.
- `boundaries`: An array of boundary values, in increasing order, that separates adjacent ranges of pixel values.   must contain   elements.
- `destination`: The destination pixel buffer.

## See Also

- [Applying tone curve adjustments to images](applying-tone-curve-adjustments-to-images.md)
  Use the vImage library’s polynomial transform to apply tone curve adjustments to images.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.InterleavedFx2>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-3sxxv.md)
  Applies a set of piecewise polynomials to a 2-channel, 8-bit interleaved buffer and writes the result to a 2-channel, 32-bit interleaved buffer.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.InterleavedFx3>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-4o5ju.md)
  Applies a set of piecewise polynomials to a 3-channel, 8-bit interleaved buffer and writes the result to a 3-channel, 32-bit interleaved buffer.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-6ohrj.md)
  Applies a set of piecewise polynomials to a 4-channel, 8-bit interleaved buffer and writes the result to a 4-channel, 32-bit interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-7sy2t)*