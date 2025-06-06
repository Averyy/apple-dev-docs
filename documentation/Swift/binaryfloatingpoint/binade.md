# binade

**Framework**: Swift  
**Kind**: property  
**Required**: Yes

The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.

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
var binade: Self { get }
```

#### Discussion

A  is a set of binary floating-point values that all have the same sign and exponent. The `binade` property is a member of the same binade as this value, but with a unit significand.

In this example, `x` has a value of `21.5`, which is stored as `1.34375 * 2**4`, where `**` is exponentiation. Therefore, `x.binade` is equal to `1.0 * 2**4`, or `16.0`.

```swift
let x = 21.5
// x.significand == 1.34375
// x.exponent == 4

let y = x.binade
// y == 16.0
// y.significand == 1.0
// y.exponent == 4
```

## See Also

- [var exponentBitPattern: Self.RawExponent](binaryfloatingpoint/exponentbitpattern.md)
  The raw encoding of the value’s exponent field.
- [var significandBitPattern: Self.RawSignificand](binaryfloatingpoint/significandbitpattern.md)
  The raw encoding of the value’s significand field.
- [var significandWidth: Int](binaryfloatingpoint/significandwidth.md)
  The number of bits required to represent the value’s significand.
- [static var exponentBitCount: Int](binaryfloatingpoint/exponentbitcount.md)
  The number of bits used to represent the type’s exponent.
- [static var significandBitCount: Int](binaryfloatingpoint/significandbitcount.md)
  The available number of fractional significand bits.
- [init(sign: FloatingPointSign, exponentBitPattern: Self.RawExponent, significandBitPattern: Self.RawSignificand)](binaryfloatingpoint/init(sign:exponentbitpattern:significandbitpattern:).md)
  Creates a new instance from the specified sign and bit patterns.
- [associatedtype RawExponent : UnsignedInteger](binaryfloatingpoint/rawexponent.md)
  A type that represents the encoded exponent of a value.
- [associatedtype RawSignificand : UnsignedInteger](binaryfloatingpoint/rawsignificand.md)
  A type that represents the encoded significand of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryfloatingpoint/binade)*