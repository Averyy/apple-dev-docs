# Numeric Protocols

**Framework**: Swift

Write generic code that works with any numeric type.

## Topics

### Basic Arithmetic
- [protocol AdditiveArithmetic](additivearithmetic.md)
  A type with values that support addition and subtraction.
- [protocol Numeric](numeric.md)
  A type with values that support multiplication.
- [protocol SignedNumeric](signednumeric.md)
  A numeric type with a negation operation.
- [protocol Strideable](strideable.md)
  A type representing continuous, one-dimensional values that can be offset and measured.
### Integer
- [protocol BinaryInteger](binaryinteger.md)
  An integer type with a binary representation.
- [protocol FixedWidthInteger](fixedwidthinteger.md)
  An integer type that uses a fixed size for every instance.
- [protocol SignedInteger](signedinteger.md)
  An integer type that can represent both positive and negative values.
- [protocol UnsignedInteger](unsignedinteger.md)
  An integer type that can represent only nonnegative values.
### Floating Point
- [protocol FloatingPoint](floatingpoint.md)
  A floating-point numeric type.
- [protocol BinaryFloatingPoint](binaryfloatingpoint.md)
  A radix-2 (binary) floating-point type.
### Floating-Point Characteristics
- [enum FloatingPointClassification](floatingpointclassification.md)
  The IEEE 754 floating-point classes.
- [enum FloatingPointRoundingRule](floatingpointroundingrule.md)
  A rule for rounding a floating-point number.
- [enum FloatingPointSign](floatingpointsign.md)
  The sign of a floating-point value.

## See Also

- [Special-Use Numeric Types](special-use-numeric-types.md)
  Work with fixed-width numeric types of different sizes.
- [SIMD Vector Types](simd-vector-types.md)
  Work with fixed-width vectors of fixed-width numeric types of different sizes.
- [Global Numeric Functions](global-numeric-functions.md)
  Use these functions with numeric values and other comparable types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/numeric-protocols)*