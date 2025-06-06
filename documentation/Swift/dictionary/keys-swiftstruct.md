# Dictionary.Keys

**Framework**: Swift  
**Kind**: struct

A view of a dictionary’s keys.

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
struct Keys
```

## Topics

### Operators
- [static func == (Dictionary<Key, Value>.Keys, Dictionary<Key, Value>.Keys) -> Bool](dictionary/keys-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var count: Int](dictionary/keys-swift.struct/count.md)
  The number of keys in the dictionary.
- [var endIndex: Dictionary<Key, Value>.Index](dictionary/keys-swift.struct/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var isEmpty: Bool](dictionary/keys-swift.struct/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: Dictionary<Key, Value>.Index](dictionary/keys-swift.struct/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func formIndex(after: inout Dictionary<Key, Value>.Index)](dictionary/keys-swift.struct/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(after: Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Index](dictionary/keys-swift.struct/index(after:).md)
  Returns the position immediately after the given index.
### Subscripts
- [subscript(Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Keys.Element](dictionary/keys-swift.struct/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [Dictionary.Keys.Element](dictionary/keys-swift.struct/element.md)
  A type representing the sequence’s elements.
- [Dictionary.Keys.Index](dictionary/keys-swift.struct/index.md)
  A type that represents a position in the collection.
- [Dictionary.Keys.Indices](dictionary/keys-swift.struct/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Dictionary.Keys.SubSequence](dictionary/keys-swift.struct/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [Collection Implementations](dictionary/keys-swift.struct/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](dictionary/keys-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](dictionary/keys-swift.struct/customstringconvertible-implementations.md)
- [Equatable Implementations](dictionary/keys-swift.struct/equatable-implementations.md)
- [Sequence Implementations](dictionary/keys-swift.struct/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](collection.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Equatable](equatable.md)
- [Sendable](sendable.md)
- [Sequence](sequence.md)

## See Also

- [Dictionary.Values](dictionary/values-swift.struct.md)
  A view of a dictionary’s values.
- [Dictionary.Index](dictionary/index.md)
  The position of a key-value pair in a dictionary.
- [Dictionary.Indices](dictionary/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Dictionary.Iterator](dictionary/iterator.md)
  An iterator over the members of a `Dictionary<Key, Value>`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/keys-swift.struct)*