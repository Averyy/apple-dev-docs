# vDSP.Biquad

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A single- or double-precision biquadratic filter.

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
struct Biquad<T> where T : vDSP_FloatingPointBiquadFilterable
```

## Overview

> **Note**:  The vDSP biquadratic filters work in place. That is, the source and destination pointers may point to the same memory.

## Topics

### Initializers
- [init?(coefficients: [Double], channelCount: vDSP_Length, sectionCount: vDSP_Length, ofType: T.Type)](./biquad/init%28coefficients,channelcount,sectioncount,oftype%29.md)
  Creates a new single-channel or multichannel cascaded biquad IIR structure.
### Instance methods
- [func apply<U>(input: U) -> [T]](./biquad/apply%28input%29.md)
  Applies a single- or double-precision single-channel or multichannel biquad IIR filter, returning the filtered signal.
- [func apply<U, V>(input: U, output: inout V)](./biquad/apply%28input,output%29.md)
  Applies a single- or double-precision single-channel or multichannel biquad IIR filter, overwriting the supplied output vector.

## See Also

### Biquadratic IIR Filters
- [Equalizing audio with discrete cosine transforms (DCTs)](../equalizing-audio-with-discrete-cosine-transforms-dcts.md)
  Change the frequency response of an audio signal by manipulating frequency-domain data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/biquad)*