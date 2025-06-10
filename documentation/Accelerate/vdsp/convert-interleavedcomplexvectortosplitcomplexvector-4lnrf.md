# convert(interleavedComplexVector:toSplitComplexVector:)

**Framework**: Accelerate  
**Kind**: method

Converts the contents of an interleaved single-precision complex vector to a split complex vector.

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
static func convert(interleavedComplexVector: [DSPComplex], toSplitComplexVector splitComplexVector: inout DSPSplitComplex)
```

## Mentions

- [Finding the component frequencies in a composite sine wave](finding-the-component-frequencies-in-a-composite-sine-wave.md)

## Parameters

- `interleavedComplexVector`: The interleaved-complex source vector.
- `splitComplexVector`: The split-complex destination vector.

## See Also

- [static func convert(interleavedComplexVector: [DSPDoubleComplex], toSplitComplexVector: inout DSPDoubleSplitComplex)](vdsp/convert(interleavedcomplexvector:tosplitcomplexvector:)-8cqd4.md)
  Converts the contents of an interleaved double-precision complex vector to a split complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/convert(interleavedcomplexvector:tosplitcomplexvector:)-4lnrf)*