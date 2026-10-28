# init(bitPattern:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a new value with the given bit pattern.

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
init(bitPattern: UInt32)
```

## Discussion

The value passed as `bitPattern` is interpreted in the binary interchange format defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `bitPattern`: The integer encoding of a `Float` instance.

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
- [static var exponentBitCount: Int](./exponentbitcount.md)
  The number of bits used to represent the type’s exponent.
- [static var radix: Int](./radix.md)
  The radix, or base of exponentiation, for a floating-point type.
- [init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt32)](./init%28sign,exponentbitpattern,significandbitpattern%29.md)
  Creates a new instance from the specified sign and bit patterns.
- [init(nan: Float.RawSignificand, signaling: Bool)](./init%28nan,signaling%29.md)
  Creates a NaN (“not a number”) value with the specified payload.
- [typealias Exponent](./exponent-swift.typealias.md)
  A type that can represent any written exponent.
- [typealias RawSignificand](./rawsignificand.md)
  A type that represents the encoded significand of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/init(bitpattern:))*