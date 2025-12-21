# MLDataTable.Rows

**Framework**: Create ML  
**Kind**: struct

A collection of rows in a data table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Rows
```

## Topics

### Accessing rows
- [subscript(Int) -> MLDataTable.Rows.Element](mldatatable/rows-swift.struct/subscript(_:).md)
  Subscript by index. This returns a row in the data table.
### Manipulating indices
- [var startIndex: Int](mldatatable/rows-swift.struct/startindex.md)
  The position of the first row in a nonempty DataTable. If the DataTable is empty, `startIndex` is equal to `endIndex`.
- [var endIndex: Int](mldatatable/rows-swift.struct/endindex.md)
  The DataTable’s “past the end” position—that is, the position one greater than the last valid subscript argument.
### Supporting types
- [MLDataTable.Row](mldatatable/row.md)
  A row of untyped values in a data table.
- [MLDataTable.Rows.Element](mldatatable/rows-swift.struct/element.md)
  The Element of a DataTable is a Row. This is represented as a Dictionary-like type containing all Column names and their corresponding values.
### Default Implementations
- [RandomAccessCollection Implementations](mldatatable/rows-swift.struct/randomaccesscollection-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [MLDataTable.Row](mldatatable/row.md)
  A row of untyped values in a data table.
- [var rows: MLDataTable.Rows](mldatatable/rows-swift.property.md)
  The rows of data in the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct)*