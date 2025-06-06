# words

**Framework**: Swift  
**Kind**: property  
**Required**: Yes

A collection containing the words of this value’s binary representation, in order from the least significant to most significant.

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
var words: Self.Words { get }
```

#### Discussion

Negative values are returned in two’s complement representation, regardless of the type’s underlying implementation.

## See Also

- [var bitWidth: Int](binaryinteger/bitwidth.md)
  The number of bits in the current binary representation of this value.
- [var trailingZeroBitCount: Int](binaryinteger/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [associatedtype Words : RandomAccessCollection](binaryinteger/words-swift.associatedtype.md)
  A type that represents the words of a binary integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryinteger/words-swift.property)*