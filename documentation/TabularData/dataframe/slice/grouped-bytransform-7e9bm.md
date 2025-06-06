# grouped(by:transform:)

**Framework**: TabularData  
**Kind**: method

Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by column identifier.

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
func grouped<InputKey, GroupingKey>(by columnID: ColumnID<InputKey>, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey> where GroupingKey : Hashable
```

#### Return Value

A collection of groups.

#### Discussion

Create groupings that group rows by:

- Telephone area codes
- The first letter of a person’s last name
- A date’s year or quarter
- Number ranges

## Parameters

- `columnID`: A column identifier.
- `transform`: A closure that transforms a column’s elements into a hashable type.

## See Also

- [func grouped(by: String, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframe/slice/grouped(by:timeunit:)-13w3o.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by name.
- [func grouped(by: ColumnID<Date>, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframe/slice/grouped(by:timeunit:)-696t5.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by column identifier.
- [func grouped<InputKey, GroupingKey>(by: String, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframe/slice/grouped(by:transform:)-5eoog.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by name.
- [struct RowGrouping](rowgrouping.md)
  A collection of row selections that have the same value in a column.
- [func grouped(by: String) -> any RowGroupingProtocol](dataframe/slice/grouped(by:).md)
  Creates a grouping of rows that the method selects by choosing unique values in a column.
- [func grouped<T0, T1>(by: ColumnID<T0>, ColumnID<T1>) -> some RowGroupingProtocol](dataframe/slice/grouped(by:_:).md)
  Creates a grouping from two columns of different types.
- [func grouped<T0, T1, T2>(by: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>) -> some RowGroupingProtocol](dataframe/slice/grouped(by:_:_:).md)
  Creates a grouping from three columns of different types.
- [protocol RowGroupingProtocol](rowgroupingprotocol.md)
  A type that represents a collection of row selections that have the same value in a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/grouped(by:transform:)-7e9bm)*