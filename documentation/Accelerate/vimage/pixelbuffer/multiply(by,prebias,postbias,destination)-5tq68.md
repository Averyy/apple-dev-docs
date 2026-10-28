# multiply(by:preBias:postBias:destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Multiplies each four channel pixel in a 32-bit-per channel, 4-channel pixel buffer by a 4 x 4 simd matrix to produce a four channel result.

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
func multiply(by matrix: simd_float4x4, preBias: (Float, Float, Float, Float), postBias: (Float, Float, Float, Float), destination: vImage.PixelBuffer<vImage.InterleavedFx4>)
```

Available when `Format` is `vImage.InterleavedFx4`.

## Discussion

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

### Matrix Multiplication
- [func multiply<Matrix>(by: Matrix, divisor: Int, preBias: (Int, Int, Int, Int), postBias: (Int, Int, Int, Int), destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](./multiply%28by,divisor,prebias,postbias,destination%29-7ikb7.md)
  Multiplies each four channel pixel in an 8-bit-per channel, 4-channel pixel buffer by a 4 x 4 matrix to produce a four channel result.
- [func multiply<Matrix>(by: Matrix, preBias: (Float, Float, Float, Float), postBias: (Float, Float, Float, Float), destination: vImage.PixelBuffer<vImage.InterleavedFx4>)](./multiply%28by,prebias,postbias,destination%29-5tm47.md)
  Multiplies each four channel pixel in a 32-bit-per channel, 4-channel pixel buffer by a 4 x 4 matrix to produce a four channel result.
- [func multiply<Matrix, DestFormat>(by: Matrix, divisor: Int, preBias: [Int], postBias: [Int], destination: vImage.PixelBuffer<DestFormat>)](./multiply%28by,divisor,prebias,postbias,destination%29-86hbw.md)
  Multiplies each four channel pixel in an 8-bit multiple-plane pixel buffer by a 4 x 4 matrix to produce a four channel result.
- [func multiply<Matrix, DestFormat>(by: Matrix, preBias: [Float], postBias: [Float], destination: vImage.PixelBuffer<DestFormat>)](./multiply%28by,prebias,postbias,destination%29-3kltz.md)
  Multiplies each four channel pixel in a 32-bit multiple-plane pixel buffer by a 4 x 4 matrix to produce a four channel result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/multiply(by:prebias:postbias:destination:)-5tq68)*