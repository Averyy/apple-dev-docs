# significandBitPattern

**Framework**: Swift  
**Kind**: property

The raw encoding of the value’s significand field.

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
var significandBitPattern: UInt32 { get }
```

#### Discussion

The `significandBitPattern` property does not include the leading integral bit of the significand, even for types like `Float80` that store it explicitly.

## See Also

- [var bitPattern: UInt32](float/bitpattern.md)
  The bit pattern of the value’s encoding.
- [var significandWidth: Int](float/significandwidth.md)
  The number of bits required to represent the value’s significand.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/significandbitpattern)*