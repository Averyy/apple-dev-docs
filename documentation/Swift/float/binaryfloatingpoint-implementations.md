# BinaryFloatingPoint Implementations

**Framework**: Swift

## Topics

### Initializers
- [init(Float80)](float/init(_:)-11orc.md)
  Creates a new instance that approximates the given value.
- [init<Source>(Source)](float/init(_:)-1488f.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init(Double)](float/init(_:)-1kp2p.md)
  Creates a new instance that approximates the given value.
- [init<Source>(Source)](float/init(_:)-1oh9p.md)
  Creates a new value, rounded to the closest possible representation.
- [init(Float)](float/init(_:)-975tv.md)
  Creates a new instance initialized to the given value.
- [init?<Source>(exactly: Source)](float/init(exactly:)-1h1oe.md)
  Creates a new value, if the given integer can be represented exactly.
- [init?<Source>(exactly: Source)](float/init(exactly:)-8esr8.md)
  Creates a new instance from the given value, if it can be represented exactly.
- [init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt32)](float/init(sign:exponentbitpattern:significandbitpattern:).md)
  Creates a new instance from the specified sign and bit patterns.
### Instance Properties
- [var binade: Float](float/binade.md)
  The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
- [var exponentBitPattern: UInt](float/exponentbitpattern.md)
  The raw encoding of the value’s exponent field.
- [var significandBitPattern: UInt32](float/significandbitpattern.md)
  The raw encoding of the value’s significand field.
- [var significandWidth: Int](float/significandwidth.md)
  The number of bits required to represent the value’s significand.
### Type Aliases
- [typealias RawExponent](float/rawexponent.md)
  A type that represents the encoded exponent of a value.
- [typealias RawSignificand](float/rawsignificand.md)
  A type that represents the encoded significand of a value.
### Type Properties
- [static var exponentBitCount: Int](float/exponentbitcount.md)
  The number of bits used to represent the type’s exponent.
- [static var significandBitCount: Int](float/significandbitcount.md)
  The available number of fractional significand bits.
### Type Methods
- [static func random(in: ClosedRange<Self>) -> Self](float/random(in:)-5o5h8.md)
  Returns a random value within the specified range.
- [static func random(in: Range<Self>) -> Self](float/random(in:)-6ided.md)
  Returns a random value within the specified range.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](float/random(in:using:)-1m6gf.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](float/random(in:using:)-613hx.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/binaryfloatingpoint-implementations)*