# Single-precision floating point to integer conversion

**Framework**: Accelerate

Perform element-wise single-precision floating-point to integer conversion.

## Topics

### Floating point to integer conversion
- [static func floatingPointToInteger<T, U>(T, integerType: U.Type, rounding: vDSP.RoundingMode) -> [U]](vdsp/floatingpointtointeger(_:integertype:rounding:)-9z84u.md)
  Returns single-precision values converted to integer values.
- [vDSP.RoundingMode](vdsp/roundingmode.md)
  Floating point to integer conversion rounding modes.
### Floating point to 8-bit integer conversion
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](vdsp/convertelements(of:to:rounding:)-48635.md)
  Converts single-precision values to 8-bit signed integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](vdsp/convertelements(of:to:rounding:)-9qu7f.md)
  Converts single-precision values to 8-bit unsigned integers.
- [vDSP.RoundingMode](vdsp/roundingmode.md)
  Floating point to integer conversion rounding modes.
### Floating point to 16-bit integer conversion
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](vdsp/convertelements(of:to:rounding:)-slaa.md)
  Converts single-precision values to 16-bit signed integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](vdsp/convertelements(of:to:rounding:)-3tofv.md)
  Converts single-precision values to 16-bit unsigned integers.
- [vDSP.RoundingMode](vdsp/roundingmode.md)
  Floating point to integer conversion rounding modes.
### Floating point to 24-bit integer conversion
- [struct vDSP_int24](vdsp_int24.md)
  A data structure that holds a 24-bit signed integer value.
- [struct vDSP_uint24](vdsp_uint24.md)
  A data structure that holds a 24-bit unsigned integer value.
### Floating point to 32-bit integer conversion
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](vdsp/convertelements(of:to:rounding:)-2dsry.md)
  Converts single-precision values to 32-bit signed integers.
- [static func convertElements<U, V>(of: U, to: inout V, rounding: vDSP.RoundingMode)](vdsp/convertelements(of:to:rounding:)-14dc1.md)
  Converts single-precision values to 32-bit unsigned integers.
- [vDSP.RoundingMode](vdsp/roundingmode.md)
  Floating point to integer conversion rounding modes.

## See Also

- [Integer to single-precision floating-point conversion](integer-to-single-precision-floating-point-conversion.md)
  Perform element-wise integer to single-precision floating-point conversion.
- [Integer to double-precision floating-point conversion](integer-to-double-precision-floating-point-conversion.md)
  Perform element-wise integer to double-precision floating-point conversion.
- [Double-precision floating point to integer conversion](double-precision-floating-point-to-integer-conversion.md)
  Perform element-wise double-precision floating-point to integer conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/single-precision-floating-point-to-integer-conversion)*