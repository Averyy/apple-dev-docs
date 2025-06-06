# init(contentsOfCSVFile:columns:rows:options:)

**Framework**: TabularData  
**Kind**: init

Creates a data frame from a CSV file.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
init<each T>(contentsOfCSVFile url: URL, columns: repeat ColumnID<each T>, rows: Range<Int>? = nil, options: CSVReadingOptions = .init()) throws
```

## Parameters

- `url`: A URL for a CSV file.
- `columns`: The column identifiers.
- `rows`: A range of indices; Set to   to use every row in the CSV file.
- `options`: The options that tell the data frame how to read the CSV file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/init(contentsofcsvfile:columns:rows:options:))*