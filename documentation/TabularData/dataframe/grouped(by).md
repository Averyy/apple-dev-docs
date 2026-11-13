# grouped(by:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Creates a grouping of rows that the method selects by choosing unique values in a column.

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
func grouped(by columnName: String) -> any RowGroupingProtocol
```

## Parameters

- `columnName`: The name of a column.

## See Also

### Grouping rows
- [func grouped(by: ColumnID<Date>, timeUnit: Calendar.Component) -> RowGrouping<Int>](../dataframeprotocol/grouped%28by,timeunit%29-78cy.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by column identifier.
- [func grouped(by: String, timeUnit: Calendar.Component) -> RowGrouping<Int>](../dataframeprotocol/grouped%28by,timeunit%29-7s782.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by name.
- [func grouped<InputKey, GroupingKey>(by: ColumnID<InputKey>, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](../dataframeprotocol/grouped%28by,transform%29-3aade.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by column identifier.
- [func grouped<InputKey, GroupingKey>(by: String, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](../dataframeprotocol/grouped%28by,transform%29-3cr4p.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by name.
- [struct RowGrouping](../rowgrouping.md)
  A collection of row selections that have the same value in a column.
- [func grouped<T0, T1>(by: ColumnID<T0>, ColumnID<T1>) -> some RowGroupingProtocol](../dataframeprotocol/grouped%28by,_%29.md)
  Creates a grouping from two columns of different types.
- [func grouped<T0, T1, T2>(by: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>) -> some RowGroupingProtocol](../dataframeprotocol/grouped%28by,_,_%29.md)
  Creates a grouping from three columns of different types.
- [protocol RowGroupingProtocol](../rowgroupingprotocol.md)
  A type that represents a collection of row selections that have the same value in a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/grouped(by:))*