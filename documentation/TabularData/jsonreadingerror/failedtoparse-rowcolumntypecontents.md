# JSONReadingError.failedToParse(row:column:type:contents:)

**Framework**: TabularData  
**Kind**: case

An error that occurs when a JSON value fails to parse as the specified type.

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
case failedToParse(row: Int, column: String, type: JSONType, contents: String)
```

## Parameters

- `row`: The index of the row that contains the incorrect value.
- `column`: The name of the column that contains the incorrect value.
- `expectedType`: The expected type.
- `value`: The JSON value.

## See Also

- [JSONReadingError.incompatibleValues(column:)](jsonreadingerror/incompatiblevalues(column:).md)
  An error that occurs when the JSON data contains incompatible values in a column.
- [JSONReadingError.unsupportedStructure](jsonreadingerror/unsupportedstructure.md)
  An error that occurs when the JSON structure is incompatible with a data frame.
- [case wrongType(row: Int, column: String, expectedType: JSONType, value: any Sendable)](jsonreadingerror/wrongtype(row:column:expectedtype:value:).md)
  An error that occurs when the JSON data contains a value of the wrong type for a type-constrained column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/jsonreadingerror/failedtoparse(row:column:type:contents:))*