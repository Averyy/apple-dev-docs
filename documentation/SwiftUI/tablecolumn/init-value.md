# init(_:value:)

**Framework**: SwiftUI  
**Kind**: init

Creates an unsortable column that displays a string property with a text label.

**Availability**:
- iOS 16.6+
- iPadOS 16.6+
- Mac Catalyst 16.6+
- macOS 13.5+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, String>) where Content == Text
```

#### Discussion

This initializer creates a [`Text`](text.md) view for you, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md). For more information about localizing strings, see [`Text`](text.md).

## Parameters

- `text`: The column’s label.
- `value`: The path to the property associated with the column.   The table uses this to display the property as verbatim text in each   row of the table.

## See Also

- [init(_:content:)](tablecolumn/init(_:content:).md)
  Creates an unsortable column with a text label


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:value:))*