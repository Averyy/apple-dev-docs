# RowGroupingProtocol

**Framework**: TabularData  
**Kind**: protocol  
**Role**: Protocol

A type that represents a collection of row selections that have the same value in a column.

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
protocol RowGroupingProtocol : CustomStringConvertible
```

## Topics

### Inspecting a Row Grouping
- [var count: Int](./rowgroupingprotocol/count.md)
  The number of groups in the row grouping.
### Transforming a Row Grouping
- [func mapGroups((DataFrame.Slice) throws -> DataFrame) rethrows -> Self](./rowgroupingprotocol/mapgroups%28_%29.md)
  Generates a row grouping that applies a transformation closure to each group in the original.
### Splitting a Row Grouping
- [func randomSplit(by: Double) -> (Self, Self)](./rowgroupingprotocol/randomsplit%28by%29.md)
  Generates two row groupings by randomly splitting the original with a proportion.
- [func randomSplit(by: Double, seed: Int?) -> (Self, Self)](./rowgroupingprotocol/randomsplit%28by,seed%29.md)
  Generates two row groupings by randomly splitting the original by a proportion.
### Aggregating a Row Grouping
- [func counts() -> DataFrame](./rowgroupingprotocol/counts%28%29.md)
  Generates a data frame with two columns, one that has a row for each group key and another for the number of rows in the group.
- [func counts(order: Order?) -> DataFrame](./rowgroupingprotocol/counts%28order%29.md)
  Generates a data frame, that you choose how to sort, with two columns, one that has a row for each group key and another for the number or rows in the group.
- [func sums<N>(String, N.Type, order: Order?) -> DataFrame](./rowgroupingprotocol/sums%28_,_,order%29.md)
  Generates a data frame that contains the sum of each group’s rows along a column you select by name.
- [func sums<N>(ColumnID<N>, order: Order?) -> DataFrame](./rowgroupingprotocol/sums%28_,order%29.md)
  Generates a data frame that contains the sum of each group’s rows along a column you select by column identifier.
- [func means<N>(String, N.Type, order: Order?) -> DataFrame](./rowgroupingprotocol/means%28_,_,order%29.md)
  Generates a data frame that contains the average mean of each group’s rows along a column you select by name.
- [func means<N>(ColumnID<N>, order: Order?) -> DataFrame](./rowgroupingprotocol/means%28_,order%29.md)
  Generates a data frame that contains the average mean of each group’s rows along a column you select by column identifier.
- [func minimums<N>(String, N.Type, order: Order?) -> DataFrame](./rowgroupingprotocol/minimums%28_,_,order%29.md)
  Generates a data frame that contains the minimums of each group’s rows along a column you select by name.
- [func minimums<N>(ColumnID<N>, order: Order?) -> DataFrame](./rowgroupingprotocol/minimums%28_,order%29.md)
  Generates a data frame that contains the minimums of each group’s rows along a column you select by column identifier.
- [func maximums<N>(String, N.Type, order: Order?) -> DataFrame](./rowgroupingprotocol/maximums%28_,_,order%29.md)
  Generates a data frame that contains the maximums of each group’s rows along a column you select by name.
- [func maximums<N>(ColumnID<N>, order: Order?) -> DataFrame](./rowgroupingprotocol/maximums%28_,order%29.md)
  Generates a data frame that contains the maximums of each group’s rows along a column you select by column identifier.
- [func aggregated<Element, Result>(on: ColumnID<Element>, into: String?, transform: (DiscontiguousColumnSlice<Element>) throws -> Result) rethrows -> DataFrame](./rowgroupingprotocol/aggregated%28on,into,transform%29.md)
  Generates a data frame with a column for the group identifier and a column of values from the transform.
- [func aggregated<Element, Result>(on: [String], naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame](./rowgroupingprotocol/aggregated%28on,naming,transform%29.md)
  Generates a data frame by aggregating each group’s contents for each column you select by name.
### Flattening a Row Grouping
- [func ungrouped() -> DataFrame](./rowgroupingprotocol/ungrouped%28%29.md)
  Generates a data frame that contains all the rows from each group in the row grouping.
### Summarizing a Row Grouping
- [func summary() -> any GroupSummaries](./rowgroupingprotocol/summary%28%29.md)
  Generates a group summaries instance of the row grouping’s columns.
- [func summary(of: [String]) -> any GroupSummaries](./rowgroupingprotocol/summary%28of%29.md)
  Generates a group summaries instance of the row grouping’s columns you select by name.
- [protocol GroupSummaries](./groupsummaries.md)
  A collection of group summaries.
### Instance Methods
- [func filter((DataFrame.Slice) throws -> Bool) rethrows -> Self](./rowgroupingprotocol/filter%28_%29.md)
  Returns a row grouping containing only the groups that satisfy a predicate.
- [func quantiles<N>(String, N.Type, quantile: N, order: Order?) -> DataFrame](./rowgroupingprotocol/quantiles%28_,_,quantile,order%29.md)
  Generates a data frame that contains the quantile of each group’s rows along a column you select by name.
- [func quantiles<N>(ColumnID<N>, quantile: N, order: Order?) -> DataFrame](./rowgroupingprotocol/quantiles%28_,quantile,order%29.md)
  Generates a data frame that contains the quantiles of each group’s rows along a column you select by column identifier.
### Subscripts
- [subscript(Any?...) -> DataFrame.Slice?](./rowgroupingprotocol/subscript%28_%29.md)
  Retrieves a group slice by key.

## Relationships

### Inherits From
- [CustomStringConvertible](../Swift/customstringconvertible.md)
### Conforming Types
- [RowGrouping](./rowgrouping.md)

## See Also

### Grouping Rows
- [struct RowGrouping](./rowgrouping.md)
  A collection of row selections that have the same value in a column.
- [func grouped(by: String) -> any RowGroupingProtocol](./dataframe/grouped%28by%29.md)
  Creates a grouping of rows that the method selects by choosing unique values in a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgroupingprotocol)*