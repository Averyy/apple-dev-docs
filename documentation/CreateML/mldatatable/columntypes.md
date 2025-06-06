# columnTypes

**Framework**: Create ML  
**Kind**: property

The type of the data in each column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var columnTypes: [String : MLDataValue.ValueType] { get }
```

#### Discussion

The keys in the dictionary provided by this column correspond to the names of the columns in the data table.

## See Also

- [var columnNames: MLDataTable.ColumnNames](mldatatable/columnnames-swift.property.md)
  The names of the columns in the data table.
- [MLDataTable.ColumnNames](mldatatable/columnnames-swift.struct.md)
  A collection of the names of the columns in a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/columntypes)*