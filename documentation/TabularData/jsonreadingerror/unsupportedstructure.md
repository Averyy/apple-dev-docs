# JSONReadingError.unsupportedStructure

**Framework**: TabularData  
**Kind**: case

An error that occurs when the JSON structure is incompatible with a data frame.

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
case unsupportedStructure
```

## See Also

- [case failedToParse(row: Int, column: String, type: JSONType, contents: String)](jsonreadingerror/failedtoparse(row:column:type:contents:).md)
  An error that occurs when a JSON value fails to parse as the specified type.
- [JSONReadingError.incompatibleValues(column:)](jsonreadingerror/incompatiblevalues(column:).md)
  An error that occurs when the JSON data contains incompatible values in a column.
- [case wrongType(row: Int, column: String, expectedType: JSONType, value: any Sendable)](jsonreadingerror/wrongtype(row:column:expectedtype:value:).md)
  An error that occurs when the JSON data contains a value of the wrong type for a type-constrained column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/jsonreadingerror/unsupportedstructure)*