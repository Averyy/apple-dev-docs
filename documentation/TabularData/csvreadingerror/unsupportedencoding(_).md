# CSVReadingError.unsupportedEncoding(_:)

**Framework**: TabularData  
**Kind**: case  
**Role**: Case

An error that indicates the CSV reader doesn’t support an encoding.

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
case unsupportedEncoding(String)
```

#### Discussion

The associated value contains a description of the error.

## See Also

### Getting Error Information
- [var column: Int?](./column.md)
  The index of the column that contains the error.
- [var row: Int](./row.md)
  The index of the row that contains the error.
- [case badEncoding(row: Int, column: Int, cellContents: Data)](./badencoding%28row,column,cellcontents%29.md)
  An error that indicates CSV data contains an invalid UTF-8 byte sequence.
- [case failedToParse(row: Int, column: Int, type: CSVType, cellContents: Data)](./failedtoparse%28row,column,type,cellcontents%29.md)
  An error that indicates the CSV reader can’t parse data in the file.
- [CSVReadingError.misplacedQuote(row:column:)](./misplacedquote%28row,column%29.md)
  An error that indicates the CSV data contains a misplaced quote.
- [CSVReadingError.missingColumn(columnName:)](./missingcolumn%28columnname%29.md)
  An error that indicates the CSV is missing a required column.
- [case wrongNumberOfColumns(row: Int, columns: Int, expected: Int)](./wrongnumberofcolumns%28row,columns,expected%29.md)
  An error that indicates the CSV data contains a row with a mismatched number of columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvreadingerror/unsupportedencoding(_:))*