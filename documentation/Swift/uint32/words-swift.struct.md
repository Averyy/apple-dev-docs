# UInt32.Words

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

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
- [init(UInt32)](./words-swift.struct/init%28_%29.md)
### Instance Properties
- [var count: Int](./words-swift.struct/count.md)
  The number of elements in the collection.
- [var endIndex: Int](./words-swift.struct/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: UInt32.Words.Indices](./words-swift.struct/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: Int](./words-swift.struct/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func index(after: Int) -> Int](./words-swift.struct/index%28after%29.md)
  Returns the position immediately after the given index.
- [func index(before: Int) -> Int](./words-swift.struct/index%28before%29.md)
  Returns the position immediately before the given index.
### Subscripts
- [subscript(Int) -> UInt](./words-swift.struct/subscript%28_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [UInt32.Words.Element](./words-swift.struct/element.md)
  A type representing the sequence’s elements.
- [UInt32.Words.Index](./words-swift.struct/index.md)
  A type that represents a position in the collection.
- [UInt32.Words.Indices](./words-swift.struct/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [UInt32.Words.Iterator](./words-swift.struct/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [UInt32.Words.SubSequence](./words-swift.struct/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](./words-swift.struct/bidirectionalcollection-implementations.md)
- [Collection Implementations](./words-swift.struct/collection-implementations.md)
- [RandomAccessCollection Implementations](./words-swift.struct/randomaccesscollection-implementations.md)
- [Sequence Implementations](./words-swift.struct/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../bidirectionalcollection.md)
- [BitwiseCopyable](../bitwisecopyable.md)
- [Collection](../collection.md)
- [Copyable](../copyable.md)
- [RandomAccessCollection](../randomaccesscollection.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)
- [Sequence](../sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint32/words-swift.struct)*