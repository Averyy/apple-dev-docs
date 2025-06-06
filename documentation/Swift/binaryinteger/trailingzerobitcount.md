# trailingZeroBitCount

**Framework**: Swift  
**Kind**: property  
**Required**: Yes

The number of trailing zeros in this value’s binary representation.

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
var trailingZeroBitCount: Int { get }
```

#### Discussion

For example, in a fixed-width integer type with a `bitWidth` value of 8, the number -8 has three trailing zeros.

```swift
let x = Int8(bitPattern: 0b1111_1000)
// x == -8
// x.trailingZeroBitCount == 3
```

If the value is zero, then `trailingZeroBitCount` is equal to `bitWidth`.

## See Also

- [var bitWidth: Int](binaryinteger/bitwidth.md)
  The number of bits in the current binary representation of this value.
- [var words: Self.Words](binaryinteger/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
- [associatedtype Words : RandomAccessCollection](binaryinteger/words-swift.associatedtype.md)
  A type that represents the words of a binary integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryinteger/trailingzerobitcount)*