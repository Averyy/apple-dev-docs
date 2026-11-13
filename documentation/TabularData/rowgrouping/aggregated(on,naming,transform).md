# aggregated(on:naming:transform:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a data frame by aggregating each group’s contents for each column you list by name.

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
func aggregated<Element, Result>(on columnNames: [String], naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame
```

## Discussion

The data frame contains two columns that:

- Identify each group
- Store the results of your aggregation transform closure

## Parameters

- `columnNames`: A comma-separated, or variadic, list of column names.
- `naming`: A closure that converts a column name to another name.
- `transform`: A closure that aggregates a group’s elements in a specific column.

## See Also

### Aggregating a row grouping
- [func counts(order: Order?) -> DataFrame](./counts%28order%29.md)
  Generates a data frame with two columns, one that has a row for each group key and another for the number of rows in the group.
- [func aggregated<Element, Result>(on: String..., naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame](../rowgroupingprotocol/aggregated%28on,naming,transform%29-7s4mf.md)
  Generates a data frame by aggregating each group’s contents for each column you select by name.
- [func sums<N>(String, N.Type, order: Order?) -> DataFrame](../rowgroupingprotocol/sums%28_,_,order%29.md)
  Generates a data frame that contains the sum of each group’s rows along a column you select by name.
- [func sums<N>(ColumnID<N>, order: Order?) -> DataFrame](../rowgroupingprotocol/sums%28_,order%29.md)
  Generates a data frame that contains the sum of each group’s rows along a column you select by column identifier.
- [func means<N>(String, N.Type, order: Order?) -> DataFrame](../rowgroupingprotocol/means%28_,_,order%29.md)
  Generates a data frame that contains the average mean of each group’s rows along a column you select by name.
- [func means<N>(ColumnID<N>, order: Order?) -> DataFrame](../rowgroupingprotocol/means%28_,order%29.md)
  Generates a data frame that contains the average mean of each group’s rows along a column you select by column identifier.
- [func minimums<N>(String, N.Type, order: Order?) -> DataFrame](../rowgroupingprotocol/minimums%28_,_,order%29.md)
  Generates a data frame that contains the minimums of each group’s rows along a column you select by name.
- [func minimums<N>(ColumnID<N>, order: Order?) -> DataFrame](../rowgroupingprotocol/minimums%28_,order%29.md)
  Generates a data frame that contains the minimums of each group’s rows along a column you select by column identifier.
- [func maximums<N>(String, N.Type, order: Order?) -> DataFrame](../rowgroupingprotocol/maximums%28_,_,order%29.md)
  Generates a data frame that contains the maximums of each group’s rows along a column you select by name.
- [func maximums<N>(ColumnID<N>, order: Order?) -> DataFrame](../rowgroupingprotocol/maximums%28_,order%29.md)
  Generates a data frame that contains the maximums of each group’s rows along a column you select by column identifier.
- [func quantiles<N>(String, N.Type, quantile: N, order: Order?) -> DataFrame](../rowgroupingprotocol/quantiles%28_,_,quantile,order%29.md)
  Generates a data frame that contains the quantile of each group’s rows along a column you select by name.
- [func quantiles<N>(ColumnID<N>, quantile: N, order: Order?) -> DataFrame](../rowgroupingprotocol/quantiles%28_,quantile,order%29.md)
  Generates a data frame that contains the quantiles of each group’s rows along a column you select by column identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/aggregated(on:naming:transform:))*