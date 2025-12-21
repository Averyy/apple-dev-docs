# Complex vector conversion

**Framework**: Accelerate

Perform element-wise split-complex to interleaved and interleaved to split-complex conversion.

## Topics

### Converting interleaved-complex vectors to split-complex vectors
- [static func convert(interleavedComplexVector: [DSPComplex], toSplitComplexVector: inout DSPSplitComplex)](vdsp/convert(interleavedcomplexvector:tosplitcomplexvector:)-4lnrf.md)
  Converts the contents of an interleaved single-precision complex vector to a split complex vector.
- [static func convert(interleavedComplexVector: [DSPDoubleComplex], toSplitComplexVector: inout DSPDoubleSplitComplex)](vdsp/convert(interleavedcomplexvector:tosplitcomplexvector:)-8cqd4.md)
  Converts the contents of an interleaved double-precision complex vector to a split complex vector.
### Converting split-complex vectors to interleaved-complex vectors
- [static func convert(splitComplexVector: DSPSplitComplex, toInterleavedComplexVector: inout [DSPComplex])](vdsp/convert(splitcomplexvector:tointerleavedcomplexvector:)-65gyx.md)
  Converts the contents of a split single-precision complex vector to an interleaved vector.
- [static func convert(splitComplexVector: DSPDoubleSplitComplex, toInterleavedComplexVector: inout [DSPDoubleComplex])](vdsp/convert(splitcomplexvector:tointerleavedcomplexvector:)-9v193.md)
  Converts the contents of a split double-precision complex vector to an interleaved vector.

## See Also

- [Conversion to decibel equivalents](conversion-to-decibel-equivalents.md)
  Convert vectors that contain power or amplitude data to decibels.
- [Type conversion](type-conversion.md)
  Perform element-wise floating-point to integer and integer to floating-point conversion.
- [Polar-rectangular conversion](polar-rectangular-conversion.md)
  Convert each element of a vector between radius-angle and Cartesian pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/complex-vector-conversion)*