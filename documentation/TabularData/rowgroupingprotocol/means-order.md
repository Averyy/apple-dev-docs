# means(_:order:)

**Framework**: TabularData  
**Kind**: method

Generates a data frame that contains the average mean of each group’s rows along a column you select by column identifier.

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
func means<N>(_ columnID: ColumnID<N>, order: Order? = nil) -> DataFrame where N : FloatingPoint
```

## Parameters

- `columnID`: A column identifier.
- `order`: A sorting order the method uses to sort the data frame by its mean column.

## See Also

- [func counts() -> DataFrame](rowgroupingprotocol/counts.md)
  Generates a data frame with two columns, one that has a row for each group key and another for the number of rows in the group.
- [func counts(order: Order?) -> DataFrame](rowgroupingprotocol/counts(order:).md)
  Generates a data frame, that you choose how to sort, with two columns, one that has a row for each group key and another for the number or rows in the group.
- [func sums<N>(String, N.Type, order: Order?) -> DataFrame](rowgroupingprotocol/sums(_:_:order:).md)
  Generates a data frame that contains the sum of each group’s rows along a column you select by name.
- [func sums<N>(ColumnID<N>, order: Order?) -> DataFrame](rowgroupingprotocol/sums(_:order:).md)
  Generates a data frame that contains the sum of each group’s rows along a column you select by column identifier.
- [func means<N>(String, N.Type, order: Order?) -> DataFrame](rowgroupingprotocol/means(_:_:order:).md)
  Generates a data frame that contains the average mean of each group’s rows along a column you select by name.
- [func minimums<N>(String, N.Type, order: Order?) -> DataFrame](rowgroupingprotocol/minimums(_:_:order:).md)
  Generates a data frame that contains the minimums of each group’s rows along a column you select by name.
- [func minimums<N>(ColumnID<N>, order: Order?) -> DataFrame](rowgroupingprotocol/minimums(_:order:).md)
  Generates a data frame that contains the minimums of each group’s rows along a column you select by column identifier.
- [func maximums<N>(String, N.Type, order: Order?) -> DataFrame](rowgroupingprotocol/maximums(_:_:order:).md)
  Generates a data frame that contains the maximums of each group’s rows along a column you select by name.
- [func maximums<N>(ColumnID<N>, order: Order?) -> DataFrame](rowgroupingprotocol/maximums(_:order:).md)
  Generates a data frame that contains the maximums of each group’s rows along a column you select by column identifier.
- [func aggregated<Element, Result>(on: ColumnID<Element>, into: String?, transform: (DiscontiguousColumnSlice<Element>) throws -> Result) rethrows -> DataFrame](rowgroupingprotocol/aggregated(on:into:transform:).md)
  Generates a data frame with a column for the group identifier and a column of values from the transform.
- [func aggregated<Element, Result>(on: [String], naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame](rowgroupingprotocol/aggregated(on:naming:transform:).md)
  Generates a data frame by aggregating each group’s contents for each column you select by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgroupingprotocol/means(_:order:))*