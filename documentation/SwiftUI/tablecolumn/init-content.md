# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an unsortable column with a text label

**Availability**:
- iOS 16.6+
- iPadOS 16.6+
- Mac Catalyst 16.6+
- macOS 13.5+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(_ text: Text, @ViewBuilder content: @escaping (RowValue) -> Content)
```

#### Discussion

This initializer creates a [`Text`](text.md) view for you, and treats the title similar to [`init(_:)`](text/init(_:).md). For information about localizing strings, see [`Text`](text.md).

## Parameters

- `text`: The column’s label.
- `content`: The view content to display for each row in a table.

## See Also

- [init(_:value:)](tablecolumn/init(_:value:).md)
  Creates an unsortable column that displays a string property with a text label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:content:))*