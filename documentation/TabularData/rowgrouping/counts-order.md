# counts(order:)

**Framework**: TabularData  
**Kind**: method

Generates a data frame with two columns, one that has a row for each group key and another for the number of rows in the group.

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
func counts(order: Order? = nil) -> DataFrame
```

#### Discussion

The name of the data frame’s column that stores the number of rows in each group is .

## Parameters

- `order`: A sorting order the method uses to sort the data frame by its count column.

## See Also

- [func aggregated<Element, Result>(on: [String], naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame](rowgrouping/aggregated(on:naming:transform:).md)
  Generates a data frame by aggregating each group’s contents for each column you list by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/counts(order:))*