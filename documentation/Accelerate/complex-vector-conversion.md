# Complex vector conversion

**Framework**: Accelerate  
**Role**: API Collection

Perform element-wise split-complex to interleaved and interleaved to split-complex conversion.

## Topics

### Converting interleaved-complex vectors to split-complex vectors
- [static func convert(interleavedComplexVector: [DSPComplex], toSplitComplexVector: inout DSPSplitComplex)](./vdsp/convert%28interleavedcomplexvector,tosplitcomplexvector%29-4lnrf.md)
  Converts the contents of an interleaved single-precision complex vector to a split complex vector.
- [static func convert(interleavedComplexVector: [DSPDoubleComplex], toSplitComplexVector: inout DSPDoubleSplitComplex)](./vdsp/convert%28interleavedcomplexvector,tosplitcomplexvector%29-8cqd4.md)
  Converts the contents of an interleaved double-precision complex vector to a split complex vector.
- [vDSP_ctoz](./vdsp_ctoz.md)
  Copies the contents of an interleaved single-precision complex vector to a split complex vector.
- [vDSP_ctozD](./vdsp_ctozd.md)
  Copies the contents of an interleaved double-precision complex vector to a split complex vector.
### Converting split-complex vectors to interleaved-complex vectors
- [static func convert(splitComplexVector: DSPSplitComplex, toInterleavedComplexVector: inout [DSPComplex])](./vdsp/convert%28splitcomplexvector,tointerleavedcomplexvector%29-65gyx.md)
  Converts the contents of a split single-precision complex vector to an interleaved vector.
- [static func convert(splitComplexVector: DSPDoubleSplitComplex, toInterleavedComplexVector: inout [DSPDoubleComplex])](./vdsp/convert%28splitcomplexvector,tointerleavedcomplexvector%29-9v193.md)
  Converts the contents of a split double-precision complex vector to an interleaved vector.
- [vDSP_ztoc](./vdsp_ztoc.md)
  Copies the contents of a split single-precision complex vector to an interleaved vector.
- [vDSP_ztocD](./vdsp_ztocd.md)
  Copies the contents of a split double-precision complex vector to an interleaved vector.

## See Also

### Vector conversion functions
- [Conversion to decibel equivalents](./conversion-to-decibel-equivalents.md)
  Convert vectors that contain power or amplitude data to decibels.
- [Type conversion](./type-conversion.md)
  Perform element-wise floating-point to integer and integer to floating-point conversion.
- [Polar-rectangular conversion](./polar-rectangular-conversion.md)
  Convert each element of a vector between radius-angle and Cartesian pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/complex-vector-conversion)*