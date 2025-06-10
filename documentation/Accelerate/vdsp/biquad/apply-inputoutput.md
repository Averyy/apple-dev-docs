# apply(input:output:)

**Framework**: Accelerate  
**Kind**: method

Applies a single- or double-precision single-channel or multichannel biquad IIR filter, overwriting the supplied output vector.

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
mutating func apply<U, V>(input: U, output: inout V) where T == U.Element, U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == V.Element
```

## See Also

- [func apply<U>(input: U) -> [T]](vdsp/biquad/apply(input:).md)
  Applies a single- or double-precision single-channel or multichannel biquad IIR filter, returning the filtered signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/biquad/apply(input:output:))*