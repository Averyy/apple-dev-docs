# MLDataTable.ColumnNames

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

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

### Accessing columns
- [subscript(_:)](./subscript%28_%29.md)
  Retrieves or adds an untyped column with the specified name.

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [RandomAccessCollection](../../Swift/randomaccesscollection.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Getting information about a data table’s columns
- [var columnNames: MLDataTable.ColumnNames](./columnnames-swift.property.md)
  The names of the columns in the data table.
- [var columnTypes: [String : MLDataValue.ValueType]](./columntypes.md)
  The type of the data in each column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/columnnames-swift.struct)*