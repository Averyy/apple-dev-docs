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

- [func grouped<GroupingKey>(by: ColumnID<GroupingKey>) -> RowGrouping<GroupingKey>](dataframeprotocol/grouped(by:)-77mq2.md)
  Creates a grouping of rows that the method selects by choosing unique values in a column.
- [func grouped(by: String, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframeprotocol/grouped(by:timeunit:)-7s782.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by name.
- [func grouped(by: ColumnID<Date>, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframeprotocol/grouped(by:timeunit:)-78cy.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by column identifier.
- [func grouped<InputKey, GroupingKey>(by: String, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframeprotocol/grouped(by:transform:)-3cr4p.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframeprotocol/grouped(by:transform:)-3aade)*