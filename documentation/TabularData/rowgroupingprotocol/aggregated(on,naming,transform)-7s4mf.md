# aggregated(on:naming:transform:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a data frame by aggregating each group’s contents for each column you select by name.

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
func aggregated<Element, Result>(on columnNames: String..., naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame
```

#### Discussion

The data frame contains two columns that:

- Identify each group
- Store the results of your aggregation transform closure

## Parameters

- `columnNames`: A comma-separated, or variadic, list of column names.
- `naming`: A closure that converts a column name to another name.
- `transform`: A closure that aggregates a group’s elements in a specific column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgroupingprotocol/aggregated(on:naming:transform:)-7s4mf)*