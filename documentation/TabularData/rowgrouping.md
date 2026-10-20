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

### Creating a Row Grouping
- [init<D>(frame: D, columnName: String, timeUnit: Calendar.Component)](./rowgrouping/init%28frame,columnname,timeunit%29.md)
  Creates a row grouping from a column with date or time elements.
- [init<D>(groups: [(GroupingKey?, D)], groupKeysColumnName: String)](./rowgrouping/init%28groups,groupkeyscolumnname%29.md)
  Creates a row grouping from a list of groups.
### Inspecting a Row Grouping
- [var count: Int](./rowgrouping/count.md)
  The number of groups in the row grouping.
- [subscript(Int) -> (key: GroupingKey?, group: DataFrame.Slice)](./rowgrouping/subscript%28_%29-5z2eg.md)
  Retrieves a group at an index.
### Transforming a Row Grouping
- [func mapGroups((DataFrame.Slice) throws -> DataFrame) rethrows -> RowGrouping<GroupingKey>](./rowgrouping/mapgroups%28_%29.md)
  Generates a row grouping that applies a transformation closure to each group in the original.
### Splitting a Row Grouping
- [func randomSplit(by: Double, seed: Int?) -> (RowGrouping<GroupingKey>, RowGrouping<GroupingKey>)](./rowgrouping/randomsplit%28by,seed%29.md)
  Generates two row groupings by randomly splitting the original with a proportion and a seed number.
### Aggregating a Row Grouping
- [func counts(order: Order?) -> DataFrame](./rowgrouping/counts%28order%29.md)
  Generates a data frame with two columns, one that has a row for each group key and another for the number of rows in the group.
- [func aggregated<Element, Result>(on: [String], naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame](./rowgrouping/aggregated%28on,naming,transform%29.md)
  Generates a data frame by aggregating each group’s contents for each column you list by name.
### Flattening a Row Grouping
- [func ungrouped() -> DataFrame](./rowgrouping/ungrouped%28%29.md)
  Generates a data frame that contains all the rows from each group in the row grouping.
### Summarizing a Row Grouping
- [func summary() -> any GroupSummaries](./rowgrouping/summary%28%29.md)
  Generates a group summaries instance for the columns of the row grouping.
- [func summary(of: [String]) -> any GroupSummaries](./rowgrouping/summary%28of%29.md)
  Generates a group summaries instance for the columns you select by name.
- [protocol GroupSummaries](./groupsummaries.md)
  A collection of group summaries.
### Describing a Row Grouping
- [var description: String](./rowgrouping/description.md)
  A text representation of the row grouping.
### Subscripts
- [subscript(Any?...) -> DataFrame.Slice?](./rowgrouping/subscript%28_%29-2xxs8.md)
  Retrieves a group slice by key.
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

### Grouping Rows
- [func grouped(by: String) -> any RowGroupingProtocol](./dataframe/grouped%28by%29.md)
  Creates a grouping of rows that the method selects by choosing unique values in a column.
- [protocol RowGroupingProtocol](./rowgroupingprotocol.md)
  A type that represents a collection of row selections that have the same value in a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping)*