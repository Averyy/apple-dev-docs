# grouped(by:)

**Framework**: TabularData  
**Kind**: method

Creates a grouping from multiple columns that you select by column identifier.

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
func grouped<T>(by columnIDs: ColumnID<T>...) -> some RowGroupingProtocol where T : Hashable
```

## Parameters

- `columnIDs`: A comma-separated, or variadic, list of column identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/grouped(by:)-qniy)*