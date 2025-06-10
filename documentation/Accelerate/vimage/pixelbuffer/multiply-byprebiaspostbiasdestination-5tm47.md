# multiply(by:preBias:postBias:destination:)

**Framework**: Accelerate  
**Kind**: method

Multiplies each four channel pixel in a 32-bit-per channel, 4-channel pixel buffer by a 4 x 4 matrix to produce a four channel result.

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
func multiply<Matrix>(by matrix: Matrix, preBias: (Float, Float, Float, Float), postBias: (Float, Float, Float, Float), destination: vImage.PixelBuffer<vImage.InterleavedFx4>) where Matrix : AccelerateBuffer, Matrix.Element == Float
```

#### Discussion

This function applies the following operation to each pixel:

```swift
p = (source.0 + preBias.0) * matrix.0 +
    (source.1 + preBias.1) * matrix.1 +
    (source.2 + preBias.2) * matrix.2 +
    (source.3 + preBias.3) * matrix.3
destination = (p + postBias)
```

## Parameters

- `matrix`: The 4 x 4 multiplication matrix values in row-major order.
- `preBias`: Values that the function adds to the source before multiplication.
- `postBias`: A value that the function adds to the result after multiplication.
- `destination`: The destination pixel buffer.

## See Also

- [func multiply<Matrix>(by: Matrix, divisor: Int, preBias: (Int, Int, Int, Int), postBias: (Int, Int, Int, Int), destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/multiply(by:divisor:prebias:postbias:destination:)-7ikb7.md)
  Multiplies each four channel pixel in an 8-bit-per channel, 4-channel pixel buffer by a 4 x 4 matrix to produce a four channel result.
- [func multiply(by: simd_float4x4, preBias: (Float, Float, Float, Float), postBias: (Float, Float, Float, Float), destination: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/multiply(by:prebias:postbias:destination:)-5tq68.md)
  Multiplies each four channel pixel in a 32-bit-per channel, 4-channel pixel buffer by a 4 x 4 simd matrix to produce a four channel result.
- [func multiply<Matrix, DestFormat>(by: Matrix, divisor: Int, preBias: [Int], postBias: [Int], destination: vImage.PixelBuffer<DestFormat>)](vimage/pixelbuffer/multiply(by:divisor:prebias:postbias:destination:)-86hbw.md)
  Multiplies each four channel pixel in an 8-bit multiple-plane pixel buffer by a 4 x 4 matrix to produce a four channel result.
- [func multiply<Matrix, DestFormat>(by: Matrix, preBias: [Float], postBias: [Float], destination: vImage.PixelBuffer<DestFormat>)](vimage/pixelbuffer/multiply(by:prebias:postbias:destination:)-3kltz.md)
  Multiplies each four channel pixel in a 32-bit multiple-plane pixel buffer by a 4 x 4 matrix to produce a four channel result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/multiply(by:prebias:postbias:destination:)-5tm47)*