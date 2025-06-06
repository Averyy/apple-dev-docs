# grouped(by:timeUnit:)

**Framework**: TabularData  
**Kind**: method

Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by column identifier.

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
func grouped(by columnID: ColumnID<Date>, timeUnit: Calendar.Component) -> RowGrouping<Int>
```

#### Return Value

A collection of groups.

#### Discussion

After the method aggregates the groups, it creates a column with the same name as the original column plus the `timeUnit` name.

## Parameters

- `columnID`: A column identifier.
- `timeUnit`: A component of a calendar date.

## See Also

- [func grouped(by: String, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframe/grouped(by:timeunit:)-huz4.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by name.
- [func grouped<InputKey, GroupingKey>(by: String, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframe/grouped(by:transform:)-4jlj3.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by name.
- [func grouped<InputKey, GroupingKey>(by: ColumnID<InputKey>, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframe/grouped(by:transform:)-11u79.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by column identifier.
- [struct RowGrouping](rowgrouping.md)
  A collection of row selections that have the same value in a column.
- [func grouped(by: String) -> any RowGroupingProtocol](dataframe/grouped(by:).md)
  Creates a grouping of rows that the method selects by choosing unique values in a column.
- [func grouped<T0, T1>(by: ColumnID<T0>, ColumnID<T1>) -> some RowGroupingProtocol](dataframe/grouped(by:_:).md)
  Creates a grouping from two columns of different types.
- [func grouped<T0, T1, T2>(by: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>) -> some RowGroupingProtocol](dataframe/grouped(by:_:_:).md)
  Creates a grouping from three columns of different types.
- [protocol RowGroupingProtocol](rowgroupingprotocol.md)
  A type that represents a collection of row selections that have the same value in a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/grouped(by:timeunit:)-538ya)*