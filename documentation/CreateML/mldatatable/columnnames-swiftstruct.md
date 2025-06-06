# MLDataTable.ColumnNames

**Framework**: Create ML  
**Kind**: struct

A collection of the names of the columns in a data table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct ColumnNames
```

## Topics

### Manipulating indices
- [var startIndex: Int](mldatatable/columnnames-swift.struct/startindex.md)
  The position of the first element in a nonempty collection.
- [var endIndex: Int](mldatatable/columnnames-swift.struct/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
### Accessing columns
- [subscript(Int) -> String](mldatatable/columnnames-swift.struct/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [MLDataTable.ColumnNames.Element](mldatatable/columnnames-swift.struct/element.md)
  A type representing the sequence’s elements.
- [MLDataTable.ColumnNames.Index](mldatatable/columnnames-swift.struct/index.md)
  A type that represents a position in the collection.
- [MLDataTable.ColumnNames.Indices](mldatatable/columnnames-swift.struct/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [MLDataTable.ColumnNames.Iterator](mldatatable/columnnames-swift.struct/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [MLDataTable.ColumnNames.SubSequence](mldatatable/columnnames-swift.struct/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](mldatatable/columnnames-swift.struct/bidirectionalcollection-implementations.md)
- [Collection Implementations](mldatatable/columnnames-swift.struct/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](mldatatable/columnnames-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mldatatable/columnnames-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mldatatable/columnnames-swift.struct/customstringconvertible-implementations.md)
- [Equatable Implementations](mldatatable/columnnames-swift.struct/equatable-implementations.md)
- [RandomAccessCollection Implementations](mldatatable/columnnames-swift.struct/randomaccesscollection-implementations.md)
- [Sequence Implementations](mldatatable/columnnames-swift.struct/sequence-implementations.md)

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

- [var columnNames: MLDataTable.ColumnNames](mldatatable/columnnames-swift.property.md)
  The names of the columns in the data table.
- [var columnTypes: [String : MLDataValue.ValueType]](mldatatable/columntypes.md)
  The type of the data in each column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/columnnames-swift.struct)*