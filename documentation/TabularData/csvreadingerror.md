# CSVReadingError

**Framework**: TabularData  
**Kind**: enum

A CSV reading error.

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
enum CSVReadingError
```

## Topics

### Getting Error Information
- [var column: Int?](csvreadingerror/column.md)
  The index of the column that contains the error.
- [var row: Int](csvreadingerror/row.md)
  The index of the row that contains the error.
- [case badEncoding(row: Int, column: Int, cellContents: Data)](csvreadingerror/badencoding(row:column:cellcontents:).md)
  An error that indicates CSV data contains an invalid UTF-8 byte sequence.
- [case failedToParse(row: Int, column: Int, type: CSVType, cellContents: Data)](csvreadingerror/failedtoparse(row:column:type:cellcontents:).md)
  An error that indicates the CSV reader can’t parse data in the file.
- [CSVReadingError.misplacedQuote(row:column:)](csvreadingerror/misplacedquote(row:column:).md)
  An error that indicates the CSV data contains a misplaced quote.
- [CSVReadingError.missingColumn(columnName:)](csvreadingerror/missingcolumn(columnname:).md)
  An error that indicates the CSV is missing a required column.
- [CSVReadingError.unsupportedEncoding(_:)](csvreadingerror/unsupportedencoding(_:).md)
  An error that indicates the CSV reader doesn’t support an encoding.
- [case wrongNumberOfColumns(row: Int, columns: Int, expected: Int)](csvreadingerror/wrongnumberofcolumns(row:columns:expected:).md)
  An error that indicates the CSV data contains a row with a mismatched number of columns.
### Enumeration Cases
- [CSVReadingError.outOfBounds(requested:actual:)](csvreadingerror/outofbounds(requested:actual:).md)
  An error that indicates that the read operation requested rows beyond the end of the CSV file.
- [case unsupportedColumnType(columnIndex: Int, columnName: String, type: String)](csvreadingerror/unsupportedcolumntype(columnindex:columnname:type:).md)
  An error that indicates that a column type is not one of the types supported by CSV.
### Default Implementations
- [CustomStringConvertible Implementations](csvreadingerror/customstringconvertible-implementations.md)
- [LocalizedError Implementations](csvreadingerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum JSONReadingError](jsonreadingerror.md)
  A JSON reading error.
- [enum CSVWritingError](csvwritingerror.md)
  A CSV writing error.
- [struct ColumnDecodingError](columndecodingerror.md)
  A column decoding error.
- [struct ColumnEncodingError](columnencodingerror.md)
  A column encoding error.
- [enum SFrameReadingError](sframereadingerror.md)
  An error when reading a Turi Create scalable data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvreadingerror)*