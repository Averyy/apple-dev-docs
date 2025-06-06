# nonzeroBitCount

**Framework**: Swift  
**Kind**: property

The number of bits equal to 1 in this value’s binary representation.

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
var nonzeroBitCount: Int { get }
```

#### Discussion

For example, in a fixed-width integer type with a `bitWidth` value of 8, the number  has five bits equal to .

```swift
let x: Int8 = 0b0001_1111
// x == 31
// x.nonzeroBitCount == 5
```

## See Also

- [static var bitWidth: Int](int/bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
- [var bitWidth: Int](int/bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var leadingZeroBitCount: Int](int/leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var trailingZeroBitCount: Int](int/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: Int.Words](int/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
- [struct Words](int/words-swift.struct.md)
  A type that represents the words of this integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/nonzerobitcount)*