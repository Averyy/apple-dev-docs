# BinaryFloatingPoint

**Framework**: Swift  
**Kind**: protocol  
**Role**: Protocol

A radix-2 (binary) floating-point type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol BinaryFloatingPoint : ExpressibleByFloatLiteral, FloatingPoint
```

## Overview

The `BinaryFloatingPoint` protocol extends the `FloatingPoint` protocol with operations specific to floating-point binary types, as defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933). `BinaryFloatingPoint` is implemented in the standard library by `Float`, `Double`, and `Float80` where available.

## Topics

### Converting Floating-Point Values
- [init(Float)](./binaryfloatingpoint/init%28_%29-57jx7.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init(Double)](./binaryfloatingpoint/init%28_%29-7ft14.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init(Float80)](./binaryfloatingpoint/init%28_%29-1nijh.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init<Source>(Source)](./binaryfloatingpoint/init%28_%29-shau.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
### Converting with No Loss of Precision
- [init?<Source>(exactly: Source)](./binaryfloatingpoint/init%28exactly%29.md)
  Creates a new instance from the given value, if it can be represented exactly.
### Creating a Random Value
- [static func random(in: ClosedRange<Self>) -> Self](./binaryfloatingpoint/random%28in%29-2j16p.md)
  Returns a random value within the specified range.
- [static func random(in: Range<Self>) -> Self](./binaryfloatingpoint/random%28in%29-8jkjb.md)
  Returns a random value within the specified range.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](./binaryfloatingpoint/random%28in,using%29-6pf7f.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](./binaryfloatingpoint/random%28in,using%29-2awm8.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
### Working with Binary Representation
- [var binade: Self](./binaryfloatingpoint/binade.md)
  The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
- [var exponentBitPattern: Self.RawExponent](./binaryfloatingpoint/exponentbitpattern.md)
  The raw encoding of the value’s exponent field.
- [var significandBitPattern: Self.RawSignificand](./binaryfloatingpoint/significandbitpattern.md)
  The raw encoding of the value’s significand field.
- [var significandWidth: Int](./binaryfloatingpoint/significandwidth.md)
  The number of bits required to represent the value’s significand.
- [static var exponentBitCount: Int](./binaryfloatingpoint/exponentbitcount.md)
  The number of bits used to represent the type’s exponent.
- [static var significandBitCount: Int](./binaryfloatingpoint/significandbitcount.md)
  The available number of fractional significand bits.
- [init(sign: FloatingPointSign, exponentBitPattern: Self.RawExponent, significandBitPattern: Self.RawSignificand)](./binaryfloatingpoint/init%28sign,exponentbitpattern,significandbitpattern%29.md)
  Creates a new instance from the specified sign and bit patterns.
- [associatedtype RawExponent : UnsignedInteger](./binaryfloatingpoint/rawexponent.md)
  A type that represents the encoded exponent of a value.
- [associatedtype RawSignificand : UnsignedInteger](./binaryfloatingpoint/rawsignificand.md)
  A type that represents the encoded significand of a value.
### Initializers
- [init(String, format: FloatingPointFormatStyle<Self>.Percent, lenient: Bool) throws](./binaryfloatingpoint/init%28_,format,lenient%29-166j0.md)
- [init(String, format: FloatingPointFormatStyle<Self>.Currency, lenient: Bool) throws](./binaryfloatingpoint/init%28_,format,lenient%29-2b9qt.md)
- [init(String, format: FloatingPointFormatStyle<Self>, lenient: Bool) throws](./binaryfloatingpoint/init%28_,format,lenient%29-2p118.md)
  Initialize an instance by parsing `value` with a `ParseStrategy` created with the given `format` and the `lenient` argument.
- [init<S>(S.ParseInput, strategy: S) throws](./binaryfloatingpoint/init%28_,strategy%29-4vta0.md)
  Initialize an instance by parsing `value` with the given `strategy`.
### Instance Methods
- [func formatted() -> String](./binaryfloatingpoint/formatted%28%29.md)
  Format `self` with `FloatingPointFormatStyle()`.
- [func formatted<S>(S) -> S.FormatOutput](./binaryfloatingpoint/formatted%28_%29-4ksqj.md)
  Format `self` with the given format.
- [func formatted<S>(S) -> S.FormatOutput](./binaryfloatingpoint/formatted%28_%29-83x4n.md)
  Format `self` with the given format. `self` is first converted to `S.FormatInput` type, then format with the given format.
### Default Implementations
- [BinaryFloatingPoint Implementations](./binaryfloatingpoint/binaryfloatingpoint-implementations.md)

## Relationships

### Inherits From
- [AdditiveArithmetic](./additivearithmetic.md)
- [Comparable](./comparable.md)
- [Equatable](./equatable.md)
- [ExpressibleByFloatLiteral](./expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](./expressiblebyintegerliteral.md)
- [FloatingPoint](./floatingpoint.md)
- [Hashable](./hashable.md)
- [Numeric](./numeric.md)
- [SignedNumeric](./signednumeric.md)
- [Strideable](./strideable.md)
### Conforming Types
- [Double](./double.md)
- [Float](./float.md)
- [Float16](./float16.md)
- [Float80](./float80.md)

## See Also

### Floating Point
- [protocol FloatingPoint](./floatingpoint.md)
  A floating-point numeric type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryfloatingpoint)*