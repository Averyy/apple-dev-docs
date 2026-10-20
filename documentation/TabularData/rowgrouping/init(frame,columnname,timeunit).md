# init(frame:columnName:timeUnit:)

**Framework**: TabularData  
**Kind**: init  
**Role**: Initializer

Creates a row grouping from a column with date or time elements.

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
init<D>(frame: D, columnName: String, timeUnit: Calendar.Component) where GroupingKey == Int, D : DataFrameProtocol
```

Available when `GroupingKey` conforms to `Hashable`.

## Parameters

- `frame`: A data frame type.
- `columnName`: The name of the column that stores a row’s date and time information.
- `timeUnit`: A calendar component that tells the row grouping how to create its groups.

## See Also

### Creating a Row Grouping
- [init<D>(groups: [(GroupingKey?, D)], groupKeysColumnName: String)](./init%28groups,groupkeyscolumnname%29.md)
  Creates a row grouping from a list of groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/init(frame:columnname:timeunit:))*