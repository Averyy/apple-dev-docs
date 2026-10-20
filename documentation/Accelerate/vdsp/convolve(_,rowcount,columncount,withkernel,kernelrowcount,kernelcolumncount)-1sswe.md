# convolve(_:rowCount:columnCount:withKernel:kernelRowCount:kernelColumnCount:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Returns the 2D convolution of a double-precision vector with an arbitrarily sized kernel.

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
static func convolve<T, U>(_ vector: T, rowCount: Int, columnCount: Int, withKernel kernel: U, kernelRowCount: Int, kernelColumnCount: Int) -> [Double] where T : AccelerateBuffer, U : AccelerateBuffer, T.Element == Double, U.Element == Double
```

## See Also

### Arbitrary-Size Kernel
- [static func convolve<T, U>(T, rowCount: Int, columnCount: Int, withKernel: U, kernelRowCount: Int, kernelColumnCount: Int) -> [Float]](./convolve%28_,rowcount,columncount,withkernel,kernelrowcount,kernelcolumncount%29-267yl.md)
  Returns the 2D convolution of a single-precision vector with an arbitrarily sized kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, withKernel: U, kernelRowCount: Int, kernelColumnCount: Int, result: inout V)](./convolve%28_,rowcount,columncount,withkernel,kernelrowcount,kernelcolumncount,result%29-4211m.md)
  Calculates the 2D convolution of a double-precision vector with an arbitrarily sized kernel.
- [static func convolve<T, U, V>(T, rowCount: Int, columnCount: Int, withKernel: U, kernelRowCount: Int, kernelColumnCount: Int, result: inout V)](./convolve%28_,rowcount,columncount,withkernel,kernelrowcount,kernelcolumncount,result%29-5hiro.md)
  Calculates the 2D convolution of a single-precision vector with an arbitrarily sized kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/convolve(_:rowcount:columncount:withkernel:kernelrowcount:kernelcolumncount:)-1sswe)*