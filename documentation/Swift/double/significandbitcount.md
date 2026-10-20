# significandBitCount

**Framework**: Swift  
**Kind**: property  
**Role**: Type Property

The available number of fractional significand bits.

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
static var significandBitCount: Int { get }
```

#### Discussion

For fixed-width floating-point types, this is the actual number of fractional significand bits.

For extensible floating-point types, `significandBitCount` should be the maximum allowed significand width (without counting any leading integral bit of the significand). If there is no upper limit, then `significandBitCount` should be `Int.max`.

Note that `Float80.significandBitCount` is 63, even though 64 bits are used to store the significand in the memory representation of a `Float80` (unlike other floating-point types, `Float80` explicitly stores the leading integral significand bit, but the `BinaryFloatingPoint` APIs provide an abstraction so that users don’t need to be aware of this detail).

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
- [typealias Exponent](./exponent-swift.typealias.md)
  A type that can represent any written exponent.
- [typealias RawSignificand](./rawsignificand.md)
  A type that represents the encoded significand of a value.
- [typealias RawExponent](./rawexponent.md)
  A type that represents the encoded exponent of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/significandbitcount)*