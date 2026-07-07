# init(_:value:)

**Framework**: SwiftUI  
**Kind**: init

Creates an unsortable column that displays a string property that generates its label from a localized string resource.

**Availability**:
- iOS 16.6+
- iPadOS 16.6+
- Mac Catalyst 16.6+
- macOS 13.5+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, String>) where Content == Text
```

#### Discussion

This initializer creates a [`Text`](text.md) view for you. For more information about localizing strings, see [`Text`](text.md).

## Parameters

- `titleResource`: Text resource for the column’s localized title.
- `value`: The path to the property associated with the column. The table uses this to display the property as verbatim text in each row of the table.

## See Also

- [init(_:content:)](tablecolumn/init(_:content:).md)
  Creates an unsortable column that generates its label from a localized string resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:value:))*