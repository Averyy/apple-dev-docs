# CSVReadingError.unsupportedColumnType(columnIndex:columnName:type:)

**Framework**: TabularData  
**Kind**: case

An error that indicates that a column type is not one of the types supported by CSV.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
case unsupportedColumnType(columnIndex: Int, columnName: String, type: String)
```

## Parameters

- `columnIndex`: The index of the column with the invalid type.
- `columnName`: The name of the column with the invalid type.
- `type`: The requested type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvreadingerror/unsupportedcolumntype(columnindex:columnname:type:))*