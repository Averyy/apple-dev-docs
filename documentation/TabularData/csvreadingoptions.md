# CSVReadingOptions

**Framework**: TabularData  
**Kind**: struct

A set of CSV file-reading options.

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
struct CSVReadingOptions
```

## Topics

### Initializers
- [init(hasHeaderRow: Bool, nilEncodings: Set<String>, trueEncodings: Set<String>, falseEncodings: Set<String>, floatingPointType: CSVType, ignoresEmptyLines: Bool, usesQuoting: Bool, usesEscaping: Bool, delimiter: Character, escapeCharacter: Character)](csvreadingoptions/init(hasheaderrow:nilencodings:trueencodings:falseencodings:floatingpointtype:ignoresemptylines:usesquoting:usesescaping:delimiter:escapecharacter:).md)
  Creates a set of options for reading a CSV file.
### Instance Properties
- [var dateParsers: [(String) -> Date?]](csvreadingoptions/dateparsers.md)
  An array of closures that parse a date from a string.
- [var delimiter: Character](csvreadingoptions/delimiter.md)
  The character that separates data fields in a CSV file, typically a comma.
- [var escapeCharacter: Character](csvreadingoptions/escapecharacter.md)
  The character that precedes other characters, such as quotation marks, so that the parser interprets them as literal characters instead of special ones.
- [var falseEncodings: Set<String>](csvreadingoptions/falseencodings.md)
  The set of strings that stores acceptable spellings for false Boolean values.
- [var floatingPointType: CSVType](csvreadingoptions/floatingpointtype.md)
  The type to use for floating-point numeric values.
- [var hasHeaderRow: Bool](csvreadingoptions/hasheaderrow.md)
  A Boolean value that indicates whether the CSV file has a header row.
- [var ignoresEmptyLines: Bool](csvreadingoptions/ignoresemptylines.md)
  A Boolean value that indicates whether to ignore empty lines.
- [var nilEncodings: Set<String>](csvreadingoptions/nilencodings.md)
  The set of strings that stores acceptable spellings for empty values.
- [var trueEncodings: Set<String>](csvreadingoptions/trueencodings.md)
  The set of strings that stores acceptable spellings for true Boolean values.
- [var usesEscaping: Bool](csvreadingoptions/usesescaping.md)
  A Boolean value that indicates whether to enable escaping.
- [var usesQuoting: Bool](csvreadingoptions/usesquoting.md)
  A Boolean value that indicates whether to enable quoting.
### Instance Methods
- [func addDateParseStrategy<T>(T)](csvreadingoptions/adddateparsestrategy(_:).md)
  Adds a date parsing strategy.

## See Also

- [init(contentsOfCSVFile: URL, columns: [String]?, rows: Range<Int>?, types: [String : CSVType], options: CSVReadingOptions) throws](dataframe/init(contentsofcsvfile:columns:rows:types:options:).md)
  Creates a data frame from a CSV file.
- [init(csvData: Data, columns: [String]?, rows: Range<Int>?, types: [String : CSVType], options: CSVReadingOptions) throws](dataframe/init(csvdata:columns:rows:types:options:).md)
  Creates a data frame from CSV data.
- [enum CSVType](csvtype.md)
  Represents the value types in a CSV file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvreadingoptions)*