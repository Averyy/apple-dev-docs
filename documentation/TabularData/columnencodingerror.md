# ColumnEncodingError

**Framework**: TabularData  
**Kind**: struct

A column encoding error.

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
struct ColumnEncodingError
```

#### Overview

An error bundles an [`EncodingError`](https://developer.apple.com/documentation/Swift/EncodingError) with the row and column that produces the error.

## Topics

### Creating an Encoding Error
- [init(columnName: String, rowIndex: Int, encodingError: EncodingError)](columnencodingerror/init(columnname:rowindex:encodingerror:).md)
  Creates a column encoding error.
### Getting Error Information
- [var columnName: String](columnencodingerror/columnname.md)
  The name of the column with the error.
- [var debugDescription: String](columnencodingerror/debugdescription.md)
  A text representation of the column encoding error suitable for debugging.
- [var encodingError: EncodingError](columnencodingerror/encodingerror.md)
  The underlying encoding error.
- [var rowIndex: Int](columnencodingerror/rowindex.md)
  The index of the column’s element with the error.
### Default Implementations
- [Error Implementations](columnencodingerror/error-implementations.md)
- [LocalizedError Implementations](columnencodingerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum JSONReadingError](jsonreadingerror.md)
  A JSON reading error.
- [enum CSVReadingError](csvreadingerror.md)
  A CSV reading error.
- [enum CSVWritingError](csvwritingerror.md)
  A CSV writing error.
- [struct ColumnDecodingError](columndecodingerror.md)
  A column decoding error.
- [enum SFrameReadingError](sframereadingerror.md)
  An error when reading a Turi Create scalable data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnencodingerror)*