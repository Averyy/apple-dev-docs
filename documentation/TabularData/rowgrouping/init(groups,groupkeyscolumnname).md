# init(groups:groupKeysColumnName:)

**Framework**: TabularData  
**Kind**: init  
**Role**: Initializer

Creates a row grouping from a list of groups.

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
init<D>(groups: [(GroupingKey?, D)], groupKeysColumnName: String) where D : DataFrameProtocol
```

#### Discussion

The member data frames must all have the same columns (count, names, and types).

## Parameters

- `groups`: An array of tuples. Each tuple pairs a key with a data frame type.
- `groupKeysColumnName`: The name of the grouping key column the row grouping creates when it generates a data frame, such as its [`ungrouped()`](./ungrouped%28%29.md) or [`counts(order:)`](./counts%28order%29.md) methods.

## See Also

### Creating a Row Grouping
- [init<D>(frame: D, columnName: String, timeUnit: Calendar.Component)](./init%28frame,columnname,timeunit%29.md)
  Creates a row grouping from a column with date or time elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/init(groups:groupkeyscolumnname:))*