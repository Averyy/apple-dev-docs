# DataFrame.Row

**Framework**: TabularData  
**Kind**: struct  
**Role**: Structure

A single row within a data frame.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Row
```

## Topics

### Inspecting a row
- [var count: Int](./row/count.md)
  The number of columns in the row.
- [let index: Int](./row/index.md)
  The row’s index in the underlying data frame.
- [var base: DataFrame](./row/base.md)
  The row’s underlying data frame.
### Accessing elements
- [subscript(Int) -> Any?](./row/subscript%28_%29-5tsj0.md)
  Accesses a value at a column index.
- [subscript(String) -> Any?](./row/subscript%28_%29-2v7qz.md)
  Accesses a value in the row you select by a column name.
- [subscript<T>(String, T.Type) -> T?](./row/subscript%28_,_%29-7gpc3.md)
  Accesses a value in the row you select by a column name and type.
- [subscript<T>(ColumnID<T>) -> T?](./row/subscript%28_%29-9o424.md)
  Accesses a value in the row you select by a column identifier.
- [subscript<T>(Int, T.Type) -> T?](./row/subscript%28_,_%29-1o38p.md)
  Accesses a value in the row you select by a column index and type.
### Describing a row
- [var description: String](./row/description.md)
  A text representation of the row.
- [var debugDescription: String](./row/debugdescription.md)
  A text representation of the row suitable for debugging.
- [var customMirror: Mirror](./row/custommirror.md)
  A mirror that reflects the row.
- [func description(options: FormattingOptions) -> String](./row/description%28options%29.md)
  A text representation of the row.
### Comparing two rows
- [static func == (DataFrame.Row, DataFrame.Row) -> Bool](./row/eqeq%28_,_%29.md)
  Returns a Boolean that indicates whether the rows are equal.
### Hashing a row
- [func hash(into: inout Hasher)](./row/hash%28into%29.md)
  Hashes the essential components of the row by feeding them into a hasher.
### Retrieving an index
- [var startIndex: Int](./row/startindex.md)
  The index of the initial column in the row.
- [var endIndex: Int](./row/endindex.md)
  The index of the final column in the row.
- [func index(before: Int) -> Int](./row/index%28before%29.md)
  Returns the column index immediately after a column index in the row.
- [func index(after: Int) -> Int](./row/index%28after%29.md)
  Returns the column index immediately before a column index in the row.
### Default Implementations
- [Collection Implementations](./row/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](./row/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](./row/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](./row/customstringconvertible-implementations.md)
- [Equatable Implementations](./row/equatable-implementations.md)
- [Hashable Implementations](./row/hashable-implementations.md)
- [RandomAccessCollection Implementations](./row/randomaccesscollection-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../../Swift/customreflectable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [MutableCollection](../../Swift/mutablecollection.md)
- [RandomAccessCollection](../../Swift/randomaccesscollection.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Supporting types
- [DataFrame.Slice](./slice.md)
  A set of a data frame’s rows you create by using a method from a data frame instance or another data frame slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/row)*