# ColumnDecodingError

**Framework**: TabularData  
**Kind**: struct

A column decoding error.

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
struct ColumnDecodingError
```

#### Overview

This error wraps a decoding error and includes the column name and row index where the decoding error occurs.

## Topics

### Creating a Decoding Error
- [init(columnName: String, rowIndex: Int, decodingError: DecodingError)](columndecodingerror/init(columnname:rowindex:decodingerror:).md)
  Creates a column decoding error.
### Getting Error Information
- [var columnName: String](columndecodingerror/columnname.md)
  The name of the column with the error.
- [var debugDescription: String](columndecodingerror/debugdescription.md)
  A text representation of the column decoding error suitable for debugging.
- [var decodingError: DecodingError](columndecodingerror/decodingerror.md)
  The underlying decoding error.
- [var rowIndex: Int](columndecodingerror/rowindex.md)
  The index of the column’s element with the error.
### Default Implementations
- [Error Implementations](columndecodingerror/error-implementations.md)
- [LocalizedError Implementations](columndecodingerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum JSONReadingError](jsonreadingerror.md)
  A JSON reading error.
- [enum CSVReadingError](csvreadingerror.md)
  A CSV reading error.
- [enum CSVWritingError](csvwritingerror.md)
  A CSV writing error.
- [struct ColumnEncodingError](columnencodingerror.md)
  A column encoding error.
- [enum SFrameReadingError](sframereadingerror.md)
  An error when reading a Turi Create scalable data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columndecodingerror)*