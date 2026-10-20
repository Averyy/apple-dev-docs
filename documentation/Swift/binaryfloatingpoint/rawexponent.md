# RawExponent

**Framework**: Swift  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

A type that represents the encoded exponent of a value.

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
associatedtype RawExponent : UnsignedInteger
```

## See Also

### Working with Binary Representation
- [var binade: Self](./binade.md)
  The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
- [var exponentBitPattern: Self.RawExponent](./exponentbitpattern.md)
  The raw encoding of the value’s exponent field.
- [var significandBitPattern: Self.RawSignificand](./significandbitpattern.md)
  The raw encoding of the value’s significand field.
- [var significandWidth: Int](./significandwidth.md)
  The number of bits required to represent the value’s significand.
- [static var exponentBitCount: Int](./exponentbitcount.md)
  The number of bits used to represent the type’s exponent.
- [static var significandBitCount: Int](./significandbitcount.md)
  The available number of fractional significand bits.
- [init(sign: FloatingPointSign, exponentBitPattern: Self.RawExponent, significandBitPattern: Self.RawSignificand)](./init%28sign,exponentbitpattern,significandbitpattern%29.md)
  Creates a new instance from the specified sign and bit patterns.
- [associatedtype RawSignificand : UnsignedInteger](./rawsignificand.md)
  A type that represents the encoded significand of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryfloatingpoint/rawexponent)*