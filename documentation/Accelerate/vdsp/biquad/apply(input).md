# apply(input:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Applies a single- or double-precision single-channel or multichannel biquad IIR filter, returning the filtered signal.

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
mutating func apply<U>(input: U) -> [T] where T == U.Element, U : AccelerateBuffer
```

## See Also

### Instance methods
- [func apply<U, V>(input: U, output: inout V)](./apply%28input,output%29.md)
  Applies a single- or double-precision single-channel or multichannel biquad IIR filter, overwriting the supplied output vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/biquad/apply(input:))*