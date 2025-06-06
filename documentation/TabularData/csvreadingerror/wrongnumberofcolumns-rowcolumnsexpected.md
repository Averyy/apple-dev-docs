# CSVReadingError.wrongNumberOfColumns(row:columns:expected:)

**Framework**: TabularData  
**Kind**: case

An error that indicates the CSV data contains a row with a mismatched number of columns.

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
case wrongNumberOfColumns(row: Int, columns: Int, expected: Int)
```

## Parameters

- `row`: The index of the row that contains the mismatched number of columns.
- `columns`: The number of columns in the row.
- `expected`: The number of columns in the other rows.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvreadingerror/wrongnumberofcolumns(row:columns:expected:))*