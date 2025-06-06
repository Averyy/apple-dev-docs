# Dictionary.Values

**Framework**: Swift  
**Kind**: struct

A view of a dictionary’s values.

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
struct Values
```

## Topics

### Instance Properties
- [var count: Int](dictionary/values-swift.struct/count.md)
  The number of values in the dictionary.
- [var endIndex: Dictionary<Key, Value>.Index](dictionary/values-swift.struct/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var isEmpty: Bool](dictionary/values-swift.struct/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: Dictionary<Key, Value>.Index](dictionary/values-swift.struct/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func formIndex(after: inout Dictionary<Key, Value>.Index)](dictionary/values-swift.struct/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(after: Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Index](dictionary/values-swift.struct/index(after:).md)
  Returns the position immediately after the given index.
- [func swapAt(Dictionary<Key, Value>.Index, Dictionary<Key, Value>.Index)](dictionary/values-swift.struct/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
### Subscripts
- [subscript(Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Values.Element](dictionary/values-swift.struct/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [Dictionary.Values.Element](dictionary/values-swift.struct/element.md)
  A type representing the sequence’s elements.
- [Dictionary.Values.Index](dictionary/values-swift.struct/index.md)
  A type that represents a position in the collection.
- [Dictionary.Values.Indices](dictionary/values-swift.struct/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Dictionary.Values.SubSequence](dictionary/values-swift.struct/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [Collection Implementations](dictionary/values-swift.struct/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](dictionary/values-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](dictionary/values-swift.struct/customstringconvertible-implementations.md)
- [MutableCollection Implementations](dictionary/values-swift.struct/mutablecollection-implementations.md)
- [Sequence Implementations](dictionary/values-swift.struct/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](collection.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomStringConvertible](customstringconvertible.md)
- [MutableCollection](mutablecollection.md)
- [Sendable](sendable.md)
- [Sequence](sequence.md)

## See Also

- [Dictionary.Keys](dictionary/keys-swift.struct.md)
  A view of a dictionary’s keys.
- [Dictionary.Index](dictionary/index.md)
  The position of a key-value pair in a dictionary.
- [Dictionary.Indices](dictionary/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Dictionary.Iterator](dictionary/iterator.md)
  An iterator over the members of a `Dictionary<Key, Value>`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/values-swift.struct)*