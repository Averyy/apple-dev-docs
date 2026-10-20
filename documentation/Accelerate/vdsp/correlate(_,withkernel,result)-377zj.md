# correlate(_:withKernel:result:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Calculates the correlation of a single-precision signal vector and a filter vector.

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
static func correlate<T, U, V>(_ vector: T, withKernel kernel: U, result: inout V) where T : AccelerateBuffer, U : AccelerateBuffer, V : AccelerateMutableBuffer, T.Element == Float, U.Element == Float, V.Element == Float
```

## Parameters

- `vector`: The input signal vector.
- `kernel`: The filter vector.
- `result`: On output, the correlation result.

## See Also

### Real Vectors
- [static func convolve<T, U>(T, withKernel: U) -> [Double]](./convolve%28_,withkernel%29-1nv65.md)
  Returns the 1D convolution of a double-precision vector.
- [static func convolve<T, U>(T, withKernel: U) -> [Float]](./convolve%28_,withkernel%29-4p0rt.md)
  Returns the 1D convolution of a single-precision vector.
- [static func convolve<T, U, V>(T, withKernel: U, result: inout V)](./convolve%28_,withkernel,result%29-8j76l.md)
  Calculates the 1D convolution of a double-precision vector.
- [static func convolve<T, U, V>(T, withKernel: U, result: inout V)](./convolve%28_,withkernel,result%29-2z66w.md)
  Calculates the 1D convolution of a single-precision vector.
- [static func correlate<T, U>(T, withKernel: U) -> [Double]](./correlate%28_,withkernel%29-7f6o0.md)
  Returns the correlation of a double-precision signal vector and a filter vector.
- [static func correlate<T, U>(T, withKernel: U) -> [Float]](./correlate%28_,withkernel%29-9sol8.md)
  Returns the correlation of a single-precision signal vector and a filter vector.
- [static func correlate<T, U, V>(T, withKernel: U, result: inout V)](./correlate%28_,withkernel,result%29-1lb82.md)
  Calculates the correlation of a double-precision signal vector and a filter vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/correlate(_:withkernel:result:)-377zj)*