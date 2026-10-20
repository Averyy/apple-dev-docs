# exponentBitCount

**Framework**: Swift  
**Kind**: property  
**Role**: Type Property

The number of bits used to represent the type’s exponent.

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
static var exponentBitCount: Int { get }
```

#### Discussion

A binary floating-point type’s `exponentBitCount` imposes a limit on the range of the exponent for normal, finite values. The *exponent bias* of a type `F` can be calculated as the following, where `**` is exponentiation:

```swift
let bias = 2 ** (F.exponentBitCount - 1) - 1
```

The least normal exponent for values of the type `F` is `1 - bias`, and the largest finite exponent is `bias`. An all-zeros exponent is reserved for subnormals and zeros, and an all-ones exponent is reserved for infinity and NaN.

For example, the `Float` type has an `exponentBitCount` of 8, which gives an exponent bias of `127` by the calculation above.

```swift
let bias = 2 ** (Float.exponentBitCount - 1) - 1
// bias == 127
print(Float.greatestFiniteMagnitude.exponent)
// Prints "127"
print(Float.leastNormalMagnitude.exponent)
// Prints "-126"
```

## See Also

### Working with Binary Representation
- [var bitPattern: UInt32](./bitpattern.md)
  The bit pattern of the value’s encoding.
- [var significandBitPattern: UInt32](./significandbitpattern.md)
  The raw encoding of the value’s significand field.
- [var significandWidth: Int](./significandwidth.md)
  The number of bits required to represent the value’s significand.
- [var exponentBitPattern: UInt](./exponentbitpattern.md)
  The raw encoding of the value’s exponent field.
- [static var significandBitCount: Int](./significandbitcount.md)
  The available number of fractional significand bits.
- [static var radix: Int](./radix.md)
  The radix, or base of exponentiation, for a floating-point type.
- [init(bitPattern: UInt32)](./init%28bitpattern%29.md)
  Creates a new value with the given bit pattern.
- [init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt32)](./init%28sign,exponentbitpattern,significandbitpattern%29.md)
  Creates a new instance from the specified sign and bit patterns.
- [init(nan: Float.RawSignificand, signaling: Bool)](./init%28nan,signaling%29.md)
  Creates a NaN (“not a number”) value with the specified payload.
- [typealias Exponent](./exponent-swift.typealias.md)
  A type that can represent any written exponent.
- [typealias RawSignificand](./rawsignificand.md)
  A type that represents the encoded significand of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/exponentbitcount)*