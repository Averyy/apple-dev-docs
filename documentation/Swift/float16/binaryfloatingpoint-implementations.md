# BinaryFloatingPoint Implementations

**Framework**: Swift

## Topics

### Initializers
- [init(Float)](float16/init(_:)-469bw.md)
  Creates a new instance that approximates the given value.
- [init<Source>(Source)](float16/init(_:)-6u8fq.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init<Source>(Source)](float16/init(_:)-7teyd.md)
  Creates a new value, rounded to the closest possible representation.
- [init(Double)](float16/init(_:)-7x3fq.md)
  Creates a new instance that approximates the given value.
- [init?<Source>(exactly: Source)](float16/init(exactly:)-6c0t5.md)
  Creates a new value, if the given integer can be represented exactly.
- [init?<Source>(exactly: Source)](float16/init(exactly:)-d42j.md)
  Creates a new instance from the given value, if it can be represented exactly.
- [init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt16)](float16/init(sign:exponentbitpattern:significandbitpattern:).md)
  Creates a new instance from the specified sign and bit patterns.
### Instance Properties
- [var binade: Float16](float16/binade.md)
  The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
- [var exponentBitPattern: UInt](float16/exponentbitpattern.md)
  The raw encoding of the value’s exponent field.
- [var significandBitPattern: UInt16](float16/significandbitpattern.md)
  The raw encoding of the value’s significand field.
- [var significandWidth: Int](float16/significandwidth.md)
  The number of bits required to represent the value’s significand.
### Type Aliases
- [typealias RawExponent](float16/rawexponent.md)
  A type that represents the encoded exponent of a value.
- [typealias RawSignificand](float16/rawsignificand.md)
  A type that represents the encoded significand of a value.
### Type Properties
- [static var exponentBitCount: Int](float16/exponentbitcount.md)
  The number of bits used to represent the type’s exponent.
- [static var significandBitCount: Int](float16/significandbitcount.md)
  The available number of fractional significand bits.
### Type Methods
- [static func random(in: Range<Self>) -> Self](float16/random(in:)-4blql.md)
  Returns a random value within the specified range.
- [static func random(in: ClosedRange<Self>) -> Self](float16/random(in:)-6nryy.md)
  Returns a random value within the specified range.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](float16/random(in:using:)-1prt0.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](float16/random(in:using:)-9qt91.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/binaryfloatingpoint-implementations)*