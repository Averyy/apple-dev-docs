# CSVReadingError

**Framework**: TabularData  
**Kind**: enum  
**Role**: Enumeration

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
- [var column: Int?](./csvreadingerror/column.md)
  The index of the column that contains the error.
- [var row: Int](./csvreadingerror/row.md)
  The index of the row that contains the error.
- [case badEncoding(row: Int, column: Int, cellContents: Data)](./csvreadingerror/badencoding%28row,column,cellcontents%29.md)
  An error that indicates CSV data contains an invalid UTF-8 byte sequence.
- [case failedToParse(row: Int, column: Int, type: CSVType, cellContents: Data)](./csvreadingerror/failedtoparse%28row,column,type,cellcontents%29.md)
  An error that indicates the CSV reader can’t parse data in the file.
- [CSVReadingError.misplacedQuote(row:column:)](./csvreadingerror/misplacedquote%28row,column%29.md)
  An error that indicates the CSV data contains a misplaced quote.
- [CSVReadingError.missingColumn(columnName:)](./csvreadingerror/missingcolumn%28columnname%29.md)
  An error that indicates the CSV is missing a required column.
- [CSVReadingError.unsupportedEncoding(_:)](./csvreadingerror/unsupportedencoding%28_%29.md)
  An error that indicates the CSV reader doesn’t support an encoding.
- [case wrongNumberOfColumns(row: Int, columns: Int, expected: Int)](./csvreadingerror/wrongnumberofcolumns%28row,columns,expected%29.md)
  An error that indicates the CSV data contains a row with a mismatched number of columns.
### Enumeration Cases
- [CSVReadingError.outOfBounds(requested:actual:)](./csvreadingerror/outofbounds%28requested,actual%29.md)
  An error that indicates that the read operation requested rows beyond the end of the CSV file.
- [case unsupportedColumnType(columnIndex: Int, columnName: String, type: String)](./csvreadingerror/unsupportedcolumntype%28columnindex,columnname,type%29.md)
  An error that indicates that a column type is not one of the types supported by CSV.
### Default Implementations
- [CustomStringConvertible Implementations](./csvreadingerror/customstringconvertible-implementations.md)
- [LocalizedError Implementations](./csvreadingerror/localizederror-implementations.md)

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
- [enum JSONReadingError](./jsonreadingerror.md)
  A JSON reading error.
- [enum CSVWritingError](./csvwritingerror.md)
  A CSV writing error.
- [struct ColumnDecodingError](./columndecodingerror.md)
  A column decoding error.
- [struct ColumnEncodingError](./columnencodingerror.md)
  A column encoding error.
- [enum SFrameReadingError](./sframereadingerror.md)
  An error when reading a Turi Create scalable data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvreadingerror)*