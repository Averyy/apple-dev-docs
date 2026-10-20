# convert(splitComplexVector:toInterleavedComplexVector:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Converts the contents of a split double-precision complex vector to an interleaved vector.

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
static func convert(splitComplexVector: DSPDoubleSplitComplex, toInterleavedComplexVector interleavedComplexVector: inout [DSPDoubleComplex])
```

## Parameters

- `splitComplexVector`: The split-complex source vector.
- `interleavedComplexVector`: The interleaved-complex destination vector.

## See Also

### Converting split-complex vectors to interleaved-complex vectors
- [static func convert(splitComplexVector: DSPSplitComplex, toInterleavedComplexVector: inout [DSPComplex])](./convert%28splitcomplexvector,tointerleavedcomplexvector%29-65gyx.md)
  Converts the contents of a split single-precision complex vector to an interleaved vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/convert(splitcomplexvector:tointerleavedcomplexvector:)-9v193)*