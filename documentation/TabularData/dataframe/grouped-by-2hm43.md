# grouped(by:)

**Framework**: TabularData  
**Kind**: method

Creates a grouping of rows that the method selects by choosing unique values in a column.

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
func grouped<GroupingKey>(by columnID: ColumnID<GroupingKey>) -> RowGrouping<GroupingKey> where GroupingKey : Hashable
```

#### Return Value

A collection of groups.

## Parameters

- `columnID`: A column identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/grouped(by:)-2hm43)*