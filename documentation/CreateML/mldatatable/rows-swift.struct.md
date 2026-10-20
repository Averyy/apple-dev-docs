# MLDataTable.Rows

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

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
- [subscript(Int) -> MLDataTable.Rows.Element](./rows-swift.struct/subscript%28_%29.md)
  Subscript by index. This returns a row in the data table.
### Manipulating indices
- [var startIndex: Int](./rows-swift.struct/startindex.md)
  The position of the first row in a nonempty DataTable. If the DataTable is empty, `startIndex` is equal to `endIndex`.
- [var endIndex: Int](./rows-swift.struct/endindex.md)
  The DataTable’s “past the end” position—that is, the position one greater than the last valid subscript argument.
### Supporting types
- [MLDataTable.Row](./row.md)
  A row of untyped values in a data table.
- [MLDataTable.Rows.Element](./rows-swift.struct/element.md)
  The Element of a DataTable is a Row. This is represented as a Dictionary-like type containing all Column names and their corresponding values.
### Default Implementations
- [RandomAccessCollection Implementations](./rows-swift.struct/randomaccesscollection-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [RandomAccessCollection](../../Swift/randomaccesscollection.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Getting information about a data table’s rows
- [MLDataTable.Row](./row.md)
  A row of untyped values in a data table.
- [var rows: MLDataTable.Rows](./rows-swift.property.md)
  The rows of data in the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct)*