# init(_:value:comparator:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a sortable column that generates its label from a localized string resource.

**Availability**:
- iOS 16.6+
- iPadOS 16.6+
- Mac Catalyst 16.6+
- macOS 13.5+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard, @ContentBuilder content: @escaping (RowValue) -> Content)
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf. See [`Text`](text.md) for more information about localizing strings.

## Parameters

- `value`: The path to the property associated with the column, used to update the table’s sorting state.
- `comparator`: The specific comparator to compare string values.
- `content`: The view content to display for each row in a table.

## See Also

- [init(_:value:content:)](tablecolumn/init(_:value:content:).md)
  Creates a sortable column for Boolean values that generates its label from a localized string resource.
- [init(_:value:comparator:)](tablecolumn/init(_:value:comparator:).md)
  Creates a sortable column that displays a string property, and generates its label from a localized string resource.
- [init(_:sortUsing:content:)](tablecolumn/init(_:sortusing:content:).md)
  Creates a sortable column that generates its label from a localized string resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:value:comparator:content:))*