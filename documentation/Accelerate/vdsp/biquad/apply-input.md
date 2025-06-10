# apply(input:)

**Framework**: Accelerate  
**Kind**: method

Applies a single- or double-precision single-channel or multichannel biquad IIR filter, returning the filtered signal.

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
mutating func apply<U>(input: U) -> [T] where T == U.Element, U : AccelerateBuffer
```

## See Also

- [func apply<U, V>(input: U, output: inout V)](vdsp/biquad/apply(input:output:).md)
  Applies a single- or double-precision single-channel or multichannel biquad IIR filter, overwriting the supplied output vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/biquad/apply(input:))*