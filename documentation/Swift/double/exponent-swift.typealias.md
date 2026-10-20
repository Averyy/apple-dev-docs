# Double.Exponent

**Framework**: Swift  
**Kind**: typealias  
**Role**: Type Alias

A type that can represent any written exponent.

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
typealias Exponent = Int
```

## See Also

### Working with Binary Representation
- [var bitPattern: UInt64](./bitpattern.md)
  The bit pattern of the value’s encoding.
- [var significandBitPattern: UInt64](./significandbitpattern.md)
  The raw encoding of the value’s significand field.
- [var significandWidth: Int](./significandwidth.md)
  The number of bits required to represent the value’s significand.
- [var exponentBitPattern: UInt](./exponentbitpattern.md)
  The raw encoding of the value’s exponent field.
- [static var significandBitCount: Int](./significandbitcount.md)
  The available number of fractional significand bits.
- [static var exponentBitCount: Int](./exponentbitcount.md)
  The number of bits used to represent the type’s exponent.
- [static var radix: Int](./radix.md)
  The radix, or base of exponentiation, for a floating-point type.
- [init(bitPattern: UInt64)](./init%28bitpattern%29.md)
  Creates a new value with the given bit pattern.
- [init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt64)](./init%28sign,exponentbitpattern,significandbitpattern%29.md)
  Creates a new instance from the specified sign and bit patterns.
- [init(nan: Double.RawSignificand, signaling: Bool)](./init%28nan,signaling%29.md)
  Creates a NaN (“not a number”) value with the specified payload.
- [typealias RawSignificand](./rawsignificand.md)
  A type that represents the encoded significand of a value.
- [typealias RawExponent](./rawexponent.md)
  A type that represents the encoded exponent of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/exponent-swift.typealias)*