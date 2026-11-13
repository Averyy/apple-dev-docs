# jsonRepresentation(options:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a JSON data instance of the data frame.

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
func jsonRepresentation(options: JSONWritingOptions = .init()) throws -> Data
```

## Parameters

- `options`: A [`JSONWritingOptions`](../jsonwritingoptions.md) instance.

## See Also

### Saving a data frame to a JSON format
- [struct JSONWritingOptions](../jsonwritingoptions.md)
  A set of JSON file-reading options.
- [func writeJSON(to: URL, options: JSONWritingOptions) throws](./writejson%28to,options%29.md)
  Creates a JSON file with the contents of the data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframeprotocol/jsonrepresentation(options:))*