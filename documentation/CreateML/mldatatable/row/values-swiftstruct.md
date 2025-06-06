# MLDataTable.Row.Values

**Framework**: Create ML  
**Kind**: struct

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Values
```

## Topics

### Manipulating indices
- [var startIndex: Int](mldatatable/row/values-swift.struct/startindex.md)
  The position of the first element in a nonempty collection.
- [var endIndex: Int](mldatatable/row/values-swift.struct/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
### Accessing columns
- [subscript(Int) -> MLDataValue](mldatatable/row/values-swift.struct/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [MLDataTable.Row.Values.Element](mldatatable/row/values-swift.struct/element.md)
  A type representing the sequence’s elements.
- [MLDataTable.Row.Values.Index](mldatatable/row/values-swift.struct/index.md)
  A type that represents a position in the collection.
- [MLDataTable.Row.Values.Indices](mldatatable/row/values-swift.struct/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [MLDataTable.Row.Values.Iterator](mldatatable/row/values-swift.struct/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [MLDataTable.Row.Values.SubSequence](mldatatable/row/values-swift.struct/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](mldatatable/row/values-swift.struct/bidirectionalcollection-implementations.md)
- [Collection Implementations](mldatatable/row/values-swift.struct/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](mldatatable/row/values-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mldatatable/row/values-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mldatatable/row/values-swift.struct/customstringconvertible-implementations.md)
- [Equatable Implementations](mldatatable/row/values-swift.struct/equatable-implementations.md)
- [RandomAccessCollection Implementations](mldatatable/row/values-swift.struct/randomaccesscollection-implementations.md)
- [Sequence Implementations](mldatatable/row/values-swift.struct/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [var keys: MLDataTable.Row.Keys](mldatatable/row/keys-swift.property.md)
- [var values: MLDataTable.Row.Values](mldatatable/row/values-swift.property.md)
- [MLDataTable.Row.Key](mldatatable/row/key.md)
- [MLDataTable.Row.Keys](mldatatable/row/keys-swift.typealias.md)
- [MLDataTable.Row.Value](mldatatable/row/value.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/row/values-swift.struct)*