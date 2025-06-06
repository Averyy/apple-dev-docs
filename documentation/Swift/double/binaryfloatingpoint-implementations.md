# BinaryFloatingPoint Implementations

**Framework**: Swift

## Topics

### Initializers
- [init<Source>(Source)](double/init(_:)-1488d.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init<Source>(Source)](double/init(_:)-1oh9r.md)
  Creates a new value, rounded to the closest possible representation.
- [init(Float)](double/init(_:)-5h7qh.md)
  Creates a new instance that approximates the given value.
- [init(Float80)](double/init(_:)-9z7ob.md)
  Creates a new instance that approximates the given value.
- [init(Double)](double/init(_:)-o1k9.md)
  Creates a new instance initialized to the given value.
- [init?<Source>(exactly: Source)](double/init(exactly:)-1h1oc.md)
  Creates a new value, if the given integer can be represented exactly.
- [init?<Source>(exactly: Source)](double/init(exactly:)-8esra.md)
  Creates a new instance from the given value, if it can be represented exactly.
- [init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt64)](double/init(sign:exponentbitpattern:significandbitpattern:).md)
  Creates a new instance from the specified sign and bit patterns.
### Instance Properties
- [var binade: Double](double/binade.md)
  The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
- [var exponentBitPattern: UInt](double/exponentbitpattern.md)
  The raw encoding of the value’s exponent field.
- [var significandBitPattern: UInt64](double/significandbitpattern.md)
  The raw encoding of the value’s significand field.
- [var significandWidth: Int](double/significandwidth.md)
  The number of bits required to represent the value’s significand.
### Type Aliases
- [typealias RawExponent](double/rawexponent.md)
  A type that represents the encoded exponent of a value.
- [typealias RawSignificand](double/rawsignificand.md)
  A type that represents the encoded significand of a value.
### Type Properties
- [static var exponentBitCount: Int](double/exponentbitcount.md)
  The number of bits used to represent the type’s exponent.
- [static var significandBitCount: Int](double/significandbitcount.md)
  The available number of fractional significand bits.
### Type Methods
- [static func random(in: ClosedRange<Self>) -> Self](double/random(in:)-5o5ha.md)
  Returns a random value within the specified range.
- [static func random(in: Range<Self>) -> Self](double/random(in:)-6idef.md)
  Returns a random value within the specified range.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](double/random(in:using:)-1m6gd.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](double/random(in:using:)-613hz.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/binaryfloatingpoint-implementations)*