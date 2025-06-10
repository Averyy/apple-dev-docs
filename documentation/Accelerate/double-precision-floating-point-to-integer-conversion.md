# Double-precision floating point to integer conversion

**Framework**: Accelerate

Perform element-wise double-precision floating-point to integer conversion.

## Topics

### Floating point to integer conversion
- [static func floatingPointToInteger<T, U>(T, integerType: U.Type, rounding: vDSP.RoundingMode) -> [U]](vdsp/floatingpointtointeger(_:integertype:rounding:)-33dtm.md)
  Returns double-precision values converted to integer values.
- [vDSP.RoundingMode](vdsp/roundingmode.md)
  Floating point to integer conversion rounding modes.
### Floating point to 8-bit integer conversion
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](vdsp/convertelements(of:to:rounding:)-2ig4y.md)
  Converts double-precision values to 8-bit signed integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](vdsp/convertelements(of:to:rounding:)-3sgv7.md)
  Converts double-precision values to 8-bit unsigned integers.
- [vDSP.RoundingMode](vdsp/roundingmode.md)
  Floating point to integer conversion rounding modes.
- [vDSP_vfix8D](vdsp_vfix8d.md)
  Converts a vector of double-precision floating-point values to signed 8-bit integer values, and rounds towards zero.
- [vDSP_vfixr8D](vdsp_vfixr8d.md)
  Converts a vector of double-precision floating-point values to signed 8-bit integer values, and rounds towards the nearest integer.
- [vDSP_vfixu8D](vdsp_vfixu8d.md)
  Converts a vector of double-precision floating-point values to unsigned 8-bit integer values, and rounds towards zero.
- [vDSP_vfixru8D](vdsp_vfixru8d.md)
  Converts a vector of double-precision floating-point values to unsigned 8-bit integer values, and rounds towards the nearest integer.
### Floating point to 16-bit integer conversion
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](vdsp/convertelements(of:to:rounding:)-4xlg5.md)
  Converts double-precision values to 16-bit signed integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](vdsp/convertelements(of:to:rounding:)-2oiwm.md)
  Converts double-precision values to 16-bit unsigned integers.
- [vDSP.RoundingMode](vdsp/roundingmode.md)
  Floating point to integer conversion rounding modes.
- [vDSP_vfix16D](vdsp_vfix16d.md)
  Converts a vector of double-precision floating-point values to signed 16-bit integer values, and rounds towards zero.
- [vDSP_vfixr16D](vdsp_vfixr16d.md)
  Converts a vector of double-precision floating-point values to signed 16-bit integer values, and rounds towards the nearest integer.
- [vDSP_vfixu16D](vdsp_vfixu16d.md)
  Converts a vector of double-precision floating-point values to unsigned 16-bit integer values, and rounds towards zero.
- [vDSP_vfixru16D](vdsp_vfixru16d.md)
  Converts a vector of double-precision floating-point values to unsigned 16-bit integer values, and rounds towards the nearest integer.
### Floating point to 32-bit integer conversion
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](vdsp/convertelements(of:to:rounding:)-3sxak.md)
  Converts double-precision values to 32-bit signed integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](vdsp/convertelements(of:to:rounding:)-3t71v.md)
  Converts double-precision values to 32-bit unsigned integers.
- [vDSP.RoundingMode](vdsp/roundingmode.md)
  Floating point to integer conversion rounding modes.
- [vDSP_vfix32D](vdsp_vfix32d.md)
  Converts a vector of double-precision floating-point values to signed 32-bit integer values, and rounds towards zero.
- [vDSP_vfixr32D](vdsp_vfixr32d.md)
  Converts a vector of double-precision floating-point values to signed 32-bit integer values, and rounds towards the nearest integer.
- [vDSP_vfixu32D](vdsp_vfixu32d.md)
  Converts a vector of double-precision floating-point values to unsigned 32-bit integer values, and rounds towards zero.
- [vDSP_vfixru32D](vdsp_vfixru32d.md)
  Converts a vector of double-precision floating-point values to unsigned 32-bit integer values, and rounds towards the nearest integer.

## See Also

- [Integer to single-precision floating-point conversion](integer-to-single-precision-floating-point-conversion.md)
  Perform element-wise integer to single-precision floating-point conversion.
- [Integer to double-precision floating-point conversion](integer-to-double-precision-floating-point-conversion.md)
  Perform element-wise integer to double-precision floating-point conversion.
- [Single-precision floating point to integer conversion](single-precision-floating-point-to-integer-conversion.md)
  Perform element-wise single-precision floating-point to integer conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/double-precision-floating-point-to-integer-conversion)*