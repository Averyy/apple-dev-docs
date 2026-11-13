# init(csvData:columns:rows:options:)

**Framework**: TabularData  
**Kind**: init  
**Role**: Initializer

Creates a data frame from CSV data.

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
init<each T>(csvData data: Data, columns: repeat ColumnID<each T>, rows: Range<Int>? = nil, options: CSVReadingOptions = .init()) throws
```

## Parameters

- `data`: The contents of a CSV file.
- `columns`: The column identifiers.
- `rows`: A range of indices; Set to `nil` to use every row in the CSV file.
- `options`: The options that tell the data frame how to read the CSV data.

## See Also

### Creating a data frame from a CSV
- [init(contentsOfCSVFile: URL, columns: [String]?, rows: Range<Int>?, types: [String : CSVType], options: CSVReadingOptions) throws](./init%28contentsofcsvfile,columns,rows,types,options%29.md)
  Creates a data frame from a CSV file.
- [init(csvData: Data, columns: [String]?, rows: Range<Int>?, types: [String : CSVType], options: CSVReadingOptions) throws](./init%28csvdata,columns,rows,types,options%29.md)
  Creates a data frame from CSV data.
- [init<each T>(contentsOfCSVFile: URL, columns: repeat ColumnID<each T>, rows: Range<Int>?, options: CSVReadingOptions) throws](./init%28contentsofcsvfile,columns,rows,options%29.md)
  Creates a data frame from a CSV file.
- [enum CSVType](../csvtype.md)
  Represents the value types in a CSV file.
- [struct CSVReadingOptions](../csvreadingoptions.md)
  A set of CSV file-reading options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/init(csvdata:columns:rows:options:))*