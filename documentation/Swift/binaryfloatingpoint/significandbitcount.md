# significandBitCount

**Framework**: Swift  
**Kind**: property  
**Required**: Yes

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

- [var binade: Self](binaryfloatingpoint/binade.md)
  The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
- [var exponentBitPattern: Self.RawExponent](binaryfloatingpoint/exponentbitpattern.md)
  The raw encoding of the value’s exponent field.
- [var significandBitPattern: Self.RawSignificand](binaryfloatingpoint/significandbitpattern.md)
  The raw encoding of the value’s significand field.
- [var significandWidth: Int](binaryfloatingpoint/significandwidth.md)
  The number of bits required to represent the value’s significand.
- [static var exponentBitCount: Int](binaryfloatingpoint/exponentbitcount.md)
  The number of bits used to represent the type’s exponent.
- [init(sign: FloatingPointSign, exponentBitPattern: Self.RawExponent, significandBitPattern: Self.RawSignificand)](binaryfloatingpoint/init(sign:exponentbitpattern:significandbitpattern:).md)
  Creates a new instance from the specified sign and bit patterns.
- [associatedtype RawExponent : UnsignedInteger](binaryfloatingpoint/rawexponent.md)
  A type that represents the encoded exponent of a value.
- [associatedtype RawSignificand : UnsignedInteger](binaryfloatingpoint/rawsignificand.md)
  A type that represents the encoded significand of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryfloatingpoint/significandbitcount)*