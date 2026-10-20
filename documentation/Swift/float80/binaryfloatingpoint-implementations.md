# BinaryFloatingPoint Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Initializers
- [init(Double)](./init%28_%29-4rh2n.md)
  Creates a new instance that approximates the given value.
- [init(Float)](./init%28_%29-5jn4i.md)
  Creates a new instance that approximates the given value.
- [init<Source>(Source)](./init%28_%29-5yold.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init(Float80)](./init%28_%29-6dyii.md)
  Creates a new instance initialized to the given value.
- [init<Source>(Source)](./init%28_%29-8p2oa.md)
  Creates a new value, rounded to the closest possible representation.
- [init?<Source>(exactly: Source)](./init%28exactly%29-5ggvi.md)
  Creates a new value, if the given integer can be represented exactly.
- [init?<Source>(exactly: Source)](./init%28exactly%29-9oml5.md)
  Creates a new instance from the given value, if it can be represented exactly.
- [init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt64)](./init%28sign,exponentbitpattern,significandbitpattern%29.md)
  Creates a new instance from the specified sign and bit patterns.
### Instance Properties
- [var binade: Float80](./binade.md)
  The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
- [var exponentBitPattern: UInt](./exponentbitpattern.md)
  The raw encoding of the value’s exponent field.
- [var significandBitPattern: UInt64](./significandbitpattern.md)
  The raw encoding of the value’s significand field.
- [var significandWidth: Int](./significandwidth.md)
  The number of bits required to represent the value’s significand.
### Type Aliases
- [typealias RawExponent](./rawexponent.md)
  A type that represents the encoded exponent of a value.
- [typealias RawSignificand](./rawsignificand.md)
  A type that represents the encoded significand of a value.
### Type Properties
- [static var exponentBitCount: Int](./exponentbitcount.md)
  The number of bits used to represent the type’s exponent.
- [static var significandBitCount: Int](./significandbitcount.md)
  The available number of fractional significand bits.
### Type Methods
- [static func random(in: Range<Self>) -> Self](./random%28in%29-3nivi.md)
  Returns a random value within the specified range.
- [static func random(in: ClosedRange<Self>) -> Self](./random%28in%29-5zpax.md)
  Returns a random value within the specified range.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](./random%28in,using%29-2llvb.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](./random%28in,using%29-lxqd.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/binaryfloatingpoint-implementations)*