# CSVType

**Framework**: TabularData  
**Kind**: enum  
**Role**: Enumeration

Represents the value types in a CSV file.

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
enum CSVType
```

## Topics

### Enumeration Cases
- [CSVType.boolean](./csvtype/boolean.md)
  A Boolean type.
- [CSVType.data](./csvtype/data.md)
  A binary data type.
- [CSVType.date](./csvtype/date.md)
  A date type.
- [CSVType.double](./csvtype/double.md)
  A double-precision floating-point type.
- [CSVType.float](./csvtype/float.md)
  A single-precision floating-point type.
- [CSVType.integer](./csvtype/integer.md)
  An integer type.
- [CSVType.string](./csvtype/string.md)
  A string type.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Data Frame from a CSV
- [init(contentsOfCSVFile: URL, columns: [String]?, rows: Range<Int>?, types: [String : CSVType], options: CSVReadingOptions) throws](./dataframe/init%28contentsofcsvfile,columns,rows,types,options%29.md)
  Creates a data frame from a CSV file.
- [init(csvData: Data, columns: [String]?, rows: Range<Int>?, types: [String : CSVType], options: CSVReadingOptions) throws](./dataframe/init%28csvdata,columns,rows,types,options%29.md)
  Creates a data frame from CSV data.
- [struct CSVReadingOptions](./csvreadingoptions.md)
  A set of CSV file-reading options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvtype)*