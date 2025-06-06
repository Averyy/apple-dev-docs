# grouped(by:timeUnit:)

**Framework**: TabularData  
**Kind**: method

Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by name.

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
func grouped(by columnName: String, timeUnit: Calendar.Component) -> RowGrouping<Int>
```

#### Return Value

A collection of groups.

#### Discussion

After the method aggregates the groups, it creates a column with the same name as the original column plus the `timeUnit` name.

## Parameters

- `columnName`: The name of a column.
- `timeUnit`: A component of a calendar date.

## See Also

- [func grouped<GroupingKey>(by: ColumnID<GroupingKey>) -> RowGrouping<GroupingKey>](dataframeprotocol/grouped(by:)-77mq2.md)
  Creates a grouping of rows that the method selects by choosing unique values in a column.
- [func grouped(by: ColumnID<Date>, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframeprotocol/grouped(by:timeunit:)-78cy.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by column identifier.
- [func grouped<InputKey, GroupingKey>(by: String, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframeprotocol/grouped(by:transform:)-3cr4p.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by name.
- [func grouped<InputKey, GroupingKey>(by: ColumnID<InputKey>, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframeprotocol/grouped(by:transform:)-3aade.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by column identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframeprotocol/grouped(by:timeunit:)-7s782)*