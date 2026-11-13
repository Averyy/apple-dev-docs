# maximums(_:_:order:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a data frame that contains the maximums of each group’s rows along a column you select by name.

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
func maximums<N>(_ columnName: String, _ type: N.Type, order: Order? = nil) -> DataFrame where N : Comparable
```

## Parameters

- `columnName`: The name of a column.
- `type`: The type of the column.
- `order`: A sorting order the method uses to sort the data frame by its maximum column.

## See Also

### Aggregating a row grouping
- [func counts(order: Order?) -> DataFrame](../rowgrouping/counts%28order%29.md)
  Generates a data frame with two columns, one that has a row for each group key and another for the number of rows in the group.
- [func aggregated<Element, Result>(on: [String], naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame](../rowgrouping/aggregated%28on,naming,transform%29.md)
  Generates a data frame by aggregating each group’s contents for each column you list by name.
- [func aggregated<Element, Result>(on: String..., naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame](./aggregated%28on,naming,transform%29-7s4mf.md)
  Generates a data frame by aggregating each group’s contents for each column you select by name.
- [func sums<N>(String, N.Type, order: Order?) -> DataFrame](./sums%28_,_,order%29.md)
  Generates a data frame that contains the sum of each group’s rows along a column you select by name.
- [func sums<N>(ColumnID<N>, order: Order?) -> DataFrame](./sums%28_,order%29.md)
  Generates a data frame that contains the sum of each group’s rows along a column you select by column identifier.
- [func means<N>(String, N.Type, order: Order?) -> DataFrame](./means%28_,_,order%29.md)
  Generates a data frame that contains the average mean of each group’s rows along a column you select by name.
- [func means<N>(ColumnID<N>, order: Order?) -> DataFrame](./means%28_,order%29.md)
  Generates a data frame that contains the average mean of each group’s rows along a column you select by column identifier.
- [func minimums<N>(String, N.Type, order: Order?) -> DataFrame](./minimums%28_,_,order%29.md)
  Generates a data frame that contains the minimums of each group’s rows along a column you select by name.
- [func minimums<N>(ColumnID<N>, order: Order?) -> DataFrame](./minimums%28_,order%29.md)
  Generates a data frame that contains the minimums of each group’s rows along a column you select by column identifier.
- [func maximums<N>(ColumnID<N>, order: Order?) -> DataFrame](./maximums%28_,order%29.md)
  Generates a data frame that contains the maximums of each group’s rows along a column you select by column identifier.
- [func quantiles<N>(String, N.Type, quantile: N, order: Order?) -> DataFrame](./quantiles%28_,_,quantile,order%29.md)
  Generates a data frame that contains the quantile of each group’s rows along a column you select by name.
- [func quantiles<N>(ColumnID<N>, quantile: N, order: Order?) -> DataFrame](./quantiles%28_,quantile,order%29.md)
  Generates a data frame that contains the quantiles of each group’s rows along a column you select by column identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgroupingprotocol/maximums(_:_:order:))*