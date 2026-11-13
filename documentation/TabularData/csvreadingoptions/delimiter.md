# delimiter

**Framework**: TabularData  
**Kind**: property  
**Role**: Instance Property

The character that separates data fields in a CSV file, typically a comma.

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
var delimiter: Character { get }
```

## Discussion

Defaults to comma (`,`).

## See Also

### Describing the file structure
- [var hasHeaderRow: Bool](./hasheaderrow.md)
  A Boolean value that indicates whether the CSV file has a header row.
- [var ignoresEmptyLines: Bool](./ignoresemptylines.md)
  A Boolean value that indicates whether to ignore empty lines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvreadingoptions/delimiter)*