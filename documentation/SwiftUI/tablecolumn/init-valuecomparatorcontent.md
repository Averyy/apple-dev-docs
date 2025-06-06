# init(_:value:comparator:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a sortable column with a text label.

**Availability**:
- iOS 16.6+
- iPadOS 16.6+
- Mac Catalyst 16.6+
- macOS 13.5+
- visionOS 1.0+

## Declaration

```swift
init(_ text: Text, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard, @ViewBuilder content: @escaping (RowValue) -> Content)
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md). See [`Text`](text.md) for more information about localizing strings.

## Parameters

- `text`: The column’s label.
- `value`: The path to the property associated with the column,   used to update the table’s sorting state.
- `comparator`: The specific comparator to compare string values.
- `content`: The view content to display for each row in a table.

## See Also

- [init(_:value:content:)](tablecolumn/init(_:value:content:).md)
  Creates a sortable column for Boolean values with a text label.
- [init(_:value:comparator:)](tablecolumn/init(_:value:comparator:).md)
  Creates a sortable column that displays a string property and has a text label.
- [init(_:sortUsing:content:)](tablecolumn/init(_:sortusing:content:).md)
  Creates a sortable column with text label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:value:comparator:content:))*