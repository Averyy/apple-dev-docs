# downsample(_:decimationFactor:filter:result:)

**Framework**: Accelerate  
**Kind**: method

Calculates the downsampled single-precision vector.

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
static func downsample<T, U, V>(_ source: U, decimationFactor: Int, filter: T, result: inout V) where T : AccelerateBuffer, U : AccelerateBuffer, V : AccelerateMutableBuffer, T.Element == Float, U.Element == Float, V.Element == Float
```

## See Also

- [Resampling a signal with decimation](resampling-a-signal-with-decimation.md)
  Reduce the sample rate of a signal by specifying a decimation factor and applying a custom antialiasing filter.
- [static func downsample<T, U>(U, decimationFactor: Int, filter: T) -> [Double]](vdsp/downsample(_:decimationfactor:filter:)-1o8it.md)
  Returns the downsampled double-precision vector.
- [static func downsample<T, U>(U, decimationFactor: Int, filter: T) -> [Float]](vdsp/downsample(_:decimationfactor:filter:)-40d8o.md)
  Returns the downsampled single-precision vector.
- [static func downsample<T, U, V>(U, decimationFactor: Int, filter: T, result: inout V)](vdsp/downsample(_:decimationfactor:filter:result:)-2y1iv.md)
  Calculates the downsampled double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/downsample(_:decimationfactor:filter:result:)-1g4a)*