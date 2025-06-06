# significandWidth

**Framework**: Swift  
**Kind**: property

The number of bits required to represent the value’s significand.

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
var significandWidth: Int { get }
```

#### Discussion

If this value is a finite nonzero number, `significandWidth` is the number of fractional bits required to represent the value of `significand`; otherwise, `significandWidth` is -1. The value of `significandWidth` is always -1 or between zero and `significandBitCount`. For example:

- For any representable power of two, `significandWidth` is zero, because `significand` is `1.0`.
- If `x` is 10, `x.significand` is `1.01` in binary, so `x.significandWidth` is 2.
- If `x` is Float.pi, `x.significand` is `1.10010010000111111011011` in binary, and `x.significandWidth` is 23.

## See Also

- [var bitPattern: UInt32](float/bitpattern.md)
  The bit pattern of the value’s encoding.
- [var significandBitPattern: UInt32](float/significandbitpattern.md)
  The raw encoding of the value’s significand field.
- [var exponentBitPattern: UInt](float/exponentbitpattern.md)
  The raw encoding of the value’s exponent field.
- [static var significandBitCount: Int](float/significandbitcount.md)
  The available number of fractional significand bits.
- [static var exponentBitCount: Int](float/exponentbitcount.md)
  The number of bits used to represent the type’s exponent.
- [static var radix: Int](float/radix.md)
  The radix, or base of exponentiation, for a floating-point type.
- [init(bitPattern: UInt32)](float/init(bitpattern:).md)
  Creates a new value with the given bit pattern.
- [init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt32)](float/init(sign:exponentbitpattern:significandbitpattern:).md)
  Creates a new instance from the specified sign and bit patterns.
- [init(nan: Float.RawSignificand, signaling: Bool)](float/init(nan:signaling:).md)
  Creates a NaN (“not a number”) value with the specified payload.
- [typealias Exponent](float/exponent-swift.typealias.md)
  A type that can represent any written exponent.
- [typealias RawSignificand](float/rawsignificand.md)
  A type that represents the encoded significand of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/significandwidth)*