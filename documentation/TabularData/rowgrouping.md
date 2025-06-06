# RowGrouping

**Framework**: TabularData  
**Kind**: struct

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

### Creating a Row Grouping
- [init<D>(frame: D, columnName: String, timeUnit: Calendar.Component)](rowgrouping/init(frame:columnname:timeunit:).md)
  Creates a row grouping from a column with date or time elements.
- [init<D>(groups: [(GroupingKey?, D)], groupKeysColumnName: String)](rowgrouping/init(groups:groupkeyscolumnname:).md)
  Creates a row grouping from a list of groups.
### Inspecting a Row Grouping
- [var count: Int](rowgrouping/count.md)
  The number of groups in the row grouping.
- [subscript(Int) -> (key: GroupingKey?, group: DataFrame.Slice)](rowgrouping/subscript(_:)-5z2eg.md)
  Retrieves a group at an index.
### Transforming a Row Grouping
- [func mapGroups((DataFrame.Slice) throws -> DataFrame) rethrows -> RowGrouping<GroupingKey>](rowgrouping/mapgroups(_:).md)
  Generates a row grouping that applies a transformation closure to each group in the original.
### Splitting a Row Grouping
- [func randomSplit(by: Double) -> (Self, Self)](rowgrouping/randomsplit(by:).md)
  Generates two row groupings by randomly splitting the original with a proportion.
- [func randomSplit(by: Double, seed: Int?) -> (RowGrouping<GroupingKey>, RowGrouping<GroupingKey>)](rowgrouping/randomsplit(by:seed:).md)
  Generates two row groupings by randomly splitting the original with a proportion and a seed number.
### Aggregating a Row Grouping
- [func counts() -> DataFrame](rowgrouping/counts.md)
  Generates a data frame with two columns, one that has a row for each group key and another for the number of rows in the group.
- [func counts(order: Order?) -> DataFrame](rowgrouping/counts(order:).md)
  Generates a data frame with two columns, one that has a row for each group key and another for the number of rows in the group.
- [func sums<N>(String, N.Type, order: Order?) -> DataFrame](rowgrouping/sums(_:_:order:).md)
  Generates a data frame that contains the sum of each group’s rows along a column you select by name.
- [func sums<N>(ColumnID<N>, order: Order?) -> DataFrame](rowgrouping/sums(_:order:).md)
  Generates a data frame that contains the sum of each group’s rows along a column you select by column identifier.
- [func means<N>(String, N.Type, order: Order?) -> DataFrame](rowgrouping/means(_:_:order:).md)
  Generates a data frame that contains the average mean of each group’s rows along a column you select by name.
- [func means<N>(ColumnID<N>, order: Order?) -> DataFrame](rowgrouping/means(_:order:).md)
  Generates a data frame that contains the average mean of each group’s rows along a column you select by column identifier.
- [func minimums<N>(String, N.Type, order: Order?) -> DataFrame](rowgrouping/minimums(_:_:order:).md)
  Generates a data frame that contains the minimums of each group’s rows along a column you select by name.
- [func minimums<N>(ColumnID<N>, order: Order?) -> DataFrame](rowgrouping/minimums(_:order:).md)
  Generates a data frame that contains the minimums of each group’s rows along a column you select by column identifier.
- [func maximums<N>(String, N.Type, order: Order?) -> DataFrame](rowgrouping/maximums(_:_:order:).md)
  Generates a data frame that contains the maximums of each group’s rows along a column you select by name.
- [func maximums<N>(ColumnID<N>, order: Order?) -> DataFrame](rowgrouping/maximums(_:order:).md)
  Generates a data frame that contains the maximums of each group’s rows along a column you select by column identifier.
- [func aggregated<Element, Result>(on: ColumnID<Element>, into: String?, transform: (DiscontiguousColumnSlice<Element>) throws -> Result) rethrows -> DataFrame](rowgrouping/aggregated(on:into:transform:).md)
  Generates a data frame with a column for the group identifier and a column of values from the transform.
- [func aggregated<Element, Result>(on: [String], naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame](rowgrouping/aggregated(on:naming:transform:).md)
  Generates a data frame by aggregating each group’s contents for each column you list by name.
- [func aggregated<Element, Result>(on: String..., naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame](rowgrouping/aggregated(on:naming:transform:)-6v6gq.md)
  Generates a data frame by aggregating each group’s contents for each column you select by name.
### Flattening a Row Grouping
- [func ungrouped() -> DataFrame](rowgrouping/ungrouped.md)
  Generates a data frame that contains all the rows from each group in the row grouping.
### Summarizing a Row Grouping
- [func summary() -> any GroupSummaries](rowgrouping/summary.md)
  Generates a group summaries instance for the columns of the row grouping.
- [func summary(of: [String]) -> any GroupSummaries](rowgrouping/summary(of:).md)
  Generates a group summaries instance for the columns you select by name.
- [protocol GroupSummaries](groupsummaries.md)
  A collection of group summaries.
### Describing a Row Grouping
- [var description: String](rowgrouping/description.md)
  A text representation of the row grouping.
### Subscripts
- [subscript(Any?...) -> DataFrame.Slice?](rowgrouping/subscript(_:)-2xxs8.md)
  Retrieves a group slice by key.
### Default Implementations
- [BidirectionalCollection Implementations](rowgrouping/bidirectionalcollection-implementations.md)
- [Collection Implementations](rowgrouping/collection-implementations.md)
- [RandomAccessCollection Implementations](rowgrouping/randomaccesscollection-implementations.md)
- [RowGroupingProtocol Implementations](rowgrouping/rowgroupingprotocol-implementations.md)
- [Sequence Implementations](rowgrouping/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [RowGroupingProtocol](rowgroupingprotocol.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [func grouped(by: String, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframe/grouped(by:timeunit:)-huz4.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by name.
- [func grouped(by: ColumnID<Date>, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframe/grouped(by:timeunit:)-538ya.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by column identifier.
- [func grouped<InputKey, GroupingKey>(by: String, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframe/grouped(by:transform:)-4jlj3.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by name.
- [func grouped<InputKey, GroupingKey>(by: ColumnID<InputKey>, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframe/grouped(by:transform:)-11u79.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by column identifier.
- [func grouped(by: String) -> any RowGroupingProtocol](dataframe/grouped(by:).md)
  Creates a grouping of rows that the method selects by choosing unique values in a column.
- [func grouped<T0, T1>(by: ColumnID<T0>, ColumnID<T1>) -> some RowGroupingProtocol](dataframe/grouped(by:_:).md)
  Creates a grouping from two columns of different types.
- [func grouped<T0, T1, T2>(by: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>) -> some RowGroupingProtocol](dataframe/grouped(by:_:_:).md)
  Creates a grouping from three columns of different types.
- [protocol RowGroupingProtocol](rowgroupingprotocol.md)
  A type that represents a collection of row selections that have the same value in a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping)*