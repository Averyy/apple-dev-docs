# Double.RawSignificand

**Framework**: Swift  
**Kind**: typealias

A type that represents the encoded significand of a value.

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
typealias RawSignificand = UInt64
```

## See Also

- [var bitPattern: UInt64](double/bitpattern.md)
  The bit pattern of the value’s encoding.
- [var significandBitPattern: UInt64](double/significandbitpattern.md)
  The raw encoding of the value’s significand field.
- [var significandWidth: Int](double/significandwidth.md)
  The number of bits required to represent the value’s significand.
- [var exponentBitPattern: UInt](double/exponentbitpattern.md)
  The raw encoding of the value’s exponent field.
- [static var significandBitCount: Int](double/significandbitcount.md)
  The available number of fractional significand bits.
- [static var exponentBitCount: Int](double/exponentbitcount.md)
  The number of bits used to represent the type’s exponent.
- [static var radix: Int](double/radix.md)
  The radix, or base of exponentiation, for a floating-point type.
- [init(bitPattern: UInt64)](double/init(bitpattern:).md)
  Creates a new value with the given bit pattern.
- [init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt64)](double/init(sign:exponentbitpattern:significandbitpattern:).md)
  Creates a new instance from the specified sign and bit patterns.
- [init(nan: Double.RawSignificand, signaling: Bool)](double/init(nan:signaling:).md)
  Creates a NaN (“not a number”) value with the specified payload.
- [typealias Exponent](double/exponent-swift.typealias.md)
  A type that can represent any written exponent.
- [typealias RawExponent](double/rawexponent.md)
  A type that represents the encoded exponent of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/rawsignificand)*