# Words

**Framework**: Swift  
**Kind**: associatedtype  
**Required**: Yes

A type that represents the words of a binary integer.

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
associatedtype Words : RandomAccessCollection where Self.Words.Element == UInt, Self.Words.Index == Int
```

#### Discussion

The `Words` type must conform to the `RandomAccessCollection` protocol with an `Element` type of `UInt` and `Index` type of `Int`.

## See Also

- [var bitWidth: Int](binaryinteger/bitwidth.md)
  The number of bits in the current binary representation of this value.
- [var trailingZeroBitCount: Int](binaryinteger/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: Self.Words](binaryinteger/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryinteger/words-swift.associatedtype)*