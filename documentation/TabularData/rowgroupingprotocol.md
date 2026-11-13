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

### Inspecting a row grouping
- [var count: Int](./rowgroupingprotocol/count.md)
  The number of groups in the row grouping.
- [subscript(Any?...) -> DataFrame.Slice?](./rowgroupingprotocol/subscript%28_%29.md)
  Retrieves a group slice by key.
### Transforming a row grouping
- [func mapGroups((DataFrame.Slice) throws -> DataFrame) rethrows -> Self](./rowgroupingprotocol/mapgroups%28_%29.md)
  Generates a row grouping that applies a transformation closure to each group in the original.
### Filtering a row grouping
- [func filter((DataFrame.Slice) throws -> Bool) rethrows -> Self](./rowgroupingprotocol/filter%28_%29.md)
  Returns a row grouping containing only the groups that satisfy a predicate.
### Splitting a row grouping
- [func randomSplit(by: Double) -> (Self, Self)](./rowgroupingprotocol/randomsplit%28by%29.md)
  Generates two row groupings by randomly splitting the original with a proportion.
- [func randomSplit(by: Double, seed: Int?) -> (Self, Self)](./rowgroupingprotocol/randomsplit%28by,seed%29.md)
  Generates two row groupings by randomly splitting the original by a proportion.
### Aggregating a row grouping
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
- [func quantiles<N>(String, N.Type, quantile: N, order: Order?) -> DataFrame](./rowgroupingprotocol/quantiles%28_,_,quantile,order%29.md)
  Generates a data frame that contains the quantile of each group’s rows along a column you select by name.
- [func quantiles<N>(ColumnID<N>, quantile: N, order: Order?) -> DataFrame](./rowgroupingprotocol/quantiles%28_,quantile,order%29.md)
  Generates a data frame that contains the quantiles of each group’s rows along a column you select by column identifier.
- [func aggregated<Element, Result>(on: ColumnID<Element>, into: String?, transform: (DiscontiguousColumnSlice<Element>) throws -> Result) rethrows -> DataFrame](./rowgroupingprotocol/aggregated%28on,into,transform%29.md)
  Generates a data frame with a column for the group identifier and a column of values from the transform.
- [func aggregated<Element, Result>(on: [String], naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame](./rowgroupingprotocol/aggregated%28on,naming,transform%29.md)
  Generates a data frame by aggregating each group’s contents for each column you select by name.
- [func aggregated<Element, Result>(on: String..., naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame](./rowgroupingprotocol/aggregated%28on,naming,transform%29-7s4mf.md)
  Generates a data frame by aggregating each group’s contents for each column you select by name.
### Flattening a row grouping
- [func ungrouped() -> DataFrame](./rowgroupingprotocol/ungrouped%28%29.md)
  Generates a data frame that contains all the rows from each group in the row grouping.
### Summarizing a row grouping
- [func summary() -> any GroupSummaries](./rowgroupingprotocol/summary%28%29.md)
  Generates a group summaries instance of the row grouping’s columns.
- [func summary(of: [String]) -> any GroupSummaries](./rowgroupingprotocol/summary%28of%29.md)
  Generates a group summaries instance of the row grouping’s columns you select by name.
- [func summary(of: String...) -> any GroupSummaries](./rowgroupingprotocol/summary%28of%29-n5ia.md)
  Generates a categorical summary of the columns you select by name.
- [protocol GroupSummaries](./groupsummaries.md)
  A collection of group summaries.

## Relationships

### Inherits From
- [CustomStringConvertible](../Swift/customstringconvertible.md)
### Conforming Types
- [RowGrouping](./rowgrouping.md)

## See Also

### Grouping rows
- [func grouped(by: ColumnID<Date>, timeUnit: Calendar.Component) -> RowGrouping<Int>](./dataframeprotocol/grouped%28by,timeunit%29-78cy.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by column identifier.
- [func grouped(by: String, timeUnit: Calendar.Component) -> RowGrouping<Int>](./dataframeprotocol/grouped%28by,timeunit%29-7s782.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by name.
- [func grouped<InputKey, GroupingKey>(by: ColumnID<InputKey>, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](./dataframeprotocol/grouped%28by,transform%29-3aade.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by column identifier.
- [func grouped<InputKey, GroupingKey>(by: String, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](./dataframeprotocol/grouped%28by,transform%29-3cr4p.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by name.
- [struct RowGrouping](./rowgrouping.md)
  A collection of row selections that have the same value in a column.
- [func grouped(by: String) -> any RowGroupingProtocol](./dataframe/grouped%28by%29.md)
  Creates a grouping of rows that the method selects by choosing unique values in a column.
- [func grouped<T0, T1>(by: ColumnID<T0>, ColumnID<T1>) -> some RowGroupingProtocol](./dataframeprotocol/grouped%28by,_%29.md)
  Creates a grouping from two columns of different types.
- [func grouped<T0, T1, T2>(by: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>) -> some RowGroupingProtocol](./dataframeprotocol/grouped%28by,_,_%29.md)
  Creates a grouping from three columns of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgroupingprotocol)*