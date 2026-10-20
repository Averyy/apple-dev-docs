# JSONReadingError

**Framework**: TabularData  
**Kind**: enum  
**Role**: Enumeration

A JSON reading error.

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
enum JSONReadingError
```

## Topics

### Getting Error Information
- [case failedToParse(row: Int, column: String, type: JSONType, contents: String)](./jsonreadingerror/failedtoparse%28row,column,type,contents%29.md)
  An error that occurs when a JSON value fails to parse as the specified type.
- [JSONReadingError.incompatibleValues(column:)](./jsonreadingerror/incompatiblevalues%28column%29.md)
  An error that occurs when the JSON data contains incompatible values in a column.
- [JSONReadingError.unsupportedStructure](./jsonreadingerror/unsupportedstructure.md)
  An error that occurs when the JSON structure is incompatible with a data frame.
- [case wrongType(row: Int, column: String, expectedType: JSONType, value: any Sendable)](./jsonreadingerror/wrongtype%28row,column,expectedtype,value%29.md)
  An error that occurs when the JSON data contains a value of the wrong type for a type-constrained column.
### Default Implementations
- [CustomStringConvertible Implementations](./jsonreadingerror/customstringconvertible-implementations.md)
- [LocalizedError Implementations](./jsonreadingerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Error](../Swift/error.md)
- [Escapable](../Swift/escapable.md)
- [LocalizedError](../Foundation/localizederror.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [enum CSVReadingError](./csvreadingerror.md)
  A CSV reading error.
- [enum CSVWritingError](./csvwritingerror.md)
  A CSV writing error.
- [struct ColumnDecodingError](./columndecodingerror.md)
  A column decoding error.
- [struct ColumnEncodingError](./columnencodingerror.md)
  A column encoding error.
- [enum SFrameReadingError](./sframereadingerror.md)
  An error when reading a Turi Create scalable data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/jsonreadingerror)*