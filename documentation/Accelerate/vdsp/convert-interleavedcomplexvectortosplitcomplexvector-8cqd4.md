# convert(interleavedComplexVector:toSplitComplexVector:)

**Framework**: Accelerate  
**Kind**: method

Converts the contents of an interleaved double-precision complex vector to a split complex vector.

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
static func convert(interleavedComplexVector: [DSPDoubleComplex], toSplitComplexVector splitComplexVector: inout DSPDoubleSplitComplex)
```

## Parameters

- `interleavedComplexVector`: The interleaved complex source vector.
- `splitComplexVector`: The split complex destination vector.

## See Also

- [static func convert(interleavedComplexVector: [DSPComplex], toSplitComplexVector: inout DSPSplitComplex)](vdsp/convert(interleavedcomplexvector:tosplitcomplexvector:)-4lnrf.md)
  Converts the contents of an interleaved single-precision complex vector to a split complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/convert(interleavedcomplexvector:tosplitcomplexvector:)-8cqd4)*