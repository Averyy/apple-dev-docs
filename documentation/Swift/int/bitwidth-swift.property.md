# bitWidth

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

The number of bits in the current binary representation of this value.

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
var bitWidth: Int { get }
```

#### Discussion

This property is a constant for instances of fixed-width integer types.

## See Also

### Working with Binary Representation
- [static var bitWidth: Int](./bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
- [var nonzeroBitCount: Int](./nonzerobitcount.md)
  The number of bits equal to 1 in this value’s binary representation.
- [var leadingZeroBitCount: Int](./leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var trailingZeroBitCount: Int](./trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: Int.Words](./words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
- [struct Words](./words-swift.struct.md)
  A type that represents the words of this integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/bitwidth-swift.property)*