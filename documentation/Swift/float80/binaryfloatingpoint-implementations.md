# BinaryFloatingPoint Implementations

**Framework**: Swift

## Topics

### Initializers
- [init(Double)](float80/init(_:)-4rh2n.md)
  Creates a new instance that approximates the given value.
- [init(Float)](float80/init(_:)-5jn4i.md)
  Creates a new instance that approximates the given value.
- [init<Source>(Source)](float80/init(_:)-5yold.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init(Float80)](float80/init(_:)-6dyii.md)
  Creates a new instance initialized to the given value.
- [init<Source>(Source)](float80/init(_:)-8p2oa.md)
  Creates a new value, rounded to the closest possible representation.
- [init?<Source>(exactly: Source)](float80/init(exactly:)-5ggvi.md)
  Creates a new value, if the given integer can be represented exactly.
- [init?<Source>(exactly: Source)](float80/init(exactly:)-9oml5.md)
  Creates a new instance from the given value, if it can be represented exactly.
- [init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt64)](float80/init(sign:exponentbitpattern:significandbitpattern:).md)
  Creates a new instance from the specified sign and bit patterns.
### Instance Properties
- [var binade: Float80](float80/binade.md)
  The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
- [var exponentBitPattern: UInt](float80/exponentbitpattern.md)
  The raw encoding of the value’s exponent field.
- [var significandBitPattern: UInt64](float80/significandbitpattern.md)
  The raw encoding of the value’s significand field.
- [var significandWidth: Int](float80/significandwidth.md)
  The number of bits required to represent the value’s significand.
### Type Aliases
- [typealias RawExponent](float80/rawexponent.md)
  A type that represents the encoded exponent of a value.
- [typealias RawSignificand](float80/rawsignificand.md)
  A type that represents the encoded significand of a value.
### Type Properties
- [static var exponentBitCount: Int](float80/exponentbitcount.md)
  The number of bits used to represent the type’s exponent.
- [static var significandBitCount: Int](float80/significandbitcount.md)
  The available number of fractional significand bits.
### Type Methods
- [static func random(in: Range<Self>) -> Self](float80/random(in:)-3nivi.md)
  Returns a random value within the specified range.
- [static func random(in: ClosedRange<Self>) -> Self](float80/random(in:)-5zpax.md)
  Returns a random value within the specified range.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](float80/random(in:using:)-2llvb.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](float80/random(in:using:)-lxqd.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/binaryfloatingpoint-implementations)*