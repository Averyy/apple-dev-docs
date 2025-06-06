# Int8.Words

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
- [init(Int8)](int8/words-swift.struct/init(_:).md)
### Instance Properties
- [var count: Int](int8/words-swift.struct/count.md)
  The number of elements in the collection.
- [var endIndex: Int](int8/words-swift.struct/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: Int8.Words.Indices](int8/words-swift.struct/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: Int](int8/words-swift.struct/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func index(after: Int) -> Int](int8/words-swift.struct/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: Int) -> Int](int8/words-swift.struct/index(before:).md)
  Returns the position immediately before the given index.
### Subscripts
- [subscript(Int) -> UInt](int8/words-swift.struct/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [Int8.Words.Element](int8/words-swift.struct/element.md)
  A type representing the sequence’s elements.
- [Int8.Words.Index](int8/words-swift.struct/index.md)
  A type that represents a position in the collection.
- [Int8.Words.Indices](int8/words-swift.struct/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Int8.Words.Iterator](int8/words-swift.struct/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [Int8.Words.SubSequence](int8/words-swift.struct/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](int8/words-swift.struct/bidirectionalcollection-implementations.md)
- [Collection Implementations](int8/words-swift.struct/collection-implementations.md)
- [RandomAccessCollection Implementations](int8/words-swift.struct/randomaccesscollection-implementations.md)
- [Sequence Implementations](int8/words-swift.struct/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [Sendable](sendable.md)
- [Sequence](sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int8/words-swift.struct)*