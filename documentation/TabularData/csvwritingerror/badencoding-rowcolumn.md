# CSVWritingError.badEncoding(row:column:_:)

**Framework**: TabularData  
**Kind**: case

An error that indicates CSV data contains an invalid UTF-8 byte sequence.

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
case badEncoding(row: Int, column: String, Data)
```

## Parameters

- `row`: The index of the row that contains the invalid sequence.
- `column`: The index of the column that contains the invalid sequence.
- `data`: The data that contains the invalid sequence.

## See Also

- [var column: String?](csvwritingerror/column.md)
  The index of the column that contains the error.
- [var row: Int](csvwritingerror/row.md)
  The index of the row that contains the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvwritingerror/badencoding(row:column:_:))*