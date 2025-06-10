# Int.Words

**Framework**: Swift  
**Kind**: struct

A type that represents the words of this integer.

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
@frozen
struct Words
```

## Topics

### Initializers
- [init(Int)](int/words-swift.struct/init(_:).md)
### Instance Properties
- [var count: Int](int/words-swift.struct/count.md)
  The number of elements in the collection.
- [var endIndex: Int](int/words-swift.struct/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: Int.Words.Indices](int/words-swift.struct/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: Int](int/words-swift.struct/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func index(after: Int) -> Int](int/words-swift.struct/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: Int) -> Int](int/words-swift.struct/index(before:).md)
  Returns the position immediately before the given index.
### Subscripts
- [subscript(Int) -> UInt](int/words-swift.struct/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [Int.Words.Element](int/words-swift.struct/element.md)
  A type representing the sequence’s elements.
- [Int.Words.Index](int/words-swift.struct/index.md)
  A type that represents a position in the collection.
- [Int.Words.Indices](int/words-swift.struct/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Int.Words.Iterator](int/words-swift.struct/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [Int.Words.SubSequence](int/words-swift.struct/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](int/words-swift.struct/bidirectionalcollection-implementations.md)
- [Collection Implementations](int/words-swift.struct/collection-implementations.md)
- [RandomAccessCollection Implementations](int/words-swift.struct/randomaccesscollection-implementations.md)
- [Sequence Implementations](int/words-swift.struct/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [Sequence](sequence.md)

## See Also

- [static var bitWidth: Int](int/bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
- [var bitWidth: Int](int/bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var nonzeroBitCount: Int](int/nonzerobitcount.md)
  The number of bits equal to 1 in this value’s binary representation.
- [var leadingZeroBitCount: Int](int/leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var trailingZeroBitCount: Int](int/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: Int.Words](int/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/words-swift.struct)*