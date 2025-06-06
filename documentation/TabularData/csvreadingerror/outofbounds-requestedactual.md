# CSVReadingError.outOfBounds(requested:actual:)

**Framework**: TabularData  
**Kind**: case

An error that indicates that the read operation requested rows beyond the end of the CSV file.

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
case outOfBounds(requested: Int, actual: Int)
```

## Parameters

- `requested`: The requested start row index.
- `actual`: The actual number of rows in the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvreadingerror/outofbounds(requested:actual:))*