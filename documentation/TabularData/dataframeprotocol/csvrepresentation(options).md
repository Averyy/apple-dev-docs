# csvRepresentation(options:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a CSV data instance of the data frame type.

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
func csvRepresentation(options: CSVWritingOptions = .init()) throws -> Data
```

## Parameters

- `options`: A [`CSVWritingOptions`](../csvwritingoptions.md) instance.

## See Also

### Saving a Data Frame Type to a CSV Format
- [func writeCSV(to: URL, options: CSVWritingOptions) throws](./writecsv%28to,options%29.md)
  Creates a CSV file with the contents of the data frame type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframeprotocol/csvrepresentation(options:))*