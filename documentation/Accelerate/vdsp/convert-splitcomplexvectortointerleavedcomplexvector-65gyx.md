# convert(splitComplexVector:toInterleavedComplexVector:)

**Framework**: Accelerate  
**Kind**: method

Converts the contents of a split single-precision complex vector to an interleaved vector.

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
static func convert(splitComplexVector: DSPSplitComplex, toInterleavedComplexVector interleavedComplexVector: inout [DSPComplex])
```

## Parameters

- `splitComplexVector`: The split-complex source vector.
- `interleavedComplexVector`: The interleaved-complex destination vector.

## See Also

- [static func convert(splitComplexVector: DSPDoubleSplitComplex, toInterleavedComplexVector: inout [DSPDoubleComplex])](vdsp/convert(splitcomplexvector:tointerleavedcomplexvector:)-9v193.md)
  Converts the contents of a split double-precision complex vector to an interleaved vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/convert(splitcomplexvector:tointerleavedcomplexvector:)-65gyx)*