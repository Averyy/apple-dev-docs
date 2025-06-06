# JSONReadingOptions

**Framework**: TabularData  
**Kind**: struct

A set of JSON file-reading options.

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
struct JSONReadingOptions
```

## Topics

### Initializers
- [init()](jsonreadingoptions/init.md)
  Creates a set of options for reading a JSON file.
### Instance Properties
- [var dateParsers: [(String) -> Date?]](jsonreadingoptions/dateparsers.md)
  An array of closures that parse a date from a string.
### Instance Methods
- [func addDateParseStrategy<T>(T)](jsonreadingoptions/adddateparsestrategy(_:).md)
  Adds a date parsing strategy.

## See Also

- [init(contentsOfJSONFile: URL, columns: [String]?, types: [String : JSONType], options: JSONReadingOptions) throws](dataframe/init(contentsofjsonfile:columns:types:options:).md)
  Creates a data frame by reading a JSON file.
- [init(jsonData: Data, columns: [String]?, types: [String : JSONType], options: JSONReadingOptions) throws](dataframe/init(jsondata:columns:types:options:).md)
  Creates a data frame by converting JSON data.
- [enum JSONType](jsontype.md)
  Represents the value types in a JSON file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/jsonreadingoptions)*