# RowGrouping

**Framework**: TabularData  
**Kind**: struct  
**Role**: Structure

A collection of row selections that have the same value in a column.

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
struct RowGrouping<GroupingKey> where GroupingKey : Hashable
```

## Topics

### Creating a row grouping
- [init<D>(frame: D, columnName: String, timeUnit: Calendar.Component)](./rowgrouping/init%28frame,columnname,timeunit%29.md)
  Creates a row grouping from a column with date or time elements.
- [init<D>(groups: [(GroupingKey?, D)], groupKeysColumnName: String)](./rowgrouping/init%28groups,groupkeyscolumnname%29.md)
  Creates a row grouping from a list of groups.
### Inspecting a row grouping
- [var count: Int](./rowgrouping/count.md)
  The number of groups in the row grouping.
- [subscript(Int) -> (key: GroupingKey?, group: DataFrame.Slice)](./rowgrouping/subscript%28_%29-5z2eg.md)
  Retrieves a group at an index.
- [subscript(Any?...) -> DataFrame.Slice?](./rowgrouping/subscript%28_%29-2xxs8.md)
  Retrieves a group slice by key.
### Transforming a row grouping
- [func mapGroups((DataFrame.Slice) throws -> DataFrame) rethrows -> RowGrouping<GroupingKey>](./rowgrouping/mapgroups%28_%29.md)
  Generates a row grouping that applies a transformation closure to each group in the original.
### Filtering a row grouping
- [func filter((DataFrame.Slice) throws -> Bool) rethrows -> RowGrouping<GroupingKey>](./rowgrouping/filter%28_%29.md)
  Returns a row grouping containing only the groups that satisfy a predicate.
### Splitting a row grouping
- [func randomSplit(by: Double, seed: Int?) -> (RowGrouping<GroupingKey>, RowGrouping<GroupingKey>)](./rowgrouping/randomsplit%28by,seed%29.md)
  Generates two row groupings by randomly splitting the original with a proportion and a seed number.
### Aggregating a row grouping
- [func counts(order: Order?) -> DataFrame](./rowgrouping/counts%28order%29.md)
  Generates a data frame with two columns, one that has a row for each group key and another for the number of rows in the group.
- [func aggregated<Element, Result>(on: [String], naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame](./rowgrouping/aggregated%28on,naming,transform%29.md)
  Generates a data frame by aggregating each group’s contents for each column you list by name.
- [func aggregated<Element, Result>(on: String..., naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame](./rowgroupingprotocol/aggregated%28on,naming,transform%29-7s4mf.md)
  Generates a data frame by aggregating each group’s contents for each column you select by name.
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
### Flattening a row grouping
- [func ungrouped() -> DataFrame](./rowgrouping/ungrouped%28%29.md)
  Generates a data frame that contains all the rows from each group in the row grouping.
### Summarizing a row grouping
- [func summary() -> any GroupSummaries](./rowgrouping/summary%28%29.md)
  Generates a group summaries instance for the columns of the row grouping.
- [func summary(of: [String]) -> any GroupSummaries](./rowgrouping/summary%28of%29.md)
  Generates a group summaries instance for the columns you select by name.
- [func summary(of: String...) -> any GroupSummaries](./rowgroupingprotocol/summary%28of%29-n5ia.md)
  Generates a categorical summary of the columns you select by name.
- [protocol GroupSummaries](./groupsummaries.md)
  A collection of group summaries.
### Describing a row grouping
- [var description: String](./rowgrouping/description.md)
  A text representation of the row grouping.
### Retrieving an index
- [var startIndex: Int](./rowgrouping/startindex.md)
  The index of the initial group in the row grouping.
- [var endIndex: Int](./rowgrouping/endindex.md)
  The index of the final group in the row grouping.
- [func index(before: Int) -> Int](./rowgrouping/index%28before%29.md)
  Returns the index immediately before an element index.
- [func index(after: Int) -> Int](./rowgrouping/index%28after%29.md)
  Returns the index immediately after an element index.
### Default Implementations
- [Collection Implementations](./rowgrouping/collection-implementations.md)
- [RandomAccessCollection Implementations](./rowgrouping/randomaccesscollection-implementations.md)
- [RowGroupingProtocol Implementations](./rowgrouping/rowgroupingprotocol-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Escapable](../Swift/escapable.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
- [RowGroupingProtocol](./rowgroupingprotocol.md)
- [Sequence](../Swift/sequence.md)

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
- [func grouped(by: String) -> any RowGroupingProtocol](./dataframe/grouped%28by%29.md)
  Creates a grouping of rows that the method selects by choosing unique values in a column.
- [func grouped<T0, T1>(by: ColumnID<T0>, ColumnID<T1>) -> some RowGroupingProtocol](./dataframeprotocol/grouped%28by,_%29.md)
  Creates a grouping from two columns of different types.
- [func grouped<T0, T1, T2>(by: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>) -> some RowGroupingProtocol](./dataframeprotocol/grouped%28by,_,_%29.md)
  Creates a grouping from three columns of different types.
- [protocol RowGroupingProtocol](./rowgroupingprotocol.md)
  A type that represents a collection of row selections that have the same value in a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping)*