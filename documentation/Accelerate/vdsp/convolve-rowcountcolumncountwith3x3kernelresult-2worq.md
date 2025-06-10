# convolve(_:rowCount:columnCount:with3x3Kernel:result:)

**Framework**: Accelerate  
**Kind**: method

Calculates the 2D convolution of a single-precision vector with a 3 x 3 kernel.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
static func convolve<T, U, V>(_ vector: T, rowCount: Int, columnCount: Int, with3x3Kernel kernel: U, result: inout V) where T : AccelerateBuffer, U : AccelerateBuffer, V : AccelerateMutableBuffer, T.Element == Float, U.Element == Float, V.Element == Float
```

## See Also

- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, with3x3Kernel: U) -> [Double]](vdsp/convolve(_:rowcount:columncount:with3x3kernel:)-1r5oa.md)
  Returns the 2D convolution of a double-precision vector with a 3 x 3 kernel.
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, with3x3Kernel: U) -> [Float]](vdsp/convolve(_:rowcount:columncount:with3x3kernel:)-7qjgw.md)
  Returns the 2D convolution of a single-precision vector with a 3 x 3 kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, with3x3Kernel: U, result: inout V)](vdsp/convolve(_:rowcount:columncount:with3x3kernel:result:)-34k76.md)
  Calculates the 2D convolution of a double-precision vector with a 3 x 3 kernel.
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, with5x5Kernel: U) -> [Double]](vdsp/convolve(_:rowcount:columncount:with5x5kernel:)-7cvh9.md)
  Returns the 2D convolution of a double-precision vector with a 5 x 5 kernel.
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, with5x5Kernel: U) -> [Float]](vdsp/convolve(_:rowcount:columncount:with5x5kernel:)-101d6.md)
  Returns the 2D convolution of a single-precision vector with a 5 x 5 kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, with5x5Kernel: U, result: inout V)](vdsp/convolve(_:rowcount:columncount:with5x5kernel:result:)-g68r.md)
  Calculates the 2D convolution of a double-precision vector with a 5 x 5 kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, with5x5Kernel: U, result: inout V)](vdsp/convolve(_:rowcount:columncount:with5x5kernel:result:)-76h85.md)
  Calculates the 2D convolution of a single-precision vector with a 5 x 5 kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/convolve(_:rowcount:columncount:with3x3kernel:result:)-2worq)*