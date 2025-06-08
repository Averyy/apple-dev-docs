# Type conversion

**Framework**: Accelerate

Perform element-wise floating-point to integer and integer to floating-point conversion.

## Topics

### Conversion between floating-point types
- [static func doubleToFloat<U>(U) -> [Float]](vdsp/doubletofloat(_:).md)
  Returns single-precision values converted from a double-precision source.
- [static func floatToDouble<U>(U) -> [Double]](vdsp/floattodouble(_:).md)
  Returns double-precision values converted from a single-precision source.
- [static func convertElements<U, V>(of: U, to: inout V)](vdsp/convertelements(of:to:)-2ejgr.md)
  Converts single-precision values to double-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](vdsp/convertelements(of:to:)-698ye.md)
  Converts double-precision values to single-precision values.
- [vDSP_vspdp](vdsp_vspdp.md)
  Converts a single-precision vector to a double-precision vector.
- [vDSP_vdpsp](vdsp_vdpsp.md)
  Converts a double-precision vector to a single-precision vector.
### Conversion between floating-point and integer types
- [Integer to single-precision floating-point conversion](integer-to-single-precision-floating-point-conversion.md)
  Perform element-wise integer to single-precision floating-point conversion.
- [Integer to double-precision floating-point conversion](integer-to-double-precision-floating-point-conversion.md)
  Perform element-wise integer to double-precision floating-point conversion.
- [Single-precision floating point to integer conversion](single-precision-floating-point-to-integer-conversion.md)
  Perform element-wise single-precision floating-point to integer conversion.
- [Double-precision floating point to integer conversion](double-precision-floating-point-to-integer-conversion.md)
  Perform element-wise double-precision floating-point to integer conversion.

## See Also

- [Conversion to decibel equivalents](conversion-to-decibel-equivalents.md)
  Convert vectors that contain power or amplitude data to decibels.
- [Complex vector conversion](complex-vector-conversion.md)
  Perform element-wise split-complex to interleaved and interleaved to split-complex conversion.
- [Polar-rectangular conversion](polar-rectangular-conversion.md)
  Convert each element of a vector between radius-angle and Cartesian pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/type-conversion)*