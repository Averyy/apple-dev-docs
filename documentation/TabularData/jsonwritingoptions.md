# JSONWritingOptions

**Framework**: TabularData  
**Kind**: struct  
**Role**: Structure

A set of JSON file-reading options.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct JSONWritingOptions
```

## Topics

### Creating the options object
- [init()](./jsonwritingoptions/init%28%29.md)
  Creates a set of options for writing a JSON file.
### Formatting the JSON output
- [var prettyPrint: Bool](./jsonwritingoptions/prettyprint.md)
  A Boolean value that indicates whether to split lines and indent the generated JSON.
- [var sortKeys: Bool](./jsonwritingoptions/sortkeys.md)
  A Boolean value that indicates whether to sort the keys.
- [var dateFormatter: (Date) -> String](./jsonwritingoptions/dateformatter.md)
  A closure that maps dates to their string representations.

## See Also

### Saving a data frame to a JSON format
- [func writeJSON(to: URL, options: JSONWritingOptions) throws](./dataframeprotocol/writejson%28to,options%29.md)
  Creates a JSON file with the contents of the data frame.
- [func jsonRepresentation(options: JSONWritingOptions) throws -> Data](./dataframeprotocol/jsonrepresentation%28options%29.md)
  Generates a JSON data instance of the data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/jsonwritingoptions)*