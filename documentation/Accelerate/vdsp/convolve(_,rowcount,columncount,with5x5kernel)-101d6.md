# convolve(_:rowCount:columnCount:with5x5Kernel:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Returns the 2D convolution of a single-precision vector with a 5 x 5 kernel.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
static func convolve<T, U>(_ vector: T, rowCount: Int, columnCount: Int, with5x5Kernel kernel: U) -> [Float] where T : AccelerateBuffer, U : AccelerateBuffer, T.Element == Float, U.Element == Float
```

## See Also

### Fixed-Size Kernel
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, with3x3Kernel: U) -> [Double]](./convolve%28_,rowcount,columncount,with3x3kernel%29-1r5oa.md)
  Returns the 2D convolution of a double-precision vector with a 3 x 3 kernel.
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, with3x3Kernel: U) -> [Float]](./convolve%28_,rowcount,columncount,with3x3kernel%29-7qjgw.md)
  Returns the 2D convolution of a single-precision vector with a 3 x 3 kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, with3x3Kernel: U, result: inout V)](./convolve%28_,rowcount,columncount,with3x3kernel,result%29-34k76.md)
  Calculates the 2D convolution of a double-precision vector with a 3 x 3 kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, with3x3Kernel: U, result: inout V)](./convolve%28_,rowcount,columncount,with3x3kernel,result%29-2worq.md)
  Calculates the 2D convolution of a single-precision vector with a 3 x 3 kernel.
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, with5x5Kernel: U) -> [Double]](./convolve%28_,rowcount,columncount,with5x5kernel%29-7cvh9.md)
  Returns the 2D convolution of a double-precision vector with a 5 x 5 kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, with5x5Kernel: U, result: inout V)](./convolve%28_,rowcount,columncount,with5x5kernel,result%29-g68r.md)
  Calculates the 2D convolution of a double-precision vector with a 5 x 5 kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, with5x5Kernel: U, result: inout V)](./convolve%28_,rowcount,columncount,with5x5kernel,result%29-76h85.md)
  Calculates the 2D convolution of a single-precision vector with a 5 x 5 kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/convolve(_:rowcount:columncount:with5x5kernel:)-101d6)*