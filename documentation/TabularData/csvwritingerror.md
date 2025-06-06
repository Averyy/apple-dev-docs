# CSVWritingError

**Framework**: TabularData  
**Kind**: enum

A CSV writing error.

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
enum CSVWritingError
```

## Topics

### Getting Error Information
- [var column: String?](csvwritingerror/column.md)
  The index of the column that contains the error.
- [var row: Int](csvwritingerror/row.md)
  The index of the row that contains the error.
- [case badEncoding(row: Int, column: String, Data)](csvwritingerror/badencoding(row:column:_:).md)
  An error that indicates CSV data contains an invalid UTF-8 byte sequence.
### Default Implementations
- [CustomStringConvertible Implementations](csvwritingerror/customstringconvertible-implementations.md)
- [Error Implementations](csvwritingerror/error-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum JSONReadingError](jsonreadingerror.md)
  A JSON reading error.
- [enum CSVReadingError](csvreadingerror.md)
  A CSV reading error.
- [struct ColumnDecodingError](columndecodingerror.md)
  A column decoding error.
- [struct ColumnEncodingError](columnencodingerror.md)
  A column encoding error.
- [enum SFrameReadingError](sframereadingerror.md)
  An error when reading a Turi Create scalable data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvwritingerror)*