# init(sign:exponentBitPattern:significandBitPattern:)

**Framework**: Swift  
**Kind**: init  
**Required**: Yes

Creates a new instance from the specified sign and bit patterns.

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
init(sign: FloatingPointSign, exponentBitPattern: Self.RawExponent, significandBitPattern: Self.RawSignificand)
```

#### Discussion

The values passed as `exponentBitPattern` and `significandBitPattern` are interpreted in the binary interchange format defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `sign`: The sign of the new value.
- `exponentBitPattern`: The bit pattern to use for the exponent field of   the new value.
- `significandBitPattern`: The bit pattern to use for the significand   field of the new value.

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
- [static var significandBitCount: Int](binaryfloatingpoint/significandbitcount.md)
  The available number of fractional significand bits.
- [associatedtype RawExponent : UnsignedInteger](binaryfloatingpoint/rawexponent.md)
  A type that represents the encoded exponent of a value.
- [associatedtype RawSignificand : UnsignedInteger](binaryfloatingpoint/rawsignificand.md)
  A type that represents the encoded significand of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryfloatingpoint/init(sign:exponentbitpattern:significandbitpattern:))*