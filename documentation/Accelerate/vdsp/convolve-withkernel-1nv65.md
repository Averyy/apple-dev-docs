# convolve(_:withKernel:)

**Framework**: Accelerate  
**Kind**: method

Returns the 1D convolution of a double-precision vector.

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
static func convolve<T, U>(_ vector: T, withKernel kernel: U) -> [Double] where T : AccelerateBuffer, U : AccelerateBuffer, T.Element == Double, U.Element == Double
```

#### Return Value

The convolution result.

## Parameters

- `vector`: The input signal vector.
- `kernel`: The filter vector.

## See Also

- [static func convolve<T, U>(T, withKernel: U) -> [Float]](vdsp/convolve(_:withkernel:)-4p0rt.md)
  Returns the 1D convolution of a single-precision vector.
- [static func convolve<T, U, V>(T, withKernel: U, result: inout V)](vdsp/convolve(_:withkernel:result:)-8j76l.md)
  Calculates the 1D convolution of a double-precision vector.
- [static func convolve<T, U, V>(T, withKernel: U, result: inout V)](vdsp/convolve(_:withkernel:result:)-2z66w.md)
  Calculates the 1D convolution of a single-precision vector.
- [static func correlate<T, U>(T, withKernel: U) -> [Double]](vdsp/correlate(_:withkernel:)-7f6o0.md)
  Returns the correlation of a double-precision signal vector and a filter vector.
- [static func correlate<T, U>(T, withKernel: U) -> [Float]](vdsp/correlate(_:withkernel:)-9sol8.md)
  Returns the correlation of a single-precision signal vector and a filter vector.
- [static func correlate<T, U, V>(T, withKernel: U, result: inout V)](vdsp/correlate(_:withkernel:result:)-1lb82.md)
  Calculates the correlation of a double-precision signal vector and a filter vector.
- [static func correlate<T, U, V>(T, withKernel: U, result: inout V)](vdsp/correlate(_:withkernel:result:)-377zj.md)
  Calculates the correlation of a single-precision signal vector and a filter vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/convolve(_:withkernel:)-1nv65)*