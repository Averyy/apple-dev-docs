# init(_:value:comparator:)

**Framework**: SwiftUI  
**Kind**: init

Creates a sortable column that displays a string property and has a text label.

**Availability**:
- iOS 16.6+
- iPadOS 16.6+
- Mac Catalyst 16.6+
- macOS 13.5+
- visionOS 1.0+

## Declaration

```swift
init(_ text: Text, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard) where Content == Text
```

#### Discussion

This initializer creates a [`Text`](text.md) view for you, and treats the title similar to [`init(_:)`](text/init(_:).md). For more information about localizing strings, see [`Text`](text.md).

## Parameters

- `text`: The column’s label.
- `value`: The path to the property associated with the column,   to display verbatim as text in each row of a table,   and the key path used to create a sort comparator when   sorting the column.
- `comparator`: The   used to order the string values.

## See Also

- [init(_:value:content:)](tablecolumn/init(_:value:content:).md)
  Creates a sortable column for Boolean values with a text label.
- [init(_:value:comparator:content:)](tablecolumn/init(_:value:comparator:content:).md)
  Creates a sortable column with a text label.
- [init(_:sortUsing:content:)](tablecolumn/init(_:sortusing:content:).md)
  Creates a sortable column with text label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:value:comparator:))*