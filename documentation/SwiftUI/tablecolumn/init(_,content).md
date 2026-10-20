# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`, `Content` conforms to `View`, and `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ text: Text, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init<S>(_ title: S, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

#### Discussion

This initializer creates a [`Text`](../text.md) view for you. For more information about localizing strings, see [`Text`](../text.md).

## Parameters

- `titleResource`: Text resource for the column’s localized title.
- `content`: The view content to display for each row in a table.

## See Also

### Creating an unsortable column
- [init(_:value:)](./init%28_,value%29.md)
  Creates an unsortable column that displays a string property that generates its label from a localized string resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:content:))*