# CSVWritingOptions

**Framework**: TabularData  
**Kind**: struct

A set of CSV file-writing options.

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
struct CSVWritingOptions
```

## Topics

### Initializers
- [init()](csvwritingoptions/init.md)
  Creates the default set of options for writing a CSV file.
- [init(includesHeader: Bool, dateFormat: String?, nilEncoding: String, trueEncoding: String, falseEncoding: String, newline: String, delimiter: Character)](csvwritingoptions/init(includesheader:dateformat:nilencoding:trueencoding:falseencoding:newline:delimiter:).md)
  Creates a set of options for writing a CSV file.
- [init(includesHeader: Bool, nilEncoding: String, trueEncoding: String, falseEncoding: String, newline: String, delimiter: Character)](csvwritingoptions/init(includesheader:nilencoding:trueencoding:falseencoding:newline:delimiter:).md)
  Creates a set of options for writing a CSV file.
### Instance Properties
- [var dateFormat: String?](csvwritingoptions/dateformat.md)
  The format the CSV file generator uses to create date strings.
- [var dateFormatter: (Date) -> String](csvwritingoptions/dateformatter.md)
  A closure that maps dates to their string representations.
- [var delimiter: Character](csvwritingoptions/delimiter.md)
  The character the CSV file generator uses to separate data fields in a CSV file.
- [var falseEncoding: String](csvwritingoptions/falseencoding.md)
  The string the CSV file generator uses to represent false Boolean values.
- [var includesHeader: Bool](csvwritingoptions/includesheader.md)
  A Boolean value that indicates whether to write a header with the column names.
- [var newline: String](csvwritingoptions/newline.md)
  The string the CSV file generator uses to represent a newline sequence.
- [var nilEncoding: String](csvwritingoptions/nilencoding.md)
  The string the CSV file generator uses to represent nil values.
- [var trueEncoding: String](csvwritingoptions/trueencoding.md)
  The string the CSV file generator uses to represent true Boolean values.

## See Also

- [func writeCSV(to: URL, options: CSVWritingOptions) throws](dataframe/writecsv(to:options:).md)
  Creates a CSV file with the contents of the data frame type.
- [func csvRepresentation(options: CSVWritingOptions) throws -> Data](dataframe/csvrepresentation(options:).md)
  Generates a CSV data instance of the data frame type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvwritingoptions)*