# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an unsortable column that generates its label from a localized string resource.

**Availability**:
- iOS 16.6+
- iPadOS 16.6+
- Mac Catalyst 16.6+
- macOS 13.5+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: @escaping (RowValue) -> Content)
```

#### Discussion

This initializer creates a [`Text`](text.md) view for you. For more information about localizing strings, see [`Text`](text.md).

## Parameters

- `titleResource`: Text resource for the column’s localized title.
- `content`: The view content to display for each row in a table.

## See Also

- [init(_:value:)](tablecolumn/init(_:value:).md)
  Creates an unsortable column that displays a string property that generates its label from a localized string resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:content:))*