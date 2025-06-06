# init(contentsOfCSVFile:columns:rows:types:options:)

**Framework**: Tabulardata  
**Kind**: init

Creates a data frame from a CSV file.

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
init(contentsOfCSVFile url: URL, columns: [String]? = nil, rows: Range<Int>? = nil, types: [String : CSVType] = [:], options: CSVReadingOptions = .init()) throws
```

#### Discussion

> **Note**: A `CSVReadingError` instance.

## Parameters

- `url`: A URL for a CSV file.
- `columns`: An array of column names; Set to   to use every column in the CSV file.
- `rows`: A range of indices; Set to   to use every row in the CSV file.
- `types`: A dictionary of column names and their CSV types.   The data frame infers the types for column names that aren’t in the dictionary.
- `options`: The options that tell the data frame how to read the CSV file.

## See Also

- [init(csvData: Data, columns: [String]?, rows: Range<Int>?, types: [String : CSVType], options: CSVReadingOptions) throws](dataframe/init(csvdata:columns:rows:types:options:).md)
  Creates a data frame from CSV data.
- [enum CSVType](csvtype.md)
  Represents the value types in a CSV file.
- [struct CSVReadingOptions](csvreadingoptions.md)
  A set of CSV file-reading options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/init(contentsofcsvfile:columns:rows:types:options:))*