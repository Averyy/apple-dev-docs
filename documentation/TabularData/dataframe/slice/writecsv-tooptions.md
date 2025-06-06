# writeCSV(to:options:)

**Framework**: TabularData  
**Kind**: method

Creates a CSV file with the contents of the data frame type.

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
func writeCSV(to url: URL, options: CSVWritingOptions = .init()) throws
```

## Parameters

- `url`: A location URL in the file system where the method saves the CSV file.
- `options`: A   instance.

## See Also

- [func csvRepresentation(options: CSVWritingOptions) throws -> Data](dataframe/slice/csvrepresentation(options:).md)
  Generates a CSV data instance of the data frame type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/writecsv(to:options:))*